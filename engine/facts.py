from pyknow import *


class Blind(Fact):
    small = Field(int, mandatory=True)
    big = Field(int, mandatory=True)


class Hand(Fact):
    id = Field(int, mandatory=True)

# Player(name, chips, BB's, cards?, suited=None, me=true/false, group?, seat)


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
