from lark import Lark, Transformer

class PokerSemantic(Transformer):
    
    def hand(self, token):
        # print("Hand number: ", token[0])
        pass

    def flop(self, token):
        if (len(token) > 2): print(token[2])