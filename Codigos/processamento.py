especiais = ['!', '"', '#', '$', '%', '&', "'", '(', ')', '*', '+', ',', '-', '.', '/', ':', ';', '<', '=', '>', '?', '@', '[', '\\', ']', '^', '_', '', '{', '|', '}', '~']



def Organizar(Lista):
    Nomes = []
    Notas = []
    for i in range(len(Lista)):
        Nomes.append(Lista[i][0])
        Notas.append(Lista[i][1])
        i += 1
    
    dados = {"Nomes": Nomes, "Notas": Notas}
    return dados

def Validar_Nomes(dados):

    Nomes_validos = []

    for i in range(len(dados)):
        nome = dados[i]
        for caractere_especial in especiais:
            nome = nome.replace(caractere_especial, "")
        Nomes_validos.append(nome)
    
    return Nomes_validos

def Validar_Notas(dados):
    Notas_validas = []
    
    for i in range(len(dados)):
        notas = dados[i]
        notas_aluno = []  
        for nota in notas:
            if nota == "" or nota is None or isinstance(nota, str):
                notas_aluno.append(0)
            else:
                notas_aluno.append(nota)
                
        Notas_validas.append(notas_aluno)  
    
    return Notas_validas

def Media(dados):
    medias = []
    for i in range(len(dados)):
        notas = dados[i]
        resul = sum(notas) / len(notas)
        medias.append(round(resul, 2))
    return medias

def Filtro(valores):
    resultado = []
    for i in range(len(valores)):
        media = valores[i]
        if media > 7:
            resultado.append("Aprovado")
        else:
            resultado.append("Reprovado")

    return resultado

def Listar(Nomes, Medias, Resultados):
    lista = []
    for i in range(len(Nomes)):
        aluno = Nomes[i]
        media = Medias[i]
        resultado = Resultados[i]
        melhor = "Melhor" if media >= 9.0 else ""
        lista.append((aluno, media, resultado, melhor))
    return lista