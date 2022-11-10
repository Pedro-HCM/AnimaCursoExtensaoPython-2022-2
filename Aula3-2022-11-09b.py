#criação de funções
preco = 1999.90
#Calcular 5% de imposto, guardar na variavel imposto e exibir na tela 
imposto = preco*0.05
preco2 = 100
imposto2 = preco2*0.05
print(imposto2)
#Criar uma função calcular_imposto() que calcula um imposto de 5%
def calcular_imposto(preco_produto):
  imposto = preco_produto *0.05
  return imposto
preco = 299
imposto = calcular_imposto(preco)
print(imposto)

print(preco)
preco_produto = 100
print(preco_produto)
#agota calcular imposto a aliquota agora é 7%
valores = [1.99,24.50,78.27,1515.5]
for valor in valores:
  print(f"O imposto de {valor} é   {calcular_imposto(valor)}")