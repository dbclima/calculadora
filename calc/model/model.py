from typing import Union

from .equation import Equation

class Model:
    operadores = ['+', '-', '/', 'x', '**']
    def __init__(self) -> None:
        self.equation: Equation = Equation()
        self._history: list[Equation] = list()
        return None

    @property
    def history(self) -> list[str]:
        return [equacao.string for equacao in self._history]

    def calcular(self) -> str:
        try:
            resultado = self._equation.digest()

        except ZeroDivisionError:
            return "Erro divisao por Zero"
        
        if isinstance(resultado, Union[float, int]):
            self.equation.append("=")
            self.equation.append(resultado)
            self._history.append(self.equation)
            self.equation = Equation()