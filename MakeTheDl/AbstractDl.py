#! /usr/bin/env python3
# -*- coding: utf-8 -*-
import os;
import sys;

from abc import ABC, abstractmethod;

MODULE_PATH = os.path.dirname ( os.path.abspath ( __file__ ) );
sys.path.insert ( 0, MODULE_PATH );

class AbstractDl ( ABC ):
    
    def __init__ ( self, location: str ):
        self.location: str = location;
        print ( 'AbstractDL :: init');