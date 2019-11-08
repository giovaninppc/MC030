import sys
import os
import datetime

# argv[1]: quantas vezes rodar
# argv[2]: que arquivo quer baixar
# argv[3]: nome do out

def appendOnTextFile(path, text):
    file = open(path, 'a+')
    file.write(text)
    file.close()

def betweenTwoDates(a, b):
	# Create datetime objects for each time (a and b)
	dateTimeA = datetime.combine(datetime.now().date(), a)
	dateTimeB = datetime.combine(datetime.now().date(), b)
	# Get the difference between datetimes (as timedelta)
	dateTimeDifference = dateTimeA - dateTimeB

print("Download time measure")
print('Run ' + sys.argv[1] + ' times')

file = sys.argv[2]

downloadStart = 0.0
downloadStop = 0.0

logPath = sys.argv[3]

cmd = 'rm ' + logPath
os.system(cmd)

appendOnTextFile(logPath, "download start, download stop\n")

for i in range(0, int(sys.argv[1])):
    print('Execution nº: ' + str(i))
    downloadStart = datetime.datetime.now()
    cmd = 'wget http://www.students.ic.unicamp.br/\~ra168609/' + file
    os.system(cmd)
    downloadStop = datetime.datetime.now()
    duration = downloadStop - downloadStart
    duration = duration.microseconds

    cmd = 'rm ' + file
    os.system(cmd)

    log = '{}, {}, {}\n'.format(str(downloadStart), str(downloadStop), str(duration))
    appendOnTextFile(logPath, log)

    print('{}\t{}\t'.format(str(downloadStart), str(downloadStop)))
