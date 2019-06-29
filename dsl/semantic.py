from lark import Lark, Transformer, v_args
from engine.main import *
from engine.facts import *
import ast

class PokerSemantic(Transformer):
    
    def __init__(self, engine = PokerInference()):
        self.engine = engine

    def hand(self, token):
        self.engine.declare(Hand(id=int(token[0])))

    def blind(self, token):
        self.engine.declare(Blind(small=int(token[1]), big=int(token[2])))
    
    def player(self, token):
        return token[0].strip()
    
    def chips(self, token):
        return ast.literal_eval(token[0])

    # @v_args(inline=True)
    def seat(self, token):
        self.engine.declare(Player(name=token[1], 
            chips=token[2], 
            seat=ast.literal_eval(token[0]),
            is_out=(len(token) == 4 and token[3].type == "IS_OUT")))

    