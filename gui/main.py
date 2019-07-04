from engine.main import *


class PokerConsole:

    def plot(self, engine=PokerInference()):
        suggestions = []
        me = None
        hand = None
        for fact in engine.facts.items():
            current_fact = fact[1].as_dict()
            if isinstance(fact[1], Suggestion):
                suggestions.append(current_fact)
            if isinstance(fact[1], Hand):
                hand = current_fact
            if isinstance(fact[1], Player):
                if 'me' in current_fact: 
                    me = current_fact

        if(hand == None):
            return

        # PRINT
        print("=====================================")
        print("Hand: {}".format(hand['id']))
        print("Player: {}".format(me['name']))
        print("Blinds: {}".format(me['bbs']))
        print("Seat: {}".format(me['seat']))
        print("")
        print("SUGGESTIONS:")
        for suggestion in suggestions:
            print(suggestion['message'])