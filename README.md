# Make The Dl

## Description
Simple python lib wrapper to download songs from :
- [x] Deezer
- [x] Youtube
- [ ] Soundcloud

Made to work with playlists.

All downloads are made in MP3 320 kbit/s.

## DEPENDENCIES

[yt-dlp](https://github.com/yt-dlp/yt-dlp) : youtube info gathering tool package. Licensed under [Unlicense](https://github.com/yt-dlp/yt-dlp/blob/master/LICENSE)

[py-deezer](https://github.com/acgonzales/pydeezer) : deezer info gathering tool package. Licensed under [GNU GPL v3.0](https://choosealicense.com/licenses/gpl-3.0/)


## Requirements

### Python

Tested on Python 3.9.2

Pip version : 20.3.4

### Pip requirements
See requirements / setup file

## Specific platform authentication needs

### Deezer
arl: it's the token used in your cookies that deezer API use
You can get it in the cookies using your browser when connected to deezer (variable : arl)


## How to

### Install

Clone the repo
```bash
$ git clone https://github.com/Schwarzion/MakeTheDl.git
$ cd MakeTheDl
$ python setup.py install
```

### Commands

Before every commands (ensure configs are taken in account)
```bash
cd /path/to/dir/with/.env/file
```

Add completion to your bash (Using typer)
```bash
$ makethedl --install-completion
```

Help
```bash
$ makethedl --help
```

Example
```bash
$ makethedl deezer
```


### Configuration

This package is using a .env file
Be sure to copy .env.example file and provide all the informations you need in order to start

| .env.example | 
| --- |
```ini 
[Deezer]
DEEZER_ARL=<Deezer_ARL>
DEEZER_DL_LOCATION=</path/to/wanted/location/for/deezer/songs>
DEEZER_PLAYLIST_ID=<Playlist_ID>

[Youtube]
YT_PLAYLIST=<Youtube_Playlist_Link>
YT_DL_LOCATION=/path/to/wanted/location/for/youtube/songs
#Where download archive should be placed (differential download)
YT_ARCHIVE_DIR=/path/to/archive/directory

[Soundcloud]
CLIENT_ID=
AUTH_TOKEN=
PATH=
NAME_FORMAT=
PLAYLIST_NAME_FORMAT=
DEEZER_DL_LOCATION=/path/to/wanted/location/for/soundcloud/songs
```


## Next steps
- [ ] Windows paths handling
- [ ] Unit testing
- [ ] Improved CLI
- [ ] Automated package publishing from tags
- [ ] Conf file (not .env)
- Archive management (differential download) :
    - [ ] Deezer
    - [x] Youtube
    - [ ] Soundcloud
- Not rely on download libs -> build every downloader from scratch :
    - [ ] Deezer
    - [ ] Youtube
    - [ ] Soundcloud


## Disclaimer

Never use this package illegally against any of :
- Deezer [terms of use](https://developers.deezer.com/termsofuse)
- Soundcloud [terms of use](https://soundcloud.com/terms-of-use)
- Youtube [terms of use](https://www.youtube.com/static?template=terms)

None of the maintainers / developers can be held responsible for misuse of this package.


## License

Licensed under [MIT](https://choosealicense.com/licenses/mit/)