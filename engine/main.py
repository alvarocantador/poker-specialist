from pyknow import *
from engine.facts import *


class PokerInference(KnowledgeEngine):

    @DefFacts()
    def _initial_action(self):
        yield UserInput()
        # yield Game()

    # region Input Data
    @Rule(AS.user_input << UserInput(gameId=''))
    def ask_game_id(self, user_input):
        self.modify(user_input, gameId='1')
        # self.modify(user_input, gameId=input("Qual o ID do jogo? "))

    @Rule(AS.user_input << UserInput(playerName=''))
    def ask_player_name(self, user_input):
        self.modify(user_input, playerName='AlyCWB')
        # self.modify(user_input, playerName=input("Qual o nome do jogador? "))
    # endregion

    # region Validation Input Data
    @Rule(AS.user_input << UserInput(is_ok=False),
          NOT(UserInput(gameId='')),
          NOT(UserInput(playerName='')),
          Game(type='TOURNAMENT'),
          Game(modality='NLH'),
          Game(players_for_table=9),
          AS.player << Player(),
          AS.game << Game(),
          TEST(lambda user_input, game: game['id'] == user_input['gameId']),
          TEST(lambda user_input, player: player['name'] == user_input['playerName']))
    def test_game_and_player(self, user_input, game, player):
        self.modify(user_input, is_ok=True)
        print("Jogo e jogador encontrados. Iniciando analise das mãos.")

    @Rule(AS.user_input << UserInput(is_ok=False),
          NOT(UserInput(gameId='')),
          AS.game << Game(),
          TEST(lambda user_input, game: game['id'] != user_input['gameId']))
    def test_game_id(self, user_input, game):
        print("{0} {1}".format(game['id'], user_input['gameId']))
        self.modify(user_input, gameId='', is_ok=False)
        print("Jogo não encontrado.")

    @Rule(AS.user_input << UserInput(is_ok=False),
          NOT(UserInput(playerName='')),
          AS.player << Player(),
          TEST(lambda user_input, player: player['name'] != user_input['playerName']))
    def test_player_name(self, user_input):
        self.modify(user_input, playerName='', is_ok=False)
        print("Jogador não encontrado.")

    @Rule(AS.game << Game(),
          NOT(Game(type='TOURNAMENT')),
          NOT(Game(type='')),
          NOT(UserInput(gameId='')),
          NOT(UserInput(playerName='')))
    def test_game_type(self, game):
        self.modify(game, type='', is_ok=False)
        print("O tipo de jogo {0} não pode ser analisado.".format(game['type']))

    @Rule(AS.game << Game(),
          NOT(Game(modality='NLH')),
          NOT(Game(modality='')),
          NOT(UserInput(gameId='')),
          NOT(UserInput(playerName='')))
    def test_game_modality(self, game):
        self.modify(game, modality='', is_ok=False)
        print("A modalidade de jogo {0} não pode ser analisado.".format(game['modality']))

    @Rule(AS.game << Game(),
          NOT(Game(players_for_table=9)),
          NOT(Game(players_for_table=None)),
          NOT(UserInput(gameId='')),
          NOT(UserInput(playerName='')))
    def test_game_players_for_table(self, game):
        self.modify(game, players_for_table=None, is_ok=False)
        print("Somente jogos com 9 jogadores por mesa podem ser analisados.".format(game['modality']))

    # endregion

    # region PREFLOP RULES
    @Rule(UserInput(is_ok=True),
          Action(street='PREFLOP'),
          Action(is_raised=False),
          AS.action << Action(),
          TEST(lambda action: action['group'] == 1 or action['group'] == 2),)
    def preflop_group_1_2(self):
        print("Sugestão de AUMENTAR a aposta!")

    @Rule(UserInput(is_ok=True),
          Action(street='PREFLOP'),
          Action(is_raised=False),
          AS.action << Action(),
          TEST(lambda action: action['group'] == 3),
          TEST(lambda action: action['position'] == 'UTG+1' or
                              action['position'] == 'MP1' or
                              action['position'] == 'MP2' or
                              action['position'] == 'HJ' or
                              action['position'] == 'CO' or
                              action['position'] == 'BTN' or
                              action['position'] == 'SB' or
                              action['position'] == 'BB'))
    def preflop_group_3_raise(self):
        print("Sugestão de AUMENTAR a aposta!")

    @Rule(UserInput(is_ok=True),
          Action(street='PREFLOP'),
          Action(is_raised=False),
          AS.action << Action(),
          TEST(lambda action: action['group'] == 3),
          TEST(lambda action: action['position'] == 'UTG'))
    def preflop_group_3_fold(self):
        print("Sugestão de DESISTIR da mão!")

    @Rule(UserInput(is_ok=True),
          Action(street='PREFLOP'),
          Action(is_raised=False),
          AS.action << Action(),
          TEST(lambda action: action['group'] == 4),
          TEST(lambda action: action['position'] == 'MP1' or
                              action['position'] == 'MP2' or
                              action['position'] == 'HJ' or
                              action['position'] == 'CO' or
                              action['position'] == 'BTN' or
                              action['position'] == 'SB' or
                              action['position'] == 'BB'))
    def preflop_group_4_raise(self):
        print("Sugestão de AUMENTAR a aposta!")

    @Rule(UserInput(is_ok=True),
          Action(street='PREFLOP'),
          Action(is_raised=False),
          AS.action << Action(),
          TEST(lambda action: action['group'] == 4),
          TEST(lambda action: action['position'] == 'UTG+1' or
                              action['position'] == 'UTG'))
    def preflop_group_4_fold(self):
        print("Sugestão de DESISTIR da mão!")

    @Rule(UserInput(is_ok=True),
          Action(street='PREFLOP'),
          Action(is_raised=False),
          AS.action << Action(),
          TEST(lambda action: action['group'] == 5),
          TEST(lambda action: action['position'] == 'MP2' or
                              action['position'] == 'HJ' or
                              action['position'] == 'CO' or
                              action['position'] == 'BTN' or
                              action['position'] == 'SB'))
    def preflop_group_5_raise(self):
        print("Sugestão de AUMENTAR a aposta!")

    @Rule(UserInput(is_ok=True),
          Action(street='PREFLOP'),
          Action(is_raised=False),
          AS.action << Action(),
          TEST(lambda action: action['group'] == 5),
          TEST(lambda action: action['position'] == 'MP1' or
                              action['position'] == 'UTG+1' or
                              action['position'] == 'UTG' or
                              action['position'] == 'BB'))
    def preflop_group_5_fold(self):
        print("Sugestão de DESISTIR da mão!")

    @Rule(UserInput(is_ok=True),
          Action(street='PREFLOP'),
          Action(is_raised=False),
          AS.action << Action(),
          TEST(lambda action: action['group'] == 6),
          TEST(lambda action: action['position'] == 'HJ' or
                              action['position'] == 'CO' or
                              action['position'] == 'BTN'))
    def preflop_group_6_raise(self):
        print("Sugestão de AUMENTAR a aposta!")

    @Rule(UserInput(is_ok=True),
          Action(street='PREFLOP'),
          Action(is_raised=False),
          AS.action << Action(),
          TEST(lambda action: action['group'] == 6),
          TEST(lambda action: action['position'] == 'MP1' or
                              action['position'] == 'MP2' or
                              action['position'] == 'UTG+1' or
                              action['position'] == 'UTG' or
                              action['position'] == 'SB' or
                              action['position'] == 'BB'))
    def preflop_group_6_fold(self):
        print("Sugestão de DESISTIR da mão!")

    @Rule(UserInput(is_ok=True),
          Action(street='PREFLOP'),
          Action(is_raised=False),
          AS.action << Action(),
          TEST(lambda action: action['group'] == 7),
          TEST(lambda action: action['position'] == 'HJ' or
                              action['position'] == 'CO' or
                              action['position'] == 'BTN'))
    def preflop_group_7_raise(self):
        print("Sugestão de AUMENTAR a aposta!")

    @Rule(UserInput(is_ok=True),
          Action(street='PREFLOP'),
          Action(is_raised=False),
          AS.action << Action(),
          TEST(lambda action: action['group'] == 7),
          TEST(lambda action: action['position'] == 'MP1' or
                              action['position'] == 'MP2' or
                              action['position'] == 'UTG+1' or
                              action['position'] == 'UTG' or
                              action['position'] == 'SB' or
                              action['position'] == 'BB'))
    def preflop_group_7_fold(self):
        print("Sugestão de DESISTIR da mão!")


    @Rule(UserInput(is_ok=True),
          Action(street='PREFLOP'),
          Action(is_raised=False),
          AS.action << Action(),
          TEST(lambda action: action['group'] == 8),
          TEST(lambda action: action['position'] == 'BTN'))
    def preflop_group_8_raise(self):
        print("Sugestão de AUMENTAR a aposta!")

    @Rule(UserInput(is_ok=True),
          Action(street='PREFLOP'),
          Action(is_raised=False),
          AS.action << Action(),
          TEST(lambda action: action['group'] == 8),
          TEST(lambda action: action['position'] == 'MP1' or
                              action['position'] == 'MP2' or
                              action['position'] == 'UTG+1' or
                              action['position'] == 'UTG' or
                              action['position'] == 'HJ' or
                              action['position'] == 'CO' or
                              action['position'] == 'SB' or
                              action['position'] == 'BB'))
    def preflop_group_8_fold(self):
        print("Sugestão de DESISTIR da mão!")

    # endregion

    @Rule(UserInput(is_ok=True),
          AS.player << Player(bbs=None), AS.blind << Blind())
    def set_player_big_blinds(self, player, blind):
        self.modify(player, bbs=player['chips']/blind['big'])

    @Rule(UserInput(is_ok=True),
          AS.player << Player(),
          AS.received_card << ReceivedCard(),
          TEST(lambda player, received_card: player['name'] == received_card['player']))
    def set_received_cards(self, player, received_card):
        f_card, s_card = received_card['cards']
        self.modify(player, me=True, cards=received_card['cards'], suited=f_card['suit'] == s_card['suit'])
        self.retract(received_card)


# to test
engine = PokerInference()
engine.reset()
engine.declare(Game(id='1', type='TOURNAMENT', modality='NLH', players_for_table=9),
               Player(name='AlyCWB', chips=1500, seat=1),
               Blind(small=10, big=20),
               Action(street='PREFLOP', group=8, position='BTN', is_raised=False),
               ReceivedCard(player='AlyCWB', cards=[{'value':'A', 'suit':'c'}, {'value':'T', 'suit':'c'}]))

engine.run()
