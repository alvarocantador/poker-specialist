from engine.main import *


class PokerConsole:

    def plot(self, engine=PokerInference()):
        suggestions = []
        me = None
        hand = None
        table = None
        summary = None

        for fact in engine.facts.items():
            current_fact = fact[1].as_dict()
            if isinstance(fact[1], Suggestion):
                suggestions.append(current_fact)
            if isinstance(fact[1], Hand):
                hand = current_fact
            if isinstance(fact[1], Table):
                table = current_fact
            if isinstance(fact[1], GameSummary):
                summary = current_fact
            if isinstance(fact[1], Player):
                if 'me' in current_fact: 
                    me = current_fact

        if(hand == None):
            return

        # PRINT
        print("=====================================")
        print("Hand: {}".format(hand['id']))
        bbs = me['bbs'] or ''
        print("Player: {} | Blinds: {}".format(me['name'], bbs))
        print("Seat: {} | Group: {}".format(me['seat'], me['group']))
        print("")
        print("CARDS {}{}, {}{}".format(me['cards'][0]['value'], me['cards'][0]['suit'], me['cards'][1]['value'], me['cards'][1]['suit']))
        print("BOARD: {}".format(table['cards_str']))
        print("")
        print("TOTAL POT -> {} BB'S | {} CHIPS".format(summary['bbs'],summary['pot']))
        print("")
        print("SUGGESTIONS:")
        print("* PREFLOP:")
        [print("# -> {}".format(suggestion['message']) ) for suggestion in (suggestions) if suggestion['street'] == 'PREFLOP']
        print("")        
        print("* FLOP:")
        [print("-> " + suggestion['message']) for suggestion in suggestions if suggestion['street'] == 'FLOP']