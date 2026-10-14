excelente = 0
bom = 0 
ruim = 0

for i in range(50):
    nome = input("Digite seu nome: ")
    idade = int(input("Digite sua idade: "))
    avaliacao = input("Digite sua avaliação (1,2,3): ")

    if avaliacao == "1":
        excelente += 1
    elif avaliacao == "2":
        bom += 1
    elif avaliacao == "3":
        ruim += 1
    else:
        print("Avaliação inválida. Por favor, digite 1, 2 ou 3.")
        
print(f"Excelente: {excelente}")
print(f"Bom: {bom}")
print(f"Ruim: {ruim}")