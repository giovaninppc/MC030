import sys
import os

print('Run ' + sys.argv[1] + ' times')

urls = ["https://www.youtube.com/watch?v=q-xSQ7MU-K8",
"https://www.youtube.com/watch?v=FNaM4qIKXc8",
"https://www.youtube.com/watch?v=fvE38raWAMg",
"https://www.youtube.com/watch?v=Nn9KqKMFhow",
"https://www.youtube.com/watch?v=XagMIeb3PyY",
"https://www.youtube.com/watch?v=m0GufRJYxfQ",
"https://www.youtube.com/watch?v=RLekLicU3RA",
"https://www.youtube.com/watch?v=cHeGWCKRnl8",
"https://www.youtube.com/watch?v=IzRwagNhUKo",
"https://www.youtube.com/watch?v=-hH-WtPlUUY",]

k = 0
for url in urls:
	k = k + 1
	for i in range(0, int(sys.argv[1])):
		outputFileName = "youtubeDownloadCSV_"+str(k)+".csv"

		print('Execution nº: ' + str(i))
		cmd = 'python3 ../main.py ' + url + ' -t -yt -log '+outputFileName
		os.system(cmd)