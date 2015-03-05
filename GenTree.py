import os, sys                          # directory
import shutil                           # copy files
from numpy import *
import winsound

import numpy as np
import matplotlib.pyplot as plt
import math
from mpl_toolkits.mplot3d import Axes3D
from mpl_toolkits.mplot3d import art3d

import Image, ImageEnhance
import numpy

import AddPipls
# !!!Vot blin kruto!! FckCKKnSHt!
import imp
imp.reload(AddPipls)


class AllFamily(object):
    AllId=[]
    family=[]
    def getNewId(self):
        a=1
        while (self.AllId.count(a)>0):
            a+=1
        self.AllId.append(a)        
        return a
    def setGenerationLvls(self):
        maxlvl=-500
        for pipl in self.family:
            pass
    def getPiplFromId(self, Id):
        print "getPiplFromId_Id=", Id
        for pipl in self.family:
            if (pipl._Id==Id):
                return pipl
        print "No pipl with Id=", Id
        return self.family[0]
    
def deligate(family, toPiplId, toRecLev):
    if not(toPiplId==-1):
        if ((family.getPiplFromId(toPiplId)).isGLevSet==False):
            setGenerLev(family, family.getPiplFromId(toPiplId), toRecLev)
        else:
            print "Else Else!!"
            
def setGenerLev(family, self, recLev):
    self.setGLev(recLev)
    self.isGLevSet=True
    deligate(family, self.DadId, recLev+1)
    deligate(family, self.MomId, recLev+1)
    for piplId in self.Childs:
        deligate(family, piplId, recLev-1)
    deligate(family, self.Spouse, recLev)
    """if not(self.DadId==-1):
        if ((family.getPiplFromId(self.DadId)).isGLevSet==False):
            setGenerLev(family, family.getPiplFromId(self.DadId), recLev+1)
        else:
            print "Else Else!!"
     """       
    
    
class Che(object):
    Name, LastName, Otche = "","",""
    isGLevSet=False
    _Id=-1
    DadId=-1
    MomId=-1
    Spouse=-1       #wedding
    DateWedding=-1
    NChilds=0       #childs    
    GenerationLevel=-500
    __EndOfRepr__="\n"

    def setGLev(self, recLev):
        self.GenerationLevel=recLev
        
    def __init__(self, LastNamein, Namein, Otchein, Family):
        self.Name=Namein
        self.LastName=LastNamein
        self.Otche=Otchein
        self._Id=Family.getNewId()
        self.Childs=[]
        Family.family.append(self)
        
    def marry(self, spouse, date='-1'):
        self.Spouse=spouse._Id
        spouse.Spouse=self._Id
        self.DateWedding=date
        spouse.DateWedding=date
        
    def addChild(self, chld):
        self.NChilds+=1
        self.Childs.append(chld._Id)
        
    def setDad(self, dad):
        self.DadId=dad._Id
        dad.addChild(self)
    def setMom(self, mom):
        self.MomId=mom._Id
        mom.addChild(self)
    def setParents(self, dad, mom):
        self.setMom(mom)
        self.setDad(dad)
        dad.marry(mom)
    
    
    def __str__(self):
        return "%sId=%2.0f, %s %s %s" % (self.__EndOfRepr__,  self._Id, self.LastName, self.Name, self.Otche)
    def __repr__(self): 
        return "%sId=%2.0f, %s %s %s" % (self.__EndOfRepr__,  self._Id, self.LastName, self.Name, self.Otche)
    def AllOut(self):
        maxLenOfAttr=0
        for attr in dir(self):
            if not((attr[1]=='_')or (type(self.__getattribute__(attr))==type(self.__getattribute__("setDad")))):
                if len(attr)>maxLenOfAttr:
                    maxLenOfAttr=len(attr)
        def separate(s="  "):
            print s
        def printList(lst, seprr="  "):
            if (type(lst)==type("abc")):
                attr=lst
                print ("{:"+str(maxLenOfAttr)+"}: {}").format(attr, self.__getattribute__(attr))
            else:
                for attr in lst:
                    print ("{:"+str(maxLenOfAttr)+"}: {}").format(attr, self.__getattribute__(attr))
            separate(seprr)
        printList(('_Id', 'LastName', 'Name', 'Otche'))
        printList(('GenerationLevel', 'isGLevSet'))
        printList(('DadId', 'MomId')," - "*10)
        #printList(('Spouse', 'DateWedding'))
        printList(('NChilds', 'Childs'))

    def __eq__(self, other):
        isEqual = True
        for attr in ('LastName', 'Name', 'Otche', 'DadId', 'MomId'):
            isEqual = isEqual and (self.__getattribute__(attr)==other.__getattribute__(attr))
        return isEqual

def PrintAll(piplArr):
    print "_"*50
    for pipl in piplArr:
        print "_"*50
        pipl.AllOut()
    print "_"*50

if __name__ == '__main__':
    PATHthisFULL=os.path.abspath(__file__)  # full name of file
    PATHthisROOT=os.path.dirname(PATHthisFULL)  # name of directory of this file
    
    Lips=AllFamily()
    #PrintAll(Lips.family)
    Lips=AddPipls.Add(Lips)
    PrintAll(Lips.family)
    setGenerLev(Lips, Lips.family[0], 0)
    print "Lips family"
    PrintAll(Lips.family)

    #print "Ilya's family:", Lips.family


    
