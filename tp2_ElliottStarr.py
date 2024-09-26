"""
elliott starr
2024-09-13
jeux de devinette
"""


from random import *

while True:

    # l'ordinateur coisis un nombre entre 0 et 1000
    num = randint(0, 1000)
    print(num)
    print("J’ai choisi un nombre au hasard entre 0 et 1000.")

    # l'humain devine
    print("À vous de le deviner...")
    ges = 0
    nb_ges = 1

    while int(ges) != int(num):

        ges = input("Entrez votre essai : ")

        if int(num) == int(ges):
            print("Bravo! Bonne réponse")
            print("vous avez réusi en", nb_ges, "essai")
            rec = input("voulez vous recomencer? entrez o/n.")

            if rec == "o":
                print("ok")

            elif rec == "n":
                print("ok")
                exit()

        elif int(num) < int(ges):
            print("le nombre est plus petit")
            nb_ges += 1

        elif int(num) > int(ges):
            print("le nombre est plus grand")
            nb_ges += 1
