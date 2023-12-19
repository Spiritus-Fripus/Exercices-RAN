#Ecrire un programme qui permet de générer un tableau d'entiers de 1 à n (saisie au clavier)
#EX: n=5 [1,2,3,4,5]

n = int(input("veuillez saisir un nombre: "))
n1= 1
tab = []

for i in range(n):
    tab.append(n1)
    n1+=1

print(tab)
