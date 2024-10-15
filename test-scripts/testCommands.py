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

PlaySound0OnceMonoA = Colour(DMX_AUDIO_COMMAND_PLAY_ONCE_MONO, 0, 0)
PlaySound0OnceMonoB = Colour(127, 0, 0)

PlaySound1OnceMonoA = Colour(DMX_AUDIO_COMMAND_PLAY_ONCE_MONO, 1, 0)
PlaySound1OnceMonoB = Colour(127, 0, 0)

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

PlaySound256LoopPolyLockedA = Colour(DMX_AUDIO_COMMAND_PLAY_LOOP_POLY_LOCKED, 0, 1)
PlaySound256LoopPolyLockedB = Colour(127, 0, 0)

PlaySound257LoopPolyLockedA = Colour(DMX_AUDIO_COMMAND_PLAY_LOOP_POLY_LOCKED, 1, 1)
PlaySound257LoopPolyLockedB = Colour(127, 0, 0)

PlaySound258LoopPolyLockedA = Colour(DMX_AUDIO_COMMAND_PLAY_LOOP_POLY_LOCKED, 2, 1)
PlaySound258LoopPolyLockedB = Colour(127, 0, 0)

PlaySound259LoopPolyLockedA = Colour(DMX_AUDIO_COMMAND_PLAY_LOOP_POLY_LOCKED, 3, 1)
PlaySound259LoopPolyLockedB = Colour(127, 0, 0)

PlaySound260LoopPolyLockedA = Colour(DMX_AUDIO_COMMAND_PLAY_LOOP_POLY_LOCKED, 4, 1)
PlaySound260LoopPolyLockedB = Colour(127, 0, 0)

PlaySound261LoopPolyLockedA = Colour(DMX_AUDIO_COMMAND_PLAY_LOOP_POLY_LOCKED, 5, 1)
PlaySound261LoopPolyLockedB = Colour(127, 0, 0)

PlaySound262LoopPolyLockedA = Colour(DMX_AUDIO_COMMAND_PLAY_LOOP_POLY_LOCKED, 6, 1)
PlaySound262LoopPolyLockedB = Colour(127, 0, 0)

PlaySound263LoopPolyLockedA = Colour(DMX_AUDIO_COMMAND_PLAY_LOOP_POLY_LOCKED, 7, 1)
PlaySound263LoopPolyLockedB = Colour(127, 0, 0)

PlaySound264LoopPolyLockedA = Colour(DMX_AUDIO_COMMAND_PLAY_LOOP_POLY_LOCKED, 8, 1)
PlaySound264LoopPolyLockedB = Colour(127, 0, 0)

PlaySound265LoopPolyLockedA = Colour(DMX_AUDIO_COMMAND_PLAY_LOOP_POLY_LOCKED, 9, 1)
PlaySound265LoopPolyLockedB = Colour(127, 0, 0)

PlaySound266LoopPolyLockedA = Colour(DMX_AUDIO_COMMAND_PLAY_LOOP_POLY_LOCKED, 10, 1)
PlaySound266LoopPolyLockedB = Colour(127, 0, 0)

PlaySound267LoopPolyLockedA = Colour(DMX_AUDIO_COMMAND_PLAY_LOOP_POLY_LOCKED, 11, 1)
PlaySound267LoopPolyLockedB = Colour(127, 0, 0)

PlaySound268LoopPolyLockedA = Colour(DMX_AUDIO_COMMAND_PLAY_LOOP_POLY_LOCKED, 12, 1)
PlaySound268LoopPolyLockedB = Colour(127, 0, 0)

PlaySound269LoopPolyLockedA = Colour(DMX_AUDIO_COMMAND_PLAY_LOOP_POLY_LOCKED, 13, 1)
PlaySound269LoopPolyLockedB = Colour(127, 0, 0)

PlaySound270LoopPolyLockedA = Colour(DMX_AUDIO_COMMAND_PLAY_LOOP_POLY_LOCKED, 14, 1)
PlaySound270LoopPolyLockedB = Colour(127, 0, 0)

PlaySound271LoopPolyLockedA = Colour(DMX_AUDIO_COMMAND_PLAY_LOOP_POLY_LOCKED, 15, 1)
PlaySound271LoopPolyLockedB = Colour(127, 0, 0)

