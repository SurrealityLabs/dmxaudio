from dmx import Colour

DMX_AUDIO_COMMAND_NOP = 0x00
DMX_AUDIO_COMMAND_STOP_ALL = 0x01
DMX_AUDIO_COMMAND_PLAY_ONCE_POLY = 0x02
DMX_AUDIO_COMMAND_PLAY_LOOP_POLY = 0x03
DMX_AUDIO_COMMAND_PLAY_ONCE_MONO = 0x04
DMX_AUDIO_COMMAND_PLAY_LOOP_MONO = 0x05
DMX_AUDIO_COMMAND_PLAY_ONCE_POLY_LOCKED = 0x06
DMX_AUDIO_COMMAND_PLAY_LOOP_POLY_LOCKED = 0x07
DMX_AUDIO_COMMAND_STOP = 0x08
DMX_AUDIO_COMMAND_PAUSE = 0x09
DMX_AUDIO_COMMAND_RESUME = 0x0A
DMX_AUDIO_COMMAND_TRACK_VOLUME = 0x0B
DMX_AUDIO_COMMAND_MASTER_VOLUME = 0x0C

NOPCommandA = Colour(DMX_AUDIO_COMMAND_NOP, 0, 0)
NOPCommandB = Colour(0, 0, 0)

PlaySound0LoopMonoA = Colour(DMX_AUDIO_COMMAND_PLAY_LOOP_MONO, 0, 0)
PlaySound0LoopMonoB = Colour(127, 0, 0)

PlaySound1LoopMonoA = Colour(DMX_AUDIO_COMMAND_PLAY_LOOP_MONO, 1, 0)
PlaySound1LoopMonoB = Colour(127, 0, 0)

PlaySound256LoopPolyA = Colour(DMX_AUDIO_COMMAND_PLAY_LOOP_POLY, 0, 1)
PlaySound256LoopPolyB = Colour(127, 0, 0)

PlaySound257LoopPolyA = Colour(DMX_AUDIO_COMMAND_PLAY_LOOP_POLY, 1, 1)
PlaySound257LoopPolyB = Colour(127, 0, 0)

PlaySound258LoopPolyA = Colour(DMX_AUDIO_COMMAND_PLAY_LOOP_POLY, 2, 1)
PlaySound258LoopPolyB = Colour(127, 0, 0)

PlaySound259LoopPolyA = Colour(DMX_AUDIO_COMMAND_PLAY_LOOP_POLY, 3, 1)
PlaySound259LoopPolyB = Colour(127, 0, 0)

PlaySound260LoopPolyA = Colour(DMX_AUDIO_COMMAND_PLAY_LOOP_POLY, 4, 1)
PlaySound260LoopPolyB = Colour(127, 0, 0)

PlaySound261LoopPolyA = Colour(DMX_AUDIO_COMMAND_PLAY_LOOP_POLY, 5, 1)
PlaySound261LoopPolyB = Colour(127, 0, 0)

PlaySound262LoopPolyA = Colour(DMX_AUDIO_COMMAND_PLAY_LOOP_POLY, 6, 1)
PlaySound262LoopPolyB = Colour(127, 0, 0)

PlaySound263LoopPolyA = Colour(DMX_AUDIO_COMMAND_PLAY_LOOP_POLY, 7, 1)
PlaySound263LoopPolyB = Colour(127, 0, 0)

PlaySound264LoopPolyA = Colour(DMX_AUDIO_COMMAND_PLAY_LOOP_POLY, 8, 1)
PlaySound264LoopPolyB = Colour(127, 0, 0)

PlaySound265LoopPolyA = Colour(DMX_AUDIO_COMMAND_PLAY_LOOP_POLY, 9, 1)
PlaySound265LoopPolyB = Colour(127, 0, 0)

PlaySound266LoopPolyA = Colour(DMX_AUDIO_COMMAND_PLAY_LOOP_POLY, 10, 1)
PlaySound266LoopPolyB = Colour(127, 0, 0)

PlaySound267LoopPolyA = Colour(DMX_AUDIO_COMMAND_PLAY_LOOP_POLY, 11, 1)
PlaySound267LoopPolyB = Colour(127, 0, 0)

PlaySound268LoopPolyA = Colour(DMX_AUDIO_COMMAND_PLAY_LOOP_POLY, 12, 1)
PlaySound268LoopPolyB = Colour(127, 0, 0)

