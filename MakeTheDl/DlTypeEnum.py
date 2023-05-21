#! /usr/bin/env python3
# -*- coding: utf-8 -*-
import os;
import sys;

from enum import Enum;

MODULE_PATH = os.path.dirname ( os.path.abspath ( __file__ ) );
sys.path.insert ( 0, MODULE_PATH );

class DlTypeEnum ( str, Enum ):
    full = "full"
    soundcloud = "soundcloud"
    deezer = "deezer"
    youtube = "youtube"
