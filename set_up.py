nb = int(input("entrez le nombre de vos taches : "))
temps_exec = []
for i in range(nb):
    temps_exec.append(
        int(input("Entrez le temps d'exécution de la tâche {}: ".format(i + 1)))
    )

print("gérez le tableau des transitions :")
rows = []
for i in range(nb):
    col = []
    for j in range(nb):
        if j == i:
            col.append(0)
        else:
            x = int(
                input(
                    "entrez la transition de la tache {} vers la tache {} : ".format(
                        i + 1, j + 1
                    )
                )
            )
            col.append(x)
    rows.append(col)
print(rows)

start = min(x for x in rows[0] if x != 0)
index = rows[0].index(min(x for x in rows[0] if x != 0))
chemin_hamilton = [start]
ordonnancement = [1, index + 1]
for j in range(1, nb - 1):
    next = min(
        rows[index][x]
        for x in range(len(rows[index]))
        if rows[index][x] != 0 and x + 1 not in ordonnancement
    )
    index = rows[index].index(
        min(
            rows[index][x]
            for x in range(len(rows[index]))
            if rows[index][x] != 0 and x + 1 not in ordonnancement
        )
    )
    chemin_hamilton.append(next)
    ordonnancement.append(index + 1)
taille_chemin = sum(chemin_hamilton)

for i in range(1, nb):
    start = min(x for x in rows[i] if x != 0)
    index = rows[i].index(min(x for x in rows[i] if x != 0))
    chemin_hamilton_test = [start]
    ordonnancement_test = [i + 1, index + 1]
    for j in range(1, nb - 1):
        next = min(
            rows[index][x]
            for x in range(len(rows[index]))
            if rows[index][x] != 0 and x + 1 not in ordonnancement_test
        )
        index = rows[index].index(
            min(
                rows[index][x]
                for x in range(len(rows[index]))
                if rows[index][x] != 0 and x + 1 not in ordonnancement_test
            )
        )
        chemin_hamilton_test.append(next)
        ordonnancement_test.append(index + 1)
    taille = sum(chemin_hamilton_test)
    if taille < taille_chemin:
        taille_chemin = taille
        chemin_hamilton = chemin_hamilton_test
        ordonnancement = ordonnancement_test


print("l'ordonnancement est :", ordonnancement)
print("Cmax= ", sum(chemin_hamilton) + sum(temps_exec))
