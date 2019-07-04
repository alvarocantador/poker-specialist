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

    def seat(self, token):
        self.engine.declare(Player(name=token[1], 
            chips=token[2], 
            seat=ast.literal_eval(token[0]),
            is_out=(len(token) == 4 and token[3].type == "IS_OUT")))

    def received_card(self, token):
        self.engine.declare(ReceivedCard(player=token[0], cards=token[1].children))

    def pre_flop(self, token):
        act_array = []
        for i, v in  enumerate(token):
            action = v.children[0]
            if(action['action'] == 'timeout'): continue
            act_array.append(action['player'])
            self.engine.declare(Action(street='PREFLOP', player=action['player'], type=action['action'], id=i, act=act_array.count(action['player'])))

    def card(self, token):
        return { 'value': token[0].value, 'suit': token[1].value }

    def fold(self, token):
        return { 'action': 'fold', 'player': token[0] }
    
    def raised(self, token):
        return { 'action': 'raise', 'player': token[0], 'chips': ast.literal_eval(token[1]) }

    def call(self, token):
        return { 'action': 'call', 'player': token[0], 'chips': ast.literal_eval(token[1]) }
    
    def bet(self, token):
        return { 'action': 'raise', 'player': token[0], 'chips': ast.literal_eval(token[1]) }

    def timeout(self, token):
        return { 'action': 'timeout', 'player': token[0] }

    
