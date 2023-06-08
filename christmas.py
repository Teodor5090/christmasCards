import re
import os

with open('employees.txt',mode= 'r') as fileEm:
    j=0
    fileTem=open('template.txt', mode='r')


    for i in fileEm.read().splitlines():
      fileA = open("christmasCards/"+ i+ ".txt", mode='w') 
      for line in fileTem:
         fileA.write(line)

       
    
    
  #  for x in range(1,20):
       #  f = open("test"+str(x), 'w')
       #  f.write(str(x) + "\n" + str(20-x))
      #   f.close()