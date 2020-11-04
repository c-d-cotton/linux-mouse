#!/usr/bin/env python3
# PYTHON_PREAMBLE_START_STANDARD:{{{

# Christopher David Cotton (c)
# http://www.cdcotton.com

# modules needed for preamble
import importlib
import os
from pathlib import Path
import sys

# Get full real filename
__fullrealfile__ = os.path.abspath(__file__)

# Function to get git directory containing this file
def getprojectdir(filename):
    curlevel = filename
    while curlevel is not '/':
        curlevel = os.path.dirname(curlevel)
        if os.path.exists(curlevel + '/.git/'):
            return(curlevel + '/')
    return(None)

# Directory of project
__projectdir__ = Path(getprojectdir(__fullrealfile__))

# Function to call functions from files by their absolute path.
# Imports modules if they've not already been imported
# First argument is filename, second is function name, third is dictionary containing loaded modules.
modulesdict = {}
def importattr(modulefilename, func, modulesdict = modulesdict):
    # get modulefilename as string to prevent problems in <= python3.5 with pathlib -> os
    modulefilename = str(modulefilename)
    # if function in this file
    if modulefilename == __fullrealfile__:
        return(eval(func))
    else:
        # add file to moduledict if not there already
        if modulefilename not in modulesdict:
            # check filename exists
            if not os.path.isfile(modulefilename):
                raise Exception('Module not exists: ' + modulefilename + '. Function: ' + func + '. Filename called from: ' + __fullrealfile__ + '.')
            # add directory to path
            sys.path.append(os.path.dirname(modulefilename))
            # actually add module to moduledict
            modulesdict[modulefilename] = importlib.import_module(''.join(os.path.basename(modulefilename).split('.')[: -1]))

        # get the actual function from the file and return it
        return(getattr(modulesdict[modulefilename], func))

# PYTHON_PREAMBLE_END:}}}


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

    importattr(__projectdir__ / Path('mousemove_window.py'), 'movetowindowpos')(args.horzper, args.vertper)
