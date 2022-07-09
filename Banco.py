from abc import ABC, abstractmethod
import tkinter as tk

class Transacao:
    def __init__(self, amount, nameSender, nameReceiver):
        self.amount = amount
        self.nameSender = nameSender
        self.nameReceiver = nameReceiver


class Cliente:
    def __init__(self, id, name, balance):
        self.id = id
        self.name = name
        self.balance = balance
        self.extratos = [Transacao(balance, "Deposito", name)]

    def get_balance(self):
        return self.balance
    
    def get_extratos(self):
        return self.extratos
    
    def get_name(self):
        return self.name

class Command(ABC):

    @abstractmethod
    def execute(self):
        raise NotImplementedError("Necessário implementar")

class StartLoop(Command):
    def execute(self, wn):
        wn.mainloop()
        



class Invoker:

    window = tk.Tk()

    def set_on_start(self, command):
        self._on_start = command