PlaySound256OncePolyA = Colour(DMX_AUDIO_COMMAND_PLAY_ONCE_POLY, 0, 1)
PlaySound256OncePolyB = Colour(127, 0, 0)

PlaySound257OncePolyA = Colour(DMX_AUDIO_COMMAND_PLAY_ONCE_POLY, 1, 1)
PlaySound257OncePolyB = Colour(127, 0, 0)

PlaySound258OncePolyA = Colour(DMX_AUDIO_COMMAND_PLAY_ONCE_POLY, 2, 1)
PlaySound258OncePolyB = Colour(127, 0, 0)

PlaySound259OncePolyA = Colour(DMX_AUDIO_COMMAND_PLAY_ONCE_POLY, 3, 1)
PlaySound259OncePolyB = Colour(127, 0, 0)

PlaySound260OncePolyA = Colour(DMX_AUDIO_COMMAND_PLAY_ONCE_POLY, 4, 1)
PlaySound260OncePolyB = Colour(127, 0, 0)

PlaySound261OncePolyA = Colour(DMX_AUDIO_COMMAND_PLAY_ONCE_POLY, 5, 1)
PlaySound261OncePolyB = Colour(127, 0, 0)

PlaySound262OncePolyA = Colour(DMX_AUDIO_COMMAND_PLAY_ONCE_POLY, 6, 1)
PlaySound262OncePolyB = Colour(127, 0, 0)

PlaySound263OncePolyA = Colour(DMX_AUDIO_COMMAND_PLAY_ONCE_POLY, 7, 1)
PlaySound263OncePolyB = Colour(127, 0, 0)

PlaySound264OncePolyA = Colour(DMX_AUDIO_COMMAND_PLAY_ONCE_POLY, 8, 1)
PlaySound264OncePolyB = Colour(127, 0, 0)

PlaySound265OncePolyA = Colour(DMX_AUDIO_COMMAND_PLAY_ONCE_POLY, 9, 1)
PlaySound265OncePolyB = Colour(127, 0, 0)

PlaySound266OncePolyA = Colour(DMX_AUDIO_COMMAND_PLAY_ONCE_POLY, 10, 1)
PlaySound266OncePolyB = Colour(127, 0, 0)

PlaySound267OncePolyA = Colour(DMX_AUDIO_COMMAND_PLAY_ONCE_POLY, 11, 1)
PlaySound267OncePolyB = Colour(127, 0, 0)

PlaySound268OncePolyA = Colour(DMX_AUDIO_COMMAND_PLAY_ONCE_POLY, 12, 1)
PlaySound268OncePolyB = Colour(127, 0, 0)

PlaySound269OncePolyA = Colour(DMX_AUDIO_COMMAND_PLAY_ONCE_POLY, 13, 1)
PlaySound269OncePolyB = Colour(127, 0, 0)

PlaySound270OncePolyA = Colour(DMX_AUDIO_COMMAND_PLAY_ONCE_POLY, 14, 1)
PlaySound270OncePolyB = Colour(127, 0, 0)

PlaySound271OncePolyA = Colour(DMX_AUDIO_COMMAND_PLAY_ONCE_POLY, 15, 1)
PlaySound271OncePolyB = Colour(127, 0, 0)

PlaySound256OncePolyLockedA = Colour(DMX_AUDIO_COMMAND_PLAY_ONCE_POLY_LOCKED, 0, 1)
PlaySound256OncePolyLockedB = Colour(127, 0, 0)

PlaySound257OncePolyLockedA = Colour(DMX_AUDIO_COMMAND_PLAY_ONCE_POLY_LOCKED, 1, 1)
PlaySound257OncePolyLockedB = Colour(127, 0, 0)

PlaySound258OncePolyLockedA = Colour(DMX_AUDIO_COMMAND_PLAY_ONCE_POLY_LOCKED, 2, 1)
PlaySound258OncePolyLockedB = Colour(127, 0, 0)

PlaySound259OncePolyLockedA = Colour(DMX_AUDIO_COMMAND_PLAY_ONCE_POLY_LOCKED, 3, 1)
PlaySound259OncePolyLockedB = Colour(127, 0, 0)

