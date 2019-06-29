import os
import settings
import logging
from pyknow import *


logging.basicConfig(level=logging.FATAL)
logging.info("Poker Specialist v{}".format(os.getenv("VERSION")))
logging.debug("Hand history at {}".format(os.getenv("HAND_HISTORY_PATH")))

from dsl.hands import *
from dsl.parser import *
from dsl.semantic import *

from engine.main import *
histories = read_all_tournaments()
engine = PokerInference()
engine.reset()

for history in histories: # enumerable
    semantic = PokerSemantic(engine=engine)
    for hand in interpret(history, semantic=semantic): # enumerable
        engine.run()
        engine.reset()