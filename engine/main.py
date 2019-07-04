from pyknow import *
from engine.facts import *


class PokerInference(KnowledgeEngine):
    pass
    # @Rule(UserInput(is_ok=True),
    #       Action(street='PREFLOP'),
    #       Action(is_raised=False),
    #       AS.action << Action(),
    #       TEST(lambda action: action['group'] == 1 or action['group'] == 2))
    # def preflop_group_1_2(self):
    #     print("Sugestão de AUMENTAR a aposta!")

    # @Rule(UserInput(is_ok=True),
    #       Action(street='PREFLOP'),
    #       Action(is_raised=False),
    #       AS.action << Action(),
    #       TEST(lambda action: action['group'] == 3),
    #       TEST(lambda action: action['position'] == 'UTG+1' or
    #                           action['position'] == 'MP1' or
    #                           action['position'] == 'MP2' or
    #                           action['position'] == 'HJ' or
    #                           action['position'] == 'CO' or
    #                           action['position'] == 'BTN' or
    #                           action['position'] == 'SB' or
    #                           action['position'] == 'BB'))
    # def preflop_group_3_raise(self):
    #     print("Sugestão de AUMENTAR a aposta!")

    # @Rule(UserInput(is_ok=True),
    #       Action(street='PREFLOP'),
    #       Action(is_raised=False),
    #       AS.action << Action(),
    #       TEST(lambda action: action['group'] == 3),
    #       TEST(lambda action: action['position'] == 'UTG'))
    # def preflop_group_3_fold(self):
    #     print("Sugestão de DESISTIR da mão!")

    # @Rule(UserInput(is_ok=True),
    #       Action(street='PREFLOP'),
    #       Action(is_raised=False),
    #       AS.action << Action(),
    #       TEST(lambda action: action['group'] == 4),
    #       TEST(lambda action: action['position'] == 'MP1' or
    #                           action['position'] == 'MP2' or
    #                           action['position'] == 'HJ' or
    #                           action['position'] == 'CO' or
    #                           action['position'] == 'BTN' or
    #                           action['position'] == 'SB' or
    #                           action['position'] == 'BB'))
    # def preflop_group_4_raise(self):
    #     print("Sugestão de AUMENTAR a aposta!")

    # @Rule(UserInput(is_ok=True),
    #       Action(street='PREFLOP'),
    #       Action(is_raised=False),
    #       AS.action << Action(),
    #       TEST(lambda action: action['group'] == 4),
    #       TEST(lambda action: action['position'] == 'UTG+1' or
    #                           action['position'] == 'UTG'))
    # def preflop_group_4_fold(self):
    #     print("Sugestão de DESISTIR da mão!")

    # @Rule(UserInput(is_ok=True),
    #       Action(street='PREFLOP'),
    #       Action(is_raised=False),
    #       AS.action << Action(),
    #       TEST(lambda action: action['group'] == 5),
    #       TEST(lambda action: action['position'] == 'MP2' or
    #                           action['position'] == 'HJ' or
    #                           action['position'] == 'CO' or
    #                           action['position'] == 'BTN' or
    #                           action['position'] == 'SB'))
    # def preflop_group_5_raise(self):
    #     print("Sugestão de AUMENTAR a aposta!")

    # @Rule(UserInput(is_ok=True),
    #       Action(street='PREFLOP'),
    #       Action(is_raised=False),
    #       AS.action << Action(),
    #       TEST(lambda action: action['group'] == 5),
    #       TEST(lambda action: action['position'] == 'MP1' or
    #                           action['position'] == 'UTG+1' or
    #                           action['position'] == 'UTG' or
    #                           action['position'] == 'BB'))
    # def preflop_group_5_fold(self):
    #     print("Sugestão de DESISTIR da mão!")

    # @Rule(UserInput(is_ok=True),
    #       Action(street='PREFLOP'),
    #       Action(is_raised=False),
    #       AS.action << Action(),
    #       TEST(lambda action: action['group'] == 6),
    #       TEST(lambda action: action['position'] == 'HJ' or
    #                           action['position'] == 'CO' or
    #                           action['position'] == 'BTN'))
    # def preflop_group_6_raise(self):
    #     print("Sugestão de AUMENTAR a aposta!")

    # @Rule(UserInput(is_ok=True),
    #       Action(street='PREFLOP'),
    #       Action(is_raised=False),
    #       AS.action << Action(),
    #       TEST(lambda action: action['group'] == 6),
    #       TEST(lambda action: action['position'] == 'MP1' or
    #                           action['position'] == 'MP2' or
    #                           action['position'] == 'UTG+1' or
    #                           action['position'] == 'UTG' or
    #                           action['position'] == 'SB' or
    #                           action['position'] == 'BB'))
    # def preflop_group_6_fold(self):
    #     print("Sugestão de DESISTIR da mão!")

    # @Rule(UserInput(is_ok=True),
    #       Action(street='PREFLOP'),
    #       Action(is_raised=False),
    #       AS.action << Action(),
    #       TEST(lambda action: action['group'] == 7),
    #       TEST(lambda action: action['position'] == 'HJ' or
    #                           action['position'] == 'CO' or
    #                           action['position'] == 'BTN'))
    # def preflop_group_7_raise(self):
    #     print("Sugestão de AUMENTAR a aposta!")

    # @Rule(UserInput(is_ok=True),
    #       Action(street='PREFLOP'),
    #       Action(is_raised=False),
    #       AS.action << Action(),
    #       TEST(lambda action: action['group'] == 7),
    #       TEST(lambda action: action['position'] == 'MP1' or
    #                           action['position'] == 'MP2' or
    #                           action['position'] == 'UTG+1' or
    #                           action['position'] == 'UTG' or
    #                           action['position'] == 'SB' or
    #                           action['position'] == 'BB'))
    # def preflop_group_7_fold(self):
    #     print("Sugestão de DESISTIR da mão!")


    # @Rule(UserInput(is_ok=True),
    #       Action(street='PREFLOP'),
    #       Action(is_raised=False),
    #       AS.action << Action(),
    #       TEST(lambda action: action['group'] == 8),
    #       TEST(lambda action: action['position'] == 'BTN'))
    # def preflop_group_8_raise(self):
    #     print("Sugestão de AUMENTAR a aposta!")

    # @Rule(UserInput(is_ok=True),
    #       Action(street='PREFLOP'),
    #       Action(is_raised=False),
    #       AS.action << Action(),
    #       TEST(lambda action: action['group'] == 8),
    #       TEST(lambda action: action['position'] == 'MP1' or
    #                           action['position'] == 'MP2' or
    #                           action['position'] == 'UTG+1' or
    #                           action['position'] == 'UTG' or
    #                           action['position'] == 'HJ' or
    #                           action['position'] == 'CO' or
    #                           action['position'] == 'SB' or
    #                           action['position'] == 'BB'))
    # def preflop_group_8_fold(self):
    #     self.declare(Suggestion(street='PREFLOP', 'Desistir da mão'))

    @Rule(AS.player << Player(bbs=None), AS.blind << Blind())
    def set_player_big_blinds(self, player, blind):
        self.modify(player, bbs=player['chips']/blind['big'])

    @Rule(AS.player << Player(),
          AS.received_card << ReceivedCard(),
          TEST(lambda player, received_card: player['name'] == received_card['player']))
    def set_received_cards(self, player, received_card):
        f_card, s_card = received_card['cards']
        self.modify(player, me=True, cards=received_card['cards'], suited=f_card['suit'] == s_card['suit'])
        self.retract(received_card)
