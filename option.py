import argparse

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
        namespace.upload_path.extend(values)


class AddDownloadPathAction(argparse.Action):
    def __call__(self, parser, namespace, values, option_string=None):
        if not isinstance(values, list):
            raise argparse.ArgumentTypeError
        namespace.download_path.extend(values)


def add_options(p):
    assert isinstance(p, argparse.ArgumentParser)

    p.add_argument('-u', dest='upload_path',
                   nargs='+', action=AddUploadPathAction,
                   default=[],
                   metavar='FILE',
                   help='input upload file(s)')

    p.add_argument('-d', dest='download_path',
                   nargs='+', action=AddDownloadPathAction,
                   default=[],
                   metavar='FILE',
                   help='input download file(s)')

    p.add_argument('-w', dest='work_path',
                   metavar='DIR',
                   help='specify working path')


    gd = p.add_argument_group('debug arguments')

    gd.add_argument('--debug',
                    action='store_true',
                    help=argparse.SUPPRESS)
