from pyknow import *
from engine.facts import *


class PokerInference(KnowledgeEngine):

    @Rule(AS.player << Player(),
          AS.received_card << ReceivedCard(),
          TEST(lambda player, received_card: player['name'] == received_card['player']))
    def set_received_cards(self, player, received_card):
        f_card, s_card = received_card['cards']
        self.retract(received_card)

        # Ordena cartas
        card_1_v = 0
        if f_card['value'] == 'A':
            card_1_v = 1
        elif f_card['value'] == 'T':
            card_1_v = 10
        elif f_card['value'] == 'J':
            card_1_v = 11
        elif f_card['value'] == 'Q':
            card_1_v = 12
        elif f_card['value'] == 'K':
            card_1_v = 13
        else:
            card_1_v = int(f_card['value'])

        card_2_v = 0
        if s_card['value'] == 'A':
            card_2_v = 1
        elif s_card['value'] == 'T':
            card_2_v = 10
        elif s_card['value'] == 'J':
            card_2_v = 11
        elif s_card['value'] == 'Q':
            card_2_v = 12
        elif s_card['value'] == 'K':
            card_2_v = 13
        else:
            card_2_v = int(s_card['value'])

        card_1_s = f_card['suit']
        card_2_s = s_card['suit']
        if card_1_v < card_2_v:
            card_temp = card_1_v
            card_1_v = card_2_v
            card_2_v = card_temp
            card_1_s = s_card['suit']
            card_2_s = f_card['suit']

        # Mpdifica player
        self.modify(player, me=True, cards=received_card['cards'],
                    card_1_v=card_1_v, card_2_v=card_2_v,
                    card_1_s=card_1_s, card_2_s=card_2_s,
                    suited=f_card['suit'] == s_card['suit'],
                    group=0)

        # Descricao das cartas
        # cards_desc = '{0}{1},{2}{3}'.format(f_card['value'], f_card['suit'], s_card['value'], s_card['suit'])
        # self.declare(Suggestion(street='PREFLOP', message='Cartas recebidas: {0}'.format(cards_desc)))

    @Rule(AS.action << Action(me=False),
          AS.player << Player(me=True),
          TEST(lambda action, player: action['player'] == player['name']))
    def set_me_in_action(self, action):
        self.modify(action, me=True)

    @Rule(AS.action << Action(me=False, type='raise'),
          AS.action_me << Action(me=True, is_raised=False),
          TEST(lambda action, action_me: action_me['street'] == action['street'] and
                                         action_me['id'] > action['id'] and
                                         action_me['act'] == action['act']))
    def is_prefop_raised_act_1(self, action_me):
        self.modify(action_me, is_raised=True)
        # self.declare(Suggestion(street='PREFLOP', message='Aumentaram no pre flop'))

    @Rule(AS.player << Player(group=0),
          TEST(lambda player: (player['card_1_v'] == 1 and player['card_2_v'] == 1) or
                              (player['card_1_v'] == 13 and player['card_2_v'] == 13) or
                              (player['card_1_v'] == 12 and player['card_2_v'] == 12) or
                              (player['card_1_v'] == 12 and player['card_2_v'] == 12) or
                              (player['card_1_v'] == 11 and player['card_2_v'] == 11) or
                              (player['card_1_v'] == 13 and player['card_2_v'] == 1 and player['suited'])
               ))
    def preflop_define_group_1(self, player):
        self.modify(player, group=1)
        # self.declare(Suggestion(street='PREFLOP', message='MAO GRUPO 1'))

    @Rule(AS.player << Player(group=0),
          TEST(lambda player: (player['card_1_v'] == 10 and player['card_2_v'] == 10) or
                              (player['card_1_v'] == 12 and player['card_2_v'] == 1 and player['suited']) or
                              (player['card_1_v'] == 11 and player['card_2_v'] == 1 and player['suited']) or
                              (player['card_1_v'] == 13 and player['card_2_v'] == 12 and player['suited']) or
                              (player['card_1_v'] == 13 and player['card_2_v'] == 1 and not player['suited'])
               ))
    def preflop_define_group_2(self, player):
        self.modify(player, group=2)
        # self.declare(Suggestion(street='PREFLOP', message='MAO GRUPO 2'))

    @Rule(AS.player << Player(group=0),
          TEST(lambda player: (player['card_1_v'] == 9 and player['card_2_v'] == 9) or
                              (player['card_1_v'] == 10 and player['card_2_v'] == 1 and player['suited']) or
                              (player['card_1_v'] == 13 and player['card_2_v'] == 11 and player['suited']) or
                              (player['card_1_v'] == 12 and player['card_2_v'] == 11 and player['suited']) or
                              (player['card_1_v'] == 11 and player['card_2_v'] == 10 and player['suited']) or
                              (player['card_1_v'] == 12 and player['card_2_v'] == 1 and not player['suited'])
               ))
    def preflop_define_group_3(self, player):
        self.modify(player, group=3)
        # self.declare(Suggestion(street='PREFLOP', message='MAO GRUPO 3'))

    @Rule(AS.player << Player(group=0),
          TEST(lambda player: (player['card_1_v'] == 8 and player['card_2_v'] == 8) or
                              (player['card_1_v'] == 13 and player['card_2_v'] == 10 and player['suited']) or
                              (player['card_1_v'] == 12 and player['card_2_v'] == 10 and player['suited']) or
                              (player['card_1_v'] == 11 and player['card_2_v'] == 9 and player['suited']) or
                              (player['card_1_v'] == 10 and player['card_2_v'] == 9 and player['suited']) or
                              (player['card_1_v'] == 9 and player['card_2_v'] == 8 and player['suited']) or
                              (player['card_1_v'] == 11 and player['card_2_v'] == 1 and not player['suited']) or
                              (player['card_1_v'] == 13 and player['card_2_v'] == 12 and not player['suited'])
               ))
    def preflop_define_group_4(self, player):
        self.modify(player, group=4)
        # self.declare(Suggestion(street='PREFLOP', message='MAO GRUPO 4'))

    @Rule(AS.action << Action(street='PREFLOP', me=True, act=1, is_raised=False),
          AS.player << Player(me=True),
          TEST(lambda player: player['group'] == 1 or player['group'] == 2))
    def preflop_group_1_2(self):
        self.declare(Suggestion(street='PREFLOP', message='Aumentar a aposta'))

    @Rule(AS.action << Action(street='PREFLOP', me=True, act=1, is_raised=False),
          AS.player << Player(me=True),
          TEST(lambda player: player['group'] == 3),
          TEST(lambda action: action['position'] == 'UTG+1' or
                              action['position'] == 'MP1' or
                              action['position'] == 'MP2' or
                              action['position'] == 'HJ' or
                              action['position'] == 'CO' or
                              action['position'] == 'BTN' or
                              action['position'] == 'SB' or
                              action['position'] == 'BB'))
    def preflop_group_3_raise(self):
        self.declare(Suggestion(street='PREFLOP', message='Aumentar a aposta'))

    @Rule(AS.action << Action(street='PREFLOP', me=True, act=1, is_raised=False),
          AS.player << Player(me=True),
          TEST(lambda player: player['group'] == 3),
          TEST(lambda action: action['position'] == 'UTG'))
    def preflop_group_3_fold(self):
        self.declare(Suggestion(street='PREFLOP', message='Desistir da mão'))

    @Rule(AS.action << Action(street='PREFLOP', me=True, act=1, is_raised=False),
          AS.player << Player(me=True),
          TEST(lambda player: player['group'] == 4),
          TEST(lambda action: action['position'] == 'MP1' or
                              action['position'] == 'MP2' or
                              action['position'] == 'HJ' or
                              action['position'] == 'CO' or
                              action['position'] == 'BTN' or
                              action['position'] == 'SB' or
                              action['position'] == 'BB'))
    def preflop_group_4_raise(self):
        self.declare(Suggestion(street='PREFLOP', message='Aumentar a aposta'))

    @Rule(AS.action << Action(street='PREFLOP', me=True, act=1, is_raised=False),
          AS.player << Player(me=True),
          TEST(lambda player: player['group'] == 4),
          TEST(lambda action: action['position'] == 'UTG+1' or
                              action['position'] == 'UTG'))
    def preflop_group_4_fold(self):
        self.declare(Suggestion(street='PREFLOP', message='Desistir da mão'))

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

