import os
from lark import Lark
import logging
from dsl.semantic import PokerSemantic
from dsl.hands import read_tournament

logging.debug("Loading language syntax")
language = Lark.open('./dsl/poker.lark')
logging.debug("Finished loading language syntax")


def run(hand_history, semantic=PokerSemantic()):
    hands = hand_history.split("\n\n\n")
    tress = [ language.parse(hand) for hand in hands ]
    [ semantic.transform(tree) for tree in tress ]