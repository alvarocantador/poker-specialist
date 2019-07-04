from engine.main import *
from gui.main import *
from dsl.semantic import *
from dsl.parser import *
from dsl.hands import *
import os
import settings
import logging
from pyknow import *


logging.basicConfig(level=logging.FATAL)
logging.info("Poker Specialist v{}".format(os.getenv("VERSION")))
logging.debug("Hand history at {}".format(os.getenv("HAND_HISTORY_PATH")))


histories = read_all_tournaments()
engine = PokerInference()
engine.reset()

gui = PokerConsole()
semantic = PokerSemantic(engine=engine)

for history in histories:  # enumerable
    for hand in interpret(history, semantic=semantic):  # enumerable
        engine.run()
        gui.plot(engine)
        engine.reset()
        input()
