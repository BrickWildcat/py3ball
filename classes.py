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

    def randgen(self, bounds=[0,113.8], pos=-1):
        self.ovr = -2
        self.pos = -2
        while self.ovr>bounds[1] or self.ovr<bounds[0] or pos != self.pos:
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
            if pos == -1:
                self.pos = -1
        self.genovr()

    def __init__(self, atts=False, pos=-1):
        if not atts:
            self.randgen()
        elif type(atts) == list:
            if len(atts)==2:
                self.randgen(atts, pos)
            else:
                while len(atts) < 10:
                    atts.append(randatt())
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
        else:
            raise Exception(
                'Player generation failed: Parameter "atts" must be a list or <player> object')

    def exportList(self):
        return [self.io, self.oo, self.pas, self.drb, self.id,
                self.od, self.blk, self.stl, self.stm, self.inj]


class team:
    def __init__(self, size=10, ovrs=[70, 99, 50, 85]):
        self.roster = []
        for i in range(5):
            self.roster.append(player([ovrs[0],ovrs[1]],i+1))
        while len(self.roster) < size:
            for i in range(5):
                self.roster.append(player([ovrs[2], ovrs[3]], i+1))
                if len(self.roster) == size:
                    break
        self.ovr = 0
        i=0
        for plyr in self.roster:
            if i<5:
                self.ovr += plyr.ovr*2
            else:
                self.ovr += plyr.ovr*(5/(len(self.roster)-5))
            i+=1
        self.ovr /= 15
        self.ovr = round(self.ovr, 1)