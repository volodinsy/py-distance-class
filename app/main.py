from __future__ import annotations


class Distance:

    def __init__(self, km: (int, float)) -> None:
        self.km = km

    def __str__(self) -> str:
        return f"Distance: {self.km} kilometers."

    def __repr__(self) -> str:
        return f"Distance(km={self.km})"

    def __add__(self, distance1: (Distance, int, float)) -> Distance:
        if isinstance(distance1, Distance):
            total_dictance = self.km + distance1.km
        else:
            total_dictance = self.km + distance1
        return Distance(total_dictance)

    def __iadd__(self, other: (Distance, int, float)) -> Distance:
        if isinstance(other, Distance):
            self.km += other.km
            return self
        else:
            self.km += other
            return self

    def __mul__(self, other: (int, float)) -> Distance:
        return Distance(self.km * other)

    def __truediv__(self, other: int) -> Distance:
        return Distance(round((self.km / other), 2))

    def __lt__(self, other: (Distance, int, float)) -> bool:
        if isinstance(other, Distance):
            return self.km < other.km
        return self.km < other

    def __gt__(self, other: (Distance, int, float)) -> bool:
        if isinstance(other, Distance):
            return self.km > other.km
        return self.km > other

    def __eq__(self, other: (Distance, int, float)) -> bool:
        return self.km == other

    def __le__(self, other: (Distance, int, float)) -> bool:
        return self.km <= other

    def __ge__(self, other: (Distance, int, float)) -> bool:
        return self.km >= other
