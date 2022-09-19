alunos = []
testes = []
provas = []
trabalhos = []
medias = []

print(f"tamanho array: {len(alunos)}")
print(len(alunos))
i = 0

while len(alunos) != 3:
    a = input("Digite o nome do aluno: ")
    alunos.append(a)

    trab = float(input("Digite a nota do trabalho: "))
    trabalhos.append(trab)

    prov = float(input("Digite nota prova: "))
    provas.append(prov)

    tes = float(input("Digite nota teste: "))
    testes.append(tes)

    medias.append( ( (testes[i] + provas[i] + trabalhos[i])/3) )

    i+=1



for media in medias:
    print(f"Média {len(alunos)} : {media}")







