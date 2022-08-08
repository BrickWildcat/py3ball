from functions import *


class player:
    def genovr(self):
        atts = [self.io, self.oo, self.pas, self.drb, self.id,
                self.od, self.blk, self.stl, self.stm, self.inj]
        atwt = [[1, 1.5, 1.9, 1.8, 0.2, 1.5, 0.1, 1.5, 1, 1],
                [1.1, 1.9, 1, 1.9, 0.3, 1.5, 0.3, 1.5, 1, 1],
                [1, 1.5, 1, 1.2, 1.5, 1.1, 0.8, 1.4, 1, 1],
                [1.8, 1, 0.6, 0.7, 1.7, 0.9, 1.8, 1, 1, 1],
                [2.1, 0.7, 0.6, 0.2, 2.1, 0.6, 2.1, 1.1, 1, 1]]
        self.ovrlist = []
        for i in range(5):
            templist = []
            ai = 0
            for a in atts:
                templist.append(a*atwt[i][ai])
                ai += 1
            self.ovrlist.append(sumlist(templist)/len(templist))
        self.ovr = round(max(self.ovrlist), 1)
        self.pos = self.ovrlist.index(max(self.ovrlist)) + 1
    def __init__(self, atts=0):
        if not atts:
            self.io = randatt()
            self.oo = randatt()
            self.pas = randatt()
            self.drb = randatt()
            self.id = randatt()
            self.od = randatt()
            self.blk = randatt()
            self.stl = randatt()
            self.stm = randatt(50)
            self.inj = randatt(50)
            self.genovr()
        elif type(atts) == player:
            self.io = atts.io
            self.oo = atts.oo
            self.pas = atts.pas
            self.drb = atts.drb
            self.id = atts.id
            self.od = atts.od
            self.blk = atts.blk
            self.stl = atts.stl
            self.stm = atts.stm
            self.inj = atts.inj
            self.ovrlist = atts.ovrlist
            self.ovr = atts.ovr
            self.pos = atts.pos
        elif type(atts) == list and len(atts) == 10:
            self.io = atts[0]
            self.oo = atts[1]
            self.pas = atts[2]
            self.drb = atts[3]
            self.id = atts[4]
            self.od = atts[5]
            self.blk = atts[6]
            self.stl = atts[7]
            self.stm = atts[8]
            self.inj = atts[9]
            self.genovr()
        else:
            raise Exception("Player generation failed: Parameter atts must be a 10-int list or player object")
    def exportList(self):
        return [self.io, self.oo, self.pas, self.drb, self.id,
                self.od, self.blk, self.stl, self.stm, self.inj]
