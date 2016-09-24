#!/usr/bin/env python

from __future__ import print_function

import argparse
import requests
import sys


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('-r', '--registry', required=True)
    parser.add_argument('-p', '--path')
    opts = parser.parse_args()

    def get(path):
        url = 'https://{}/v2/{}'.format(opts.registry, path)
        return requests.get(url).json()

    if opts.path:
        import json
        print(json.dumps(get(opts.path), indent=2))
        return 0

    repos = get('_catalog')['repositories']
    for repo in repos:
        tags = get('{}/tags/list'.format(repo))['tags']
        for tag in tags:
            print('{}:{}'.format(repo, tag))

    return 0

if __name__ == '__main__':
    sys.exit(main())
