def Organizar(Lista):
    Nomes = []
    Notas = []
    for i in range(len(Lista)):
        Nomes.append(Lista[i][0])
        Notas.append(Lista[i][1])
        i += 1
    print(Nomes)
    print(Notas)