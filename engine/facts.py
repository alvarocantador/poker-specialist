from pyknow import *

class Blind(Fact):
    small = Field(int,mandatory=True)
    big = Field(int,mandatory=True)

class Hand(Fact):
    number = Field(int,mandatory=True)
