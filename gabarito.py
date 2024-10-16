gabarito = []
nomesAlunos = []
notasAlunos = []

for i in range(5):
    while True:
        questao = str(input(f"Digite o gabarito da {i+1}º questão: ").lower())

        if(questao != 'a' and questao != 'b' and questao != 'c' and questao != 'd'):
            print("Digite um valor correto.")
        else:
            gabarito.append(questao)
            break
            

# 3 Alunos
for i in range(3):
    print(f"-- ALUNO {i+1} --")
    nomeAluno = str(input("Digite o nome do aluno: "))
    nomesAlunos.append(nomeAluno)


    notaAluno = 0
    print("RESPOSTAS DADAS: ")
    for j in range(5):
        while True:
            gabaritoAluno =  str(input(f"Questão {j+1}: ").lower())
            if(gabaritoAluno != 'a' and gabaritoAluno != 'b' and gabaritoAluno != 'c' and gabaritoAluno != 'd'):
                print("Digite um valor correto.")
            else:
                if gabaritoAluno == gabarito[j]:
                    notaAluno += 2
                break
    notasAlunos.append(notaAluno)

for i in range(3):
    print(f"Aluno: {nomesAlunos[i]}  -  Nota: {notasAlunos[i]}")
