from pyknow import *
from engine.facts import *

class PokerInference(KnowledgeEngine):

    @Rule(Blind(small=MATCH.s,big=MATCH.b), TEST(lambda s,b: b < 100))
    def small_stack(self):
        print("small stack")
    
    @Rule(AS.h << Hand())
    def hand_declare(self, h):
        print("Hand ", h)