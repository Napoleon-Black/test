#!/usr/bin/env python
# -*- coding: utf-8 -*-

__author__ = 'Yuriy K.'

import sqlite3, re, chardet

class Parser(object):

    def __init__(self):
        super(Parser, self).__init__()
        conn = sqlite3.connect('my.db')

    def main(self):
        self.send_to_database()

    def send_to_database(self):
        for i in range(1000):
            lst = []
            file = open('siemens/test-%s.csv'% i, 'r')
            first_line = file.readline()
            enc = re.findall(r'=(\w*)', first_line)
            print first_line
            print enc[0]
            #while opened_file:
            #    lst.append(opened_file)
            #    opened_file = file.readline()

            #print lst
            break


if __name__ == '__main__':
    start = Parser()
    start.main()

        