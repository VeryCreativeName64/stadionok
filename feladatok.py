from Stadion import Stadion
from datetime import datetime
import fajlbeolvas


stadionok=fajlbeolvas.beolvas("stadionok.txt",[])

def newyorkstadion():
    i=0
    newyork=0
    for i in range(0,len(stadionok),1):
        if ((stadionok[i].varos)=="New York"):
            newyork+=1
        i+=1

    print(f"{newyork} darab stadion van New Yorkban.")



def ossz_csapat():
    i=0
    csapatszam=0
    for i in range(0,len(stadionok),1):
        if((stadionok[i].csapatok_szama)):
            csapatszam+=stadionok[i].csapatok_szama
        i+=1
    
    print(f"{csapatszam} darab focicsapat van összesen.")



def buffalo_csapat():
    i=0
    buffcsapat=0
    for i in range(0,len(stadionok),1):
        if((stadionok[i].varos)=="Buffalo"):
            buffcsapat+=stadionok[i].csapatok_szama
        i+=1
    
    print(f"{buffcsapat} darab csapat játszott Buffaloban.")


def ezerkilencszaz():
    i=0
    kilencszaz=[]
    for i in range(0,len(stadionok),1):
        if(stadionok[i].elso_merk<datetime.strptime("1900-01-01","%Y-%m-%d")):
            kilencszaz.append(stadionok[i].nev)
        i+=1

    print(f"Stadionok, ahol 1900.01.01 előtt játszottak: {kilencszaz}")

def ketezer():
    i=0
    kettoezer=0
    for i in range(0,len(stadionok),1):
        if(stadionok[i].utolso_merk<datetime.strptime("2000-01-01","%Y-%m-%d")):
            kettoezer+=1
        i+=1
    
    print(f"{kettoezer} darab stadionban nem volt mérkőzés 2000 óta.")

def beker():
    parosszam1=int(input("Kérem az 1. páros számot: "))
    while(parosszam1%2!=0):
        parosszam1=int(input("Ez nem páros. Egy 1. PÁROS számot kérek: "))
    if(parosszam1%2==0):
        parosszam2=int(input("Kérem a 2. páros számot: "))
        while(parosszam2%2!=0):
            parosszam2=int(input("Ez nem páros. Egy 2. PÁROS számot kérek: "))
        if(parosszam2%2==0):
            parosszam3=int(input("Kérem a 3. páros számot: "))
            while(parosszam3%2!=0):
                parosszam3=int(input("Ez nem páros. Egy 3. PÁROS számot kérek: "))
            if(parosszam3%2==0):
                print(parosszam1,parosszam2,parosszam3)


        
        
