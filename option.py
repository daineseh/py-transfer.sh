import argparse
import os
import sys

class Option(object):
    def __init__(self):
        self.work_path = '.'
        self.upload_path = []
        self.download_path = []
        self.debug = False


class AddUploadPathAction(argparse.Action):
    def __call__(self, parser, namespace, values, option_string=None):
        if not isinstance(values, list):
            raise argparse.ArgumentTypeError

        for path in values:
            if os.path.isdir(path):
                sys.stderr.write('[Error] %s%s%s is a directory.\n' %(bcolors.FAIL, path, bcolors.ENDC))
                sys.stderr.write("We don't suport uploading a directory.\n")
                sys.stderr.write('You can archive that directory by tar, zip, ...\n')
                sys.exit(-1)

        namespace.upload_path.extend(values)


class AddDownloadPathAction(argparse.Action):
    def __call__(self, parser, namespace, values, option_string=None):
        if not isinstance(values, list):
            raise argparse.ArgumentTypeError

        for url in values:
            if not url.startswith('https://transfer.sh/'):
                sys.stderr.write('[Error] %s%s%s is not a valid url to download.' %(bcolors.FAIL, url, bcolors.ENDC))
                sys.exit(-1)

            if not len(url[len('https://transfer.sh/'):].split('/')) == 2:
                sys.stderr.write('[Error] %s%s%s is not a valid url to download.' %(bcolors.FAIL, url, bcolors.ENDC))
                sys.exit(-1)

        namespace.download_path.extend(values)


def add_options(p):
    assert isinstance(p, argparse.ArgumentParser)

    p.add_argument('-u', dest='upload_path',
                   nargs='+', action=AddUploadPathAction,
                   default=[],
                   metavar='FILE',
                   help='specify the path of file(s) you want to upload.')

    p.add_argument('-d', dest='download_url',
                   nargs='+', action=AddDownloadPathAction,
                   default=[],
                   metavar='URL',
                   help='specify one or more URL you want to download.')

    p.add_argument('-w', dest='work_path',
                   metavar='DIR',
                   help='specify a directory to download. The default directory is the working directory.')


    gd = p.add_argument_group('debug arguments')

    gd.add_argument('--debug',
                    action='store_true',
                    help=argparse.SUPPRESS)


class bcolors(object):
    FAIL = '\033[91m'
    ENDC  = '\033[0m'

