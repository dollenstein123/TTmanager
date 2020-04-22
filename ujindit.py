from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from tkinter.ttk import *
import locale
import datetime
import screencfg
#aquativo, black, blue, clearlooks, elegance, keramik, kroc, plastic, radiance, scid, smog, winxpblue

class Comp():
    athlstruct = ('num', 'firstname', 'secondname', 'place')

    def __init__(self):
        self.cname = ''
        self.cdate = datetime.date.today()
        self.cfilename = ''
        self.cstatus = ''
        self.cfirstround = 'A'
        self.csecondround = ''
        self.athletes = [] #{num:, firstname:, secondname:, place:}
        self.matches = [] #{number:, player1:, player2:, result:, sets:}

    def startnewcomp(self, cname, cdate):
        self.cname = cname
        self.cdate = cdate
        self.cstatus = 'created'
        with open('versenyek.comp', 'r') as f:
            compscontent = [line.strip().split(',') for line in f]
            savedcomps = [i[0] for i in compscontent]
        self.cfilename = 'comp' + str(len(savedcomps) + 1)
        f = open('versenyek.comp', 'a+')
        newcomp = '\n' + cname + ',' + cdate.strftime('%Y.%m.%d') + ',' + self.cfilename + ',' + self.cstatus + ',A,'
        f.write(newcomp)
        f.close()

    def loadcomp(self, cname, cdate, cfilename, cstatus, cfirstround, csecondround):
        self.cname = cname
        self.cdate = cdate
        self.cfilename = cfilename
        self.cstatus = cstatus
        self.cfirstround = cfirstround
        self.csecondround = csecondround
        try:
            with open(self.cfilename + '.athl', encoding='UTF-8') as f:
                athldatas = [line.strip().split(',') for line in f]
            for item in athldatas:
                self.athletes.append(dict(zip(self.athlstruct, item)))
        except OSError:
            print('Hiba')
        print(self.athletes)

if __name__ == '__main__':
    c = Comp()
    c.loadcomp('1. verseny','2019.04.20','comp1','closed','AB','MR')