from typing import Union, Optional
from enum import Enum, auto

class EqStatus(Enum):
    OK = auto()
    

class Equation:
    SPACER: str = ''
    OPERATORS = ["**(2) **(1/2)", '* /', '+ -']

    def __init__(self):
        self.raw_elements: list[str] = list()
        
    @property
    def string(self) -> str:
        return self.SPACER.join(self.raw_elements)

    def append(self, element) -> None:
        self.raw_elements.append(element)

    def pop(self) -> Optional[str]:
        if len(self.raw_elements) == 0:
            return None
        return self.raw_elements.pop()

    def digest(self) -> Optional[Union[int, float]]:
        if len(self.raw_elements) == 0:
            return None
         
        return self._recursive_digest(self.string)

    def _extrair_parenteses(self, texto: str) -> Optional[str]:
        contador_parenteses = 0
        idx_abre = -1
        idx_fecha = -1

        for idx_letra, letra in enumerate(texto):
            if letra == "(":
                contador_parenteses += 1
                if idx_abre == -1:
                    idx_abre = idx_letra
                
            if letra == ")":
                contador_parenteses -= 1
                if contador_parenteses == 0:
                    idx_fecha = idx_letra

        if idx_fecha == -1:
            return None

        return texto[idx_abre: idx_fecha]
    
    def solve(self, equacao: str) -> str:
        
        return None


    def _recursive_digest(self, equacao: str) -> list[Union[str, list]]:
        if (not "(" in equacao) or (not ")" in equacao):
            return str(self.solve(equacao))

        prioridade = self._extrair_parenteses(equacao)
        
        if prioridade is None:
            return None
        
        return equacao.replace(f"({prioridade})", self._recursive_digest(prioridade))


