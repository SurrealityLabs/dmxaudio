#!/usr/bin/python

from dmx import Colour, DMXInterface, DMXLight3Slot, DMXUniverse
import testCommands
import time

# Open an interface
with DMXInterface("FT232R") as interface:
    # Create a universe
    universe = DMXUniverse()

    # Define a light
    lightA = DMXLight3Slot(address=0)
    lightB = DMXLight3Slot(address=3)

    # Add the light to a universe
    universe.add_light(lightA)
    universe.add_light(lightB)

    # Update the interface's frame to be the universe's current state
    interface.set_frame(universe.serialise())

    # Send an update to the DMX network
    interface.send_update()

    # Play the sound
    lightA.set_colour(testCommands.PlaySound256LoopPolyLockedA)
    lightB.set_colour(testCommands.PlaySound256LoopPolyLockedB)

    print("Playing sound 256, looping, moderate volume - did you hear it?")

    # Update the interface's frame to be the universe's current state
    interface.set_frame(universe.serialise())

    # Send an update to the DMX network
    interface.send_update()

    time.sleep(5)

    # Play the sound
    lightA.set_colour(testCommands.PlaySound257LoopPolyLockedA)
    lightB.set_colour(testCommands.PlaySound257LoopPolyLockedB)

    print("Playing sound 257, looping, moderate volume - did you hear it?")

    # Update the interface's frame to be the universe's current state
    interface.set_frame(universe.serialise())

    # Send an update to the DMX network
    interface.send_update()

    time.sleep(5)

    # Play the sound
    lightA.set_colour(testCommands.PlaySound258LoopPolyLockedA)
    lightB.set_colour(testCommands.PlaySound258LoopPolyLockedB)

    print("Playing sound 258, looping, moderate volume - did you hear it?")

    # Update the interface's frame to be the universe's current state
    interface.set_frame(universe.serialise())

    # Send an update to the DMX network
    interface.send_update()

    time.sleep(5)

    # Play the sound
    lightA.set_colour(testCommands.PlaySound259LoopPolyLockedA)
    lightB.set_colour(testCommands.PlaySound259LoopPolyLockedB)

    print("Playing sound 259, looping, moderate volume - did you hear it?")

    # Update the interface's frame to be the universe's current state
    interface.set_frame(universe.serialise())

    # Send an update to the DMX network
    interface.send_update()

    time.sleep(5)

    # Play the sound
    lightA.set_colour(testCommands.PlaySound260LoopPolyLockedA)
    lightB.set_colour(testCommands.PlaySound260LoopPolyLockedB)

    print("Playing sound 260, looping, moderate volume - did you hear it?")

    # Update the interface's frame to be the universe's current state
    interface.set_frame(universe.serialise())

    # Send an update to the DMX network
    interface.send_update()

    time.sleep(5)

    # Play the sound
    lightA.set_colour(testCommands.PlaySound261LoopPolyLockedA)
    lightB.set_colour(testCommands.PlaySound261LoopPolyLockedB)

    print("Playing sound 261, looping, moderate volume - did you hear it?")

    # Update the interface's frame to be the universe's current state
    interface.set_frame(universe.serialise())

    # Send an update to the DMX network
    interface.send_update()

    time.sleep(5)

    # Play the sound
    lightA.set_colour(testCommands.PlaySound262LoopPolyLockedA)
    lightB.set_colour(testCommands.PlaySound262LoopPolyLockedB)

    print("Playing sound 262, looping, moderate volume - did you hear it?")

    # Update the interface's frame to be the universe's current state
    interface.set_frame(universe.serialise())

    # Send an update to the DMX network
    interface.send_update()

    time.sleep(5)

    # Play the sound
    lightA.set_colour(testCommands.PlaySound263LoopPolyLockedA)
    lightB.set_colour(testCommands.PlaySound263LoopPolyLockedB)

    print("Playing sound 263, looping, moderate volume - did you hear it?")

    # Update the interface's frame to be the universe's current state
    interface.set_frame(universe.serialise())

    # Send an update to the DMX network
    interface.send_update()

    time.sleep(5)

    # Pause sound 256
    lightA.set_colour(testCommands.Pause256CommandA)
    lightB.set_colour(testCommands.Pause256CommandB)

    print("Pausing sound 256, it should pause")

    # Update the interface's frame to be the universe's current state
    interface.set_frame(universe.serialise())

    # Send an update to the DMX network
    interface.send_update()

    time.sleep(5)

    # Resume sound 256
    lightA.set_colour(testCommands.Resume256CommandA)
    lightB.set_colour(testCommands.Resume256CommandB)

    print("Resuming sound 256, it should resume")

    # Update the interface's frame to be the universe's current state
    interface.set_frame(universe.serialise())

    # Send an update to the DMX network
    interface.send_update()

    time.sleep(5)

    # Pause sound 257
    lightA.set_colour(testCommands.Pause257CommandA)
    lightB.set_colour(testCommands.Pause257CommandB)

    print("Pausing sound 257, it should pause")

    # Update the interface's frame to be the universe's current state
    interface.set_frame(universe.serialise())

    # Send an update to the DMX network
    interface.send_update()

    time.sleep(5)

    # Resume sound 257
    lightA.set_colour(testCommands.Resume257CommandA)
    lightB.set_colour(testCommands.Resume257CommandB)

    print("Resuming sound 257, it should resume")

    # Update the interface's frame to be the universe's current state
    interface.set_frame(universe.serialise())

    # Send an update to the DMX network
    interface.send_update()

    time.sleep(5)

    # Pause sound 258
    lightA.set_colour(testCommands.Pause258CommandA)
    lightB.set_colour(testCommands.Pause258CommandB)

    print("Pausing sound 258, it should pause")

    # Update the interface's frame to be the universe's current state
    interface.set_frame(universe.serialise())

    # Send an update to the DMX network
    interface.send_update()

    time.sleep(5)

    # Resume sound 258
    lightA.set_colour(testCommands.Resume258CommandA)
    lightB.set_colour(testCommands.Resume258CommandB)

    print("Resuming sound 258, it should resume")

    # Update the interface's frame to be the universe's current state
    interface.set_frame(universe.serialise())

    # Send an update to the DMX network
    interface.send_update()

    time.sleep(5)

    # Pause sound 259
    lightA.set_colour(testCommands.Pause259CommandA)
    lightB.set_colour(testCommands.Pause259CommandB)

    print("Pausing sound 259, it should pause")

    # Update the interface's frame to be the universe's current state
    interface.set_frame(universe.serialise())

    # Send an update to the DMX network
    interface.send_update()

    time.sleep(5)

    # Resume sound 259
    lightA.set_colour(testCommands.Resume259CommandA)
    lightB.set_colour(testCommands.Resume259CommandB)

    print("Resuming sound 259, it should resume")

    # Update the interface's frame to be the universe's current state
    interface.set_frame(universe.serialise())

    # Send an update to the DMX network
    interface.send_update()

    time.sleep(5)

    # Pause sound 260
    lightA.set_colour(testCommands.Pause260CommandA)
    lightB.set_colour(testCommands.Pause260CommandB)

    print("Pausing sound 260, it should pause")

    # Update the interface's frame to be the universe's current state
    interface.set_frame(universe.serialise())

    # Send an update to the DMX network
    interface.send_update()

    time.sleep(5)

    # Resume sound 260
    lightA.set_colour(testCommands.Resume260CommandA)
    lightB.set_colour(testCommands.Resume260CommandB)

    print("Resuming sound 260, it should resume")

    # Update the interface's frame to be the universe's current state
    interface.set_frame(universe.serialise())

    # Send an update to the DMX network
    interface.send_update()

    time.sleep(5)

    # Pause sound 261
    lightA.set_colour(testCommands.Pause261CommandA)
    lightB.set_colour(testCommands.Pause261CommandB)

    print("Pausing sound 261, it should pause")

    # Update the interface's frame to be the universe's current state
    interface.set_frame(universe.serialise())

    # Send an update to the DMX network
    interface.send_update()

    time.sleep(5)

    # Resume sound 261
    lightA.set_colour(testCommands.Resume261CommandA)
    lightB.set_colour(testCommands.Resume261CommandB)

    print("Resuming sound 261, it should resume")

    # Update the interface's frame to be the universe's current state
    interface.set_frame(universe.serialise())

    # Send an update to the DMX network
    interface.send_update()

    time.sleep(5)

    # Pause sound 262
    lightA.set_colour(testCommands.Pause262CommandA)
    lightB.set_colour(testCommands.Pause262CommandB)

    print("Pausing sound 262, it should pause")

    # Update the interface's frame to be the universe's current state
    interface.set_frame(universe.serialise())

    # Send an update to the DMX network
    interface.send_update()

    time.sleep(5)

    # Resume sound 262
    lightA.set_colour(testCommands.Resume262CommandA)
    lightB.set_colour(testCommands.Resume262CommandB)

    print("Resuming sound 262, it should resume")

    # Update the interface's frame to be the universe's current state
    interface.set_frame(universe.serialise())

    # Send an update to the DMX network
    interface.send_update()

    time.sleep(5)

    # Pause sound 263
    lightA.set_colour(testCommands.Pause263CommandA)
    lightB.set_colour(testCommands.Pause263CommandB)

    print("Pausing sound 263, it should pause")

    # Update the interface's frame to be the universe's current state
    interface.set_frame(universe.serialise())

    # Send an update to the DMX network
    interface.send_update()

    time.sleep(5)

    # Resume sound 263
    lightA.set_colour(testCommands.Resume263CommandA)
    lightB.set_colour(testCommands.Resume263CommandB)

    print("Resuming sound 263, it should resume")

    # Update the interface's frame to be the universe's current state
    interface.set_frame(universe.serialise())

    # Send an update to the DMX network
    interface.send_update()

    time.sleep(5)

    # Send a Stop All
    lightA.set_colour(StopAllCommandA)
    lightB.set_colour(StopAllCommandB)

    print("Sending a Stop All, sound should stop")

    # Update the interface's frame to be the universe's current state
    interface.set_frame(universe.serialise())

    # Send an update to the DMX network
    interface.send_update()
