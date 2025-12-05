#CORRECTION
from numpy import array
# Fonction pour saisir la taille
def sasir():
    n = int(input("Donner la taille du tableau : "))
    while not (2 <= n <= 100):
        n = int(input("Donner la taille du tableau : "))
    return n

# Fonction pour remplir le tableau
def remplir(t, n):
    for i in range(n):
        t[i] = input("t["+str(i)+"]= ")
        while not (0 < len(t[i]) < 20):
            print("La longueur doit être entre 1 et 19 caractères")
            t[i] = input("t["+str(i)+"]= ")
def crypter_message(msg):
    if len(msg) == 0:
        return msg
    
    cle = msg[0]
    message_crypte = ""
    
    for caractere in msg:
        code = ord(cle) + ord(caractere)
        if code > 127:
            code = code - 127
        message_crypte += chr(code)
    
    return message_crypte

def crypter_tableau(t, n):
    for i in range(n):
        crypt[i] = crypter_message(t[i])
    return crypt



# Fonction pour afficher
def afficher(t, n, nom):
    print(f"\n{nom} :")
    for i in range(n):
        print(f'"{t[i]}"', end=" ")
    print()

# Programme Principal
# Saisie de la taille
n = sasir()
# Création des tableaux
t = array([str] * n)
# Remplissage
remplir(t, n)
# Affichage avant cryptage
afficher(t, n,)
crypter_tableau(t,n)
afficher(t, n,)


