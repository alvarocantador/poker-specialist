from pyknow import *
from engine.facts import *

lambda_group_1 = lambda player: (player['card_1_v'] == 1 and player['card_2_v'] == 1) or (player['card_1_v'] == 13 and player['card_2_v'] == 13) or (player['card_1_v'] == 12 and player['card_2_v'] == 12) or (player['card_1_v'] == 12 and player['card_2_v'] == 12) or (player['card_1_v'] == 11 and player['card_2_v'] == 11) or (player['card_1_v'] == 13 and player['card_2_v'] == 1 and player['suited'])
lambda_group_2 = lambda player: (player['card_1_v'] == 10 and player['card_2_v'] == 10) or (player['card_1_v'] == 12 and player['card_2_v'] == 1 and player['suited']) or (player['card_1_v'] == 11 and player['card_2_v'] == 1 and player['suited']) or (player['card_1_v'] == 13 and player['card_2_v'] == 12 and player['suited']) or (player['card_1_v'] == 13 and player['card_2_v'] == 1 and not player['suited'])
lambda_group_3 = lambda player: (player['card_1_v'] == 9 and player['card_2_v'] == 9) or (player['card_1_v'] == 10 and player['card_2_v'] == 1 and player['suited']) or (player['card_1_v'] == 13 and player['card_2_v'] == 11 and player['suited']) or (player['card_1_v'] == 12 and player['card_2_v'] == 11 and player['suited']) or (player['card_1_v'] == 11 and player['card_2_v'] == 10 and player['suited']) or (player['card_1_v'] == 12 and player['card_2_v'] == 1 and not player['suited'])
lambda_group_4 = lambda player: (player['card_1_v'] == 8 and player['card_2_v'] == 8) or (player['card_1_v'] == 13 and player['card_2_v'] == 10 and player['suited']) or (player['card_1_v'] == 12 and player['card_2_v'] == 10 and player['suited']) or (player['card_1_v'] == 11 and player['card_2_v'] == 9 and player['suited']) or (player['card_1_v'] == 10 and player['card_2_v'] == 9 and player['suited']) or (player['card_1_v'] == 9 and player['card_2_v'] == 8 and player['suited']) or (player['card_1_v'] == 11 and player['card_2_v'] == 1 and not player['suited']) or (player['card_1_v'] == 13 and player['card_2_v'] == 12 and not player['suited'])
lambda_group_5 = lambda player: (player['card_1_v'] == 7 and player['card_2_v'] == 7) or (player['card_1_v'] <= 9 and player['card_1_v'] >= 2 and player['card_2_v'] == 1 and player['suited']) or (player['card_1_v'] == 12 and player['card_2_v'] == 9 and player['suited']) or (player['card_1_v'] == 10 and player['card_2_v'] == 8 and player['suited']) or (player['card_1_v'] == 9 and player['card_2_v'] == 7 and player['suited']) or (player['card_1_v'] == 8 and player['card_2_v'] == 7 and player['suited']) or (player['card_1_v'] == 7 and player['card_2_v'] == 6 and player['suited']) or (player['card_1_v'] == 6 and player['card_2_v'] == 5 and player['suited']) or (player['card_1_v'] == 13 and player['card_2_v'] == 11 and not player['suited']) or (player['card_1_v'] == 12 and player['card_2_v'] == 11 and not player['suited']) or (player['card_1_v'] == 11 and player['card_2_v'] == 10 and not player['suited'])
lambda_group_6 = lambda player: (player['card_1_v'] == 6 and player['card_2_v'] == 6) or (player['card_1_v'] == 5 and player['card_2_v'] == 5) or (player['card_1_v'] <= 13 and player['card_2_v'] == 9 and player['suited']) or (player['card_1_v'] == 11 and player['card_2_v'] == 8 and player['suited']) or (player['card_1_v'] == 8 and player['card_2_v'] == 6 and player['suited']) or (player['card_1_v'] == 7 and player['card_2_v'] == 5 and player['suited']) or (player['card_1_v'] == 5 and player['card_2_v'] == 4 and player['suited']) or (player['card_1_v'] == 10 and player['card_2_v'] == 1 and not player['suited']) or (player['card_1_v'] == 9 and player['card_2_v'] == 1 and not player['suited']) or (player['card_1_v'] == 13 and player['card_2_v'] == 10 and not player['suited']) or (player['card_1_v'] == 12 and player['card_2_v'] == 10 and not player['suited'])
lambda_group_7 = lambda player: (player['card_1_v'] == 4 and player['card_2_v'] == 4) or (player['card_1_v'] == 3 and player['card_2_v'] == 3) or (player['card_1_v'] == 2 and player['card_2_v'] == 2) or (player['card_1_v'] == 13 and player['card_2_v'] <= 8 and player['card_2_v'] >= 2 and player['card_2_v'] == 13 and player['suited']) or (player['card_1_v'] == 12 and player['card_2_v'] == 8 and player['suited']) or (player['card_1_v'] == 10 and player['card_2_v'] == 7 and player['suited']) or (player['card_1_v'] == 6 and player['card_2_v'] == 4 and player['suited']) or (player['card_1_v'] == 5 and player['card_2_v'] == 3 and player['suited']) or (player['card_1_v'] == 4 and player['card_2_v'] == 3 and player['suited']) or (player['card_1_v'] <= 8 and player['card_1_v'] >= 6 and player['card_2_v'] == 1 and not player['suited']) or (player['card_1_v'] == 11 and player['card_2_v'] == 9 and not player['suited']) or (player['card_1_v'] == 10 and player['card_2_v'] == 9 and not player['suited']) or (player['card_1_v'] == 8 and player['card_2_v'] == 8 and not player['suited'])
lambda_group_8 = lambda player: (player['card_1_v'] == 11 and player['card_2_v'] <= 7 and player['card_2_v'] >= 2 and player['card_2_v'] == 13 and player['suited']) or (player['card_1_v'] == 9 and player['card_2_v'] == 6 and player['suited']) or (player['card_1_v'] == 8 and player['card_2_v'] == 5 and player['suited']) or (player['card_1_v'] == 7 and player['card_2_v'] == 4 and player['suited']) or (player['card_1_v'] == 4 and player['card_2_v'] == 2 and player['suited']) or (player['card_1_v'] == 3 and player['card_2_v'] == 2 and player['suited']) or (player['card_1_v'] <= 5 and player['card_1_v'] >= 2 and player['card_2_v'] == 1 and not player['suited']) or (player['card_1_v'] == 13 and player['card_2_v'] == 9 and not player['suited']) or (player['card_1_v'] == 12 and player['card_2_v'] == 9 and not player['suited']) or (player['card_1_v'] == 11 and player['card_2_v'] == 8 and not player['suited']) or (player['card_1_v'] == 10 and player['card_2_v'] == 8 and not player['suited']) or (player['card_1_v'] == 8 and player['card_2_v'] == 7 and not player['suited']) or (player['card_1_v'] == 7 and player['card_2_v'] == 7 and not player['suited']) or (player['card_1_v'] == 6 and player['card_2_v'] == 5 and not player['suited']) or (player['card_1_v'] == 5 and player['card_2_v'] == 5 and not player['suited'])

