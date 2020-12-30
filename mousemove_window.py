#!/usr/bin/env python3
import os
from pathlib import Path
import sys

__projectdir__ = Path(os.path.dirname(os.path.realpath(__file__)) + '/')


def movetowindowpos(horzper, vertper):
    import subprocess

    horzco = None
    vertco = None

    pid = subprocess.check_output(['xdotool','getwindowfocus'])
    pid = pid.decode('utf-8')

    output = subprocess.check_output(['xdotool', 'getwindowgeometry', pid])
    output = output.decode('utf-8')
    temp = output.split('\n')[2]
    temp = temp.replace('Geometry: ', '')
    width = int(temp.split('x')[0])
    height = int(temp.split('x')[1])

    subprocess.call(['xdotool', 'mousemove', '--window', pid, str(horzper * width / 100), str(vertper * height / 100)])


def movetowindowpos_ap():
    import argparse
    parser=argparse.ArgumentParser()
    parser.add_argument("--horzper",type=int,help="integer percentage distance from left")
    parser.add_argument("--vertper",type=int,help="integer percentage distance from top")

    args=parser.parse_args()

    movetowindowpos(args.horzper, args.vertper)
