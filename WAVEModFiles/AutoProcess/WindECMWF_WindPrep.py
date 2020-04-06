#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Dec 19 15:03:30 2019

@author: hydrobecs
"""

import numpy as np
from netCDF4 import Dataset
from datetime import datetime
import glob
import os

windfilesDir = '/home/hydrobecs/Documents/HindcastData/ECMWF/'
year = ['2017']

WindU = year[0]+'_UWind.nc'
WindV = year[0]+'_VWind.nc'

UWind = Dataset(windfilesDir+WindU)
VWind = Dataset(windfilesDir+WindV)

print(UWind.variables.keys())
Lon = UWind.variables['lon'][:].data
Lat = UWind.variables['lat'][:].data

Uwind = UWind.variables['uas'][:].data
Vwind = VWind.variables['vas'][:].data


firstRec = datetime(int(year[0]),1,1,0)
print(firstRec)

month = ['01','03','05','07','08','10','12']
month = ['04','06','09','11']
month = ['02']
month = ['10']

hour = [
            '00','01',
            '02','03'
            ,'04','05','06'
            ,'07','08','09'
            ,'10','11','12'
            ,'13','14','15'
            ,'16','17','18'
            ,'19','20','21'
            ,'22','23'
        ]
day =  [
             '01','02','03'
            ,'04','05','06'
            ,'07','08','09'
            ,'10','11','12'
            ,'13','14','15'
            ,'16','17','18'
            ,'19','20','21'
            ,'22','23','24'
            ,'25','26','27'
            ,'28'
            ,'29'
            ,'30'
            ,'31'
        ]

#FirstWind = datetime(int(year[0]),int(month[0]),int(day[0]),int(hour[0]))
#recordNum = int((FirstWind- firstRec).total_seconds()/3600)

#for i in np.arange(recordNum,size(time,0)):
#load Samples - U Wind
SwanGrdY = len(Lat)
SwanGrdX = len(Lon)

for m in range(0,np.size(month,0)):
    FirstWind = datetime(int(year[0]),int(month[m]),int(day[0]),int(hour[0]))
    recordNum = int((FirstWind- firstRec).total_seconds()/3600)
    k = recordNum
    UVopen = open(year[0]+month[m]+'_WindFile.wnd','w')
    for d in range(0,np.size(day,0)):
        for h in range(0,np.size(hour,0)):
            SWANGrd = np.zeros((SwanGrdY*2,SwanGrdX))
            SWANGrd[:SwanGrdY,:] = Uwind[k,:,:]
            SWANGrd[SwanGrdY:,:] = Vwind[k,:,:]
            
            np.savetxt(year[0] + month[m] + day[d] + '_' + hour[h]+'UVwnd_Perc',SWANGrd,fmt='%2.3f',delimiter=' ')

            UVopen.write(year[0] + month[m] + day[d] + '.' + hour[h] + '0000\n')
            Uopen = open(year[0] + month[m] + day[d] + '_' + hour[h]+'UVwnd_Perc','r')
            UVopen.write(Uopen.read())
            Uopen.close()
            k=k+1
    UVopen.close()
    for fle in glob.glob('*_Perc'):
        os.remove(fle)
            