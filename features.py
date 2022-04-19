from dataclasses import dataclass, field
from typing import Protocol


class IFeature(Protocol):
    charm: int

    def calculate_charm(self) -> int:
        pass


@dataclass
class Tail:
    charm: int = field(default_factory=int)

    def calculate_charm(self) -> int:
        return self.charm

    def __hash__(self):
        return hash(self.charm)


class Fur:
    charm: int

    def set_charm(self, charm: int) -> None:
        self.charm = charm

    def calculate_charm(self) -> int:
        pass


@dataclass
class RegularFur(Fur):
    charm: int = field(default_factory=int)

    def calculate_charm(self) -> int:
        return self.charm

    def __hash__(self):
        return hash(self.charm)


@dataclass
class StrippedFur(Fur):
    charm: int = field(default_factory=int)

    def calculate_charm(self) -> int:
        return 3 * self.charm

    def __hash__(self):
        return hash(self.charm)


@dataclass
class DottedFur(Fur):
    charm: int = field(default_factory=int)

    def calculate_charm(self) -> int:
        return 5 * self.charm

    def __hash__(self):
        return hash(self.charm)
