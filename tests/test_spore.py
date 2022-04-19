import random

from constants import *
from features import *
from spore import Guest, GuestTribe, IGuest


def test_tail_feature_charm_1():
    guest = Guest()
    guest.add_feature(Tail(charm=3))
    assert guest.get_features_charm() == 3


def test_tails_feature_charm():
    guest = Guest()
    tail = Tail(charm=3)
    for x in range(1, 100):
        guest.add_feature(tail)
        assert guest.get_features_charm() == 3 * x


def add_tail_regular_features(guest: IGuest):
    tail = Tail(charm=3)

    num_tail = 10

    for x in range(num_tail):
        guest.add_feature(tail)

    cur_charm = num_tail * tail.calculate_charm()

    fur = RegularFur()
    fur.set_charm(cur_charm)
    guest.add_feature(fur)


def test_tail_regular_features_charm():
    guest = Guest()
    add_tail_regular_features(guest)
    assert guest.get_features_charm() == 60


def add_tail_stripped_features(guest: IGuest):
    tail = Tail(charm=3)

    num_tail = 10

    for x in range(num_tail):
        guest.add_feature(tail)

    cur_charm = num_tail * tail.calculate_charm()

    fur = StrippedFur()
    fur.set_charm(cur_charm)
    guest.add_feature(fur)


def test_tail_stripped_features_charm():
    guest = Guest()
    add_tail_stripped_features(guest)
    assert guest.get_features_charm() == 120


def add_tail_dotted_features(guest: IGuest):
    tail = Tail(charm=3)

    num_tail = 10

    for x in range(num_tail):
        guest.add_feature(tail)

    cur_charm = num_tail * tail.calculate_charm()

    fur = DottedFur()
    fur.set_charm(cur_charm)
    guest.add_feature(fur)


def test_tail_dotted_features_charm():
    guest = Guest()
    add_tail_dotted_features(guest)

    assert guest.get_features_charm() == 180


def test_guest_energy():
    guest = Guest(energy=20)

    assert guest.get_energy() == 20

    for i in range(0, 20):
        assert guest.has_enough_energy(i)

    for i in range(1, 20):
        guest.decrease_energy(1)
        assert guest.get_energy() == 20 - i


def add_features(guest: IGuest) -> None:
    tail = Tail(charm=3)
    num_tail = 4

    for x in range(num_tail):
        guest.add_feature(tail)

    cur_charm = num_tail * tail.calculate_charm()

    fur = random.choice(furs)()
    fur.set_charm(cur_charm)
    guest.add_feature(fur)


def add_guests() -> list[IGuest]:
    guests = []
    guest1 = Guest(energy=10,
                   performance=performances[0])
    add_tail_stripped_features(guest1)
    guests.append(guest1)
    guest2 = Guest(energy=5, performance=performances[1])
    add_tail_dotted_features(guest2)
    guests.append(guest2)
    return guests


def test_guest_tribe_charm():
    guests = add_guests()
    guest_tribe = GuestTribe(guests)
    assert guest_tribe.get_energy() == 15
    assert guest_tribe.get_total_charm() == 304
