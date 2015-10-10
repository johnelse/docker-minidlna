#!/usr/bin/env python

"""
Helper script for launching minidlna in a docker container.
"""

import argparse
import os
import subprocess
import sys


DEFAULT_ADDRESS = '127.0.0.1'
DEFAULT_PORT = 8200


def main():
    """
    Main entry point.
    """
    parser = argparse.ArgumentParser()
    parser.add_argument('--address', default=DEFAULT_ADDRESS,
                        help='Host address on which the container will listen')
    parser.add_argument('--port', default=DEFAULT_PORT, type=int,
                        help='Host port which will forwarded to the '
                             'container\'s listening port')
    parser.add_argument('--name',
                        help='Friendly name for the DLNA server')
    parser.add_argument('--root',
                        help='Root directory to be served')
    parser.add_argument('--inotify', action='store_true',
                        help='Enable inotify monitoring of new media')

    args = parser.parse_args(sys.argv[1:])
    image = "%s/minidlna" % os.getenv("USER")
    inotify = "no"
    if args.inotify:
        inotify = "yes"
    docker_args = [
        "docker", "run", "-d", "--name", "minidlna", "--net=host",
        "-v", "%s:/media" % args.root,
        "-e", "MINIDLNA_MEDIA_DIR=/media",
        "-e", "MINIDLNA_LISTENING_IP=%s" % args.address,
        "-e", "MINIDLNA_PORT=%d" % args.port,
        "-e", "MINIDLNA_FRIENDLY_NAME=%s" % args.name,
        "-e", "MINIDLNA_INOTIFY=%s" % inotify,
        image
        ]
    print "Launching docker with args %s" % docker_args
    subprocess.call(docker_args)


if __name__ == "__main__":
    main()
