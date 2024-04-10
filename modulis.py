A=70

def printA():
    print('as esu nauja printA funkcija')


class Vehicle():
    def __init__(self, P, R):
        self.P = P
        self.R = R

class Car(Vehicle):
    def __init__(self, P, R, S):
       super().__init__(P, R)
       self.S = S
    
    def GetSeats(self):
        Txt = self.P + " turi " + str(self.S) + " sedimu vietu"
        return Txt

class Bus(Vehicle):
    def __init__(self, P, R, S):
       super().__init__(P, R)
       self.S = S
    
    def GetSeats(self):
        Txt = self.P + " turi " + str(self.S) + " sedimu vietu "
        return Txt

class Train(Vehicle):
    def __init__(self, P, R, S):
       super().__init__(P, R)
       self.S = S
    
    def GetSeats(self):
        Txt = self.P + " turi " + str(self.S) + " sedimu vietu"
        return Txt



class TxtNuskaitymas():
    def __init__(self, pav, skirtukas):
        self.pavadinimas = pav
        self.skirt = skirtukas
        self.i = []
        self.u = []
        self.j = []
        self.p = []
        self.TxtReader()
        pass

    def TxtReader(self):
        fname = self.pavadinimas
        f = open(fname, mode='r', encoding='utf-8')
        tekstas = f.readlines()
        f.close()
        for elem in tekstas[1:]:
            self.u.append(float(elem.split(self.skirt)[0]))
            self.i.append(float(elem.split(self.skirt)[1]))
            self.j.append(float(elem.split(self.skirt)[2]))
            self.p.append(float(elem.split(self.skirt)[3]))
    
    def getMaxP(self):
        maxP = max(self.p)
        return maxP
    
    def getpceP(self):
        maxP = self.getMaxP()
        pce = round((maxP / 1000 * 100),2)
        return pce
    




class FileReader():
    """
   Labai kieta mano klase
    """
    def __init__(self, FileName):
        self.FileName = FileName
        self.I = []
        self.U = []
        self.j = []
        self.P = []

    def getFileContent(self):
        File = open(self.FileName, mode = 'r')
        FileContent = File.readlines()
        File.close()

        for line in FileContent[1:]:
            u = float(line.split(';')[0])
            self.U.append(u)
            i = float(line.split(';')[1])
            self.I.append(i)
            J = float(line.split(';')[2])
            self.j.append(J)
            p = float(line.split(';')[3])
            self.P.append(p)

    def maxP(self):
        maxP = max(self.P)
        return maxP
    
    def pce(self):
        maxi = self.maxP()
        pce = maxi / 10
        return pce
    


class Mokinys():
    def __init__(self, vardas, pavarde):
        self.V = vardas
        self.P = pavarde
        self.__pazymiai = []

    def getVidurkis(self):
        vidurkis = sum(self.__pazymiai)/len(self.__pazymiai)
        return vidurkis
    
    def getMax(self): 
        pazymysMax = max(self.__pazymiai)
        return pazymysMax

    def getMin(self):
        pazymysMin = min(self.__pazymiai)
        return pazymysMin
    
    def addPaz(self, pazymys):
        if pazymys > 0 and pazymys <= 10:
            self.__pazymiai.append(pazymys)

    def getPazymiai(self):
        return self.__pazymiai
    

class Abiturientas(Mokinys):
    def __init__(self, vardas, pavarde):
        super().__init__(vardas, pavarde)
        self.exRes = []

    def addExRes(self, Res):
        self.exRes.append(Res)

    def getBendrasVid(self):
        bendriPazymiai = self.pazymiai + self.exRes
        bendrasVid = sum(bendriPazymiai)/len(bendriPazymiai)
        return bendrasVid
    

class Mokykla():
    def __init__(self):
        self.Mokiniai = []

    def addMokinys(self, mokinys):
        self.Mokiniai.append(mokinys)

    def removeMokinys(self, mokinys):
        self.Mokiniai.remove(mokinys)

    def VisuMokiniuVidurkis(self):
        VisuMokiniuPazymiai = []
        for mokinys in self.Mokiniai:
            VisuMokiniuPazymiai.extend(mokinys.pazymiai) # extend leidzia sujungti skirtingus sarasus, prisplecia sarasas, esantis pries extend metoda
        VisuMokiniuVidurkis = sum(VisuMokiniuPazymiai)/len(VisuMokiniuPazymiai)
        return VisuMokiniuVidurkis