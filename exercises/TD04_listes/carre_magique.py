

def affichage(carre):
    for i in range(len(carre)):
        print("\n| ",end="")
        for j in range(len(carre[i])):
            
            print(str(carre[i][j])+" | ",end="")
    print("")


def testLignesEgales(carre):

    egal=True

    liste_somme=[]
    for i in range(len(carre)):
        somme=0
        for j in range(len(carre[i])):

            somme+=carre[i][j]

        liste_somme.append(somme)

    for k in range (len(liste_somme)):
        for l in range(len(liste_somme)):
            if liste_somme[k]!=liste_somme[l]:
                egal=False  
    return egal


def testColonnesEgales(carre):
    """ Renvoie la somme des éléments d'une colonne de la liste 2D carre si toutes les colonnes ont la même somme, et -1 sinon """
    egal=True

    liste_somme=[]
    for i in range(len(carre)):
        somme=0
        for j in range(len(carre[i])):

            somme+=carre[j][i]

        liste_somme.append(somme)

    for k in range (len(liste_somme)):
        for l in range(len(liste_somme)):
            if liste_somme[k]!=liste_somme[l]:
                egal=False  
    return egal



def testDiagonalesEgales(carre):
    """ Renvoie la somme des éléments d'une diagonale de la liste 2D carre si les 2 diagonales ont la même somme, et -1 sinon """
    egal=True
    somme=0
    somme_2=0
    liste_somme=[]
    for i in range(len(carre)):
       
        somme+=carre[i][i]
        somme_2+=carre[i][-i-1]
        #print(carre[i][i])
    
    #print(somme,somme_2)

    if somme!=somme_2:
        egal=False


    return egal

def estCarreMagique(carre):
    """ Renvoie True si c'est un carre magique et False sinon"""
    magique=True
    if testColonnesEgales(carre) == False or testDiagonalesEgales(carre)==False or testLignesEgales(carre)==False:
        magique=False
    
    return magique


def estNormal(carre):
    """ Retourne True si contient toutes les valeurs de 1 à n^2 où n est la taille 
        du carré, et False sinon """
    normal=True
    element=[]
    for i in range(len(carre)):
        for j in range(len(carre[i])):
            element.append(carre[i][j])
    
    for k in range(1,len(carre[0])**2+1):
        if k not in element:
            normal=False
    return normal

                

 



carre_mag=[[4,14,15,1],[9,7,6,12],[5,11,10,8],[16,2,3,13]]
carre_non_mag=[[4,14,15,1],[9,7,6,12],[5,11,10,8],[16,2,7,13]]

affichage(carre_mag)

#print("\n",testLignesEgales(carre_mag))
#print(testColonnesEgales(carre_mag))
#print(testDiagonalesEgales(carre_mag))
print(estCarreMagique(carre_mag))
print(estNormal(carre_mag))


#print("\n",testLignesEgales(carre_non_mag))
#print(testColonnesEgales(carre_non_mag))
#print(testDiagonalesEgales(carre_non_mag))
print(estCarreMagique(carre_non_mag))
print(estNormal(carre_non_mag))