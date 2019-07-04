from pyknow import *

class Blind(Fact):
    small = Field(int, mandatory=True)
    big = Field(int, mandatory=True)


class Hand(Fact):
    id = Field(int, mandatory=True)


class ReceivedCard(Fact):
    player = Field(str, mandatory=True)
    cards = Field(list)


class Player(Fact):
    name = Field(str, mandatory=True)
    chips = Field(int, mandatory=True)
    seat = Field(int, mandatory=True)
    is_out = Field(bool)
    bbs = Field(float, default=None)
    cards = Field(list)
    suited = Field(bool)
    me = Field(bool)
    group = Field(int, default=None)  # 1, 2, 3, 4, 5, 6, 7 or 8
    card_1_v = Field(int, default=0)  # 1 ao 13 -> A, 2, 3... Q, K
    card_1_s = Field(str)  # c, h, s, d
    card_2_v = Field(int, default=0)  # 1 ao 13 -> A, 2, 3... Q, K
    card_2_s = Field(str)  # c, h, s, d


class Action(Fact):
    id = Field(int, mandatory=True)
    type = Field(str, mandatory=True)
    player = Field(str, mandatory=True)
    street = Field(str, mandatory=True)  # PREFLOP | FLOP | TURN | RIVER
    position = Field(str)  # SB | BB | UTG | UTG+1 | MP1 | MP2 | HJ | CO | BNT
    is_raised = Field(bool, mandatory=True, default=False)
    me = Field(bool, mandatory=True)


class Suggestion(Fact):
    street = Field(str, mandatory=True)  # PREFLOP | FLOP | TURN | RIVER
    message = Field(str, mandatory=True)

class Table(Fact):
    cards_str = Field(str, default=None)
    cards = Field(list)


class GameSummary():
    pot=Field(int, mandatory=True)
    bbs = Field(float, default=None)
