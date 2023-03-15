import funcao_main

while True:
    pergunta = input('Deseja adicionar aulas ou atividades (1 para aulas, 2 para atividades )? ')

    lista = funcao_main.input_do_usuario(pergunta)

    funcao_main.automacao(pergunta, lista)

