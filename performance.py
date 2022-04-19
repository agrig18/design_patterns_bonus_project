from dataclasses import dataclass
from typing import Protocol


class Performance(Protocol):
    required_energy: int
    uses_energy: int
    charm: int

    def perform(self) -> None:
        pass

    def calculate_charm(self) -> int:
        pass


@dataclass
class Sing:
    required_energy: int
    uses_energy: int
    charm: int

    def perform(self) -> None:
        # print("I am singing")
        pass

    def calculate_charm(self) -> int:
        return self.charm


@dataclass
class Dance:
    required_energy: int
    uses_energy: int
    charm: int

    def perform(self) -> None:
        # print("I am dancing")
        pass

    def calculate_charm(self) -> int:
        return self.charm


class Instrument:
    required_energy: int
    uses_energy: int
    charm: int

    def perform(self) -> None:
        pass

    def calculate_charm(self) -> int:
        pass

    def get_sound(self) -> None:
        pass

    def __hash__(self):
        return sum(
            hash(obj) for obj in [self.required_energy, self.uses_energy, self.charm]
        )


@dataclass
class Horn(Instrument):
    required_energy: int
    uses_energy: int
    charm: int

    def perform(self) -> None:
        # print("I am playing horn")
        pass

    def calculate_charm(self) -> int:
        return self.charm

    def get_sound(self) -> None:
        pass


@dataclass
class Maraca(Instrument):
    required_energy: int
    uses_energy: int
    charm: int

    def perform(self) -> None:
        # print("I am playing maraca")
        pass

    def calculate_charm(self) -> int:
        return self.charm

    def get_sound(self) -> None:
        pass


@dataclass
class Didgeridoo(Instrument):
    required_energy: int
    uses_energy: int
    charm: int

    def perform(self) -> None:
        # print("I am playing didgeridoo")
        pass

    def calculate_charm(self) -> int:
        return self.charm

    def get_sound(self) -> None:
        pass
