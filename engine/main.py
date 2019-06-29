from pyknow import *
from engine.facts import *

class PokerInference(KnowledgeEngine):
 
    @Rule(AS.player << Player(bbs=None), AS.blind << Blind())
    def set_player_big_blinds(self, player, blind):
        self.modify(player, bbs=player["chips"]/blind["big"])

    @Rule(AS.player << Player(), 
    AS.received_card << ReceivedCard(), 
    TEST(lambda player, received_card: player['name'] == received_card['player']))
    def set_received_cards(self, player, received_card):
        f_card, s_card = received_card['cards']
        self.modify(player, me=True, cards=received_card['cards'], suited=f_card['suit']==s_card['suit'])
        self.retract(received_card)