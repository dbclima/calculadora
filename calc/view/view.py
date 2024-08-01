from typing import Protocol

from .layout import Ui_MainWindow

class Presenter(Protocol):
    ...


class View(Ui_MainWindow):
    def __init__(self):
        super().__init__()