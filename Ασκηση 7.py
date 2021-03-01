import requests
import multiprocessing
import simplejson as json
import numpy
import time
from datetime import datetime

nowdate = datetime.today().date()

y = nowdate.day
arr = [0 for x in range(81)]
for x in range(1,y + 1):
   fdom = str(nowdate.replace(day=x))
   url = "https://api.opap.gr/draws/v3.0/1100/draw-date/"+fdom+"/"+fdom
   r = requests.get(url)
   d = r.json()
   for i in range(10):
      for j in range(20):
         k = d['content'][i]['winningNumbers']['list'][j]
         arr[k] += 1
   maxelmnt = numpy.where(arr == numpy.amax(arr))
   print("Ο/Οι αριθμός/οί που εμφανίστικε/καν τις περισσότερες φορές στις",fdom,"είναι",maxelmnt)
   print("--------------------------------------------------------------------------------------")
   for rty in range(81):
      arr[rty] = 0
   maxint = 0  
time.sleep(10)
