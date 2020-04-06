#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Mar  2 09:22:17 2020

@author: hydrobecs
"""

import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from datetime import datetime
from datetime import timedelta
from scipy.interpolate import interp1d
import os


__author__ = 'Frans van Eeden'
__email__ = 'frans.vaneeden@ugent.be'
__created__ = datetime(2020, 3,2)
__modified__ = datetime(2020, 3, 16)
__version__ = "0.1"
__status__ = "Development"

swanSpecFileIn = 'GridNest_ZBR_SWASH_BND_2.sp2'
swanSpecFileIn = 'GridNest_OST_SWASH_BND.sp2'
DateStart = datetime(2011,12,7,0)
DateEnd = datetime(2011,12,7,4) #8,6)
diff = DateEnd - DateStart
NumRecs = int(diff.days*24 + diff.seconds/3600)

#def swan1Dspec_toDataframe(swanSpecFileIn,DateStart,DateEnd,NumRecs):

    '''
    This function reads in a SWAN 1D spectral file and extracts the Energy, Period and Direction
    per TimeStamp and Per location
    
    In: 1D SWAN Spectrum file
        Number of time steps (eg 1 year simulation output every hour: numTime = 365 x 24)
    Output is 4D array with:
        1 Dim = Energy, Period and Direction
        2 Dim = Frequency
        3 Dim = Locations
        4 Dim = NumTime
        
    awkCheck:
        awk 'NR==6991313,NR==6991380' Spec_MDK_lrg.sp1
        ModelSpect[:,:,-1,-1].T
    '''
    
    Fopen = open(swanSpecFileIn, 'r')
    #HeadFile
    #lines = Fopen.readlines()
    l = Fopen.readlines()
    #lines = l
    Header = []
    [Header.append(Hd) for Hd in l[:][0:3]]
    #Header.append('LOCATIONS                                   locations in x-y-space')
    [Header.append(Hd) for Hd in l[:][5:6]]
    Header.append('      2                                 number of locations')
    Locations = int(l[6][:7])
    loc = 6 + Locations + 2
    SWANloc = []
    [SWANloc.append(Sloc) for Sloc in l[:][7:loc-1]]
    SWANFreq = []
    numFreq = int(l[loc][:7])
    [SWANFreq.append(SwFre) for SwFre in l[:][loc-1:loc+1+numFreq]]
   
    SWANfreq = np.array([float(i) for i in l[:][loc+1:loc+1+numFreq]])
    startDir = loc+2+numFreq
    numDir = int(l[loc+numFreq+2][:7])
    SWANDir = []
    [SWANDir.append(SwDir) for SwDir in l[:][startDir-1:startDir+numDir+1]]
    tHstart = startDir+numDir+2
    tailHeader = []
    [tailHeader.append(tHead) for tHead in l[tHstart-1:tHstart + 4]]

    ''' Calc start int for start date'''
    startNum = 16 + Locations + numFreq + numDir
    SpecStartDate = datetime(int(l[startNum][:4]),int(l[startNum][4:6]),int(l[startNum][6:8]),int(l[startNum][9:11]),int(l[startNum][11:13]))
    timeStart = int((DateStart - SpecStartDate).total_seconds()/3600)
    timesim = int((DateEnd - DateStart).total_seconds()/3600)
    timeStartLoc = startNum + timeStart*(Locations*(numFreq+2)+1)
    l[:][timeStartLoc]
    
    ''' Loop through 2D spec file to extract individual components, assemble and write to file '''
    i=0
    fileNum = 0
    #FleList = open('LocLIST.txt','w')
    #FleList.write('LOCLIST\n')
    for fileNum in range(timesim):
        newTime = timeStartLoc +fileNum*(numFreq+2)*Locations+i
        #print (newTime, l[newTime][:15])
        newpath = l[newTime][:8] + '_' + l[newTime][9:11] 
        if not os.path.exists(newpath):
            os.makedirs(newpath)
        os.chdir(newpath)  
        FBndOpen = open(l[newTime][:8] + '_BND.txt','w')
        for locs in range(Locations-1):
            locList = []
            tStartLoc = timeStartLoc + 1 +fileNum*(numFreq+2)*Locations + locs*(numFreq+2)+i
            tmpSpec = []
            tmpSpec = l[tStartLoc:tStartLoc+numFreq+2][:]
            secLocIs = tStartLoc+numFreq+2
            tmpSpec2 = []
            tmpSpec2 = l[secLocIs:secLocIs+numFreq+2][:]
            locList.append('\n'+SWANloc[locs])
            locList.append(SWANloc[locs+1])
            print (l[newTime][:15] + '_loc' + str(locs+1) + '.inp')
            print (tStartLoc,l[tStartLoc][:15] )
            FleOpen = open('loc'+ str(locs+1) + '_' + l[newTime][:8] + '_' + l[newTime][9:11] + '.inp','w')
            [FleOpen.write(Header[i]) for i in range(len(Header))]
            [FleOpen.write(locList[i]) for i in range(len(locList))]
            [FleOpen.write(SWANFreq[i]) for i in range(len(SWANFreq))]
            [FleOpen.write(SWANDir[i]) for i in range(len(SWANDir))]
            [FleOpen.write(tailHeader[i]) for i in range(len(tailHeader))]
            [FleOpen.write(tmpSpec[i]) for i in range(len(tmpSpec))]
            [FleOpen.write(tmpSpec2[i]) for i in range(len(tmpSpec2))]
            FleOpen.close()
            FBndOpen.write('BOU SEGM XY ')
            [FBndOpen.write(locList[i].strip('\n')) for i in range(len(locList))]
            FBndOpen.write(" BTYPE WEAK VAR SPECSWAN '")
            FBndOpen.write('loc'+ str(locs+1) + '_' + l[newTime][:8] + '_' + l[newTime][9:11] + ".inp' ")
            FBndOpen.write('55 min\n')
        FBndOpen.close()
        i=i+1
        os.chdir('../')
            #FlOpen = open('loc'+ str(locs+1) + '_' + l[newTime][:8] + '_' + l[newTime][9:11] + '.inp','w')
            #FlOpen.close()
        
        #locList = list(map(str.strip, locList))
        #LocList = open('LocLIST_' + l[newTime][:15] + '.txt','w')
        #LocList.write('LOCLIST\n')
        #[LocList.write(locList[j] + '   FileList_loc'+ str(j+1) + '.txt\n') for j in range(len(locList))]
        #LocList.close()
        #LocList.write('LocLIST_' + l[newTime][:15] + '.txt')
        #i = i +1
    #LocList.close()
    
    FCFirstDate - timedelta(days=2)
    FistSpecRec = tHstart+4
    RecordLen = numFreq+2
    DateBlockLen =  (numFreq+2)*Locations
    l[:][FistSpecRec]
    l[:][RecordLen]
    l[:][FistSpecRec+DateBlockLen+1]

   
    
    ModelSpect = np.zeros((3,numFreq,Locations,numTime))
    startNum = 20 + Locations + numFreq
    t=0
    while startNum < len(l)-1:
        
        if  l[startNum][len(l[startNum])-14:] == 'date and time\n':
            dateStr = datetime(int(l[startNum][:4]),int(l[startNum][4:6]),int(l[startNum][6:8]),int(l[startNum][9:11]),int(l[startNum][11:13]))
        if t == 0:
            DateStr = np.array(dateStr,dtype='datetime64')
            print('Time (t) = ',t,' ',DateStr)
        else:
            DateStr = np.append(DateStr,dateStr)
            #print('Time (t) = ',t,' ',DateStr[t])
            
        for j in range(Locations):
            #print('Location (j+1) = ',j+1)
            if l[startNum+1][:3] == 'LOC':
                startNum = startNum + 1
                for i in range(numFreq):
                    ModelSpect[:,i,j,t] = list(map(float,l[startNum+1+i].split()))
                    if ModelSpect[0,i,j,t] > 0:
                        ModelSpect[0,i,j,t] = ModelSpect[0,i,j,t]/(1025*9.81)
                    else:
                        continue
                startNum = startNum + numFreq   
            elif l[startNum+1][:3] == 'NOD':
                startNum = startNum + 1
            #try:
                #print(l[startNum+1][:15])
            #except:
                #continue
            #print('startNum = ', startNum)
        t=t+1
        startNum = startNum + 1
    return ModelSpect, DateStr, SWANfreq