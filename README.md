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


### Help

Run `python3 audioTrackExtractor/main.py --help` for help


### Local tests script
- Run the audio conversion from a local path N times
```
$ python3 audioTrackExtractor/test_scripts/runNTimesLocalFile.py <N> <path>
```
it will log every execution on the log file.


- Run the audio conversion from a remote video url N times
```
$ python3 audioTrackExtractor/test_scripts/runNTimesYouTubeVideo.py <N> <path>
```
it will log every execution on the log file.
