class Model:
    operadores = ['+', '-', '/', 'x', '**']
    def __init__(self) -> None:
        return None

    def realizar_operacao(self, simbolo: str, valor1: float, valor2: float) -> float:
        pass

    def solucionar_equacao_valida(self, equacao: str) -> float:
        pass

    def verificar_validade(self, equacao: str) -> bool:
        contador = 0
        for idx, elemento in enumerate(equacao):
            if contador < 0:
                return False
            if elemento == '(':
                contador += 1
            elif elemento == ')':
                contador -= 1

            if (elemento in operadores) and (equacao[idx + 1] in operadores):
                return False

        if contador == 0:
            return True
        return False