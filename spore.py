import random
from dataclasses import dataclass, field
from functools import cached_property
from typing import List, Protocol

from constants import *
from performance import *


class IChoosePerformance(Protocol):
    def choose(self, performances_list: List[Performance]) -> Performance:
        pass


class RandomlyChoosePerformance:
    def choose(self, performances_list: List[Performance]) -> Performance:
        return random.choice(performances_list)


class IGuest(Protocol):
    def add_feature(self, feature: IFeature) -> None:
        pass

    def get_total_charm(self) -> int:
        pass

    def get_energy(self) -> int:
        pass

    def has_enough_energy(self, required_energy: int) -> bool:
        pass

    def decrease_energy(self, energy_loss: int) -> None:
        pass

    def select_performance(self, instruments: List[Instrument]) -> None:
        pass

    def get_performance(self) -> Performance:
        pass

    def perform(self) -> None:
        pass


class IHost(Protocol):
    def set_composure(self, composure: int) -> None:
        pass

    def get_total_composure(self) -> int:
        pass

    def decrease_composure(self, charm: int) -> None:
        pass


class IDistributeCharm(Protocol):
    def distribute(self, num_hosts: int) -> List[int]:
        pass


class RandomlyDistributeCharm:
    def distribute(self, num_hosts: int) -> List[int]:
        composures = []
        random_host = random.randint(1, num_hosts)
        for i in range(1, num_hosts + 1):
            if i == random_host:
                composure = random.randint(300, 700)
            else:
                composure = 0
            composures.append(composure)
        return composures


class EquallyDistributeCharm:
    def distribute(self, num_hosts: int) -> List[int]:
        pass


class IApplyFeatures(Protocol):
    def apply(self, guest: IGuest) -> None:
        pass


class RandomlyApplyFeatures:
    def apply(self, guest: IGuest) -> None:
        tail = Tail(charm=3)
        num_tail = random.randint(1, 5)

        for x in range(num_tail):
            guest.add_feature(tail)
        cur_charm = num_tail * tail.calculate_charm()

        fur = random.choice(furs)()
        fur.set_charm(cur_charm)
        guest.add_feature(fur)


@dataclass
class Guest:
    energy: int = field(default_factory=int)
    features: dict = field(
        default_factory=dict
    )  # mapping from IFeature to int (count of a particular feature)
    choose_performance: IChoosePerformance = None
    apply_features: IApplyFeatures = None
    performance: Performance = None

    def add_feature(self, feature: IFeature) -> None:
        self.features.setdefault(feature, 0)
        self.features[feature] += 1

    def add_features(self) -> None:
        self.apply_features.apply(self)

    # @cached_property
    def get_features_charm(self) -> int:
        return sum(
            self.features.get(feature) * feature.calculate_charm()
            for feature in self.features
        )

    def get_total_charm(self) -> int:
        if self.performance is not None:
            return self.get_features_charm() + self.performance.charm
        return self.get_features_charm()

    def get_energy(self) -> int:
        return self.energy

    def has_enough_energy(self, required_energy: int) -> bool:
        return self.energy > required_energy

    def decrease_energy(self, energy_loss: int) -> None:
        self.energy = self.energy - energy_loss

    def select_performance(self, instruments: List[Instrument]) -> None:
        while True:
            if self.get_energy() == 0:
                self.performance = None
                break
            self.performance = self.choose_performance.choose(performances)
            if self.has_enough_energy(self.performance.required_energy):
                if (not isinstance(self.performance, Instrument)) or (
                        self.performance in instruments
                ):
                    break

    def get_performance(self) -> Performance:
        return self.performance

    def perform(self) -> None:
        if self.performance is not None:
            self.performance.perform()
            self.decrease_energy(self.performance.uses_energy)


@dataclass
class GuestTribe:
    guests: list[IGuest] = field(default_factory=list)
    instruments: list = field(default_factory=list)

    def add_guest(self, guest: IGuest) -> None:
        self.guests.append(guest)

    def add_instrument(self, instrument: Instrument) -> None:
        self.instruments.append(instrument)

    def get_total_charm(self) -> int:
        return sum(guest.get_total_charm() for guest in self.guests)

    def get_energy(self) -> int:
        return sum(guest.get_energy() for guest in self.guests)

    def has_enough_energy(self, required_energy: int) -> bool:
        return all(guest.has_enough_energy(required_energy) for guest in self.guests)

    def select_performances(self) -> None:
        instruments_left = self.instruments.copy()
        for guest in self.guests:
            guest.select_performance(instruments_left)
            if guest.get_performance() in instruments:
                instruments_left.remove(guest.get_performance())

    def perform(self) -> None:
        for guest in self.guests:
            guest.perform()


@dataclass
class Host:
    composure: int = field(default_factory=int)

    def set_composure(self, composure: int) -> None:
        self.composure = composure

    def get_total_composure(self) -> int:
        return self.composure

    def decrease_composure(self, charm: int) -> None:
        self.composure = self.composure - charm


@dataclass
class HostTribe:
    hosts: list[IHost] = field(default_factory=list)
    distribution: IDistributeCharm = field(default_factory=IDistributeCharm)

    def add_host(self, host: IHost) -> None:
        self.hosts.append(host)

    def get_total_composure(self) -> int:
        return sum(host.get_total_composure() for host in self.hosts)

    def distribute_composure(self) -> None:
        num_hosts = len(self.hosts)
        composures = self.distribution.distribute(num_hosts)
        for i in range(num_hosts):
            self.hosts[i].set_composure(composures[i])

    def shake_composure(self, emitted_charm: int) -> None:
        left = emitted_charm
        for host in self.hosts:
            if left <= host.get_total_composure():
                host.decrease_composure(left)
                left = 0
            else:
                left -= host.get_total_composure()
                host.set_composure(0)
