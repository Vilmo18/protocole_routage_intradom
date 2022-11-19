def trouve_min(sommets,dist):
    mini = float('inf')
    sommet = -1
    for s in sommets:
        if dist[s] < mini:
            mini = dist[s]
            sommet = s
    return sommet

def parcours_en_largeur(graphe, sommet):
    if not(sommet in graphe.keys()):
        return None
    F = [sommet]
    liste_sommets = []
    while len(F) != 0:
        S = F[0]
        for voisin in graphe[S]:
            if not(voisin in liste_sommets) and not(voisin in F):
                F.append(voisin)
        liste_sommets.append(F.pop(0))
    return liste_sommets

def Dijkstra(graphe,depart,arrivee):
    dist = {}
    predecesseurs = {}
    for sommet in graphe.keys():
        dist[sommet] = float('inf')
    dist[depart] = 0
    sommets = parcours_en_largeur(G,depart)
    while len(sommets) != 0:
        s1 = trouve_min(sommets,dist)
        sommets.remove(s1)
        if s1 == -1:
            pass
        else:
            fils=graphe[s1]
            for c in fils:
                if dist[c] > dist[s1] + fils[c]:
                    dist[c] = dist[s1] + fils[c]
                    predecesseurs[c] = s1
    sommet = arrivee
    chemin_plus_court = []
    while sommet != depart:
        chemin_plus_court.insert(0,sommet)
        sommet = predecesseurs[sommet]
    chemin_plus_court.insert(0,depart)
    return (dist[arrivee],chemin_plus_court)
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


G={
   "S":{"A":9,"B":14,"C":15},
   "A":{"G":24},
   "B":{"C":5,"E":30,"G":18},
   "C":{"E":20,"D":44},
   "D":{},
   "E":{"F":11,"D":16},
   "F":{"D":6,"G":6},
   "G":{"E":2}
   }

for i in range(7):
    depart=input("Entrer le depart ")
    arriv=input("Entrer l'arrivee ")
    print("Le chemin le plus court ",Dijkstra(G,depart,arriv))
