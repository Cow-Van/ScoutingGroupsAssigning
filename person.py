from dataclasses import dataclass


@dataclass
class Person:
    first_name: str
    last_name: str
    prefs: list[str]

    def __init__(self, first_name: str, last_name: str, prefs: str) -> None:
        self.first_name = first_name
        self.last_name = last_name
        self.prefs = [pref for pref in prefs.split(", ") if pref != ""]
    
    def __str__(self) -> str:
        return f"{self.first_name} {self.last_name}"
    
    def __repr__(self) -> str:
        return self.__str__()