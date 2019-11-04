import sys
import os
from datetime import datetime

def appendOnTextFile(path, text):
    file = open(path, 'a+')
    file.write(text)
    file.close()

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
    cmd = 'wget http://www.students.ic.unicamp.br/\~ra177677/' + file
    
    os.system(cmd)
    downloadStop = datetime.now().time()

    cmd = 'rm ' + file
    os.system(cmd)

    log = '{}, {}\n'.format(str(downloadStart), str(downloadStop))
    appendOnTextFile(logPath, log)

    print('{}\t{}\t'.format(str(downloadStart), str(downloadStop)))
