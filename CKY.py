

def rechercheClefs(dictOfElements, valueToFind):
    listOfKeys = list()
    listOfItems = dictOfElements.items()
    for item  in listOfItems:
        for i in item[1]:
            if i == valueToFind:
                listOfKeys.append(item[0])
    return  listOfKeys

#parsing des règles
G = {}
f = open("rules.txt", "r")
for line in f:
    tab = line.split("-->")
    ind = tab[0].strip()
    tab_res = tab[1].strip(' \t\n\r').split(" ")
    res = []
    for i in tab_res:
        res.append(i)
    if ind in G:
        G[ind].append(res)
    else:
        G[ind] = [res]

seq = ['a','a','a','b','b']
matrice = [[[] for _ in range(len(seq))] for _ in range(len(seq))]

#initiation de la matrice
for i in range(0, len(seq)):
    for j in G.values():
        for k in j:
            if k == [seq[i]]:
                matrice[i][i] = rechercheClefs(G, k)

#remplissage de la matrice
for j in range(1, len(seq)):
    for i in range(j-1, -1, -1):
        for k in range(i, j):
            a = matrice[i][k]
            b = matrice[k+1][j]
            for z in a:
                for w in b:
                    for p in rechercheClefs(G, [z, w]):
                        matrice[i][j].append(p)

if 'S' in matrice[0][len(seq)-1]:
    print("La séquence est acceptée\n")
else:
    print("La séquence est refusée\n")
