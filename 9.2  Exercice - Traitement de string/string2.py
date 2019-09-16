# Consigne : Rechercher le nombre d'occurences du mot "exemple" et l'afficher. Remplacer le mot "est" par "représente".
# Bonus : Inverser le sens de lecture.
texte = "Ceci est un exemple exemplaire d'exemple exempté d'exemple."

txtSplit = texte.split("")
cptExemple = 0

for m in txtSplit:
    reSplit = m.split("'")
    print(reSplit)


print(cptExemple)