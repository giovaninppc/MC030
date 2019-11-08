import sys
import os

print('Run ' + sys.argv[1] + ' times')


files = ['10s.mp4', '20s.mp4', '45s.mp4', '60s.mp4', '90s.mp4', '120s.mp4', '150s.mp4', '180s.mp4', '300s.mp4', '420s.mp4', '600s.mp4']

for file in files:
	outputFileName = "wgetCSV_"+file
	for i in range(0, int(sys.argv[1])):
		print('Execution nº: ' + str(i))
		cmd = 'python3 wgetDownloadTime.py '+sys.argv[1]+" "+ file + " " + outputFileName+".csv"
		os.system(cmd)