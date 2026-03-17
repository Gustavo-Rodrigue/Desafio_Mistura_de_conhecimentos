def Coleta():
    Notas = []
    dados = []
    while True:
        Nome = str(input("Digite o nome do aluno \n >> "))
        quantidade = int(input("Quantas notas iram constituir a média \n >> "))
        for i in range(quantidade):
            Notas.append(input(f"Digite a {i + 1}° nota do aluno (Utilize . para notas não inteiras) \n >> "))
        break
    dados.append([Nome, Notas])
    return(dados)

Coleta()