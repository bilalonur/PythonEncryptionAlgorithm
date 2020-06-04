# Python ile şifreleme algoritması
# Bilal Onur Eskili // 04.06.2020 
# İletişim/For Contact: onur@bilalonureskili.com

import random as rd
import string 

#Encrypt Function
def sifrele(girdi):   
    karakter = len(girdi)
    anahtar = {"a":3,"b":5,"c":7,"d":11,"e":13,"f":17,"g":19,"h":23}           # Keys  (Prime numbers)
    kar_anah = {1:"A",2:"B",3:"C",4:"D",5:"E",6:"F",7:"G",8:"H",9:"J"}         # Keys for Character length encoding
    thash = 1                                                                  # Total product of prime numbers for input
    thash2 = ""                                                                # Order of numbers for input
    a = 0                                                                      # To find index of max 
    deg = []                                                                   # Prime number equivalents of input text in list (will use in ordering of maxs)
    
    rast = rd.choice(string.ascii_uppercase)+kar_anah[karakter]+rd.choice(string.ascii_uppercase)    # Last two charactesrs of output (two is randomized letter, other is encoded length of input)
    rast2 = ''.join(rd.choices(string.ascii_uppercase,k=3))                                          # First three randomized characters
    
    # To get prime numbers multiplication and adding these prime numbers to 'deg' list
    for i in girdi:
        thash *= anahtar[i]
        deg.append(anahtar[i])
    

    ceg = deg[::]  # Creating another equal list for getting index b/c we'll delete max of prime numbers in 'deg' list
    
    # We get max value of prime numbers in deg list and try to find index of this and add this to thash2
    while deg != []:
        maks = max(deg)
        if ceg.count(maks) > 1:
            try:
                m_in = ceg.index(maks,a)+1
            except:
                a = 0
                m_in = ceg.index(maks,a)+1
            a = m_in    
        else:
            m_in = ceg.index(maks)+1

        thash2 += str(m_in)
        deg.remove(maks)
    
    # returning output in a bit mixed way
    return rast2+thash2[0:(len(thash2)//2)+1]+str(thash)+thash2[(len(thash2)//2)+1:]+str(rast)

#Decrypt Function
def sifre_coz(girdi):
    anahtar = {"a":3,"b":5,"c":7,"d":11,"e":13,"f":17,"g":19,"h":23}
    kar_anah = {1:"A",2:"B",3:"C",4:"D",5:"E",6:"F",7:"G",8:"H",9:"J"}

    # Dictionary to list
    key_anahtar = list(anahtar.keys())         
    val_anahtar = list(anahtar.values()) 

    key_kar = list(kar_anah.keys()) 
    val_kar = list(kar_anah.values())    

    karakter = int(key_kar[val_kar.index(girdi[-2])])   # Get encoded length of encrypted word and decode it

    c = girdi[3:(3+karakter//2)+1]                      # Order of prime numbers 
    d = girdi[-4:-3+(-karakter//2):-1]                  # Order of prime numbers 
    d = d[::-1]
    thash = int(girdi[4+karakter//2:len(girdi)+(-3+(-karakter//2)+1)])     # Multiplication of prime numbers
    thash2 = c+d                                                           # Joined order of prime numbers (final version)
    deger = []                     # List that includes prime numbers of encrypted word
    cozum = {}                     # Order of prime numbers in encrypted word
    cikti = ""                     # Decrypted word 
    for i in val_anahtar:
        while thash%int(i) == 0:
            deger.append(int(i))
            thash /= int(i)
    for t in thash2:
        cozum[int(t)] = max(deger)
        deger.remove(max(deger))

    for f in range(1,karakter+1):
        cikti += key_anahtar[val_anahtar.index(cozum[f])]
    return cikti



x = input("Şifrelenecek? ")          # Trying encrypt function
print(sifrele(x))

y = input("Çözülecek Şifre? ")       # Trying decrypt function
print(sifre_coz(y))

