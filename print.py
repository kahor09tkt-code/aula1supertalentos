print("Hello, World")
a = int(input("number1: ")); # Inserir comentários sobre o código
b = int(input("number2: "));

# a = int(3.5)
print(a);

soma = a + b;
subtracao = a - b;
multiplicacao = a * b;
resto = a % b;
potencia = a ** b;

print(f"Soma = {soma}");
print(f"Subtração = {subtracao}");
print(f"Multiplicação = {multiplicacao}");
print(f"Resto = {resto}");
print(f"Potência = {potencia}");

if soma > 0: # a minha soma é maior do que zero?
 print("o resultado da soma é maior que zero") # se a minha soma é maior do que zero, imprima que o resultado é maior do que zero
elif soma == 0: # caso a minha soma não seja maior do que zero MAS seja IGUAL a zero,
  print(" o resultado da soma é igual á zero") # imprima que a o resultado é igual a zero
else: # caso contrário (ou seja, soma não é nem maior do que zero, nem igual a zero), então faça o seguinte:
  print("o resultado da soma é negativo") # imprima que a soma é menor do que zero

if subtracao < 0 : 
  print("o número é negativo")

contador = 10

while contador >=0:
  print("Meu contador: ", contador)
  # contador = contador -1
  contador -= 1
print('lançar foguete') 