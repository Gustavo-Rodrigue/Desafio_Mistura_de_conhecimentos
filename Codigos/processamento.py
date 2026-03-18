def Organizar(Lista):
    Nomes = []
    Notas = []
    for i in range(len(Lista)):
        Nomes.append(Lista[i][0])
        Notas.append(Lista[i][1])
        i += 1
    
    dados = {"Nomes": Nomes, "Notas": Notas}
    return dados