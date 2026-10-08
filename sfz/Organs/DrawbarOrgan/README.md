# DrawbarOrgan - Simple SFZ-based Hammond B3 emulation with CC-controlled drawbars

NOTE: Every drawbar that's not at zero uses a voice.  That's a lot.
To reduce voice usage, a drawbar voice is not played if that drawbar
is at zero.  What this means is, while you can change drawbars as
you play, moving a drawbar from up from zero has no effect until
new notes are played.

The general idea for this sfz is that you'll adjust drawbars and
save the preset, and in general won't be fiddling drawbars as you
play with this organ.  If you want to do stuff like that, use SetBFree.

For best results use with X42 Whirl rotary speaker sim.

## Planned

- Fixed registrations, like:
  - 888-000-000
  - 888-001-000
  - 888-800-000
  - 888-801-000
  - 808-000-000
  - 808-001-000
  - 800-800-000
  - 800-801-000
  - 800-008-000
  - 864-001-234
  - 840-012-340
- keyclick, if I can find a good set of samples

## Not likely to happen

- percussion, because sfz doesn't have the capability to do it properly (it'd trigger on every keystrike.)
- scanner (vibrato/chorus) because looping the samples would be a nightmare
- foldback (possible but tedious)
