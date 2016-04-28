#!/usr/bin/env python
# -*- coding: utf-8 -*-

__author__ = 'Yuriy K.'

import sys, sqlite3, re, chardet

class Parser(object):

    def __init__(self):
        super(Parser, self).__init__()
        self.conn = sqlite3.connect('my.db')
        self.cur = self.conn.cursor()

    def main(self):
        self.cur.execute("""DELETE FROM info""")
        self.conn.commit()
        self.send_to_database()

    def send_to_database(self):

        for i in range(1000):
            file = open('siemens/test-%s.csv'% i, 'r')
            first_line = file.readline()
            data = file.readline()
            enc = re.findall(r'=(\w*-\w*|\w*)', first_line)
            
            while data:
                new_lst = data.split(',')
                first = new_lst[0]
                second = new_lst[1]

                if str(enc) or str(enc.lower()) != 'utf-8':

                    try:
                        third = new_lst[2].decode(str(enc))
                    except UnicodeDecodeError:
                        third_str = ''
                        for char in new_lst[2]:
                            detect = chardet.detect(char).get('encoding')

                            try:
                                third_str += char.decode(detect)
                            except:
                                if ord(char) == 129:
                                    char = char.decode('cp437')
                                third_str += char

                        third = third_str
                    
                else:
                    third = new_lst[2]


                sql = """INSERT INTO info (e_name, value, string) 
                         VALUES (?, ?, ?)"""
                self.cur.execute(sql, (first, second, third))
                
                data = file.readline()

        self.conn.commit()
        self.how_much_entity()

    def how_much_entity(self):
        a = self.cur.execute("""SELECT * FROM info WHERE e_name is 'a'""")
        print 'a = %s' % len(a.fetchall())

        b = self.cur.execute("""SELECT * FROM info WHERE e_name is 'b'""")
        print 'b = %s' % len(b.fetchall())

        c = self.cur.execute("""SELECT * FROM info WHERE e_name is 'c'""")
        print 'c = %s' % len(c.fetchall())

        d = self.cur.execute("""SELECT * FROM info WHERE e_name is 'd'""")
        print 'd = %s' % len(d.fetchall())

        e = self.cur.execute("""SELECT * FROM info WHERE e_name is 'e'""")
        print 'e = %s' % len(e.fetchall())

        f = self.cur.execute("""SELECT * FROM info WHERE e_name is 'f'""") 
        print 'f = %s' % len(f.fetchall())

        self.how_much_str()


    def how_much_str(self):
        unq = self.cur.execute("""SELECT DISTINCT string FROM info""")
        print '\nUnique strings:  %s' % len(unq.fetchall())

        self.show_histogram()


    def show_histogram(self):
        pass



if __name__ == '__main__':
    start = Parser()
    start.main()

        