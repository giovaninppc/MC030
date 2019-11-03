import sys
import os

print('Run ' + sys.argv[1] + ' times')


files = ['video/10s.mp4', 'video/20s.mp4', 'video/45s.mp4', 'video/60s.mp4', 'video/90s.mp4', 'video/120s.mp4', 'video/150s.mp4', 'video/180s.mp4', 'video/300s.mp4', 'video/420s.mp4', 'video/600s.mp4']

for file in files:
    for i in range(0, int(sys.argv[1])):
        print('Execution nº: ' + str(i))
        cmd = 'python3 audioTrackExtractor/main.py ' + file + ' -d -t'
        os.system(cmd)
