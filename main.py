#!/usr/bin/python3
import subprocess


def screens():
    output = [l for l in
              subprocess.check_output(["xrandr"]).decode("utf-8").splitlines()]
    monitor = []
    resolution = []
    for i, j in zip(output, output[1:]):
        if " connected " in i:
            monitor.append(i.split()[0])
            resolution.append(j.split()[0])
    return (monitor, resolution)


# tuple of list
# the first list is the monitor names
# the second the resolutions
monitors = screens()

foreign_width = int(monitors[1][1].split('x')[0])
foreign_height = int(monitors[1][1].split('x')[1])
normal_height = int(monitors[1][0].split('x')[1])
# SWAP LINE TAKE THIS SHIT OUT BOI
foreign_width, foreign_height = foreign_height, foreign_width
foreign_name = monitors[0][1]
main_name = monitors[0][0]
a = foreign_width
b = foreign_height - normal_height
# (a, b) is the coord pos to place the main display at
command = f'xrandr --output {foreign_name} --auto --pos 0x0 --output {main_name} --auto --primary --pos {a}x{b}'

print(command)
