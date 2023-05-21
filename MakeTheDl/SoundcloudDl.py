#! /usr/bin/env python3
# -*- coding: utf-8 -*-
import os;
import sys;

MODULE_PATH = os.path.dirname ( os.path.abspath ( __file__ ) );
sys.path.insert ( 0, MODULE_PATH );

from MakeTheDl.AbstractDl import AbstractDl;


class SoundcloudDl ( AbstractDl ):
    def __init__ ( self, token: str, location: str):
        print ( 'DeezerDl :: init');
    
        """Super init"""
        super () .__init__ (
            location = location
        );
        
        """Resources init"""
        self._init_resources (
            token = token
        );


    def _init_resources ( self, token: str ):
        """init resources

        Args:
            token (str): auth token
        """
        self.set_token (
            token = token
        );


    def set_token ( self, token: str ):
        """Token Accessor : set

        Args:
            token (str): auth token
        """
        self.__token = token;


    def get_token ( self ):
        """Token Accessor : get

        Returns:
            str: auth token
        """
        return self.__token;
    
    # def download_playlist ( self ) -> bool:
    #     ids = [];
        