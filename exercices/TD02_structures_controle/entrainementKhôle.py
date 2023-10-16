"""import time
import random"""
import re
"""
b = 0
tempsDepart = time.time()
for i in range(5):
    num1 = random.randint(0, 9)
    num2 = random.randint(0, num1)
    reponseEleve = int(input("Que vaut"+str(num1)+"-"+str(num2)+"?"))
    reponse = num1-num2
    if reponse == reponseEleve:
        print("bravo !!!")
        b += 1
    else:
        print("mauvaise réponse :/")

tempsFin = time.time()
tempsFinal = tempsFin-tempsDepart
print("Vous avez eu ", b, "bonnes réponses en", int(tempsFinal), 'secondes !')

b = 0
continuer = 'Y'
tempsDepart = time.time()
while continuer == 'Y':
    num1 = random.randint(0, 9)
    num2 = random.randint(0, num1)
    reponseEleve = int(input("Que vaut"+str(num1)+"-"+str(num2)+"?"))
    reponse = num1-num2
    if reponse == reponseEleve:
        print("bravo !!!")
        b += 1
    else:
        print("mauvaise réponse :/")
    continuer = str(input("Tapez 'Y' pour continuer "))

tempsFin = time.time()
tempsFinal = tempsFin-tempsDepart
print("Vous avez eu ", b, "bonne(s) réponse(s) en\
      ", int(tempsFinal), 'secondes !')

"""
"""res = " "  # chaine a afficher
cpt = 0  # compteur de nombres
for i in range(100, 1001):
    if i % 5 == 0 and i % 6 == 0:
        res += str(i) + " "  # on ajoute le nombre a la chaine courante
        cpt += 1  # on dit que l'on a un nombre de plus
        if cpt == 10:  # on a trouve 10 nombres
            print(res)
            res = " "  # on reinitiale les variables
            cpt = 0  # on reinitiale les variables
print(res)  # s'il manque des nombres non affichés
"""
"""
b1 = 0
b2 = 0
coup = ["pierre", "papier", "ciseau"]
print(" 0 : pierre, 1 : papier, 2 : ciseau")
while b1 < 3 and b2 < 3:
    coupOrdinateur = coup[random.randint(0, 2)]
    coupHumain = coup[int(input('Un nombre entre 0 et 2 ? '))]
    if coupHumain == 'pierre' and coupOrdinateur == 'ciseau':
        print("Vous avez gagnez !!! ")
        b1 += 1
    elif coupHumain == 'papier' and coupOrdinateur == 'pierre':
        print("vous avez gagné !!! ")
        b1 += 1
    elif coupHumain == 'ciseau' and coupOrdinateur == 'papier':
        print("Vous avez gagné !!!")
        b1 += 1
    elif coupOrdinateur == 'pierre' and coupHumain == 'ciseau':
        print("Vous avez perdue !!! ")
        b2 += 1
    elif coupOrdinateur == 'papier' and coupHumain == 'pierre':
        print("vous avez perdue !!! ")
        b2 += 1
    elif coupOrdinateur == 'ciseau' and coupHumain == 'papier':
        print("Vous avez perdue !!!")
        b2 += 1
    elif coupHumain == coupOrdinateur:
        print("Ex-eaquo !!!")

if b1 > b2:
    print("le score est de", b1, "pour vous et de", b2, "pour la machine,\
 vous avez donc gagné ! ")
elif b1 < b2:
    print("le score est de", b1, "pour vous et de", b2, "pour la machine,\
 vous avez donc perdue ! ")
"""

print("Pour que le mot de passe soit valide, vous devez respecter les \
conditions suivantes :\n\
- Au moins une lettre minuscule et une lettre en majuscule\n\
- Au moins un chiffre\n\
- Au moins un caractere parmi [$#@]\n\
- La longueur du mot de passe se situe entre 6 et 16 caractères")

mdp_utilisateur = str(input("rentrer un mot de passe ? "))
print(" Votre mot de passe est : ", mdp_utilisateur)

lettre_minuscule = re.search("[a-z]", mdp_utilisateur)
lettre_majuscule = re.search("[A-Z]", mdp_utilisateur)
chiffre = re.search("[0-9]", mdp_utilisateur)
caractere_special = re.search("[$,#,@]", mdp_utilisateur)


if (6 <= len(mdp_utilisateur) <= 16) and lettre_majuscule and lettre_minuscule and chiffre and caractere_special:
    print('mot de passe valide')
else:
    print("rentrer un nouveau mot de passe")
