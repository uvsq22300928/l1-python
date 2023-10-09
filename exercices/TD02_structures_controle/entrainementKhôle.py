import time
import random

b=0
tempsDepart=time.time()
for i in range(5):
    num1=random.randint(0,9)
    num2=random.randint(0,num1)
    reponseEleve=int(input("Que vaut"+str(num1)+"-"+str(num2)+"?"))
    reponse=num1-num2
    if reponse==reponseEleve:
        print("bravo !!!")
        b+=1
    else:
        print("mauvaise réponse :/")

tempsFin=time.time()
tempsFinal=tempsFin-tempsDepart
print("Vous avez eu ", b, "bonnes réponses en", int(tempsFinal), 'secondes !')