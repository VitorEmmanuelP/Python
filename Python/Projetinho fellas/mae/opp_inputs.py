import re


class Input:

    def __init__(self):
        self.dicti = {}
        self.on = True
        self.n = 0

    def input_add_atividade(self):

        while self.on:
            turma = self.__turma()
            disciplina = self.__disciplina()
            bimestre = self.__bimestre()
            valor = self.__valor()
            descricao = input('Descrição: ')
            tipo_de_atividade = input('Se for normal digite 1, se for recuperacao digite 2: ')

            self.dicti[self.n] = {'turma': turma, 'disciplina': disciplina, 'bimestre': bimestre, 'valor': valor,
                                  'conteudo': descricao, 'tipo_de_atividade': tipo_de_atividade}
            self.n += 1

            return self.dicti

    def input_add_aula(self):

        while self.on:

            turma = self.__turma()
            disciplina = self.__disciplina()
            bimestre = self.__bimestre()
            data = self.__data()
            conteudo = input('Conteudo: ')
            faltas = self.__faltas()

            self.dicti[self.n] = {'turma': turma, 'disciplina': disciplina, 'bimestre': bimestre, 'data': data,
                                  'conteudo': conteudo, 'faltas': faltas}
            self.n += 1

            cancelamento = self.__cancelamento()

            if cancelamento:
                self.on = False
                return self.dicti

    @staticmethod
    def __turma():

        while True:

            turma = input('Turma ( ex:3 REG 2): ').upper()

            if turma == '1':
                return 1

            pattern_turma = r'(\d{1}\s(REG|INT) \d)'
            pattern = re.compile(pattern_turma)
            matches = pattern.findall(turma)

            if matches:
                final = matches[0][0].strip()
                return final

            else:
                print('Digite da forma esperada, exemplo: 3 REG 2')

    @staticmethod
    def __disciplina():
        while True:
            disciplina = input('Disciplina (ex: Lingua Portuguesa): ').upper()

            pattern_disciplinas = r"^([a-zA-z]+\s[a-zA-Z]+|[a-zA-z]+)"
            pattern = re.compile(pattern_disciplinas)
            matches = pattern.findall(disciplina)

            if matches:
                final = matches[0].strip()
                return final

            else:
                print('Digite da forma esperada, exemplo: ( Lingua Portuguesa )')

    @staticmethod
    def __bimestre():
        while True:
            bimestre = input('Bimestre (ex: 3): ')

            pattern_bimestre = r'^(\d{1})$'
            pattern = re.compile(pattern_bimestre)
            matches = pattern.findall(bimestre)

            if matches:
                final = matches[0].strip()
                return final

            else:
                print('Digite da forma esperada, exemplo: ( 3 )')

    @staticmethod
    def __data():
        while True:
            data = input('Data (ex: 20/10 ou 20 ou 05/04): ')

            pattern_data = r'(\d{2}/\d{2}|\d{2}|\d{1})$'
            pattern = re.compile(pattern_data)
            matches = pattern.findall(data)

            if matches:
                final = matches[0].strip()
                return final
            else:
                print('Digite da forma esperada, exemplo: ( 20/10 ou 20 ou 05/04 )')

    @staticmethod
    def __faltas():
        lista = []
        while True:

            faltas = input('Faltas ( Primeiro e Ultimo Nome): ').upper()

            pattern_faltas = r"^[a-zA-z]+\s[a-zA-Z]+"
            pattern = re.compile(pattern_faltas)
            matches = pattern.findall(faltas)
            if matches:
                final = matches[0]
                lista.append(final)

            elif faltas == 'N' or faltas == 'NAO':

                return lista

    @staticmethod
    def __valor():

        valor = input('Digite o valor da atividade: ')
        pattern_turma = r'^(\d{2}|\d{1})$'
        pattern = re.compile(pattern_turma)
        matches = pattern.search(valor)

        if matches:
            final = matches[0]
            return final

        else:
            print('Digite um valor de no maximo 2 digitos')

    @staticmethod
    def __cancelamento():

        cancelamento = input('Deseja adicionar mais turmas ? ').lower()

        pattern_cancelamento = r'(sim|s)$'
        pattern = re.compile(pattern_cancelamento)
        matches = pattern.findall(cancelamento)

        if matches:
            return False
        else:
            return True
