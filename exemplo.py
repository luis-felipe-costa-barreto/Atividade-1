class Funcionario():
    def __init__(self, nome, cpf, salario):
        self.nome = nome
        self.__cpf = cpf
        self._salario = salario
    def get_cpf(self):
        return self.__cpf
    def set_salario(self, x):
        self._salario = x
        print(f'salário atualizado para {self._salario}')

class Operario(Funcionario):
    def __init__(self, nome, cpf, salario, departamento):
        super().__init__(nome, cpf, salario)
        self.__departamento = departamento
    def get_departamento(self):
        return self.__departamento

