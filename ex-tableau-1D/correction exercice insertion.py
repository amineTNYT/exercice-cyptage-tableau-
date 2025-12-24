from numpy import *
def saisir():
    global N,P,X
    N=int(input("N="))
    while not(N in range(2,100)):
        N=int(input("N="))
    P=int(input("P="))
    #while not(P in range(0,N)):
    while not(0<=P<=N-1):
        P=int(input("P="))

    X=int(input("X="))

def remplir(N):
    #global T erreur
    for i in range(N):
        T[i]=int(input("T["+str(i)+"]= "))

def decale(P,X):
    global N
    N=N+1
    for i in range (N-1,P,-1):
        T[i]=T[i-1]
    T[P]=X

def afficher(T,N):
    for i in range(N):
        print(T[i],end="|")
    print()

#pp
saisir()
T=array([int()]*(N+1))
remplir(N)
afficher(T,N)
decale(P,X)
afficher(T,N)
