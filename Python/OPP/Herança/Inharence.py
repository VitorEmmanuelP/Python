class DatabaseConn:

    def __init__(self):

        self.__databse = 'Postgree'
        self._conn = '//conhection-string'
        self.user = 'Root'


    def get_database(self) -> None:
        print(self.__databse)


    def _testing_conection(self) -> None:
        print('Connection ok')




class Repository(DatabaseConn):


    def __init__(self):
        super().__init__()


    def select(self) -> None:
        self._testing_conection()
        print(f'connectung to {self._conn}')
        print('Select * FROM table')

repo = Repository()

repo.select()