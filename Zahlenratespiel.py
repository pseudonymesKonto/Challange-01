import random

for x in range (1):# Für x soll im Bereich (1) :
 zufaeligeZahl = random.randint(1, 100)# Zahlen zwischen (1 und 100) ausgegeben werden.
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
