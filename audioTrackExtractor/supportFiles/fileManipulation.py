def readTextFile(path):
    file = open(path, 'r')
    txt = file.read()
    file.close()
    return txt


def writeTextFile(path, text):
    file = open(path, 'w+')
    file.write(text)
    file.close()



def appendOnTextFile(path, text):
    file = open(path, 'a+')
    file.write(text)
    file.close()
