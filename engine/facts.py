from pyknow import *


class UserInput(Fact):
    gameId = Field(str, default='')
    playerName = Field(str, default='')
    is_ok = Field(bool, default=False)


class Game(Fact):
    id = Field(str, mandatory=True)
    type = Field(str, mandatory=True) # TOURNAMENT
    modality = Field(str, mandatory=True) # NLH
    players_for_table = Field(int, default=None)


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


class Action(Fact):
    street = Field(str, mandatory=True)  # PREFLOP | FLOP | TURN | RIVER
    group = Field(int, mandatory=True)
    position = Field(str, mandatory=True)  # SB | BB | UTG | UTG+1 | MP1 | MP2 | HJ | CO | BNT

