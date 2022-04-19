from features import *
from performance import *

MAX_INSTRUMENTS = 15
MAX_MEMBERS = 5

furs = [RegularFur, StrippedFur, DottedFur]

instruments = [Horn(40, 2, 4), Maraca(60, 4, 6), Didgeridoo(80, 4, 8)]
performances = [Sing(0, 1, 1), Dance(20, 2, 3)] + instruments
