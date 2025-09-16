nome_aluno = input("digite o nome do aluno: ")
prova_1 = float(input("digite a nota da primeira prova: "))
prova_2 = float(input("digite a nota da segunda prova: "))
prova_3 = float(input("digite a nota da terceira prova:  "))

média = (prova_1 + prova_2 + prova_3)/3

if média >= 7:
    print("está aprovado")
elif média >= 4:
    print(" está em recuperação")
else:
    print("está reprovado")

print(f"a média do aluno {nome_aluno} é {média:.1f}")
