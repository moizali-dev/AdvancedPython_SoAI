import pickle
from abc import ABC, abstractmethod
from typing import Any
from pathlib import Path

class Animal(ABC):

    @abstractmethod
    def make_sound(self) -> None:
        pass

    @property
    @abstractmethod
    def number_of_legs(self) -> int:
        pass

class Dog(Animal):

    def make_sound(self) -> None:
        print("woof!")

    @property
    def number_of_legs(self) -> int:
        return 4

if __name__ == "__main__":
    doggo = Dog()
    print(doggo.make_sound)
    doggo.make_sound()