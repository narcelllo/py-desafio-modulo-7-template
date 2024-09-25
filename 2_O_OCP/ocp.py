from abc import ABC, abstractmethod

class ExameHandlerInterface(ABC):
    @abstractmethod
    def verifica_condicoes_exame_sangue(self,exame):
        return self.__exame.sange(exame)
    
    @abstractmethod
    def verifica_condicoes_raio_x(self, exame):
        return self.__exame.raio_x(exame)
    

class CondicoesExame(ExameHandlerInterface):
    def __init__(self) -> None:
        self.__exame = Exame

    def verifica_condicoes_exame_sangue(self,exame):
        # implemente as condições específicas do exame de sangue
        return self.__exame.sange(exame)

    def verifica_condicoes_raio_x(self, exame):
        # implemente as condições específicas do exame de raio-x
        return self.__exame.raio_x(exame)

class AprovaExame:
    def aprovar_solicitacao_exame(self, aprova_exame: ExameHandlerInterface):
        self.__aprova_exame = aprova_exame

        if exame_sangue.tipo == "sangue":
            if aprovador.self.__aprova_exame(exame_sangue):
                print("Exame sanguíneo aprovado!")

        elif exame_raio_x.tipo == "raio-x":
            if aprovador.self.__aprova_exame(exame_raio_x):
                print("Raio-X aprovado!")
                pass

# Exemplo de uso:
class Exame:
    def __init__(self, tipo):
        self.tipo = tipo

aprovador = AprovaExame()

exame_sangue = Exame("sangue")
exame_raio_x = Exame("raio-x")
