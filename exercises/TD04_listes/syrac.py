def syracuse(n):
    """ Retourne la liste des valeurs de la suite en partant de n jusqu'à 1 """

    nb=[]
    while n!=1:
        if n%2==0:
            nb.append(n)
            n=n/2
        else:
            nb.append(n)
            n=3*n+1
    nb.append(n)
    return nb

print(syracuse(3))

def testeConjecture(n_max):
    """ Teste la conjecture de Collatz pour toutes les valeurs de 1 à n_max """
    conjecture=True
    for i in range(1,n_max):
        last_nb=syracuse(i)[-1]
        if last_nb!=1:
            conjecture=False
    
    return conjecture

print(testeConjecture(10000))


def tempsVol(n):
    """ Retourne le temps de vol de n """
    nb=[]
    compteur=0
    while n!=1:
        if n%2==0:
            nb.append(n)
            n=n/2
        else:
            nb.append(n)
            n=3*n+1
        compteur+=1
    nb.append(n)
    return compteur

print("Le temps de vol de", 3, "est", tempsVol(3))

def tempsVolListe(n_max):
    """ Retourne la liste de tous les temps de vol de 1 à n_max """
    temps_de_vol_total=[]
    for i in range(1,n_max):
        temps_de_vol_total.append(tempsVol(i))
    return temps_de_vol_total

#print(tempsVolListe(100))

def plus_grand_temps_de_vol(n_max):
    a=tempsVolListe(n_max)
    plus_grand_vol=max(a)
    print(plus_grand_vol)
    for i in range(len(a)):
        if plus_grand_vol==a[i]:
            indice_du_plus_grand=i+1
    return indice_du_plus_grand


print(plus_grand_temps_de_vol(10000))


def plus_grand_nb(n_max):
    plus_grand_nb_atteint=[1]
    plus_grand_entier=[]
    compteur=0
    for i in range(1,n_max):
    
        while i!=1:
            if i>max(plus_grand_nb_atteint):
                plus_grand_nb_atteint.append(i)
                plus_grand_entier.append(compteur)

            if i%2==0:
               
                i=i/2
            else:

                i=3*i+1
        compteur+=1
    plus_grand=max(plus_grand_nb_atteint)

    return plus_grand,max(plus_grand_entier)+1

print(plus_grand_nb(10000))