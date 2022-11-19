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

def cherche_tous_chemins_graphe_pondere(graphe, depart,arrivee):
    chemins = []
    if not(depart in graphe.keys()) or not(arrivee in graphe.keys()):
        return None
    pile = [(depart,[depart])]
    chemin = []
    while len(pile) != 0:
        print(len(pile))
        sommet,chemin = pile.pop()
        if len(sommet) == 2:
            sommet = sommet[0]
        liste_nouveaux_sommets_voisins = []
        for voisin in graphe[sommet]:
            if len(voisin) == 2 and not (voisin in chemin):
                liste_nouveaux_sommets_voisins.append(voisin)
            if voisin[0] == arrivee:
                chemins.append(chemin + [voisin])
            pile.append((voisin,chemin + [voisin]))
    return chemins

def calcule_longueur_chemin(chemin,distances):
    sommet1 = chemin[0]
    longueur = 0
    for ind in range(1,len(chemin)):
        sommet2 = chemin[ind]
        trouve = False
        for distance in distances:
            if distance[0] == sommet1 and distance[1] == sommet2:
                longueur += distance[2]
                trouve = True
                break
        if not(trouve):
            return "Grand probleme"
        sommet1 = sommet2
    return longueur

def cherche_chemin_plus_court_graphe_pondere(graphe, distances, depart,arrivee):
    chemins = cherche_tous_chemins(graphe,depart,arrivee)
    if len(chemins) == 0:
        return None
    lg_chemin_min = calcule_longueur_chemin(chemins[0],distances)
    chemin_min = chemins[0]
    for chemin in chemins:
        lg_chemin = calcule_longueur_chemin(chemin, distances)
        if lg_chemin < lg_chemin_min:
            lg_chemin_min = lg_chemin
            chemin_min = chemin.copy()
    return (chemin_min,lg_chemin_min)

def ospf(graphe,dist):
    for i in range(len(graphe.keys())):
        s=input("Entrer le sommet ")
        print("\tOSPF: Table de routage du routeur",s)
        print()
        print("Destination | Chemin de la source ----> Metrique")
        print()
        for adj in graphe.keys():
            #adj=input("Entrer le sommet ")
            if(s!=adj):
                L=cherche_chemin_plus_court_graphe_pondere(graphe,dist,s,adj)
                print("",adj,"|",L[0],"---->",L[1]+1)
            else:
                print("",s,"| [",s,',',s,"] ----> 1")
        print("\n")

def creation():
    graphe={}
    distance=[]
    dist=0
    nb=int(input("entrer le nombre de sommet "))
    for i in range(1,nb+1):
        print("Entrer le sommet ",i)
        sommet=input()
        adj=int(input("entrer le nombre de sommet adjacent "))
        l=[]
        for j in range(adj):
            sadj=input("Entrer le sommet adjacent ")
            dist=int(input("Entrer la distance entre les 2 sommets"))
            distance.append((sommet,sadj,dist))
            l.append(sadj)
        graphe[sommet]=l
    return graphe,distance
"""
G,L=creation()
print(G,L)
"""    
G={"R1":("R2","R4","R5"),
   "R2":("R1","R3"),
   "R3":("R2","R4","R8"),
   "R4":("R1","R3","R5","R6","R7"),
   "R5":("R1","R4","R6"),
   "R6":("R4","R5","R7"),
   "R7":("R4","R6","R8"),
   "R8":("R3","R7")}

L=[("R1","R2",3),("R1","R4",3),("R1","R5",2),
   ("R2","R1",3),("R2","R3",2),
   ("R3","R2",2),("R3","R4",3),("R3","R8",4),
   ("R4","R1",3),("R4","R3",3),("R4","R5",2),("R4","R6",3),("R4","R7",5),
   ("R5","R1",2),("R5","R4",2),("R5","R6",4),
   ("R6","R4",3),("R6","R5",4),("R6","R7",2),
   ("R7","R4",5),("R7","R6",2),("R7","R8",3),
   ("R8","R3",4),("R8","R7",3)]
ospf(G,L)
