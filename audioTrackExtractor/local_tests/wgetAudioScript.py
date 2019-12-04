import sys
import os
print('Run ' + sys.argv[1] + ' times')
files = ['10s.mp3', '20s.mp3', '45s.mp3', '60s.mp3', '90s.mp3', '120s.mp3', '150s.mp3', '180s.mp3', '300s.mp3', '420s.mp3', '600s.mp3']
for file in files:
	outputFileName = "wgetCSV_audio_"+file
	cmd = 'python3 wgetDownloadTime.py '+sys.argv[1]+" "+ file + " " + outputFileName+".csv"
	os.system(cmd)