PlaySound269LoopPolyA = Colour(DMX_AUDIO_COMMAND_PLAY_LOOP_POLY, 13, 1)
PlaySound269LoopPolyB = Colour(127, 0, 0)

PlaySound270LoopPolyA = Colour(DMX_AUDIO_COMMAND_PLAY_LOOP_POLY, 14, 1)
PlaySound270LoopPolyB = Colour(127, 0, 0)

PlaySound271LoopPolyA = Colour(DMX_AUDIO_COMMAND_PLAY_LOOP_POLY, 15, 1)
PlaySound271LoopPolyB = Colour(127, 0, 0)

PlaySound256LoopOnceA = Colour(DMX_AUDIO_COMMAND_PLAY_LOOP_ONCE, 0, 1)
PlaySound256LoopOnceB = Colour(127, 0, 0)

PlaySound257LoopOnceA = Colour(DMX_AUDIO_COMMAND_PLAY_LOOP_ONCE, 1, 1)
PlaySound257LoopOnceB = Colour(127, 0, 0)

PlaySound258LoopOnceA = Colour(DMX_AUDIO_COMMAND_PLAY_LOOP_ONCE, 2, 1)
PlaySound258LoopOnceB = Colour(127, 0, 0)

PlaySound259LoopOnceA = Colour(DMX_AUDIO_COMMAND_PLAY_LOOP_ONCE, 3, 1)
PlaySound259LoopOnceB = Colour(127, 0, 0)

PlaySound260LoopOnceA = Colour(DMX_AUDIO_COMMAND_PLAY_LOOP_ONCE, 4, 1)
PlaySound260LoopOnceB = Colour(127, 0, 0)

PlaySound261LoopOnceA = Colour(DMX_AUDIO_COMMAND_PLAY_LOOP_ONCE, 5, 1)
PlaySound261LoopOnceB = Colour(127, 0, 0)

PlaySound262LoopOnceA = Colour(DMX_AUDIO_COMMAND_PLAY_LOOP_ONCE, 6, 1)
PlaySound262LoopOnceB = Colour(127, 0, 0)

PlaySound263LoopOnceA = Colour(DMX_AUDIO_COMMAND_PLAY_LOOP_ONCE, 7, 1)
PlaySound263LoopOnceB = Colour(127, 0, 0)

PlaySound264LoopOnceA = Colour(DMX_AUDIO_COMMAND_PLAY_LOOP_ONCE, 8, 1)
PlaySound264LoopOnceB = Colour(127, 0, 0)

PlaySound265LoopOnceA = Colour(DMX_AUDIO_COMMAND_PLAY_LOOP_ONCE, 9, 1)
PlaySound265LoopOnceB = Colour(127, 0, 0)

PlaySound266LoopOnceA = Colour(DMX_AUDIO_COMMAND_PLAY_LOOP_ONCE, 10, 1)
PlaySound266LoopOnceB = Colour(127, 0, 0)

PlaySound267LoopOnceA = Colour(DMX_AUDIO_COMMAND_PLAY_LOOP_ONCE, 11, 1)
PlaySound267LoopOnceB = Colour(127, 0, 0)

PlaySound268LoopOnceA = Colour(DMX_AUDIO_COMMAND_PLAY_LOOP_ONCE, 12, 1)
PlaySound268LoopOnceB = Colour(127, 0, 0)

PlaySound269LoopOnceA = Colour(DMX_AUDIO_COMMAND_PLAY_LOOP_ONCE, 13, 1)
PlaySound269LoopOnceB = Colour(127, 0, 0)

PlaySound270LoopOnceA = Colour(DMX_AUDIO_COMMAND_PLAY_LOOP_ONCE, 14, 1)
PlaySound270LoopOnceB = Colour(127, 0, 0)

PlaySound271LoopOnceA = Colour(DMX_AUDIO_COMMAND_PLAY_LOOP_ONCE, 15, 1)
PlaySound271LoopOnceB = Colour(127, 0, 0)

StopAllCommandA = Colour(DMX_AUDIO_COMMAND_STOP_ALL, 0, 0)
StopAllCommandB = Colour(0, 0, 0)

Stop1CommandA = Colour(DMX_AUDIO_COMMAND_STOP, 1, 0)
Stop1CommandB = Colour(0, 0, 0)

