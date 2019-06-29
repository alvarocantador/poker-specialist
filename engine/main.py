from pyknow import *
from engine.facts import *

class PokerInference(KnowledgeEngine):
 
    @Rule(AS.player << Player(bbs=None), AS.blind << Blind())
    def set_player_big_blinds(self, player, blind):
        self.modify(player, bbs=player["chips"]/blind["big"])