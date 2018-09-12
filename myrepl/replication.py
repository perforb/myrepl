# -*- coding: utf-8 -*-
import argparse
import logging

logger = logging.getLogger('myrepl')
ch = logging.StreamHandler()
ch.setLevel(logging.DEBUG)
logger.addHandler(ch)


def dump():
    pass


def load():
    pass


def backup():
    pass


def cleanup():
    pass


def parse_argument():
    parser = argparse.ArgumentParser()
    parser.set_defaults(
        source=None,
        destination=None,
        config='/etc/myrepl.ini',
        dryrun=False,
        verbose=False,
    )

    parser.add_argument(
        '-s',
        '--source',
        required=True,
        help='source environment'
    )
    parser.add_argument(
        '-d',
        '--destination',
        required=True,
        help='destination environment'
    )
    parser.add_argument(
        '-c',
        '--config',
        help='database settings'
    )
    parser.add_argument(
        '--dryrun',
        action='store_true',
        help='dry run if this option is passed'
    )
    parser.add_argument(
        '-v',
        '--verbose',
        action='store_true',
        help='verbose mode if this option is passed'
    )

    args = parser.parse_args()
    if args.verbose:
        logger.setLevel(logging.DEBUG)

    return args


def main():
    args = parse_argument()
    logger.debug(args)


if __name__ == '__main__':
    main()
