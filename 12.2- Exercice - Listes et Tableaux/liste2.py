# Problème : Etant donné un tableau, afficher l'indice du tableau comportant la valeur la plus elevée.
# Résultat attendu : Un affichage comme ceci : "La valeur maximum est :  x  et elle se trouve à l'indice [ n ][ m ]

tab = [[4, 7, 3, 20, 42], [2, 4, 5, 7, 2], [23, 24, 15, 75, 23]]


max = 0
for i in range(0, len(tab)):
    for p in range(0, len(tab[i])):
        if tab[i][p] > max:
            max = tab[i][p]
            n = i
            m = p
print("La valeur maximum est : ", max, " et elle se trouve à l'indice [", n, "][", m, "]")
