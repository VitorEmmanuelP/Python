import time
import pyautogui


class AutomacaoAula:

    def __init__(self, driver, By):
        self.driver = driver
        self.By = By
        self.driver.implicitly_wait(10)
        self.div = 4

    def add_aulas(self, turma, disciplina, bimestre, data, conteudo, lista):

        self.__entrada(turma)
        time.sleep(0.3)
        self.__turmas(turma)
        time.sleep(0.3)
        self.__disciplina(disciplina)
        time.sleep(0.3)
        self.__etapa()
        time.sleep(0.3)
        self.__bimestre(bimestre)
        time.sleep(0.3)
        self.__data(data)
        time.sleep(0.3)
        self.__conteudo_lecionado(conteudo)
        time.sleep(0.3)

        if '1 INT' in str(turma):
            self.driver.find_element(self.By.XPATH, '/html/body/div[1]/div/div/div/div/div/div[2]/div/div/div/div[1]/'
                                                    'div[2]/div/button[6]').click()
        else:
            self.driver.find_element(self.By.XPATH, '/html/body/div[1]/div/div/div/div/div/div[2]/div/div/div/div[1]/'
                                                    'div[2]/div/button[7]').click()

        time.sleep(0.3)
        if len(lista) != 0:

            self.__faltas(lista)
        else:
            time.sleep(2)

    def __entrada(self, turma):

        if '1 INT' in str(turma):
            self.driver.find_element(self.By.XPATH, '/html/body/div[1]/div/div/div/div/div/div[1]/div[2]/div/div/ul/'
                                                    'li[1]/a/span').click()

            self.driver.find_element(self.By.XPATH, '/html/body/div[1]/div/div/div/div/div/div[1]/div[2]/div/div/ul/'
                                                    'li[1]/ul/li[1]/a/span').click()

            time.sleep(1)

            self.driver.find_element(self.By.XPATH, '/html/body/div[1]/div/div/div/div/div/div[2]/div/div/div/div[1]/'
                                                    'div[2]/div/button[8]').click()

        else:

            self.driver.find_element(self.By.XPATH,
                                     '/html/body/div[1]/div/div/div/div/div/div[1]/div[2]/div/div/ul/li[2]/a/span').click()
            time.sleep(0.1)
            self.driver.find_element(self.By.XPATH,
                                     '/html/body/div[1]/div/div/div/div/div/div[2]/div/div/div/div[1]/div[2]/div/button[9]').click()

    def __turmas(self, turma_escolhida):

        try:
            self.driver.find_element(self.By.XPATH,
                                     '/ html/body/div[1]/div/div/div/div/div/div[2]/div/div/div/div[3]/div[1]/div[2]/div[1]/div[1]/span[3]/a').click()

            pyautogui.hotkey('ctrl', 'shift', 'i')

            len_de_turmas = len(
                self.driver.find_elements(self.By.XPATH,
                                          f'/html/body/div[{self.div}]/div/div/div[3]/table/tbody[1]/tr'))
            on = True

            while on:

                for i in range(1, len_de_turmas + 1):

                    turma = self.driver.find_element(self.By.XPATH,
                                                     f'/html/body/div[{self.div}]/div/div/div[3]/table/tbody[1]/tr[{i}]/td[1]/div')

                    time.sleep(0.1)
                    turma_texto = self.__filtrar_texto(modo='turma', texto=turma.text)

                    if turma_escolhida == turma_texto:
                        turma.click()
                        on = False
                        break

                    if i == len_de_turmas and len_de_turmas == 5:

                        self.driver.find_element(self.By.XPATH,
                                                 f'/html/body/div[{self.div}]/div/div/div[4]/div/ul/li[4]/a').click()
                        time.sleep(0.1)

                        len_de_turmas = len(
                            self.driver.find_elements(self.By.XPATH,
                                                      f'/html/body/div[{self.div}]/div/div/div[3]/table/tbody[1]/tr'))
                        time.sleep(0.5)

            pyautogui.hotkey('ctrl', 'shift', 'i')
        except:
            raise print('Erro na turma')

    def __disciplina(self, disciplina_escolhida):

        try:
            self.driver.find_element(self.By.XPATH, '/html/body/div[1]/div/div/div/div/div/div[2]/div/div/div/div[3]/'
                                                    'div[1]/div[2]/div[1]/div[2]/span[2]/a').click()

            time.sleep(0.1)
            len_disciplina = len(
                self.driver.find_elements(self.By.XPATH,
                                          f'/html/body/div[{self.div}]/div/div/div[3]/table/tbody[1]/tr'))

            if len_disciplina > 1:
                for i in range(1, len_disciplina + 1):

                    discisplina = self.driver.find_element(self.By.XPATH,
                                                           f'/html/body/div[{self.div}]/div/div/div[3]/table/tbody[1]/tr[{i}]/td/div')

                    disciplina_texto = self.__filtrar_texto(modo='disciplina', texto=discisplina.text)

                    if disciplina_texto == disciplina_escolhida:
                        discisplina.click()

                        break

        except:
            raise print('Erro na disciplinas')

    def __etapa(self):
        try:
            self.driver.find_element(self.By.XPATH, '/html/body/div[1]/div/div/div/div/div/div[2]/div/div/div/div[3]/'
                                                    'div[1]/div[2]/div[1]/div[3]/span[3]/a').click()
            time.sleep(0.5)

        except:
            raise print('Erro na etapa')

    def __bimestre(self, bimestre):
        try:
            self.driver.find_element(self.By.XPATH, '/html/body/div[1]/div/div/div/div/div/div[2]/div/div/div/div[3]/'
                                                    'div[1]/div[2]/div[1]/div[4]/span[3]/a').click()

            time.sleep(0.5)
            len_bimestre = len(
                self.driver.find_elements(self.By.XPATH,
                                          f'/html/body/div[{self.div}]/div/div/div[3]/table/tbody[1]/tr'))

            for i in range(1, len_bimestre + 1):

                bimestre_texto = self.driver.find_element(self.By.XPATH,
                                                          f'/html/body/div[{self.div}]/div/div/div[3]/table/tbody[1]/tr[{i}]/td/div')

                if int(bimestre_texto.text[0]) == int(bimestre):
                    bimestre_texto.click()
                    break
        except:
            raise print('Erro no bimestre')

    def __data(self, data):

        try:
            self.driver.find_element(self.By.XPATH, '/html/body/div[1]/div/div/div/div/div/div[2]/div/div/div/div[3]'
                                                    '/div[1]/div[2]/div[1]/div[5]/span[3]/input').send_keys(data)
        except:
            raise print('Erro na data')

    def __conteudo_lecionado(self, conteudo):

        try:
            self.driver.find_element(self.By.XPATH, '/html/body/div[1]/div/div/div/div/div/div[2]/div/div/div/div[3]'
                                                    '/div[1]/div[2]/div[1]/div[6]/input').send_keys(conteudo)
        except:
            raise print('Erro no conteudo')

    def __faltas(self, lista):
        try:
            self.driver.find_element(self.By.XPATH, '/html/body/div[1]/div/div/div/div/div/div[2]/div/div/div/div[3]/'
                                                    'div[1]/div[2]/div[2]/button').click()

            len_faltas = len(
                self.driver.find_elements(self.By.XPATH, '/html/body/div[1]/div/div/div/div/div/div[2]/div/div/'
                                                         'div/div[3]/div[2]/div[2]/div/div[2]/div/div/table/'
                                                         'tbody[1]/tr[2]/td/div/div/div[3]/table/tbody[1]/tr'))

            for i in range(1, len_faltas + 1):

                nome = self.driver.find_element(self.By.XPATH, '/html/body/div[1]/div/div/div/div/div/div[2]/div/div/div/'
                                                               'div[3]/div[2]/div[2]/div/div[2]/div/div/table/tbody[1]/'
                                                               f'tr[2]/td/div/div/div[3]/table/tbody[1]/tr[{i}]/td[3]/'
                                                               'div/span[1]').text

                nome_filtrado = self.__filtrar_texto('faltas', nome)

                if nome_filtrado in lista:
                    lista.remove(nome_filtrado)

                    self.driver.find_element(self.By.XPATH,
                                             '/html/body/div[1]/div/div/div/div/div/div[2]/div/div/div/div[3]/'
                                             'div[2]/div[2]/div/div[2]/div/div/table/tbody[1]/tr[2]/td/div/div/div[3]/'
                                             f'table/tbody[1]/tr[{i}]/td[5]/div/button').click()
                    time.sleep(0.5)
                    pyautogui.hotkey('esc')

                    self.driver.find_element(self.By.XPATH,
                                             '/html/body/div[1]/div/div/div/div/div/div[2]/div/div/div/div[3]/'
                                             'div[2]/div[2]/div/div[2]/div/div/table/tbody[1]/tr[2]/'
                                             f'td/div/div/div[3]/table/tbody[1]/tr[{i}]/td[4]/div/div/div').click()

            time.sleep(0.5)

            self.driver.execute_script("window.scrollTo(-8,-8)")

            time.sleep(0.5)

            self.driver.find_element(self.By.XPATH, '/html/body/div[1]/div/div/div/div/div/div[2]/div/div/div/div[1]/'
                                                    'div[2]/div/button[7]').click()

            if self.div == 4:
                self.driver.find_element(self.By.XPATH, '/html/body/div[5]/div[2]/table[2]/tbody/tr/td/table/tbody/tr/'
                                                        'td/button').click()
            elif self.div == 5:
                self.driver.find_element(self.By.XPATH, '/html/body/div[6]/div[2]/table[2]/tbody/tr/td/table/tbody/tr/td/'
                                                        'button').click()

            self.div = 5

        except:
            raise print('Erro na falta')

    @staticmethod
    def __filtrar_texto(modo, texto=''):

        if modo == 'turma':

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
