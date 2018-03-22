# -*- coding: utf-8 -*-

import sys
import argparse
import logging

logger = logging.getLogger('myreplica')
ch = logging.StreamHandler()
ch.setLevel(logging.DEBUG)
logger.addHandler(ch)


def parse_argument():
    parser = argparse.ArgumentParser()
    parser.set_defaults(
        source=None,
        destination=None,
        dbsettings='/etc/myreplica.ini',
        dryrun=True,
        verbose=False,
    )

    parser.add_argument('-s',
                        '--source',
                        required=True,
                        dest='source_env',
                        help='source environment')
    parser.add_argument('-d',
                        '--destination',
                        required=True,
                        dest='dest_env',
                        help='destination environment')
    parser.add_argument('--dryrun',
                        action='store_true',
                        help='dry run if this option is passed.')
    parser.add_argument('-v',
                        '--verbose',
                        action='store_true',
                        help='set verbose mode')

    args = parser.parse_args()
    if args.verbose:
        logger.setLevel(logging.DEBUG)

    return args


def main():
    args = parse_argument()
    logger.debug(args)


if __name__ == '__main__':
    main()