PlaySound260OncePolyLockedA = Colour(DMX_AUDIO_COMMAND_PLAY_ONCE_POLY_LOCKED, 4, 1)
PlaySound260OncePolyLockedB = Colour(127, 0, 0)

PlaySound261OncePolyLockedA = Colour(DMX_AUDIO_COMMAND_PLAY_ONCE_POLY_LOCKED, 5, 1)
PlaySound261OncePolyLockedB = Colour(127, 0, 0)

PlaySound262OncePolyLockedA = Colour(DMX_AUDIO_COMMAND_PLAY_ONCE_POLY_LOCKED, 6, 1)
PlaySound262OncePolyLockedB = Colour(127, 0, 0)

PlaySound263OncePolyLockedA = Colour(DMX_AUDIO_COMMAND_PLAY_ONCE_POLY_LOCKED, 7, 1)
PlaySound263OncePolyLockedB = Colour(127, 0, 0)

PlaySound264OncePolyLockedA = Colour(DMX_AUDIO_COMMAND_PLAY_ONCE_POLY_LOCKED, 8, 1)
PlaySound264OncePolyLockedB = Colour(127, 0, 0)

PlaySound265OncePolyLockedA = Colour(DMX_AUDIO_COMMAND_PLAY_ONCE_POLY_LOCKED, 9, 1)
PlaySound265OncePolyLockedB = Colour(127, 0, 0)

PlaySound266OncePolyLockedA = Colour(DMX_AUDIO_COMMAND_PLAY_ONCE_POLY_LOCKED, 10, 1)
PlaySound266OncePolyLockedB = Colour(127, 0, 0)

PlaySound267OncePolyLockedA = Colour(DMX_AUDIO_COMMAND_PLAY_ONCE_POLY_LOCKED, 11, 1)
PlaySound267OncePolyLockedB = Colour(127, 0, 0)

PlaySound268OncePolyLockedA = Colour(DMX_AUDIO_COMMAND_PLAY_ONCE_POLY_LOCKED, 12, 1)
PlaySound268OncePolyLockedB = Colour(127, 0, 0)

PlaySound269OncePolyLockedA = Colour(DMX_AUDIO_COMMAND_PLAY_ONCE_POLY_LOCKED, 13, 1)
PlaySound269OncePolyLockedB = Colour(127, 0, 0)

PlaySound270OncePolyLockedA = Colour(DMX_AUDIO_COMMAND_PLAY_ONCE_POLY_LOCKED, 14, 1)
PlaySound270OncePolyLockedB = Colour(127, 0, 0)

PlaySound271OncePolyLockedA = Colour(DMX_AUDIO_COMMAND_PLAY_ONCE_POLY_LOCKED, 15, 1)
PlaySound271OncePolyLockedB = Colour(127, 0, 0)

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

Pause256CommandA = Colour(DMX_AUDIO_COMMAND_PAUSE, 0, 1)
Pause256CommandB = Colour(0, 0, 0)

Pause257CommandA = Colour(DMX_AUDIO_COMMAND_PAUSE, 1, 1)
Pause257CommandB = Colour(0, 0, 0)

Pause258CommandA = Colour(DMX_AUDIO_COMMAND_PAUSE, 2, 1)
Pause258CommandB = Colour(0, 0, 0)

Pause259CommandA = Colour(DMX_AUDIO_COMMAND_PAUSE, 3, 1)
Pause259CommandB = Colour(0, 0, 0)

Pause260CommandA = Colour(DMX_AUDIO_COMMAND_PAUSE, 4, 1)
Pause260CommandB = Colour(0, 0, 0)

Pause261CommandA = Colour(DMX_AUDIO_COMMAND_PAUSE, 5, 1)
Pause261CommandB = Colour(0, 0, 0)

Pause262CommandA = Colour(DMX_AUDIO_COMMAND_PAUSE, 6, 1)
Pause262CommandB = Colour(0, 0, 0)

Pause263CommandA = Colour(DMX_AUDIO_COMMAND_PAUSE, 7, 1)
Pause263CommandB = Colour(0, 0, 0)

Pause264CommandA = Colour(DMX_AUDIO_COMMAND_PAUSE, 8, 1)
Pause264CommandB = Colour(0, 0, 0)

