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

    while 0>j or j>31:
        j=int(input("jour: "))

    h=int(input("heure: "))

    while 0>h or h>24:
        h=int(input("heure: "))

    m=int(input("min: "))

    while 0>m or m>60:
        m=int(input("min: "))

    s=int(input("seconde: "))

    while 0>s or s>60:
        s=int(input("seconde: "))


    return (j,h,m,s)

#afficheTemps(demandeTemps())




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


def afficheDate(date):
    print(date[0],"années",date[1],"mois",date[2],"jour",date[3],"heure",date[4],"min",date[5],"sec")

    
temps = secondeEnTemps(1000000000)
afficheTemps(temps)
print(tempsEnDate(temps))
afficheDate(tempsEnDate(temps))
