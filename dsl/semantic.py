from lark import Lark, Transformer

class PokerSemantic(Transformer):
    
    def fold(self, token):
        print(token[0])
