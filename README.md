# Remote video processing
##### with moviepy

### Setup the environment

- Download and install moviepy
`pip3 install moviepy`

### Run the program from root folder

```bash
$ python3 audioTrackExtractor/main.py [video path / url] -yt -d -t
```

- `-yt` if you are using a YouTube url
- `-d` to print debug information onscreen
- `-t` to log the time information on a log file (recommended)
- `-o [output]` set output mp3 file path (default= `extractedAudio.mp3`)
- `-l [log]` set log file path (default= `log.csv`)

### Help

Run `python3 audioTrackExtractor/main.py --help` for help

### Download files from YouTube

It may be useful to download videos into our remote servers
```
$ python3 audioTrackExtractor/downloader/downloader.py [URL] [outputPath]
```
