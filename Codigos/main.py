import processamento as pr

Dados = [("Math$eus", [10, 8, "j", 8]), 
         ("Beatriz", [8.4, 9.0, 9.1, 9.6]),
         ("Lu@cas", [8.5, 9.9, "", 9.5]),
         ("Mariana", [8.0, "t", 8.5, 9.3])]

dados = pr.Organizar(Dados)

Nomes = pr.Validar_Nomes(dados["Nomes"])
Notas = pr.Validar_Notas(dados["Notas"])
medias = pr.Media(Notas)

print(Nomes)
print(Notas)
print(medias)

