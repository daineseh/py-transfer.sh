#! /usr/bin/env python2

import argparse
import urllib2
import os
import shlex
import subprocess

import option

def download(path_list, work_path):
    for path in path_list:
        try:
            response = urllib2.urlopen('%s' % path)
        except urllib2.HTTPError, e:
            print e
            print "Could not retrieve file: %s" % path
            continue

        save_path = os.path.join(work_path, os.path.basename(path))
        fp = open(save_path, 'w')
        fp.write(response.read())
        fp.close()
        print 'Download %s done.' % save_path


def upload(path_list):
    url_list = []
    for path in path_list:
        cmd = 'curl -s --upload-file %s https://transfer.sh/%s' %(path, os.path.basename(path))
        print 'We are uploading %s.' %os.path.basename(path)
        try:
            url = subprocess.check_output(shlex.split(cmd))
            url_list.append(url)
        except OSError as e:
            print 'Execution failed:', e
        print '%s is successfully uploaded.' %os.path.basename(path)

    if not url_list:
        return
    print '\nNow you can download file(s) by the following url(s):'
    for url in url_list:
        print url,

def main():
    parser = argparse.ArgumentParser()
    option.add_options(parser)

    opts = option.Option()
    parser.parse_args(namespace=opts)

    if opts.upload_path:
        upload(opts.upload_path)

    if opts.download_path:
        download(opts.download_path, opts.work_path)

if __name__ == '__main__':
    main()
