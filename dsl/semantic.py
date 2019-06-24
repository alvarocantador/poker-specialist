from lark import Lark, Transformer

class PokerSemantic(Transformer):
    def player(self):
        print(self)