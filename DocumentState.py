from abc import ABC, abstractmethod

class Context:
    _state = None

    def __init__(self, state):
        self.transition_to(state)
    
    def transition_to(self, state):
        self._state = state
        self._state.context = self
    
    def request1(self):
        self._state.handleFirst()
    
    def request2(self):
        self._state.handleSecond()

class State(ABC):

    @property
    def context(self):
        return self._context
    
    @context.setter
    def context(self, context):
        self._context = context
    
    @abstractmethod
    def handleFirst(self):
        raise NotImplementedError("Implementar!")
    
    def handleSecond(self):
        raise NotImplementedError("Implementar!")


class Draft(State):
    def handleFirst(self):
        print("Published by user")
        self.context.transition_to(Moderation())
    
    def handleSecond(self):
        print("Published by admin")
        self.context.transition_to(Published())

class Moderation(State):
    def handleFirst(self):
        print("Review Failed")
        self.context.transition_to(Draft())
    
    def handleSecond(self):
        print("Approved by admin")
        self.context.transition_to(Published())

class Published(State):
    def handleFirst(self):
        print("Publication expired")
        self.context.transition_to(Draft())
    
    def handleSecond(self):
        print("Published!!\n")


# ---------- TESTES ----------

context1 = Context(Draft())
context1.request2()
context1.request2()

print("\n")
context2 = Context(Draft())
context2.request1()
context2.request2()
context2.request1()
context2.request1()
context2.request2()
context2.request2()
        

