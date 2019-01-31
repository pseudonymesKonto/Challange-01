import random

for x in range (1):# Fopr x create (one) number :
 zufaeligeZahl = random.randint(0, 100)#numbers between 0 and 100.
print("Das ist das Zahlenratespiel. Dein Ziel ist es die zufällige Zahl zu finden")
eingabe = int(input("Gib eine Zahl ein"))

while eingabe != zufaeligeZahl:
 if eingabe > zufaeligeZahl:
  print("Dein Tipp ist größer als die gesuchte Zahl")
  eingabe = int(input("gib bitte einen neuen Tipp ab "))
  #Ende of if-condition

 else:
  print("Dein Tipp ist kleiner als die gesuchte Zahl")
  eingabe = int(input("gib bitte einen neuen Tipp ab "))
  #End of else-condition
  
#still part of while-loop 
print("Glückwunsch! Du hast die richtige Zahl erraten. ")
print("Die gesuchte Zahl war") 
print(zufaeligeZahl)
#End of program
