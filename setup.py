#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os;
import sys;

from setuptools import setup;

from MakeTheDl import __version__;


os.system ( '{binPip} install -r requirements'.format (
    binPip = os.path.join ( os.path.dirname ( sys.executable ), 'pip' )
) );


setup (
    name = 'MakeTheDl',
    version = __version__,
    description = 'Awesome Song Download Tool',
    url = 'https://github.com/Schwarzion/MakeTheDl',
    author = 'Victor Lehouck',
    author_email = 'victor.lehouck@gmail.com',
    license = 'MIT',
    packages = [
        'MakeTheDl',
        'mtd_entrypoints'
    ],
    install_requires = [
        'py-deezer',
        'ffmpeg',
        'yt-dlp',
        'typer'
    ],
    entry_points = {
        'console_scripts': [
            'makethedl = mtd_entrypoints.mtdl:app'
        ]
    },
    zip_safe = False
);