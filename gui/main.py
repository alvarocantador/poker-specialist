from engine.main import *


class PokerConsole:

    def plot(self, engine=PokerInference()):
        suggestions = []
        me = None
        hand = None
        table = None

        for fact in engine.facts.items():
            current_fact = fact[1].as_dict()
            if isinstance(fact[1], Suggestion):
                suggestions.append(current_fact)
            if isinstance(fact[1], Hand):
                hand = current_fact
            if isinstance(fact[1], Table):
                table = current_fact
            if isinstance(fact[1], Player):
                if 'me' in current_fact: 
                    me = current_fact

        if(hand == None):
            return

        # PRINT
        print("=====================================")
        print("Hand: {}".format(hand['id']))
        print("Player: {} | Blinds: {}".format(me['name'], me['bbs']))
        print("Seat: {} | Group: {}".format(me['seat'], me['group']))
        print("CARDS {}{}, {}{}".format(me['card_1_v'], me['card_1_s'], me['card_2_v'], me['card_2_s']))
        print("BOARD: {}".format(table['cards_str']))
        print("")
        print("SUGGESTIONS:")
        print("* PREFLOP:")
        [print("# -> {}".format(suggestion['message']) ) for suggestion in (suggestions) if suggestion['street'] == 'PREFLOP']
        print("")        
        print("* FLOP:")
        [print("-> " + suggestion['message']) for suggestion in suggestions if suggestion['street'] == 'FLOP']