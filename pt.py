#! /usr/bin/env python2

import argparse
import urllib2
import os
import sys
import shlex
import subprocess

import option

def download(path_list, work_path):
    assert isinstance(path_list, list)
    for path in path_list:
        try:
            response = urllib2.urlopen('%s' % path)
        except urllib2.HTTPError, e:
            sys.stderr.write('%s\n' %e)
            sys.stderr.write("Could not retrieve file: %s\n" % path)
            continue

        save_path = os.path.join(work_path, os.path.basename(path))
        fp = open(save_path, 'w')
        fp.write(response.read())
        fp.close()
        print 'Download %s done.' % save_path


def upload(path_list):
    assert isinstance(path_list, list)

    if len(path_list) == 1:
        print '---'
        print 'The following file will be uploaded:'
        print path_list[0]
        print '---'
    else:
        print '---'
        print 'The following files will be uploaded:'
        for file_ in path_list:
            print file_
        print '---'

    url_list = []
    for path in path_list:
        cmd = 'curl -s --upload-file %s https://transfer.sh/%s' %(path, os.path.basename(path))
        print 'We are uploading %s.' %os.path.basename(path)
        try:
            url = subprocess.check_output(shlex.split(cmd))
            url_list.append(url)
        except OSError as e:
            sys.stderr.write('Execution failed: %s\n' %e)
        print '%s is successfully uploaded.' %os.path.basename(path)

    if not url_list:
        return
    print '\nNow you can download file(s) by the following url(s):'
    for url in url_list:
        print url,


def has_curl():
    try:
        fnull = open(os.devnull, 'w')
        subprocess.check_call(["which", "curl"], stdout=fnull, stderr=fnull)
        fnull.close()
        return True
    except subprocess.CalledProcessError:
        return False


def main():
    parser = argparse.ArgumentParser()
    option.add_options(parser)

    opts = option.Option()
    parser.parse_args(namespace=opts)

    if opts.upload_path:
        upload(opts.upload_path)

    if opts.download_path:
        if not has_curl():
            sys.stderr.write('We need curl to work. Please install it(http://curl.haxx.se/) on you system.\n')
            sys.exit(-1)
        download(opts.download_path, opts.work_path)

if __name__ == '__main__':
    main()