Stop0CommandA = Colour(DMX_AUDIO_COMMAND_STOP, 0, 0)
Stop0CommandB = Colour(0, 0, 0)

Stop256CommandA = Colour(DMX_AUDIO_COMMAND_STOP, 0, 1)
Stop256CommandB = Colour(0, 0, 0)

Stop257CommandA = Colour(DMX_AUDIO_COMMAND_STOP, 1, 1)
Stop257CommandB = Colour(0, 0, 0)

Stop258CommandA = Colour(DMX_AUDIO_COMMAND_STOP, 2, 1)
Stop258CommandB = Colour(0, 0, 0)

Stop259CommandA = Colour(DMX_AUDIO_COMMAND_STOP, 3, 1)
Stop259CommandB = Colour(0, 0, 0)

Stop260CommandA = Colour(DMX_AUDIO_COMMAND_STOP, 4, 1)
Stop260CommandB = Colour(0, 0, 0)

Stop261CommandA = Colour(DMX_AUDIO_COMMAND_STOP, 5, 1)
Stop261CommandB = Colour(0, 0, 0)

Stop262CommandA = Colour(DMX_AUDIO_COMMAND_STOP, 6, 1)
Stop262CommandB = Colour(0, 0, 0)

Stop263CommandA = Colour(DMX_AUDIO_COMMAND_STOP, 7, 1)
Stop263CommandB = Colour(0, 0, 0)

Stop264CommandA = Colour(DMX_AUDIO_COMMAND_STOP, 8, 1)
Stop264CommandB = Colour(0, 0, 0)

Stop265CommandA = Colour(DMX_AUDIO_COMMAND_STOP, 9, 1)
Stop265CommandB = Colour(0, 0, 0)

Stop266CommandA = Colour(DMX_AUDIO_COMMAND_STOP, 10, 1)
Stop266CommandB = Colour(0, 0, 0)

Stop267CommandA = Colour(DMX_AUDIO_COMMAND_STOP, 11, 1)
Stop267CommandB = Colour(0, 0, 0)

Stop268CommandA = Colour(DMX_AUDIO_COMMAND_STOP, 12, 1)
Stop268CommandB = Colour(0, 0, 0)

Stop269CommandA = Colour(DMX_AUDIO_COMMAND_STOP, 13, 1)
Stop269CommandB = Colour(0, 0, 0)

Stop270CommandA = Colour(DMX_AUDIO_COMMAND_STOP, 14, 1)
Stop270CommandB = Colour(0, 0, 0)

Stop271CommandA = Colour(DMX_AUDIO_COMMAND_STOP, 15, 1)
Stop271CommandB = Colour(0, 0, 0)

Pause0CommandA = Colour(DMX_AUDIO_COMMAND_PAUSE, 0, 0)
Pause0CommandB = Colour(0, 0, 0)

Pause1CommandA = Colour(DMX_AUDIO_COMMAND_PAUSE, 1, 0)
Pause1CommandB = Colour(0, 0, 0)

Resume0CommandA = Colour(DMX_AUDIO_COMMAND_RESUME, 0, 0)
Resume0CommandB = Colour(0, 0, 0)

Resume1CommandA = Colour(DMX_AUDIO_COMMAND_RESUME, 1, 0)
Resume1CommandB = Colour(0, 0, 0)

Volume0UpCommandA = Colour(DMX_AUDIO_COMMAND_TRACK_VOLUME, 0, 0)
Volume0UpCommandB = Colour(192, 0, 0)

Volume0DownCommandA = Colour(DMX_AUDIO_COMMAND_TRACK_VOLUME, 0, 0)
Volume0DownCommandB = Colour(64, 0, 0)

Volume1UpCommandA = Colour(DMX_AUDIO_COMMAND_TRACK_VOLUME, 1, 0)
Volume1UpCommandB = Colour(192, 0, 0)

Volume1DownCommandA = Colour(DMX_AUDIO_COMMAND_TRACK_VOLUME, 1, 0)
Volume1DownCommandB = Colour(64, 0, 0)

MasterVolumeUpCommandA = Colour(DMX_AUDIO_COMMAND_MASTER_VOLUME, 0, 0)
MasterVolumeUpCommandB = Colour(192, 0, 0)

MasterVolumeDownCommandA = Colour(DMX_AUDIO_COMMAND_MASTER_VOLUME, 0, 0)
MasterVolumeDownCommandB = Colour(64, 0, 0)