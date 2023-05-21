#! /usr/bin/env python3
# -*- coding: utf-8 -*-
import os;
import sys

from pprint import pprint;
from pydeezer import Deezer;
from pydeezer import Downloader
from pydeezer.constants import track_formats

MODULE_PATH = os.path.dirname ( os.path.abspath ( __file__ ) );
sys.path.insert ( 0, MODULE_PATH );

from MakeTheDl.AbstractDl import AbstractDl;


class DeezerDl ( AbstractDl ):
    def __init__ ( self, arl: str, playlist_id: str, location: str):
        print ( 'DeezerDl :: init');
    
        super () .__init__ (
            location = location
        );
        
        self._playlist_id = playlist_id;
        
        self._dl_service: Deezer = None;
        self.__arl_token: str = None;

        """Resources init"""
        self._init_resources (
            arl_token = arl
        );


    def _init_resources ( self, arl_token: str ):
        """init resources

        Args:
            arl_token (str): auth arl_token
        """
        self.set_arl_token (
            arl_token = arl_token
        );
        
        self._init_dl_service ();


    def _init_dl_service ( self ):
        print ( 'Deezer Service :: init');
        self._dl_service = Deezer ();

        user = self._dl_service.login_via_arl (
            self.get_arl_token ()
        );
        print ( 'Deezer Service :: logged');
        
        self.set_user ( user );
        print ( 'Deezer Service :: got user');

    def set_arl_token ( self, arl_token: str ):
        """arl_token Accessor : set

        Args:
            arl_token (str): auth arl_token
        """
        self.__arl_token = arl_token;


    def get_arl_token ( self ):
        """arl_token Accessor : get

        Returns:
            str: auth arl_token
        """
        return self.__arl_token;
    

    def set_user ( self, user: dict):
        """user Accessor : set

        Args:
            user (str): authenticated user
        """
        self.__user = user;


    def get_user ( self ) -> dict:
        """user Accessor : get

        Returns:
            dict: deezer user
        """
        return self.__user;
    

    def get_playlist ( self ) -> dict:
        """Return playlist information from playlist ID

        Returns:
            dict: playlist info
        """
        return self._dl_service.get_playlist ( self._playlist_id );
    
    
    def get_playlist_ids ( self ) -> list:
        """Retrieve playlist songs and parse it to keep only song ids

        Returns:
            list: list of song ids
        """
        playlist_info: dict = self.get_playlist ();
        playlist_ids: list = [];
        for songs in playlist_info [ 'SONGS' ] [ 'data' ]:
            playlist_ids.append ( songs [ 'SNG_ID' ] );
        return playlist_ids;
    
    
    def download_playlist ( self ) -> bool:
        """Download songs from deezer playlist

        Returns:
            bool: success
        """
        ids: list = self.get_playlist_ids ();

        downloader = Downloader (
            deezer = self._dl_service,
            track_ids_to_download = ids,
            download_dir = self.location,
            quality = track_formats.MP3_320,
            concurrent_downloads = 10
        );
        downloader.start ();
        return True;