# DrawbarOrgan - Simple SFZ-based Hammond B3 emulation with CC-controlled drawbars

Three SFZ files:

DrawbarOrgan.sfz - control drawbars with CCs.  NOTE: uses too many voices.
keyswitch.sfz - select registration by keyswitch
modwheel.sfz - select registration by Mod wheel

For best results, use with X42 Whirl rotary speaker sim.

Details below.

## DrawbarOrgan.sfz

Control drawbars by CC

NOTE: Every drawbar that's not at zero uses a voice.  That's a lot!
To reduce voice usage, a drawbar voice is not played if that drawbar
is at zero.  What this means is, while you can change drawbars as
you play, moving a drawbar from up from zero has no effect until
new notes are played.

The general idea for this sfz is that you'll adjust drawbars and
save the preset, and in general won't be fiddling drawbars as you
play with this organ.  If you want to do stuff like that, use SetBFree.

## keyswitch.sfz

Keyswitch Registrations

- blues
A0  - 8880-00-000
A#0 - 8880-02-000
B0  - 8888-00-000
C1  - 8888-02-000

- flutes
C#1 - 8080-00-000
D1  - 8080-02-000
D#1 - 8008-00-000
E1  - 8008-02-000
F1  - 8000-08-000

- swing
F#1 - 8400-12-340
G1  - 8640-01-234

- full
G#1 - 8888-88-888

## modwheel.sfz

Mod Wheel -> Registration

- blues
  0 -   9  - 8880-00-000
 10 -  19  - 8880-02-000
 20 -  29  - 8888-00-000
 30 -  39  - 8888-02-000

- flutes
 40 -  49  - 8080-00-000
 50 -  59  - 8080-02-000
 60 -  69  - 8008-00-000
 70 -  79  - 8008-02-000
 80 -  89  - 8000-08-000

- swing
 90 -  99  - 8400-12-340
100 - 109  - 8640-01-234

- full
110 - 127  - 8888-88-888

## Hopeful improvemens

- keyclick, if I can find a good sample
- python program to create wave file and sfz for a user-specified set of registrations.

## Not likely to happen

- percussion, because sfz doesn't have the capability to do it properly (it'd trigger on every keystrike.)
- scanner (vibrato/chorus) because looping the samples would be a nightmare
- foldback (possible but tedious)
