# funcao que retorna 30% do preco
def calcular_imposto(preco):
    return preco * 0.3

print(calcular_imposto(1000))
# or use lambda

calcular_impost0_lambda = lambda preco : preco * 0.3
print(calcular_impost0_lambda(1000))

# calcular o imposto para todos od items com map ( map pega cada item de uma lista e faz algo com eles) ( funcao, iterable )

precos = [1000,500,300,250,10]


imposto = list(map(lambda x : x * 0.3, precos))

print(imposto)