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
    lightA.set_colour(testCommands.PlaySound1LoopMonoA)
    lightB.set_colour(testCommands.PlaySound1LoopMonoB)

    print("Playing sound 1, looping, moderate volume - did you hear it?")

    # Update the interface's frame to be the universe's current state
    interface.set_frame(universe.serialise())

    # Send an update to the DMX network
    interface.send_update()

    time.sleep(5)

    # Send a pause
    lightA.set_colour(Pause1CommandA)
	lightB.set_colour(Pause1CommandB)

    print("Sending a Pause 1 command, sound should pause")

    # Update the interface's frame to be the universe's current state
    interface.set_frame(universe.serialise())

    # Send an update to the DMX network
    interface.send_update()

    time.sleep(5)

    # Send a resume
    lightA.set_colour(Resume1CommandA)
    lightB.set_colour(Resume1CommandB)

    print("Sending a Resume 1 command, sound should resume")

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
