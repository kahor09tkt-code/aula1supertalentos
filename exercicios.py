#Exercício 1

nome = input ("Qual o seu nome ? ")
carne = input ("Qual carne você quer comprar ? ")
preco = float (input("Digite o preço do quilo:  "))
quilo = float (input("Quantos quilos deseja ? "))

valor = preco * quilo

print (f"\n{nome} quis comprar a carne {carne}.")
print(f"O valor total da compra ficou: R$ {valor}")

#Exercício 2

pessoas = int(input("\nQuantas pessoas tem na mesa ? "))
conta = float(input(" Qual o valor da conta ? "))

valorfinal = conta / pessoas 
valorinteiro = conta // pessoas
resto = conta % pessoas


print (f"\n.Valor exato por pessoa : {valorfinal:.2f} ")
print (f"\n.Valor inteiro por pessoa : {valorinteiro:.2f} ")
print (f"\n. Resto que sobrou da divisão inteira : {resto:.2f} ")

#Exercício 3

nome = input("Digite o nome do participante: ")
idade = int(input("Digite a idade: "))
resposta = input("Possui conhecimento prévio em lógica (sim/não)? ").strip().lower()

tem_conhecimento = resposta == "sim"

if resposta == "sim" or resposta == "não" or resposta == "nao":
    if idade < 18:
        categoria = "Infanto-Juvenil"
    elif idade >= 18 and tem_conhecimento:
        categoria = "Avançado"
    elif idade >= 18 and not tem_conhecimento:
        categoria = "Iniciante"

    print(f"\nParticipante: {nome}")
    print(f"Idade: {idade}")
    print(f"Sua categoria no meetup: {categoria}")

else:
    print("\nResposta inválida. Digite apenas Sim ou Não.")

#Exercício 4

notaum = int(input ("Digite a primeira nota : "))
notadois = int(input ("Digite a segunda nota : "))
notatres = int(input("Digite a terceira nota : "))

media = (notaum + notadois+ notatres) / 3


print (f"\nA maior nota foi : {max(notaum, notadois or notatres)} ")
print(f"A menor nota foi : {min(notaum, notadois or notatres)}")
print(f"A média final é : {media:.2f}")

#Exercício 5

data = input("Digite sua data de nascimento (DD/MM/AAAA): ")
nome = input("Digite seu nome completo: ")

data_formatada = data.replace("/", "-")
partes_data = data_formatada.split("-")
nome_formatado = " ".join(nome.split()).upper()

print("\nData formatada:", data_formatada)
print("Lista com dia, mês e ano:", partes_data)
print("Nome formatado:", nome_formatado)