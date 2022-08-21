import pickle
import json
from abc import ABC, abstractmethod
from typing import Any
from pathlib import Path

import yaml
import joblib

from musicalbum import MusicAlbum

class Serializer(ABC):

    @abstractmethod
    def dump(self, obj : Any, save_path : Path) -> None:
        pass

    @abstractmethod
    def load(self, load_path: Path) -> Any:
        pass

class PickleSerializer(Serializer):

    def __init__(self, protocol: int = 5, encoding:str = "ASCII") -> None:
        self.protocol = protocol
        self.encoding = encoding

    def dump(self, obj: Any, save_path: Path) -> None:
        with open(save_path, "wb") as file:
            pickle.dump(obj, file, protocol=self.protocol)

    def load(self, load_path: Path) -> Any:
        with open(load_path, "rb") as file:
            return pickle.load(file, encoding=self.encoding)


class JsonSerializer(Serializer):

    def __init__(self, sort_keys :bool = True, indent :int = 4):
        self.sort_keys = sort_keys
        self.indent = indent

    def dump(self, obj: Any, save_path: Path) -> None:
        with open(save_path, "w") as file:
            json.dump(obj, file, sort_keys=self.sort_keys, indent=self.indent)

    def load(self, load_path: Path) -> Any:
        with open(load_path, "rb") as file:
            return json.load(file)

class YamlSerializer(Serializer):

    def __init__(self, default_flow_style:bool = False) -> None:
        self.default_flow_style = default_flow_style


    def dump(self, obj: Any, save_path: Path) -> None:
        with open(save_path, "w") as file:
            yaml.dump(obj, file, default_flow_style=self.default_flow_style)

    def load(self, load_path: Path) -> Any:
        with open(load_path, "r") as file:
            return yaml.safe_load(file)

class JoblibSerializer(Serializer):

    def __init__(self, pickle_protocol:int = 5) -> None:
        self.pickle_protocol = pickle_protocol

    def dump(self, obj: Any, save_path: Path) -> None:
        joblib.dump(obj, save_path, protocol=self.pickle_protocol)

    def load(self, load_path: Path) -> Any:
        return joblib.load(load_path)

if __name__ == "__main__":
    params = {
        "title":"The Wall",
        "artist":"Pink Floyd",
        "year":1979,
        "songs":["ABiTW1", "ABiTW2"]
    }

    the_wall = MusicAlbum(**params)
    the_wall_dict = the_wall.dict()
    print(the_wall_dict)
    path = Path("the_wall.joblib")

    joblib_serializer = JoblibSerializer()
    joblib_serializer.dump(the_wall, path)
    the_wall_2 = joblib_serializer.load(path)
    print(the_wall_2)