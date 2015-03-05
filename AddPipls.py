import os, sys                          # directory
import shutil                           # copy files
from numpy import *
import winsound

import numpy

#from GenTree import Che
import GenTree
import imp
imp.reload(GenTree)

def Add(piplArr):
    #piplArr=[]
    Ilya=GenTree.Che("Lipatov", "Ilya", "Alexandrovich", piplArr)

    Alex=GenTree.Che("Lipatov", "Alexandr", "Leonidovich", piplArr)
    Nat=GenTree.Che("Lipatova", "Nataliya", "Evgenjevna", piplArr)

    Evg=GenTree.Che("Bukatin", "Evgeniy", "Matveevich", piplArr)
    Gala=GenTree.Che("Bukatina", "Galina", "Ivanovna", piplArr)

    Leonid=GenTree.Che("Lipatov", "Leonid", "Sergeevich", piplArr)
    Valja=GenTree.Che("Lipatova", "Valentina", "Ivanovna", piplArr)

    SergLips=GenTree.Che("Lipatov", "Sergey", "Leonidovich", piplArr)
    Sveta=GenTree.Che("Lipatova", "Svetlana", "Vadimovna", piplArr)

    SergBar=GenTree.Che("Baranov", "Sergey", "Hzhzhz", piplArr)
    Lena=GenTree.Che("Baranova", "Elena", "Evgenjevna", piplArr)
    Nastja=GenTree.Che("Baranova", "Anastasija", "Sergeevna", piplArr)
    
    SergPra=GenTree.Che("Lipatov", "Sergey", "Hzhzhz", piplArr)#Deda Otec
    Dusja=GenTree.Che("Lipatova", "Evdokija", "Hzhzhz", piplArr)#Deda Mama
    SashaDedBro=GenTree.Che("Lipatov", "Alexandr", "Sergeevich", piplArr)#Deda Brat

    IvanPra=GenTree.Che("NotLip", "Ivan", "Hzhzhz", piplArr)#Bbshk Otec
    KlavaPra=GenTree.Che("NotLip", "Klavdija", "Hzhzhz", piplArr)#Bbshk Mama
    
    ZoyaS=GenTree.Che("NotSokolova", "Zoya", "Ivanovna", piplArr)
    ZinaS=GenTree.Che("Kosheleva", "Zinaida", "Ivanovns", piplArr)
    LubaS=GenTree.Che("NotSokolova", "Lubov'", "Ivanovna", piplArr)
    DLenjaK=GenTree.Che("Koshelev", "Leonid", "Georgievich", piplArr)
    LeshaK=GenTree.Che("Koshelev", "Alexey", "Leonidovich", piplArr)
    NatashaK=GenTree.Che("Kosheleva", "Natalyja", "Hzhzhz", piplArr)
    LeonidBrat=GenTree.Che("Koshelev", "Leonid", "Alexeevich", piplArr)
    DSlavaS=GenTree.Che("Sokolov", "Vjacheslav'", "Ivanovich", piplArr)
    NatashaS=GenTree.Che("Sokolova", "Natalyja", "Hzhzhz", piplArr)
    NastjaS=GenTree.Che("Sokolova", "Anastsija", "Vjacheslavovna", piplArr)
    ToljaKud=GenTree.Che("Kudrjavcev", "Anatolyi", "Hzhzhz", piplArr)
    SevaBrat=GenTree.Che("Kudrjavcev", "Vsevolod", "Anatoljevich", piplArr)
    SlavaBrat=GenTree.Che("Kudrjavcev", "Svjatoslav", "Anatoljevich", piplArr)
    PlatonBrat=GenTree.Che("Kudrjavcev", "Platon", "Anatoljevich", piplArr)
    #=GenTree.Che("", "", "", piplArr)

    #Ilya.AllOut()

    Ilya.setParents(Alex, Nat)
    Nat.setParents(Evg, Gala)
    Alex.setParents(Leonid, Valja)
    Lena.setParents(Evg, Gala)
    Nastja.setParents(SergBar, Lena)
    SergLips.setParents(Leonid, Valja)
    Leonid.setParents(SergPra, Dusja)
    SashaDedBro.setParents(SergPra, Dusja)
    #Not only Koshelevi
    Valja.setParents(IvanPra, KlavaPra)
    ZinaS.setParents(IvanPra, KlavaPra)
    ZoyaS.setParents(IvanPra, KlavaPra)
    LubaS.setParents(IvanPra, KlavaPra)
    DSlavaS.setParents(IvanPra, KlavaPra)
    LeshaK.setParents(DLenjaK, ZinaS)
    LeonidBrat.setParents(LeshaK, NatashaK)
    NastjaS.setParents(DSlavaS, NatashaS)
    SevaBrat.setParents(ToljaKud, NastjaS)
    SlavaBrat.setParents(ToljaKud, NastjaS)
    PlatonBrat.setParents(ToljaKud, NastjaS)
    # setParents(, )
        
    SergLips.marry(Sveta, 1989)
    Alex.marry(Nat, 1992)
    Leonid.marry(Valja, 1963)
    Evg.marry(Gala)
    SergBar.marry(Lena, 2004)
    DLenjaK.marry(ZinaS)
    LeshaK.marry(NatashaK)
    DSlavaS.marry(NatashaS)
    ToljaKud.marry(NastjaS)
    #.marry()

    return piplArr

    
