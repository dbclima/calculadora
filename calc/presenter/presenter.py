from __future__ import annotations
from typing import Callable, Protocol
from PySide6 import QtWidgets, QtCore

from ..model import Model


class View(Protocol):
    def setupUi(self, main_window: QtWidgets.QMainWindow) -> None:
        ...

    def setup_signals(self, presenter: Presenter) -> None:
        ...


class Presenter:
    warning = "Equacao Incorreta"

    def __init__(self, model: Model, view: View) -> None:
        self.model = model
        self.view = view
        return None

    @QtCore.Slot()
    def handle_signal_igual(self):
        str = self.model.calcular()
        self.view.update_history(self.model.history)
        self.view.update_display(self.model.equation.string)

    @QtCore.Slot()
    def handle_signal_botao_trivial(self, texto_botao: str) -> None:        
        self.model.equation.append_to_equation(texto_botao)
        self.view.update_display(self.model.equation.string)
        return None

    @QtCore.Slot()
    def handle_signal_backspace(self) -> None:
        self.model.equation.pop()
        self.view.update_display(self.model.equation.string)
        return None 

    def run(self) -> None:
        app = QtWidgets.QApplication([])
        window = QtWidgets.QMainWindow()
        self.view.setupUi(window)
        self.view.setup_signals(self)
        window.show()
        app.exec()
