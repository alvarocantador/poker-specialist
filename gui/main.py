from engine.main import *

class PokerConsole:

    def plot(self, engine=PokerInference()):
        suggestions = []
        for i in range(len(engine.facts)):
            if isinstance(engine.facts[i], Suggestion):
                suggestions.append(engine.facts[i].as_dict())
        print(suggestions)