Pause265CommandA = Colour(DMX_AUDIO_COMMAND_PAUSE, 9, 1)
Pause265CommandB = Colour(0, 0, 0)

Pause266CommandA = Colour(DMX_AUDIO_COMMAND_PAUSE, 10, 1)
Pause266CommandB = Colour(0, 0, 0)

Pause267CommandA = Colour(DMX_AUDIO_COMMAND_PAUSE, 11, 1)
Pause267CommandB = Colour(0, 0, 0)

Pause268CommandA = Colour(DMX_AUDIO_COMMAND_PAUSE, 12, 1)
Pause268CommandB = Colour(0, 0, 0)

Pause269CommandA = Colour(DMX_AUDIO_COMMAND_PAUSE, 13, 1)
Pause269CommandB = Colour(0, 0, 0)

Pause270CommandA = Colour(DMX_AUDIO_COMMAND_PAUSE, 14, 1)
Pause270CommandB = Colour(0, 0, 0)

Pause271CommandA = Colour(DMX_AUDIO_COMMAND_PAUSE, 15, 1)
Pause271CommandB = Colour(0, 0, 0)

Resume0CommandA = Colour(DMX_AUDIO_COMMAND_RESUME, 0, 0)
Resume0CommandB = Colour(0, 0, 0)

Resume1CommandA = Colour(DMX_AUDIO_COMMAND_RESUME, 1, 0)
Resume1CommandB = Colour(0, 0, 0)

Resume256CommandA = Colour(DMX_AUDIO_COMMAND_RESUME, 0, 1)
Resume256CommandB = Colour(0, 0, 0)

Resume257CommandA = Colour(DMX_AUDIO_COMMAND_RESUME, 1, 1)
Resume257CommandB = Colour(0, 0, 0)

Resume258CommandA = Colour(DMX_AUDIO_COMMAND_RESUME, 2, 1)
Resume258CommandB = Colour(0, 0, 0)

Resume259CommandA = Colour(DMX_AUDIO_COMMAND_RESUME, 3, 1)
Resume259CommandB = Colour(0, 0, 0)

Resume260CommandA = Colour(DMX_AUDIO_COMMAND_RESUME, 4, 1)
Resume260CommandB = Colour(0, 0, 0)

Resume261CommandA = Colour(DMX_AUDIO_COMMAND_RESUME, 5, 1)
Resume261CommandB = Colour(0, 0, 0)

Resume262CommandA = Colour(DMX_AUDIO_COMMAND_RESUME, 6, 1)
Resume262CommandB = Colour(0, 0, 0)

Resume263CommandA = Colour(DMX_AUDIO_COMMAND_RESUME, 7, 1)
Resume263CommandB = Colour(0, 0, 0)

Resume264CommandA = Colour(DMX_AUDIO_COMMAND_RESUME, 8, 1)
Resume264CommandB = Colour(0, 0, 0)

Resume265CommandA = Colour(DMX_AUDIO_COMMAND_RESUME, 9, 1)
Resume265CommandB = Colour(0, 0, 0)

Resume266CommandA = Colour(DMX_AUDIO_COMMAND_RESUME, 10, 1)
Resume266CommandB = Colour(0, 0, 0)

Resume267CommandA = Colour(DMX_AUDIO_COMMAND_RESUME, 11, 1)
Resume267CommandB = Colour(0, 0, 0)

Resume268CommandA = Colour(DMX_AUDIO_COMMAND_RESUME, 12, 1)
Resume268CommandB = Colour(0, 0, 0)

Resume269CommandA = Colour(DMX_AUDIO_COMMAND_RESUME, 13, 1)
Resume269CommandB = Colour(0, 0, 0)

Resume270CommandA = Colour(DMX_AUDIO_COMMAND_RESUME, 14, 1)
Resume270CommandB = Colour(0, 0, 0)

Resume271CommandA = Colour(DMX_AUDIO_COMMAND_RESUME, 15, 1)
Resume271CommandB = Colour(0, 0, 0)

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

MasterVolumeNormalCommandA = Colour(DMX_AUDIO_COMMAND_MASTER_VOLUME, 0, 0)
MasterVolumeNormalCommandB = Colour(127, 0, 0)