class PokerInference(KnowledgeEngine):

    @Rule(AS.player << Player(),
          AS.received_card << ReceivedCard(),
          TEST(lambda player, received_card: player['name'] == received_card['player']),
          )
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

    # Grupo de Maos
    @Rule(AS.player << Player(group=0),
          TEST(lambda player: lambda_group_1(player)))
    def preflop_define_group_1(self, player):
        self.modify(player, group=1)

    @Rule(AS.player << Player(group=0),
          TEST(lambda player: lambda_group_2(player)))
    def preflop_define_group_2(self, player):
        self.modify(player, group=2)

    @Rule(AS.player << Player(group=0),
          TEST(lambda player: lambda_group_3(player)))
    def preflop_define_group_3(self, player):
        self.modify(player, group=3)

    @Rule(AS.player << Player(group=0),
          TEST(lambda player: lambda_group_4(player)))
    def preflop_define_group_4(self, player):
        self.modify(player, group=4)

    @Rule(AS.player << Player(group=0),
          TEST(lambda player: lambda_group_5(player)))
    def preflop_define_group_5(self, player):
        self.modify(player, group=5)

    @Rule(AS.player << Player(group=0),
          TEST(lambda player: lambda_group_6(player)))
    def preflop_define_group_6(self, player):
        self.modify(player, group=6)

    @Rule(AS.player << Player(group=0),
          TEST(lambda player: lambda_group_7(player)))
    def preflop_define_group_7(self, player):
        self.modify(player, group=7)

    @Rule(AS.player << Player(group=0),
          TEST(lambda player: lambda_group_8(player)))
    def preflop_define_group_8(self, player):
        self.modify(player, group=8)

    @Rule(AS.player << Player(group=0),
          TEST(lambda player: not lambda_group_1(player)),
          TEST(lambda player: not lambda_group_2(player)),
          TEST(lambda player: not lambda_group_3(player)),
          TEST(lambda player: not lambda_group_4(player)),
          TEST(lambda player: not lambda_group_5(player)),
          TEST(lambda player: not lambda_group_6(player)),
          TEST(lambda player: not lambda_group_7(player)),
          TEST(lambda player: not lambda_group_8(player)))
    def preflop_define_group_9(self, player):
        self.modify(player, group=9)

    # Regras Pre Flop
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

    @Rule(AS.action << Action(street='PREFLOP', me=True, act=1, is_raised=False),
          AS.player << Player(me=True),
          TEST(lambda player: player['group'] == 5),
          TEST(lambda action: action['position'] == 'MP2' or
                              action['position'] == 'HJ' or
                              action['position'] == 'CO' or
                              action['position'] == 'BTN' or
                              action['position'] == 'SB'))
    def preflop_group_5_raise(self):
        self.declare(Suggestion(street='PREFLOP', message='Aumentar a aposta'))

    @Rule(AS.action << Action(street='PREFLOP', me=True, act=1, is_raised=False),
          AS.player << Player(me=True),
          TEST(lambda player: player['group'] == 5),
          TEST(lambda action: action['position'] == 'MP1' or
                              action['position'] == 'UTG+1' or
                              action['position'] == 'UTG' or
                              action['position'] == 'BB'))
    def preflop_group_5_fold(self):
        self.declare(Suggestion(street='PREFLOP', message='Desistir da mão'))

    @Rule(AS.action << Action(street='PREFLOP', me=True, act=1, is_raised=False),
          AS.player << Player(me=True),
          TEST(lambda player: player['group'] == 6),
          TEST(lambda action: action['position'] == 'HJ' or
                              action['position'] == 'CO' or
                              action['position'] == 'BTN'))
    def preflop_group_6_raise(self):
        self.declare(Suggestion(street='PREFLOP', message='Aumentar a aposta'))

    @Rule(AS.action << Action(street='PREFLOP', me=True, act=1, is_raised=False),
          AS.player << Player(me=True),
          TEST(lambda player: player['group'] == 6),
          TEST(lambda action: action['position'] == 'MP1' or
                              action['position'] == 'MP2' or
                              action['position'] == 'UTG+1' or
                              action['position'] == 'UTG' or
                              action['position'] == 'SB' or
                              action['position'] == 'BB'))
    def preflop_group_6_fold(self):
        self.declare(Suggestion(street='PREFLOP', message='Desistir da mão'))

    @Rule(AS.action << Action(street='PREFLOP', me=True, act=1, is_raised=False),
          AS.player << Player(me=True),
          TEST(lambda player: player['group'] == 7),
          TEST(lambda action: action['position'] == 'HJ' or
                              action['position'] == 'CO' or
                              action['position'] == 'BTN'))
    def preflop_group_7_raise(self):
        self.declare(Suggestion(street='PREFLOP', message='Aumentar a aposta'))

    @Rule(AS.action << Action(street='PREFLOP', me=True, act=1, is_raised=False),
          AS.player << Player(me=True),
          TEST(lambda player: player['group'] == 7),
          TEST(lambda action: action['position'] == 'MP1' or
                              action['position'] == 'MP2' or
                              action['position'] == 'UTG+1' or
                              action['position'] == 'UTG' or
                              action['position'] == 'SB' or
                              action['position'] == 'BB'))
    def preflop_group_7_fold(self):
        self.declare(Suggestion(street='PREFLOP', message='Desistir da mão'))

    @Rule(AS.action << Action(street='PREFLOP', me=True, act=1, is_raised=False),
          AS.player << Player(me=True),
          TEST(lambda player: player['group'] == 8),
          TEST(lambda action: action['position'] == 'BTN'))
    def preflop_group_8_raise(self):
        self.declare(Suggestion(street='PREFLOP', message='Aumentar a aposta'))

    @Rule(AS.action << Action(street='PREFLOP', me=True, act=1, is_raised=False),
          AS.player << Player(me=True),
          TEST(lambda player: player['group'] == 8),
          TEST(lambda action: action['position'] == 'MP1' or
                              action['position'] == 'MP2' or
                              action['position'] == 'UTG+1' or
                              action['position'] == 'UTG' or
                              action['position'] == 'HJ' or
                              action['position'] == 'CO' or
                              action['position'] == 'SB' or
                              action['position'] == 'BB'))
    def preflop_group_8_fold(self):
        self.declare(Suggestion(street='PREFLOP', message='Desistir da mão'))

    @Rule(AS.action << Action(street='PREFLOP', me=True, act=1, is_raised=False),
          AS.player << Player(me=True),
          TEST(lambda player: player['group'] == 9),)
    def preflop_group_9_fold(self):
        self.declare(Suggestion(street='PREFLOP', message='Desistir da mão'))

    @Rule(AS.action << Action(street='FLOP', me=True, act=1, is_raised=False),
          AS.player << Player(me=True),
          TEST(lambda player: player['group'] == 1 or player['group'] == 2))
    def flop_group_1_2(self):
        self.declare(Suggestion(street='FLOP', message='Aumentar a aposta'))

    @Rule(AS.action << Action(street='FLOP', me=True, act=1, is_raised=True),
          AS.player << Player(me=True),
          TEST(lambda player: player['group'] == 1 or player['group'] == 2))
    def flop_group_1_2_raised(self):
        self.declare(Suggestion(street='FLOP', message='Pagar a aposta'))

    @Rule(AS.action << Action(street='FLOP', me=True, act=1, is_raised=False),
          AS.player << Player(me=True),
          TEST(lambda player: player['group'] > 4), TEST(lambda action:  action['position'] == 'BTN'))
    def flop_blef_btn(self):
        self.declare(Suggestion(street='FLOP', message='Blefe - Aposte 0.7 do POT para roubar os blinds'))

    # Outras Regras

    @Rule(AS.player << Player(bbs=None), AS.blind << Blind())
    def set_player_big_blinds(self, player, blind):
        self.modify(player, bbs=player['chips']/blind['big'])

    @Rule(AS.table << Table(cards_str=None))
    def set_table_cards_string(self, table):
        self.modify(table, cards_str=''.join(["{}{} ".format(card['value'], card['suit']) for card in table['cards']]))

    @Rule(AS.game << GameSummary(bbs=None), AS.blind << Blind())
    def set_summary_bbs(self, game, blind):
        self.modify(game, bbs=game['pot']/blind['big'])

    @Rule(AS.action << Action(street='PREFLOP', me=True, act=1))
    def set_street_position_message_preflop(self, action):
        self.declare(Suggestion(street='PREFLOP', message='Posição atual {}'.format(action['position'])))

    @Rule(AS.action << Action(street='FLOP', me=True, act=1))
    def set_street_position_message_flop(self, action):
        self.declare(Suggestion(street='FLOP', message='Posição atual {}'.format(action['position'])))
