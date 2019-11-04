import sys
import os
from supportFiles import *

print("Dowload time measure")
print('Run ' + sys.argv[1] + ' times')

file = sys.argv[2]

downloadStart = 0.0
downloadStop = 0.0
logPath = "wget_download_time.csv"

appendOnTextFile(logPath, "download start, download stop")

for i in range(0, int(sys.argv[1])):
    print('Execution nº: ' + str(i))
    downloadStart = datetime.now().time()
    cmd = 'wget students.ic.unicamp.br/ra177677/' + file
    os.system(cmd)
    downloadStop = datetime.now().time()

    log = '{}, {}\n'.format(str(downloadStart), str(downloadStop))
    appendOnTextFile(logPath, log)

    print('{}\t{}\t'.format(str(downloadStart), str(downloadStop)))
