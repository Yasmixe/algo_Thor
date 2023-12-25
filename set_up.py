# supprimer un element dans un tableau
def supprimer(T, i):
    T.pop(i)


# supprimer une ligne dans une matrice
def supprimer_ligne(matrice, indice_ligne):
    if 0 <= indice_ligne < len(matrice):
        matrice.pop(indice_ligne)


def supprimer_colonne(matrice, indice_colonne):
    for row in matrice:
        if 0 <= indice_colonne < len(row):
            row.pop(indice_colonne)


nb_taches = int(input("entrer le nombre de taches que vous avez: "))
Ordre_taches = []
cij = []
p = []
c = []

for i in range(nb_taches):
    row = []
    for j in range(nb_taches):
        transition_time = int(
            input(
                "donner le temps de transition entre les taches "
                + str(i)
                + " et "
                + str(j)
                + " : "
            )
        )
        row.append(transition_time)
    cij.append(row)
    pi = int(input("entrer la duree de la tache " + str(i) + " : "))
    p.append(pi)


# display the array des pi
print("Tableau des Pi:", p)


# Display la matrice de transition
print("Matrice des temps de transition:")
for row in cij:
    print(row)

# Find the minimum value in the matrix
min_indices_value = min(
    (
        (i, j, value)
        for i, row in enumerate(cij)
        for j, value in enumerate(row)
        if i != j
    ),
    key=lambda x: x[2],
)

min_value = min_indices_value[2]
min_indices = (min_indices_value[0], min_indices_value[1])

print("Le temps de transition minimum est:", min_value)
print("Les indices de la valeur minimale sont:", min_indices)

si = 0
cmax = p[min_indices[0]] + cij[min_indices[0]][min_indices[1]]
c.append(cmax)
Ordre_taches.append("T" + str(min_indices[1]))
print("Ordre des taches: ")
print(Ordre_taches)
supprimer(p, min_indices[0])

# supprimer la ligne I  et la colonne i de la matrice Cij
supprimer_ligne(cij, min_indices[0])
supprimer_colonne(cij, min_indices[0])

for row in cij:
    print(row)


tasks_remaining = True
minimum = min_indices[1]
if len(p) > 2:
    for i in range(nb_taches):
        for j in range(nb_taches):
            if tasks_remaining and cij and any(cij):
                min_indices_value = min(
                    (
                        (i, j, value)
                        for i, row in enumerate(cij)
                        for j, value in enumerate(row)
                        if i != j
                    ),
                    key=lambda x: x[2],
                )
                min_value = min_indices_value[2]
                min_indices = (min_indices_value[0], min_indices_value[1])

                sj = cmax
                cmax = cmax + p[min_indices[0]] + cij[min_indices[0]][min_indices[1]]
                c.append(cmax)
                Ordre_taches.append("T" + str(min_indices[1]))
                print("Ordre des taches: ")
                print(Ordre_taches)
                minimum = min_indices[1]
                supprimer(p, min_indices[0])
                supprimer_ligne(cij, min_indices[0])
                supprimer_colonne(cij, min_indices[0])
            else:
                tasks_remaining = False
                break

        if not tasks_remaining:
            break


sj = cmax
cmax = sj + p[min_indices[0]]
Ordre_taches.append("T" + str(min_indices[1] + 1))
print("Ordre des taches: ")
print(Ordre_taches)
c.append(cmax)
print(c)
