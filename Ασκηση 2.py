import multiprocessing
import random
import time


def fibo(x):
    if x == 1 or x == 2:
        return 1
    elif x > 2:
        return fibo(x-1)+fibo(x-2)  
    elif x < 1:
        return -1
fib = 0   
while fib < 1:
    fib = int(input("Δώσε έναν αριθμό για να τον αντιστοιχίσω με την ακολουθία Fibonacci: "))
    if fib >= 1 :
        n = fibo(fib)
        print ("Ο όρος της ακολυθίας που επέλεξες είναι:", n) 
c = 0
for i in range (20):
    a = random.randint(1,2**32)
    if n != 1 and (a**n) % n == a % n: 
         c += 1        

if c == 20:
    print ("Ο αριθμός", n ,"είναι πρώτος")
else:
    print ("Ο αριθμός", n ,"ΔΕΝ είναι πρώτος")

time.sleep(5)
