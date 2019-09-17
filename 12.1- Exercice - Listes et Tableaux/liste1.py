# Problème : Réaliser une table de multiplication de taile 10x10 en utilisant la liste fournie.
# Résultat attendu : un affichage comme ceci :   1  2  3  4  5  6  7  8  9  10
#                                             1  1  2  3  4  5  6  7  8  9  10
#                                             2  2  4  6  8  10 12 14 16 18 20
#                                             . .  .  .  .  .  .  .  .  .  .
# Indication :   L'alignement rectiligne n'est pas une contrainte, tant que la table est visible ligne par ligne c'est ok.
#               Si vous êtes perfectionnistes faites vous plaisir.
liste = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

print("    ", end='')
for o in range(0, len(liste)):
    print(liste[o], "  ", end='')
print("")
for o in range(0, len(liste)):
    print(liste[o], "  ", end='')
    for p in range(0, len(liste)):
        produit = liste[p] * liste[o]
        print(produit, "  ", end='')
    print("")
