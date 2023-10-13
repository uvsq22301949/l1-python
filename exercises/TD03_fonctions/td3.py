#temps[0] : jours, temps[1]: heures, temps[2]: minutes, temps[3]: secondes

def tempsEnSeconde(temps):
    """ Renvoie la valeur en seconde de temps donné comme jour, heure, minute, seconde."""
    return 3600*24*temps[0]+3600*temps[1]+60*temps[2]+temps[3]



def secondeEnTemps(seconde):
    """Renvoie le temps (jour, heure, minute, seconde) qui correspond au nombre de seconde passé en argument"""

    return seconde//(3600*24),(seconde%(3600*24))//3600,((seconde%(3600*24))%3600)//60,((seconde%(3600*24)%3600)%60)



temps = (3,23,1,34)
print(type(temps))
print(tempsEnSeconde(temps)) 

temps = secondeEnTemps(100000)
print(temps)
print(temps[0],"jours",temps[1],"heures",temps[2],"minutes",temps[3],"secondes")
print(tempsEnSeconde(temps)) 




#fonction auxiliaire ici

def afficheTemps(temps):
    if temps[0]>1:
        print(temps[0],"jours",end=" ")
    else:
        print(temps[0],"jour",end=" ")
    
    if temps[1]>1:
        print(temps[1],"heures",end=" ")
    else:
        print(temps[1],"heure",end=" ")

    if temps[2]>1:
        print(temps[2],"minutes",end=" ")
    else:
        print(temps[2],"minute",end=" ")

    if temps[2]>1:
        print(temps[3],"secondes")
    else:
        print(temps[3],"seconde")
    
afficheTemps((1,0,14,23)) 


def demandeTemps():

    j=int(input("jour: "))

    while 0>j :
        j=int(input("jour: "))

    h=int(input("heure: "))

    while 0>h or h>=24:
        h=int(input("heure: "))

    m=int(input("min: "))

    while 0>m or m>=60:
        m=int(input("min: "))

    s=int(input("seconde: "))

    while 0>s or s>=60:
        s=int(input("seconde: "))


    return (j,h,m,s)

afficheTemps(demandeTemps())




def sommeTemps(temps1,temps2):

    temps1=tempsEnSeconde(temps1)
    temps2=tempsEnSeconde(temps2)
    temps=temps1+temps2
    temps=secondeEnTemps(temps)

    return temps

afficheTemps(sommeTemps((2,3,4,25),(5,22,57,1)))


def proportionTemps(temps,proportion):

    temps=tempsEnSeconde(temps)
    temps*=proportion

    return secondeEnTemps(temps)



afficheTemps(proportionTemps(proportion=0.2,temps=(2,0,36,0)))
#appeler la fonction en échangeant l'ordre des arguments



def tempsEnDate(temps):
    date_0=(1970,0,1,0,0,0)
    date= temps[0]//365,(temps[0]%365)//31,temps[0]%365,temps[1],temps[2],temps[3]
    jour_mois=(31,28,31,30,31,30,31,31,30,31,31,30,31)

    
    a=date[0]+date_0[0]
    m=date[1]+date_0[1]
    j=date[2]+date_0[2]
    h=date[3]+date_0[3]
    min=date[4]+date_0[4]
    s=date[5]+date_0[5]

    if s>60:
        h+=1
        s=s%60

    if min>60:
        h+=1
        min=min%60

    if h>24:
        j+=1
        h=h%24

    if j>31:
        m+=1
        j=j%31

    if m>12:
        a+=1
        m=m%12

    if jour_mois[m]<j:
        j=j%jour_mois[m]
        m+=1

    date=a,m,j,h,min,s
    return date


def afficheDate(date=(1970,0,1,0,0,0)):
    #print(date)
    mois=('janvier','février','mars','avril','mai','juin','juillet','aout','septembre','octobre','novembre','décembre')
    print(date[2],mois[date[1]],date[0],date[3],":",date[4],":",date[5])

    
temps = secondeEnTemps(1000000000)
afficheTemps(temps)
print(tempsEnDate(temps))
afficheDate(tempsEnDate(temps))


def bisextile(jour):
    compteur_annee_bisextile=1970
    annee_bisextile=[]

    while jour>0:

        
        #print(compteur_annee_bisextile-1968)
        #print(compteur_annee_bisextile)

        if ((compteur_annee_bisextile-1968)%4==0):  

            if ((compteur_annee_bisextile)%100==0 and (compteur_annee_bisextile)%400!=0 ):
                
                jour-=365

            else: 
                annee_bisextile.append(compteur_annee_bisextile)
                jour-=366
        else:

            jour-=365

        compteur_annee_bisextile+=1

    return annee_bisextile
print(bisextile(20000))


def nombreBisextile(jour):
   return len( bisextile(jour))


def tempsEnDateBisextile(temps):

    date_0=(1970,0,1,0,0,0)
    
    new_temps=temps[0]-nombreBisextile(temps[0])*366

    date= new_temps//365,(new_temps%365)//31,new_temps%365,temps[1],temps[2],temps[3]


    
    a=date[0]+date_0[0]
    m=date[1]+date_0[1]
    j=date[2]+date_0[2]
    h=date[3]+date_0[3]
    min=date[4]+date_0[4]
    s=date[5]+date_0[5]

    if s>60:
        h+=1
        s=s%60

    if min>60:
        h+=1
        min=min%60

    if h>24:
        j+=1
        h=h%24

    if j>31:
        m+=1
        j=j%31

    if m>12:
        a+=1
        m=m%12


    date=a,m,j,h,min,s
    return date
    





temps = secondeEnTemps(1000000000)
afficheTemps(temps)
afficheDate(tempsEnDateBisextile(temps))
afficheDate(tempsEnDate(temps))


def verifie(liste_temps):

    seconde_des_semaines=0
    for i in range(len(liste_temps)):
        if tempsEnSeconde(liste_temps[i])<48*3600:
            print(f"semaine {i} ok")

    for j in range(len(liste_temps)):
        seconde_des_semaines+=tempsEnSeconde(liste_temps[j])
    if seconde_des_semaines<140*3600:
        print("mois ok")


liste_temps = [[1,2,39,34],[0,1,9,4],[0,29,39,51],[0,31,13,46]]
verifie(liste_temps)
