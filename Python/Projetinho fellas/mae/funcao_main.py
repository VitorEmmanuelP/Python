import time

from opp_aula import AutomacaoAula
from opp_atividade import AutomacaoAtividade
from opp_inputs import Input

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By


def input_do_usuario(pergunta):

    inputt = Input()

    while True:

        if pergunta == '1':
            lista = inputt.input_add_aula()

            return lista

        elif pergunta == '2':
            lista = inputt.input_add_atividade()
            return lista


def iniciar_chrome(driver, login, senha):
    try:
        driver.get(url='https://www.diarioescolardigital.educacao.mg.gov.br/diarioeletronico-frontend/')
        driver.find_element(By.XPATH,
                            '/html/body/div/div/div/div/div/div/div/div/div/div/div[1]/div[1]/input').send_keys(login)
        driver.find_element(By.XPATH,
                            '/html/body/div/div/div/div/div/div/div/div/div/div/div[1]/div[2]/input').send_keys(senha)

        driver.maximize_window()

    except:
        iniciar_chrome(driver, login, senha)


def automacao(pergunta, lista):

    service = Service(ChromeDriverManager().install())

    options = webdriver.ChromeOptions()
    # options.add_experimental_option('debuggerAddress', 'localhost:8989')
    options.add_experimental_option('excludeSwitches', ['enable-logging'])
    options.add_experimental_option('detach', True)

    driver = webdriver.Chrome(service=service, options=options)
    driver.implicitly_wait(10)

    login = 'USER'
    senha = 'PASSWORD'

    iniciar_chrome(driver, login, senha)

    if pergunta == '1':

        auto = AutomacaoAula(driver, By)

        for i in range(len(lista)):

            turma = lista[i]['turma']
            disciplina = lista[i]['disciplina']
            bimestre = lista[i]['bimestre']
            data = lista[i]['data']
            conteudo = lista[i]['conteudo']
            lista_faltas = lista[i]['faltas']

            auto.add_aulas(turma, disciplina, bimestre, data, conteudo, lista_faltas)

            time.sleep(1)

        driver.quit()

    elif pergunta == '2':

        auto = AutomacaoAtividade(driver, By)

        for i in range(len(lista)):

            turma = lista[i]['turma']
            disciplina = lista[i]['disciplina']
            bimestre = lista[i]['bimestre']
            valor = lista[i]['valor']
            conteudo = lista[i]['conteudo']
            tipo_de_atividade = lista[i]['tipo_de_atividade']

            auto.add_atividade(turma, disciplina, bimestre, valor, conteudo, tipo_de_atividade)

            time.sleep(1)

        driver.quit()

