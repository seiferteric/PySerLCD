#!/usr/bin/env python3

import argparse
from PySerLCD import Lcd


def main():
    parser = argparse.ArgumentParser(description='Configure LCD')
    parser.add_argument('--device', '-d', help='tty device to use', default='/dev/ttyUSB0')
    parser.add_argument('--baud', '-b', help='BAUD Rate', default=9600, type=int)
    subparsers = parser.add_subparsers(dest="command")
    write = subparsers.add_parser('write', help='Write something')
    write.add_argument('string')
    write.add_argument('--clear', '-c', help='Clear before write', action='store_true')
    subparsers.add_parser('clear', help='Clear Screen')
    pos = subparsers.add_parser('pos', help='Set cursor position')
    pos.add_argument('-x', help="X Position", required=True, type=int)
    pos.add_argument('-y', help="Y Position", required=True, type=int)
    subparsers.add_parser('scroll-left', help='Scroll left')
    subparsers.add_parser('scroll-right', help='Scroll right')



    args = parser.parse_args()
    l = Lcd(args.device, args.baud, reset=False)

    if args.command == 'write':
        if args.clear:
            l.clear()
        l.write(args.string)
    if args.command == 'clear':
        l.clear()
    if args.command == 'pos':
        l.set_cursor_pos(args.x, args.y)
    if args.command == 'scroll-left':
        l.scroll_left()
    if args.command == 'scroll-right':
        l.scroll_right()


if __name__ == "__main__":
  main()