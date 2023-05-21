#! /usr/bin/env python3
# -*- coding: utf-8 -*-
import os;
import sys;

from yt_dlp import YoutubeDL as Youtube_dl_service;

MODULE_PATH = os.path.dirname ( os.path.abspath ( __file__ ) );
sys.path.insert ( 0, MODULE_PATH );

from MakeTheDl.AbstractDl import AbstractDl;


class MyLogger:
    def debug ( self, msg ):
        if msg.startswith ( '[debug] ' ):
            pass;
        else:
            self.info ( msg );

    def info ( self, msg ):
        print ( msg );

    def warning ( self, msg):
        print ( values = msg, file = sys.stderr );

    def error ( self, msg):
        print ( values = msg, file = sys.stderr  );


def my_hook ( d ):
    if d [ 'status' ] == 'finished':
        print ( 'Done downloading, now post-processing ...' );


class YoutubeDl ( AbstractDl ):
    def __init__ ( self, playlist: str, location: str, archive_dir: str):

        super () .__init__ (
            location = location
        );
        
        
        if archive_dir [-1]  == '/':
            self._archive_dir: str = f'{archive_dir}youtube_archive';
        else:
            self._archive_dir: str = f'{archive_dir}/youtube_archive';

        self._playlist: str = playlist;


    def download_playlist ( self ) -> bool:
        ydl_opts = {
            'paths': { 'home' : self.location },
            'logger': MyLogger (),
            'progress_hooks': [ my_hook ],
            'format': 'bestaudio/best',
            'postprocessors': [{
                'key': 'FFmpegExtractAudio',
                'preferredcodec': 'mp3',
                'preferredquality': '338'
            }],
            'download_archive': f'{ self._archive_dir }',
            'outtmpl': "%(title)s.%(ext)s",
            'quiet': True
        };
        
        Youtube_dl_service ( ydl_opts ) .download ( [ self._playlist ] );
