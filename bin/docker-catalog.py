#!/usr/bin/env python

from __future__ import print_function

import argparse
import requests
import sys


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('-r', '--registry', required=True)
    opts = parser.parse_args()

    def get(path):
        url = 'https://{}/v2/{}'.format(opts.registry, path)
        return requests.get(url).json()

    repos = get('_catalog')['repositories']
    for repo in repos:
        tags = get('{}/tags/list'.format(repo))['tags']
        for tag in tags:
            print('{}:{}'.format(repo, tag))

    return

if __name__ == '__main__':
    sys.exit(main())
