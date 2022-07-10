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
    name_var =None
    amount_var =None
    costumer = None

    def submit_transacao(self):
        name = self.name_var.get()
        amount = self.amount_var.get()

        self.costumer.balance = int(self.costumer.balance) - int(amount)
        self.costumer.extratos.append(Transacao(int(amount), self.costumer.name, name))

        self.name_var.set("")
        self.amount_var.set("")
    

    def show_transacoes(self):
        for transacao in self.costumer.extratos:
            if(transacao.nameReceiver == self.costumer.name):
                tk.Label(text="Recebido " + str(transacao.amount) + " de " + transacao.nameSender).pack()
            else:
                tk.Label(text="Enviado " + str(transacao.amount) + " para " + transacao.nameReceiver).pack()


    def execute(self, wn, cliente):
        self.name_var = tk.StringVar()
        self.amount_var = tk.StringVar()
        self.costumer = cliente
        tk.Label(text="                             Hello, " + cliente.name + "                       \n").pack()
        tk.Label(text = "Seu saldo: " + str(cliente.balance) + "\n").pack()
        tk.Label(text="Transferir para: ").pack()
        entry = tk.Entry(width = 20, textvariable=self.name_var)
        entry.focus_set()
        entry.pack()

        tk.Label(text="Quantidade a transferir: ").pack()
        entry = tk.Entry(width = 20, textvariable=self.amount_var)
        entry.focus_set()
        entry.pack()
        tk.Button(text="Transferir", command= lambda : {self.submit_transacao(self)}).pack()

        tk.Button(text="Ver extrato", command= lambda: {self.show_transacoes(self)}).pack()

        wn.mainloop()

        
        

class Invoker:

    window = tk.Tk()

    def set_on_start(self, command, cliente):
        self._on_start = command
        self._on_start.execute(self._on_start, self.window, cliente)

# ------ Testes ------------

invoker = Invoker()
cliente = Cliente(1, "Luiz", 500)
invoker.set_on_start(StartLoop, cliente)

