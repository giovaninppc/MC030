import sys
import os

print('URL to be downloaded: ' + sys.argv[2])
print('Run ' + sys.argv[1] + ' times')

for i in range(0, int(sys.argv[1])):
    print('Execution nº: ' + str(i))
    cmd = 'python3 audioTrackExtractor/main.py ' + sys.argv[2] + ' -d -t -yt'
    os.system(cmd)
