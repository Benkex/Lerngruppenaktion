
from dataclasses import dataclass
from typing import Any, Union


@dataclass
class Color:
    red: int
    green: int
    blue: int
 
    def __post__init__(self):
        if 0 <= self.red <= 255:
            raise ValueError
        elif 0 <= self.green <= 255:
            raise ValueError
        elif 0 <= self.blue <= 255:
            raise ValueError
 
        self.var_dict: dict[str, int] = {"red": self.red, "green": self.green, "blue": self.blue}
 
    def __str__(self) -> str:
        return f"Color with RGB = ({self.red}, {self.green}, {self.blue})"
 
    def add(self, other: Any) -> "Color":
        match other:
            case Color():
                r_new: int = (self.red + other.red if self.red + other.red <= 255 else 255)
                g_new: int = (self.green + other.green if self.green + other.green <= 255 else 255) 
                b_new: int = (self.blue + other.blue if self.blue + other.blue <= 255 else 255) 
                return Color(r_new, g_new, b_new)
            case int():
                r_new: int = (self.red + other if self.red + other <= 255 else 255)
                g_new: int = (self.green + other if self.green + other <= 255 else 255)
                b_new: int = (self.blue + other if self.blue + other <= 255 else 255)
                return Color(r_new, g_new, b_new)
            case _:
                raise TypeError
                
    def __add__(self, other) -> "Color":
        return self.add(other)
 
    def __radd__(self, other) -> "Color":
        return self.add(other)
 
    def get_brightness(self) -> float:
        return (0.2126 * self.red + 0.7152 * self.green + 0.0722 * self.blue)
 
    def __lt__(self, other: Union["Color", float]) -> bool:
        return (self.get_brightness() < other.get_brightness() if isinstance(other, Color) else self.get_brightness() < other)
 
    def __eq__(self, other: Union["Color", float]) -> bool:
        return (self.get_brightness() == other.get_brightness() if isinstance(other, Color) else self.get_brightness() == other)
 
    def __gt__(self, other: Union["Color", float]) -> bool:
        return (self.get_brightness() > other.get_brightness() if isinstance(other, Color) else self.get_brightness() > other)
 
    def __pos__(self):
        return Color(self.red, self.green, self.blue)

    def __neg__(self):
        return Color(255 - self.red, 255 - self.green, 255 - self.blue)
 
    def __getitem__(self, i: str) -> int:
        try:
            return self.var_dict[i]
        except KeyError:
            return "not valid"
 
    def colorMap(self, f) -> "Color":
        return Color(f(self.red), f(self.green), f(self.blue))
 
    def map_add(self, i: int) -> "Color":
        return self.colorMap(lambda x: (i + x if x + i <= 255 else 255))
 
    def map_neg(self) -> "Color":
        return self.colorMap(lambda x: 255 - x)
