from typing import Protocol
import PySide6
from PySide6 import QtWidgets

if PySide6.__version__ != "6.7.2":
    print("WARNING: Versao PySide6 nao recomendada - Versao Esperada \"6.7.2\"")

from .layout import Ui_MainWindow

class Presenter(Protocol):
    def handle_signal_igual(self, event=None) -> None:
        ...

    def handle_signal_botao_trivial(self, botao_trivial: QtWidgets.QPushButton) -> None:
        ...

    def handle_signal_backspace(self, botao: QtWidgets.QPushButton) -> None:
        ...

class View(Ui_MainWindow):
    def __init__(self) -> None:
        super().__init__()

    def setup_signals(self, presenter: Presenter) -> None:
        lista_botoes_triviais = [
            self.botao_0,
            self.botao_1,
            self.botao_2,
            self.botao_3,
            self.botao_4,
            self.botao_5,
            self.botao_6,
            self.botao_7,
            self.botao_8,
            self.botao_9,
            self.botao_abre_parenteses,
            self.botao_fecha_parenteses,
            self.botao_multiplica,
            self.botao_adicao,
            self.botao_divide,
            self.botao_subtracao,
            self.botao_percent,
            self.botao_ponto,
            self.botao_pi,
            self.botao_modulo,
            self.botao_raiz_quadrada,
            self.botao_quadrado
        ]
        
        # Conectando os botoes triviais
        for botao in lista_botoes_triviais:
            botao.clicked.connect(lambda _, btn=botao: presenter.handle_signal_botao_trivial(btn.text()))

        self.botao_backspace.clicked.connect(lambda: presenter.handle_signal_backspace())

        self.botao_calcular.clicked.connect(lambda: presenter.handle_signal_igual())

    def update_display(self, equacao: str) -> None:
        self.line_equacao.clear()
        self.line_equacao.setText(equacao)
        return None
    
    def update_history(self, equacoes: list[str]) -> None:
        self.text_historico.clear()
        for equacao in equacoes:
            self.text_historico.insertPlainText(f"<p align=\"right\">{equacao}\n")