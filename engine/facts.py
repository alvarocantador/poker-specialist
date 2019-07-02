from pyknow import *


class UserInput(Fact):
    tournamentId = Field(int, default=0)
    playerName = Field(str, default='')
    is_ok = Field(bool, default=False)


class Tournament(Fact):
    id = Field(int, default=0)


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
    group = Field(int)
