from lark import Lark, Transformer
from engine.main import *
from engine.facts import *

class PokerSemantic(Transformer):
    
    def __init__(self, engine = PokerInference()):
        self.engine = engine

    def hand(self, token):
        self.engine.declare(Hand(number=int(token[0])))

    def blind(self, token):
        self.engine.declare(Blind(small=int(token[1]), big=int(token[2])))