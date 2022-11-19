def cherche_tous_chemins(graphe, depart,arrivee):
    chemins = []
    if not(depart in graphe.keys()) or not(arrivee in graphe.keys()):
        return None
    pile = [(depart,[depart])]
    while len(pile) != 0:
        sommet,chemin = pile.pop()
        liste_nouveaux_sommets_voisins = [voisin for voisin in graphe[sommet] if not(voisin in chemin)]
        for voisin in liste_nouveaux_sommets_voisins:
            if voisin == arrivee:
                chemins.append(chemin + [arrivee])
            pile.append((voisin,chemin + [voisin]))
    return chemins

def cherche_chemin_plus_court(graphe, depart,arrivee):
    chemins = cherche_tous_chemins(graphe,depart,arrivee)
    if len(chemins) == 0:
        return []
    lg_chemin_min = len(chemins[0])
    chemin_min = chemins[0]
    for chemin in chemins:
        if len(chemin) < lg_chemin_min:
            lg_chemin_min = len(chemin)
            chemin_min = chemin.copy()
    return chemin_min


def compte_saut(liste):
        return len(liste)-1

def rip(graphe,liste_de_sommet):
    for i in range(len(graphe.keys())):
        s=input("Entrer le sommet ")
        print()
        print("\tRIP: Table de routage du routeur ",s)
        print()
        print("Destination | Chemin de la source ----> Metrique")
        print()
        for adj in liste_de_sommet:
            if(s!=adj):
                L=cherche_chemin_plus_court(graphe,s,adj)
                print("",adj,"|",L,"---->",compte_saut(L),"SAUTS")
            else:
                print("",s,"| [",s,',',s,"] ----> 0 SAUT")
        print("\n")
def creation():
    graphe={}
    nb=int(input("entrer le nombre de sommet "))
    for i in range(1,nb+1):
        print("Entrer le sommet ",i)
        sommet=input()
        adj=int(input("entrer le nombre de sommet adjacent "))
        l=[]
        for j in range(adj):
            sadj=input("Entrer le sommet adjacent ")
            l.append(sadj)
        graphe[sommet]=l
    return graphe
        
"""G=creation()
print(G)"""
    
G={"R1":("R2","R4","R5"),
   "R2":("R1","R3"),
   "R3":("R2","R4","R8"),
   "R4":("R3","R5","R7"),
   "R5":("R1","R4","R6"),
   "R6":("R4","R5","R7"),
   "R7":("R4","R6","R8"),
   "R8":("R3","R7")}

rip(G,G.keys())
s=input()
