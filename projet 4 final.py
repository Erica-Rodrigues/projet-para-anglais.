somme_joueur = 100
list_r = [2, 4, 6, 8, 10, 12, 14, 16, 18, 20,
          22, 24, 26, 28, 30, 32, 34, 36]
list_n = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19,
          21, 23, 25, 27, 29, 30, 31, 33, 35]
list_a =[]
list_p=[]
NP = int(input("Combien de paris souhaitez vous effectuer ? "))
for x in range(NP):
    list_a.append(int(input("Combien d'argent souhaitez vous parier ? ")))
    list_p.append(input("Que souhaitez vous parier ?"))
    if sum(list_a)>=somme_joueur:
        continue
import random
b = random.randint(0, 36)
print(b)
i = 0
while i < len(list_p):
    if list_p[i] == b or b == 0 and list_p[i] == "vert":
        somme_joueur = somme_joueur + (list_a[i]*35)
    elif b == 0 and list_p[i] == "rouge" or b == 0 and list_p[i] == "noir":
        somme_joueur = somme_joueur - list_a[i] 
    elif b == 0 and list_p[i] == "pair" or list_p[i] == "impair":
        somme_joueur = somme_joueur - list_a[i]
    elif b in list_r and list_p[i] == "pair" or b in list_r and list_p[i]=="rouge":
        somme_joueur = somme_joueur + list_a[i]
    elif b in list_n and list_p[i] == "impair" or b in list_n and list_p[i] == "noir":
        somme_joueur = somme_joueur + list_a[i]
    else:
        somme_joueur = somme_joueur - list_a[i]
    i = i + 1
    if somme_joueur == 0:
        print("Vous êtes arrivé à zéro, vous devez quitter le casino")