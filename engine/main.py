from pyknow import *
from engine.facts import *


class PokerInference(KnowledgeEngine):

    @DefFacts()
    def _initial_action(self):
        yield UserInput()
        # yield Game()

    @Rule(AS.user_input << UserInput(gameId=''))
    def ask_game_id(self, user_input):
        self.modify(user_input, gameId=input("Qual o ID do jogo? "))

    @Rule(AS.user_input << UserInput(playerName=''))
    def ask_player_name(self, user_input):
        self.modify(user_input, playerName=input("Qual o nome do jogador? "))

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

    @Rule(UserInput(is_ok=True),
          Action(street='PREFLOP'))
    def preflop_action(self):
        print("Colocar novas regras aqui.")

    # @Rule(UserInput(is_ok=True),
    #       AS.player << Player(bbs=None), AS.blind << Blind())
    # def set_player_big_blinds(self, player, blind):
    #     self.modify(player, bbs=player['chips']/blind['big'])
    #
    # @Rule(UserInput(is_ok=True),
    #       AS.player << Player(),
    #       AS.received_card << ReceivedCard(),
    #       TEST(lambda player, received_card: player['name'] == received_card['player']))
    # def set_received_cards(self, player, received_card):
    #     f_card, s_card = received_card['cards']
    #     self.modify(player, me=True, cards=received_card['cards'], suited=f_card['suit'] == s_card['suit'])
    #     self.retract(received_card)


# to test
engine = PokerInference()
engine.reset()
engine.declare(Game(id='1', type='TOURNAMENT', modality='NLH', players_for_table=9),
               Player(name='a', chips=1500, seat=1),
               Blind(small=10, big=20),
               Action(street='PREFLOP', group=1, position='BTN'))
# ReceivedCard(player='AlyCWB', cards=[]),

engine.run()
