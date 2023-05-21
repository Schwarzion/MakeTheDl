#! /usr/bin/env python3
# -*- coding: utf-8 -*-
import os;
import sys;

import typer;
import warnings;


from cryptography.utils import CryptographyDeprecationWarning
from dotenv import dotenv_values;
from typing_extensions import Annotated;


MODULE_PATH = os.path.dirname ( os.path.abspath ( __file__ ) );
sys.path.insert ( 0, MODULE_PATH );


from MakeTheDl.DlTypeEnum import DlTypeEnum
from MakeTheDl.DeezerDl import DeezerDl;
from MakeTheDl.SoundcloudDl import SoundcloudDl;
from MakeTheDl.YoutubeDl import YoutubeDl;


config = dotenv_values ( ".env" );
app = typer.Typer (
    help = "Awesome Song Download Tool",
    pretty_exceptions_show_locals = False
);
dl_type_enum_annotation = Annotated [ DlTypeEnum, typer.Option ( default = None, case_sensitive = False ) ];
warnings.filterwarnings ( "ignore", category=CryptographyDeprecationWarning );


def fromYoutube ( playlist: str, location: str, archive_dir: str ) -> bool:
    youtube_dl = YoutubeDl (
        playlist = playlist,
        location = location,
        archive_dir = archive_dir
    );
    youtube_dl.download_playlist ();
    return True;


def fromDeezer ( arl: str, playlist_id: str, location: str ) -> bool:
    deezer_dl = DeezerDl (
        arl = arl,
        playlist_id = playlist_id,
        location = location
    );
    deezer_dl.download_playlist ();
    return True;


def fromSoundcloud ( auth_token: str, location: str ) -> bool:
    soundcloud_dl = SoundcloudDl (
        token = auth_token,
        location = location
    );
    return True;


@app.command ()
def dl ( dl_type: dl_type_enum_annotation ) -> None:
    run_all: bool = False;
   
    if dl_type == 'full':
        run_all = True;
    
    if dl_type == 'youtube' or run_all:
        fromYoutube (
            playlist = config [ "YT_PLAYLIST" ],
            location = config [ "YT_DL_LOCATION" ],
            archive_dir = config [ "YT_ARCHIVE_DIR" ]
        );

    if dl_type == 'deezer' or run_all:
        fromDeezer ( 
            arl = config [ "DEEZER_ARL" ],
            playlist_id = config [ "DEEZER_PLAYLIST_ID" ],
            location = config [ "DEEZER_DL_LOCATION" ]
        );
    if dl_type == 'soundcloud' or run_all:
        fromSoundcloud (
            auth_token = config [ "AUTH_TOKEN" ],
            location = config [ "SOUNDCLOUD_DL_LOCATION" ]
        );


if __name__ == "__main__":
    app ()