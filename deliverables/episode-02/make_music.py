"""Create an original warm pop cue using synthesized instruments only."""
import wave
import numpy as np

rate = 48000
beat = 60 / 96
rng = np.random.default_rng(2026)
mix = np.zeros((int(rate * 23), 2))
chords = [(57, 60, 64, 67), (53, 57, 60, 64), (48, 55, 59, 64), (55, 59, 62, 69),
          (57, 60, 64, 71), (53, 57, 60, 67), (48, 55, 60, 64), (55, 59, 62, 69),
          (48, 55, 60, 64)]

def add(start, signal, gain, pan=0):
    offset = round(start * rate)
    signal = signal[:len(mix) - offset]
    mix[offset:offset + len(signal)] += signal[:, None] * gain * np.sqrt([(1-pan)/2, (1+pan)/2])

def note(key, start, length, gain, pan, kind):
    t = np.arange(round(length * rate)) / rate
    phase = 2 * np.pi * 440 * 2 ** ((key - 69) / 12) * t
    if kind == 'keys':
        signal = (np.sin(phase) + .19*np.sin(phase*2.004) + .09*np.sin(phase*3.01)) * np.exp(-t*2.5)
        attack, release = .019, .15
    elif kind == 'pad':
        signal = (.5*np.sin(phase*.998) + .5*np.sin(phase*1.002) + .11*np.sin(phase*2)) * (.91 + .09*np.sin(2*np.pi*2.1*t))
        attack, release = .65, .76
    else:
        signal = (np.sin(phase) + .20*np.sin(phase*2)) * np.exp(-t*1.6)
        attack, release = .04, .18
    env = np.clip(t / attack, 0, 1) * np.clip((length-t)/release, 0, 1)
    add(start, signal * env, gain, pan)

for bar, chord in enumerate(chords):
    at = bar * 4 * beat
    for index, key in enumerate(chord):
        note(key, at, 3.2, .035, (index - 1.5) * .35, 'pad')
    pattern = (0, 2, 1, 3, 2, 1, 3, 2) if bar < 8 else (0, 2, 1, 3)
    for step, index in enumerate(pattern):
        note(chord[index] + 12, at + step * beat/2, 1.05, .052 if step%2 else .071, -.29+.18*index, 'keys')
    if bar < 8:
        for step in (0, 2.5):
            note(chord[0] - 12, at + step*beat, .91, .082, 0, 'bass')
        for step in (0, 2.5):
            t = np.arange(rate//5)/rate
            add(at + step*beat, np.sin(2*np.pi*(46*t+2.5*(1-np.exp(-30*t)))) * np.exp(-t*35) * np.minimum(t*1000,1), .12)
        for step in (1, 3):
            t = np.arange(rate//8)/rate
            noise = rng.normal(size=len(t))
            add(at + step*beat, np.diff(noise, prepend=0)*np.exp(-t*65)*np.minimum(t*2000,1), .024, .14)
    if 1 <= bar < 8:
        note(chord[-1] + 12, at + 1.5*beat, 1.7, .042, .29, 'keys')

for delay, gain in ((.17, .14), (.31, .075), (.47,.035)):
    samples = int(delay*rate)
    mix[samples:] += mix[:-samples, ::-1] * gain
mix *= .75 / np.max(np.abs(mix))
with wave.open('episode2-original-pop.wav', 'wb') as audio:
    audio.setparams((2, 2, rate, 0, 'NONE', 'not compressed'))
    audio.writeframes((mix * 32767).astype('<i2').tobytes())
