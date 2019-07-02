from pyknow import *
from engine.facts import *


class PokerInference(KnowledgeEngine):

    @DefFacts()
    def _initial_action(self):
        yield UserInput()
        yield Tournament()

    @Rule(AS.user_input << UserInput(tournamentId=0))
    def ask_tournament_id(self, user_input):
        self.modify(user_input, tournamentId=int(input("Qual o ID do torneio? ")))

    @Rule(AS.user_input << UserInput(playerName=''))
    def ask_player_name(self, user_input):
        self.modify(user_input, playerName=input("Qual o nickname do jogador? "))

    @Rule(AS.user_input << UserInput(is_ok=False),
          NOT(UserInput(tournamentId=0)),
          NOT(UserInput(playerName='')),
          AS.player << Player(),
          AS.tournament << Tournament(),
          TEST(lambda user_input, tournament: tournament['id'] == user_input['tournamentId']),
          TEST(lambda user_input, player: player['name'] == user_input['playerName']))
    def test_tournament_and_player(self, user_input, tournament, player):
        self.modify(user_input, is_ok=True)
        print("Torneio e jogador encontrados. Iniciando analise das mãos.")

    @Rule(AS.user_input << UserInput(is_ok=False),
          NOT(UserInput(tournamentId=0)),
          AS.tournament << Tournament(),
          TEST(lambda user_input, tournament: tournament['id'] != user_input['tournamentId']))
    def test_tournament_id(self, user_input, tournament):
        print("{0} {1}".format(tournament['id'], user_input['tournamentId']))
        self.modify(user_input, tournamentId=0, is_ok=False)
        print("Torneio não encontrado.")

    @Rule(AS.user_input << UserInput(is_ok=False),
          NOT(UserInput(playerName='')),
          AS.player << Player(),
          TEST(lambda user_input, player: player['name'] != user_input['playerName']))
    def test_player_name(self, user_input):
        self.modify(user_input, playerName='', is_ok=False)
        print("Jogador não encontrado.")

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
engine.declare(Player(name='AlyCWB', chips=1500, seat=1),
               Blind(small=10, big=20),
               Tournament(id=1),)
               # ReceivedCard(player='AlyCWB', cards=[])
engine.run()
