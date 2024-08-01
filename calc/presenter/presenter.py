from typing import Callable, Protocol
from PySide6 import QtWidgets

class Model (Protocol):
    def realizar_operacao(self, simbolo: str, valor1: float, valor2: float) -> float:
        ...

    def solucionar_equacao(self, equacao: str) -> float:
        ...

    def verificar_validade(self, equacao: str) -> bool:
        ...

class View(Protocol):
    ...

class Presenter:
    def __init__(self, model: Model, view: View) -> None:
        self.model = model
        self.view = view
        return None

    def run(self) -> None:
        app = QtWidgets.QApplication([])
        window = QtWidgets.QMainWindow()
        self.view.setupUi(window)
        window.show()
        app.exec()