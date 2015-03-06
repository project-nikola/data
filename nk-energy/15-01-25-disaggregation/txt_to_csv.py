#!/usr/bin/env python3
"""Convert the txt files in this directory to csv files

'time,current,power'
"""
import fileinput
import re


def main():
    ex = '(\d+-\d+-\d+ \d+:\d+:\d+).*current: (\d*\.\d*) amps\spower: (\d*\.\d*)'
    p = re.compile(ex)
    for line in fileinput.input():
        m = p.match(line)
        if m is None:
            continue

        dt, current, power = m.groups()
        print("{}, {}, {}".format(dt, current, power))


if __name__ == '__main__':
    main()
