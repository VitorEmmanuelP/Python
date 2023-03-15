import time


class Nota:

    def __init__(self, driver, By):
        self.driver = driver
        self.By = By
        self.todas_notas = []
        self.div_numero = '5'

    def entrar_na_atividade_avaliativa(self):

        self.driver.find_element(self.By.XPATH,
                                 '/html/body/div[1]/div/div/div/div/div/div[1]/div[2]/div/div/ul/li[4]/a').click()

    def comeco(self):

        # Ano Administrativo
        self.driver.find_element(self.By.XPATH,
                                 '/html/body/div[1]/div/div/div/div/div/div[2]/div/div/div/div[2]/div[1]/div[2]/div/div[1]/div/span/a').click()

        self.driver.find_element(self.By.XPATH, '/html/body/div[4]/ul/li[1]').click()

        # Periodo Letivo
        self.driver.find_element(self.By.XPATH,
                                 '/html/body/div[1]/div/div/div/div/div/div[2]/div/div/div/div[2]/div[1]/div[2]/div/div[2]/div/span/a').click()
        self.driver.find_element(self.By.XPATH, '/html/body/div[4]/div/div/div[3]/table/tbody[1]/tr[1]/td/div').click()
        time.sleep(0.5)

        # Tipo Ensino
        self.tipo_de_ensino('regular')
        time.sleep(0.5)

        # Nível
        self.driver.find_element(self.By.XPATH,
                                 '/html/body/div[1]/div/div/div/div/div/div[2]/div/div/div/div[2]/div[1]/div[2]/div/div[4]/div/span/a').click()
        time.sleep(0.5)

        # Ano/Série/Etapa
        self.ano_serie('2')
        time.sleep(0.5)

        # Turno
        self.turno('manha')
        time.sleep(0.5)

        # Turma
        self.turma()

    def tipo_de_ensino(self, tipo_do_ensino):

        self.driver.find_element(self.By.XPATH,
                                 '/html/body/div[1]/div/div/div/div/div/div[2]/div/div/div/div[2]/div[1]/div[2]/div/div[3]/span[2]/a').click()

        if tipo_do_ensino != 'integral':

            self.driver.find_element(self.By.XPATH,
                                     '/html/body/div[4]/div/div/div[3]/table/tbody[1]/tr[1]/td/div').click()

        else:

            self.driver.find_element(self.By.XPATH,
                                     '/html/body/div[4]/div/div/div[3]/table/tbody[1]/tr[2]/td/div').click()

    def ano_serie(self, ano):

        self.driver.find_element(self.By.XPATH,
                                 '/html/body/div[1]/div/div/div/div/div/div[2]/div/div/div/div[2]/div[1]/div[2]/div/div[5]/div/span/a').click()

        if ano == '2':
            self.driver.find_element(self.By.XPATH,
                                     '/html/body/div[4]/div/div/div[3]/table/tbody[1]/tr[1]/td/div').click()
        else:
            self.driver.find_element(self.By.XPATH,
                                     '/html/body/div[4]/div/div/div[3]/table/tbody[1]/tr[2]/td/div').click()

    def turno(self, turno):

        self.driver.find_element(self.By.XPATH,
                                 '/html/body/div[1]/div/div/div/div/div/div[2]/div/div/div/div[2]/div[1]/div[2]/div/div[6]/div/span/a').click()

        if turno == 'manha':

            self.driver.find_element(self.By.XPATH,
                                     '/html/body/div[4]/div/div/div[3]/table/tbody[1]/tr[1]/td/div').click()

        elif turno == 'tarde':

            self.driver.find_element(self.By.XPATH,
                                     '/html/body/div[4]/div/div/div[3]/table/tbody[1]/tr[2]/td/div').click()

        else:

            self.driver.find_element(self.By.XPATH,
                                     '/html/body/div[4]/div/div/div[3]/table/tbody[1]/tr[3]/td/div').click()

    def turma(self, funcao):

        on = True

        self.driver.find_element(self.By.XPATH,
                                 '/html/body/div[1]/div/div/div/div/div/div[2]/div/div/div/div[2]/div[1]/div[2]/div/div[7]/div/span/a').click()
        len_de_turmas = len(
            self.driver.find_elements(self.By.XPATH, '/html/body/div[4]/div/div/div[3]/table/tbody[1]/tr'))

        time.sleep(0.5)

        while on:

            for i in range(1, len_de_turmas + 1):
                time.sleep(1)
                text = self.driver.find_element(self.By.XPATH,
                                                f'/html/body/div[4]/div/div/div[3]/table/tbody[1]/tr[{i}]/td[1]/div').text

                time.sleep(1)
                self.driver.find_element(self.By.XPATH,
                                         f'/html/body/div[4]/div/div/div[3]/table/tbody[1]/tr[{i}]/td[1]/div').click()

                dados_gerais = self.disciplina()

                funcao(dados_gerais, text)

                self.todas_notas = []

                if i == len_de_turmas or len_de_turmas == 5 and i == len_de_turmas:

                    self.driver.find_element(self.By.XPATH,
                                             '/html/body/div[1]/div/div/div/div/div/div[2]/div/div/div/div[2]/div[1]/div[2]/div/div[8]/div/span/a').click()
                    time.sleep(1)
                    self.driver.find_element(self.By.XPATH,
                                             '/html/body/div[1]/div/div/div/div/div/div[2]/div/div/div/div[2]/div[1]/div[2]/div/div[7]/div/span/a').click()
                    time.sleep(1)
                    self.driver.find_element(self.By.XPATH,
                                             '/html/body/div[4]/div/div/div[4]/div/ul/li[4]/a').click()
                    time.sleep(0.3)

                    len_de_turmas = len(
                        self.driver.find_elements(self.By.XPATH, '/html/body/div[4]/div/div/div[3]/table/tbody[1]/tr'))

                    if text == '1º EM INT 6 - RUA CARLOS CHAGAS, 3':
                        on = False
                        break

                self.driver.find_element(self.By.XPATH,
                                         '/html/body/div[1]/div/div/div/div/div/div[2]/div/div/div/div[2]/div[1]/div[2]/div/div[8]/div/span/a').click()
                time.sleep(1)

                self.driver.find_element(self.By.XPATH,
                                         '/html/body/div[1]/div/div/div/div/div/div[2]/div/div/div/div[2]/div[1]/div[2]/div/div[7]/div/span/a').click()

    def pegar_dados(self):

        pass

    def disciplina(self):

        time.sleep(1)
        self.driver.find_element(self.By.XPATH,
                                 '/html/body/div[1]/div/div/div/div/div/div[2]/div/div/div/div[2]/div[1]/div[2]/div/div[8]/div/span/a').click()
        time.sleep(0.5)

        len_de_disciplinas = len(
            self.driver.find_elements(self.By.XPATH, '/html/body/div[4]/div/div/div[3]/table/tbody[1]/tr'))

        if len_de_disciplinas == 0:
            len_de_disciplinas = len(
                self.driver.find_elements(self.By.XPATH, '/html/body/div[5]/div/div/div[3]/table/tbody[1]/tr'))

        on = True
        time.sleep(1)
        self.driver.find_element(self.By.XPATH, '/html/body/div[4]/div/div/div[4]/div/ul/li[1]/a').click()
        time.sleep(1)

        while on:

            for i in range(1, len_de_disciplinas + 1):

                try:

                    dis = self.driver.find_element(self.By.XPATH,
                                                   f'/html/body/div[4]/div/div/div[3]/table/tbody[1]/tr[{i}]/td/div')

                except:
                    dis = self.driver.find_element(self.By.XPATH,
                                                   f'/html/body/div[5]/div/div/div[3]/table/tbody[1]/tr[{i}]/td/div')

                nome = dis.text

                if nome == 'ATIVIDADE COMPLEMENTAR PROJETO DE VIDA' or nome == 'ATIVIDADE COMPLEMENTAR EM PRÁTICAS COMUNICATIVAS E CRIATIVAS':
                    continue

                time.sleep(1)
                dis.click()

                self.driver.find_element(self.By.XPATH,
                                         '/html/body/div[1]/div/div/div/div/div/div[2]/div/div/div/div[2]/div[1]/div[2]/div/div[9]/span[2]/a').click()

                time.sleep(0.5)
                self.bimestre(nome)

                time.sleep(0.5)
                self.pesquisa_e_atividade()
                time.sleep(0.5)

                self.pegando_notas()
                time.sleep(0.5)

                if i == len_de_disciplinas or len_de_disciplinas == 5 and i == len_de_disciplinas:

                    try:
                        self.driver.find_element(self.By.XPATH,
                                                 '/html/body/div[4]/div/div/div[4]/div/ul/li[4]/a').click()
                    except:
                        self.driver.find_element(self.By.XPATH,
                                                 '/html/body/div[5]/div/div/div[4]/div/ul/li[4]/a').click()

                    time.sleep(0.5)

                    try:
                        len_de_disciplinas = len(
                            self.driver.find_elements(self.By.XPATH,
                                                      '/html/body/div[4]/div/div/div[3]/table/tbody[1]/tr'))

                    except:
                        len_de_disciplinas = len(
                            self.driver.find_elements(self.By.XPATH,
                                                      '/html/body/div[5]/div/div/div[3]/table/tbody[1]/tr'))

                    if nome == 'TUTORIA' or nome == 'ARTE':
                        on = False
                        break

        return self.todas_notas

    def bimestre(self, nome):

        time.sleep(0.5)

        self.driver.find_element(self.By.XPATH,
                                 '/html/body/div[1]/div/div/div/div/div/div[2]/div/div/div/div[2]/div[1]/div[2]/div/div[10]/span[2]/a').click()

        time.sleep(0.5)

        if nome == 'ATIVIDADE COMPLEMENTAR PROJETO DE VIDA' or nome == 'ATIVIDADE COMPLEMENTAR EM PRÁTICAS COMUNICATIVAS E CRIATIVAS':
            try:
                self.driver.find_element(self.By.XPATH,
                                         '/html/body/div[4]/div/div/div[3]/table/tbody[1]/tr[1]/td/div').click()
            except:
                self.driver.find_element(self.By.XPATH,
                                         '/html/body/div[5]/div/div/div[3]/table/tbody[1]/tr[1]/td/div').click()

        else:
            try:
                self.driver.find_element(self.By.XPATH,
                                         '/html/body/div[4]/div/div/div[3]/table/tbody[1]/tr[3]/td/div').click()
            except:
                self.driver.find_element(self.By.XPATH,
                                         '/html/body/div[5]/div/div/div[3]/table/tbody[1]/tr[3]/td/div').click()

        time.sleep(0.5)

    def pesquisa_e_atividade(self):

        self.driver.find_element(self.By.XPATH,
                                 '/html/body/div[1]/div/div/div/div/div/div[2]/div/div/div/div[1]/div[2]/div/button[7]').click()
        time.sleep(0.5)

        self.driver.find_element(self.By.XPATH,
                                 '/html/body/div[1]/div/div/div/div/div/div[2]/div/div/div/div[2]/div[2]/div[2]/div/div[4]/table/tbody[1]/tr[1]/td[1]/div').click()

        time.sleep(0.5)

    def pegando_notas(self):

        len_de_alunos = len(self.driver.find_elements(self.By.XPATH,
                                                      '/html/body/div[1]/div/div/div/div/div/div[2]/div/div/div/div[3]/div[3]/div[2]/div/div[2]/div[2]/div/div/table/tbody[1]/tr[2]/td/div/div/div[3]/table/tbody[1]/tr'))

        nome_dis = self.driver.find_element(self.By.XPATH,
                                            '/html/body/div[1]/div/div/div/div/div/div[2]/div/div/div/div[3]/div[1]/div[2]/div/div[2]/div[1]/span[2]').text

        for i in range(1, len_de_alunos + 1):

            self.driver.find_element(self.By.XPATH,
                                     f'/html/body/div[1]/div/div/div/div/div/div[2]/div/div/div/div[3]/div[3]/div[2]/div/div[2]/div[2]/div/div/table/tbody[1]/tr[2]/td/div/div/div[3]/table/tbody[1]/tr[{i}]/td[11]/div/button').click()
            try:
                nome = self.driver.find_element(self.By.XPATH,
                                                f'/html/body/div[5]/div[2]/div[1]/div[1]/div/div/span').text

                len_de_aluno = len(
                    self.driver.find_elements(self.By.XPATH, f'/html/body/div[5]/div[2]/div[1]/div[2]/div'))

            except:
                nome = self.driver.find_element(self.By.XPATH,
                                                f'/html/body/div[6]/div[2]/div[1]/div[1]/div/div/span').text

                len_de_aluno = len(
                    self.driver.find_elements(self.By.XPATH, f'/html/body/div[6]/div[2]/div[1]/div[2]/div'))

            lista = []

            for i in range(1, len_de_aluno + 1):
                try:
                    notas = self.driver.find_element(self.By.XPATH,
                                                     f'/html/body/div[5]/div[2]/div[1]/div[2]/div[{i}]/div[1]/div/div').text
                except:
                    notas = self.driver.find_element(self.By.XPATH,
                                                     f'/html/body/div[6]/div[2]/div[1]/div[2]/div[{i}]/div[1]/div/div').text

                lista.append(notas)

            notas_filtradas = self.filtrar_nome(conteudo=lista, modo='notas')

            self.colocando_no_dict(nome_dis, notas_filtradas, nome)

            try:
                self.driver.find_element(self.By.XPATH, f'/html/body/div[5]/div[1]/div/i').click()
            except:
                self.driver.find_element(self.By.XPATH, f'/html/body/div[6]/div[1]/div/i').click()

        time.sleep(0.5)

        self.driver.execute_script("window.scrollTo(-8,-8)")

        self.driver.find_element(self.By.XPATH,
                                 '/html/body/div[1]/div/div/div/div/div/div[2]/div/div/div/div[1]/div[2]/div/button[9]').click()

        self.desbugando()

    def desbugando(self):

        self.driver.find_element(self.By.XPATH,
                                 '/html/body/div[1]/div/div/div/div/div/div[2]/div/div/div/div[2]/div[1]/div[2]/div/div[6]/div/span/a').click()

        time.sleep(0.3)

        try:
            self.driver.find_element(self.By.XPATH, '/html/body/div[5]/div/div/div[3]/table/tbody[1]/tr/td/div').click()
        except:
            self.driver.find_element(self.By.XPATH, '/html/body/div[4]/div/div/div[3]/table/tbody[1]/tr/td/div').click()

        time.sleep(0.3)

        self.driver.find_element(self.By.XPATH,
                                 '/html/body/div[1]/div/div/div/div/div/div[2]/div/div/div/div[2]/div[1]/div[2]/div/div[8]/div/span/a').click()

    def colocando_no_dict(self, nome_dis, notas, extra=''):

        for i in range(0, len(self.todas_notas)):
            if extra in self.todas_notas[i]:

                dict_nome = {nome_dis: {}}

                fora = self.todas_notas[i][extra]

                for i in range(0, len(notas)):
                    a = notas[i][0]
                    b = notas[i][1]

                    dict_nome[nome_dis].update({a: b})

                fora.update(dict_nome)

                return

        dict_nome = {nome_dis: {}}
        fora = {extra: {}}

        for i in range(0, len(notas)):
            a = notas[i][0]
            b = notas[i][1]

            dict_nome[nome_dis].update({a: b})

        fora[extra].update(dict_nome)

        self.todas_notas.append(fora)

    def filtrar_nome(self, conteudo, modo, extra=''):

        if modo == 'disciplina':
            nomes_dis = conteudo

            index_inicial = nomes_dis.index(')') + 2
            index_final = nomes_dis.index('-')

            nomes_dis = nomes_dis[index_inicial:index_final]

            return nomes_dis

        elif modo == 'notas':
            lista = []

            for nomes in conteudo:
                index_comeco = nomes.index('º')
                bimestre = nomes[index_comeco - 1:]
                bimestre = bimestre[:11]

                bimestre.strip()

                notas = nomes[-5:]
                notas.strip()

                lista.append([bimestre, notas])

            return lista
