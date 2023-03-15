import time
import pyautogui


class AutomacaoAtividade:

    def __init__(self, driver, By):
        self.driver = driver
        self.By = By
        self.driver.implicitly_wait(10)

    def add_atividade(self, turma, disciplona, bimestre, valor, conteudo, tipo_de_atividade):
        self.entrada(turma)
        time.sleep(0.3)
        self.__turma(turma)
        time.sleep(0.3)
        self.__disciplina(disciplona)
        time.sleep(0.3)
        self.__etapa()
        time.sleep(0.3)
        self.__bimestre(bimestre)
        time.sleep(0.3)
        self.__valor(valor)
        time.sleep(0.3)
        self.__descricao(conteudo)
        time.sleep(0.3)
        self.__tipo_de_atividade(tipo_de_atividade)
        time.sleep(0.3)
        self.__inserir_notas()

    def entrada(self, turma):
        try:
            if '1 INT' in turma:
                self.driver.find_element(self.By.XPATH, '/html/body/div[1]/div/div/div/div/div/div[1]/div[2]/'
                                                        'div/div/ul/li[1]/a/span').click()

                self.driver.find_element(self.By.XPATH, '/html/body/div[1]/div/div/div/div/div/div[1]/div[2]/'
                                                        'div/div/ul/li[1]/ul/li[3]/a/span').click()
                time.sleep(1)

                self.driver.find_element(self.By.XPATH, '/html/body/div[1]/div/div/div/div/div/div[2]/div/div/'
                                                        'div/div[1]/div[2]/div/button[9]').click()

            else:
                self.driver.find_element(self.By.XPATH, '/html/body/div[1]/div/div/div/div/div/div[1]/div[2]/div/div/'
                                                        'ul/li[4]/a/span').click()
                time.sleep(0.3)
                self.driver.find_element(self.By.XPATH,
                                         '/html/body/div[1]/div/div/div/div/div/div[2]/div/div/div/div[1]/'
                                         'div[2]/div/button[9]').click()
                time.sleep(0.3)

        except:
            raise print('erro entrada')

    def __turma(self, turma_escolhida):

        self.driver.find_element(self.By.XPATH, '/html/body/div[1]/div/div/div/div/div/div[2]/div/div/div/div[3]/'
                                                'div[1]/div[2]/div/div[1]/div/span[1]/a').click()
        pyautogui.hotkey('ctrl', 'shift', 'i')
        len_de_turmas = len(
            self.driver.find_elements(self.By.XPATH, '/html/body/div[4]/div/div/div[3]/table/tbody[1]/tr'))

        time.sleep(0.5)
        on = True

        while on:

            for i in range(1, len_de_turmas + 1):

                turma = self.driver.find_element(self.By.XPATH,
                                                 f'/html/body/div[4]/div/div/div[3]/table/tbody[1]/tr[{i}]/'
                                                 'td[1]/div')

                turma_texto = self.__filtrar_texto('turma', turma.text)

                if turma_escolhida == turma_texto:
                    turma.click()
                    on = False
                    break

                if i == len_de_turmas and len_de_turmas == 5:
                    self.driver.find_element(self.By.XPATH,
                                             '/html/body/div[4]/div/div/div[4]/div/ul/li[4]/a').click()

                    time.sleep(0.1)

                    len_de_turmas = len(
                        self.driver.find_elements(self.By.XPATH, f'/html/body/div[4]/div/div/div[3]/'
                                                                 f'table/tbody[1]/tr'))

                    time.sleep(0.5)

        pyautogui.hotkey('ctrl', 'shift', 'i')

    def __disciplina(self, disciplina_escolhida):
        try:
            self.driver.find_element(self.By.XPATH,
                                     '/html/body/div[1]/div/div/div/div/div/div[2]/div/div/div/div[3]/div[1]/div[2]/div[1]/div[2]/span[2]/a').click()

            time.sleep(0.1)

            len_disciplina = len(self.driver.find_elements(self.By.XPATH, '/html/body/div[4]/div/div/div[3]/'
                                                                          'table/tbody[1]/tr'))

            if len_disciplina > 1:

                for i in range(1, len_disciplina + 1):
                    disciplina = self.driver.find_element(self.By.XPATH,
                                                          f'/html/body/div[4]/div/div/div[3]/table/tbody[1]/'
                                                          f'tr[{i}]/td/div')

                    disciplina_texto = self.__filtrar_texto('disciplina', disciplina.text)
                    if disciplina_texto.lower() == disciplina_escolhida.lower():
                        disciplina.click()
                        break

        except:
            raise print('Erro na disciplina')

    def __etapa(self):
        try:
            self.driver.find_element(self.By.XPATH, '/html/body/div[1]/div/div/div/div/div/div[2]/div/div/div/div[3]/'
                                                    'div[1]/div[2]/div/div[3]/div/span/a').click()
        except:
            raise print('Erro na etapa')

    def __bimestre(self, bimestre_escolhido):
        try:
            self.driver.find_element(self.By.XPATH, '/html/body/div[1]/div/div/div/div/div/div[2]/div/div/div/div[3]/'
                                                    'div[1]/div[2]/div/div[4]/div[1]/span/a').click()
            time.sleep(0.5)

            len_de_bimestre = len(
                self.driver.find_elements(self.By.XPATH, '/html/body/div[4]/div/div/div[3]/table/tbody[1]/tr'))

            for i in range(1, len_de_bimestre + 1):

                bimestre_texto = self.driver.find_element(self.By.XPATH, f'/html/body/div[4]/div/div/div[3]/table/'
                                                                         f'tbody[1]/tr[{i}]/td/div')

                if int(bimestre_texto.text[0]) == int(bimestre_escolhido):
                    bimestre_texto.click()
                    break

        except:
            raise print('Erro no bimestre')

    def __valor(self, valor):

        try:
            self.driver.find_element(self.By.XPATH, '/html/body/div[1]/div/div/div/div/div/div[2]/div/div/div/div[3]'
                                                    '/div[1]/div[2]/div/div[5]/div/input').send_keys(valor)

        except:
            raise print('Erro no valor')

    def __descricao(self, descricao):
        try:
            self.driver.find_element(self.By.XPATH, '/html/body/div[1]/div/div/div/div/div/div[2]/div/div/div/div[3]/'
                                                    'div[1]/div[2]/div/div[6]/div/input').send_keys(descricao)
        except:
            raise print('Erro na descricao')

    def __tipo_de_atividade(self, tipo_de_atividade):
        try:
            self.driver.find_element(self.By.XPATH, '/html/body/div[1]/div/div/div/div/div/div[2]/div/div/div/div[3]/'
                                                    'div[1]/div[2]/div/div[8]/div/span/a').click()

            if tipo_de_atividade == '1':
                self.driver.find_element(self.By.XPATH, '/html/body/div[4]/div/div/div[3]/table/tbody[1]/'
                                                        'tr[1]/td/div').click()
            else:
                self.driver.find_element(self.By.XPATH, '/html/body/div[4]/div/div/div[3]/table/tbody[1]/'
                                                        'tr[2]/td/div').click()

            self.driver.find_element(self.By.XPATH, '/html/body/div[1]/div/div/div/div/div/div[2]/div/div/div/div[1]/'
                                                    'div[2]/div/button[7]').click()

        except:
            raise print('Erro no tipo da atividade')

    def __inserir_notas(self):

        self.driver.find_element(self.By.XPATH, '/html/body/div[1]/div/div/div/div/div/div[2]/div/div/div/div[3]/'
                                                'div[3]/div[2]/div/div[1]/button').click()

        time.sleep(0.5)

        len_inserir_notas = len(self.driver.find_elements(self.By.XPATH, '/html/body/div[1]/div/div/div/div/div/div[2]/'
                                                                         'div/div/div/div[3]/div[3]/div[2]/div/div[2]/'
                                                                         'div[2]/div/div/table/tbody[1]/tr[2]/td/div/'
                                                                         'div/div[3]/table/tbody[1]/tr'))
        print(len_inserir_notas)
        for i in range(1, len_inserir_notas + 1):
            nome = self.driver.find_element(self.By.XPATH, '/html/body/div[1]/div/div/div/div/div/div[2]/div/div/div/'
                                                           'div[3]/div[3]/div[2]/div/div[2]/div[2]/div/div/table/'
                                                           f'tbody[1]/tr[2]/td/div/div/div[3]/table/tbody[1]/tr[{i}]/'
                                                           'td[3]/div/div[1]/span')

            a = input(f'{nome.text}:')

            self.driver.find_element(self.By.XPATH, '/html/body/div[1]/div/div/div/div/div/div[2]/div/div/div/div[3]/'
                                                    'div[3]/div[2]/div/div[2]/div[2]/div/div/table/tbody[1]/tr[2]/'
                                                    f'td/div/div/div[3]/table/tbody[1]/tr[{i}]/td[4]/'
                                                    f'div/input').send_keys(a)

        self.driver.execute_script("window.scrollTo(-8,-8)")
        time.sleep(0.5)

        self.driver.find_element(self.By.XPATH, '/html/body/div[1]/div/div/div/div/div/div[2]/div/div/div/div'
                                                '[1]/div[2]/div/button[7]').click()
        time.sleep(0.5)

        self.driver.find_element(self.By.XPATH, '/html/body/div[5]/div[2]/table[2]/tbody/tr/td/table/tbody/tr/'
                                                'td/button').click()

    @staticmethod
    def __filtrar_texto(modo, texto=''):

        if modo == 'turma':
            if texto[0] == 1:
                a = '1'
                return a

            temp = texto

            inde = temp.index('-')
            temp = temp.replace('EM', '')
            temp = temp.replace('º', '')
            temp = " ".join(temp.split())

            final = temp[:inde - 5]

            return final

        elif modo == 'disciplina':
            inde = texto.index('-')
            final = texto[5:inde - 1]

            return final

        elif modo == 'faltas':

            separada = texto.split()
            final = f'{separada[0]} {separada[-1]}'

            return final
