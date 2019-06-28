import os
import settings
import logging

logging.basicConfig(level=os.getenv("LOG_LEVEL"))
logging.info("Poker Specialist v{}".format(os.getenv("VERSION")))
logging.debug("Hand history at {}".format(os.getenv("HAND_HISTORY_PATH")))

from dsl.hands import *
from dsl.parser import *

histories = read_all_tournaments()
[run(history) for history in histories]

