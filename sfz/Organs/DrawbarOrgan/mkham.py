#!/usr/bin/env python3

# Make hammond wave files for given registrations
# Outputs xxxx-xx-xxx.wav for each registration

# After building the waveform, you can add them to
# Drawbars.sfz, or create a new single .sfz file
# for each, using the existing ones as templates.

# TODO: make this better for Zynthian users:
# - add script to create venv and add requirements.txt
# - take registrations on command line
# - build SFZ using the waveforms
# - sfz filename parameter
# - options for keyswitch or CC control
# - output zynthian .yml
# - (maybe) option for shape (sine, square, triangle, sawtooth)

import numpy as np
from scipy.io import wavfile

# Audio configurations
sample_rate = 48000  # Standard CD quality audio
amplitude = 0.5      # Scale down to prevent digital clipping when combined

# Frequencies based on note C4 (261.63 Hz)
f_C = 261.5     # pitch of Middle C
f_1 = f_C / 2   # One octave lower (130.81 Hz)
f_2 = f_1 * 3   # Perfect fifth higher than DB1, 3rd harmonic (784.89 Hz)
f_3 = f_C * 1   # Fundamental pitch
f_4 = f_C * 2   # 1st harmonic
f_5 = f_C * 3   # 2nd harmonic
f_6 = f_C * 4   # 3rd harmonic
f_7 = f_C * 5   # 4th harmonic
f_8 = f_C * 6   # 5th harmonic
f_9 = f_C * 8   # 7th harmonic

duration = 10 * 1/f_1

# Time axis array
t = np.linspace(0, duration, int(sample_rate * duration), endpoint=False)

# Sine wave for each drawbar.  Coefficients were based on audio comparison with SetBFree.
drawbars = (
      np.sin(2 * np.pi * f_1 * t)
    , np.sin(2 * np.pi * f_2 * t)/4
    , np.sin(2 * np.pi * f_3 * t)
    , np.sin(2 * np.pi * f_4 * t)/4
    , np.sin(2 * np.pi * f_5 * t)/4
    , np.sin(2 * np.pi * f_6 * t)/4
    , np.sin(2 * np.pi * f_7 * t)/4
    , np.sin(2 * np.pi * f_8 * t)/4
    , np.sin(2 * np.pi * f_9 * t)/8
    )

wave_0 = 0 * np.sin(2 * np.pi * f_1 * t) # zero wave for starting with

registrations = (
      "8880-00-000"
    , "8880-02-000"
    , "8888-00-000"
    , "8888-02-000"
    , "8080-00-000"
    , "8080-02-000"
    , "8008-00-000"
    , "8008-02-000"
    , "8000-08-000"
    , "8640-01-234"
    , "8400-12-340"
    , "8888-88-888"
    )

for str_reg in registrations:
    reg = list(str_reg)
    # print(str_reg)
    # remove dashes
    del reg[7]
    del reg[4]

    if True:
        wave = wave_0
        dbnum = 0
        for db in reg:
            gain = int(db) / 8.0
            # print("  ", dbnum, gain)
            wave = wave + gain * drawbars[dbnum]
            dbnum += 1
    else:
        wave = drawbars[0] + drawbars[1] + drawbars[2]

    # Normalize
    # wave = wave / np.max(np.abs(wave))

    # scale to 16-bit audio range
    audio_data = np.int16(wave * amplitude * 32767)

    # Save the result as a WAV file
    output_filename = str_reg + ".wav"
    wavfile.write(output_filename, sample_rate, audio_data)

    print(f"'{output_filename}'")

