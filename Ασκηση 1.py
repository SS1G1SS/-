import multiprocessing
import random
import math
import time

rows = int(input("Δώσε το μήκος του τετραγώνου: "))
cols = int(input("Δώσε το ύψος του τετραγώνου: "))
pop = rows * cols
hpop = math.ceil(pop / 2)
arr = [[0 for x in range(rows)]for y in range(cols)] 
fc = 0
fch = 0
fcv = 0
fcd = 0
quad = 0

for n in range(100):
  c = 0
  for j in range(rows):
    for i in range(cols):
         a = random.randint(0,1) #Επιλέγει τυχαία 0 ή 1 ,εαν ειναι 1 και δεν έχει φτάσει το μισό πλήθος του πίνακα βάζει 1 στην θεση του αλλιως βάζει 0
         if c == hpop:
             break
         if a == 1 and c != hpop and arr[j][i] != 1 :
             arr[j][i] = 1 
             c += 1
         elif arr[j][i]:
             arr[j][i] = 0
  
  if c < hpop:           #Κάνει έλεγχο εαν υπάρχουν λιγότερες μονάδες απο οτι πρέπει και τις συμπληρώνει 
       while c < hpop:
           for q in range(rows):
               for f in range(cols):
                if  c == hpop:
                    break
                if arr[q][f] == 1:
                    continue
                elif arr[q][f] == 0:
                    arr[q][f] = 1
                    c += 1
                

  elif c > hpop:       #Κάνει έλεγχο εαν υπάρχουν περισσότερες μονάδες απο οτι πρέπει και τις αφαιρεί
       while c > hpop:
           for g in range(rows):
               for v in range(cols):
                   if c == hpop:
                      break
                   elif c > hpop and arr[g][v] == 1:
                       arr[g][v] = 0
                       c -= 1
                                            
  g = 0
  f = 0
  v = 0
  q = 0

  
  for s in range(rows):
     for d in range(cols): #Μετράει τετράδες οριζόντια και κάθετα 
       if arr[s][d] == 1:
         fch += 1
       else:
         fch = 0
       if fch == 4:
         quad += 1
         fch = 0
       if arr[d][s] == 1:
         fcv += 1
       else:
         fcv = 0
       if fcv == 4:
         quad += 1
         try:
            if arr[s + 1][d + 1] == 1:
              quad += 1
         except:
              pass
         fcv = 0

         
  for cd in range(rows):
    for vb in range(cols): #Μετράει τετράδες διαγώνια
      if vb == cd:
        if arr[cd][vb] == 1:
          fcd += 1
        if fcd == 4:
          quad += 1
          try:
            if arr[cd + 1][vb + 1] == 1:
              quad += 1
          except:
            pass
          fcd = 0
          
        break
      else:
        break
  '''for h in range(rows):
    print(arr[h])
  print(" ")''' #Εάν θέλετε να εμφανίζει τους πίνακες  

print("Ο μέσος όρος των τετράδων είναι: ",quad/n)
time.sleep(10)

