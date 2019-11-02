import argparse

class Arguments():
    def __init__(self, path: str, args):
        self.path = path
        self.args = args

def setupArguments() -> Arguments:
    argParser = argparse.ArgumentParser(description='Arguments for the Image processing')
    argParser.add_argument('file_path', help='The path to image file to be processed')
    argParser.add_argument('-yt', '--youtube', help='Video processing from remote youtube video', action='store_true')
    argParser.add_argument('-t', '--time', help='Log download time information / process time information', action='store_true')
    argParser.add_argument('-d', '--debug', help='Use this flag to enable debugging', action='store_true')

    args = argParser.parse_args()
    file_path = args.file_path

    return Arguments(file_path, args)
