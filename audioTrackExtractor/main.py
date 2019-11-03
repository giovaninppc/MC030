from supportFiles import *
from downloader import *
from datetime import datetime

downloadStart = 0.0
downloadStop = 0.0
convertStart = 0.0
convertStop = 0.0


# Run arguments
configuration = setupArguments()
path = configuration.path
args = configuration.args
outputPath = args.outputFilePath
debug = args.debug
logPath = args.logFilePath


#Download from YouTube
if args.youtube:
    if debug: print('Downloading video from YouTube')

    downloadStart = datetime.now().time()
    PytubeDownloader().downloadVideo(path)
    downloadStop = datetime.now().time()

    path = 'temp.mp4'


# Convert to mp3
if debug: print('Processing video at ' + path)

converter = VideoConverter(path)
convertStart = datetime.now().time()
converter.getAudioFromVideo(outputPath)
convertStop = datetime.now().time()

videoDuration = converter.getVideoDuration()


#Log times
if args.time:
    log = '{}, {}, {}, {}, {}\n'.format(str(downloadStart), str(downloadStop), str(videoDuration), str(convertStart), str(convertStop))
    appendOnTextFile(logPath, log)

    if args.debug:
        print('download start\tdownload stop\tconvert start\tconvert stop')
        print('{}\t{}\t{}\t{}\t{}'.format(str(downloadStart), str(downloadStop), str(videoDuration), str(convertStart), str(convertStop)))
