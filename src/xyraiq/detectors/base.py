# src/xyraiq/detectors/base.py
from abc import ABC, abstractmethod
class Detector(ABC):
    name: str
    @abstractmethod
    def run(self, transcript: list[dict]) -> int:
        """Return count of failures for this detector."""
