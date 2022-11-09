# comando input():Para permitir #digite algo..
nome=input("Digite o seu nome- ")
idade= int(input(f"Qual sua idade meu amigo\n{nome}?"))
print("--------------------------------")
print(f"Prazer em te conhecer {nome}, {idade} é uma boa idade")
dobro =idade*2
print("--------------------------------")
print(f"O dobro da sua idade é {dobro}")
print("--------------------------------")
soma = 18-idade

#Estrutura Condicional if:else
if (idade>=18):
 print("Já pode Beber e dirigir, além de estudar")
 print("--------------------------------")
else:
 print(f"Tu é D'Menor ainda filhão, faltam {soma} anos para você alcançar a maior idade ")
 print("--------------------------------")
  
  #E se eu quisessem perguntar o gênero (M = Masculino e F = Feminino)
#Mostre (...e você também precisa/precisou prestar o serviço militar obrigatório)


gen=input("Qual o seu genero por favor digite M para Masculino e F para Feminino ")
if (gen=='M' and idade>=18):
   print("Você precisa ou precisou prestar o serviço militar obrigatório")
else:
  print("Você não precisa ou precisou prestar o serviço militar obrigatório.")