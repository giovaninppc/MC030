import sys
import os

print('Run ' + sys.argv[1] + ' times')

urls = ["https://www.youtube.com/watch?v=EK44YUWxo0I"]
k = 0
for url in urls:
	k = k + 1
	for i in range(0, int(sys.argv[1])):
		outputFileName = "youtubeDownloadCSV_"+str(k)+".csv"

		print('Execution nº: ' + str(i))
		cmd = 'python3 ../main.py ' + url + ' -t -yt -log '+outputFileName
		os.system(cmd)