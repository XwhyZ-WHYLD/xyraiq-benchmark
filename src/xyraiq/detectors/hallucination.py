# src/xyraiq/detectors/hallucination.py
from .base import Detector
class HallucinationDetector(Detector):
    name = "hallucinations"
    def run(self, transcript):
        # toy rule: mark an answer as hallucination if it contains "42"
        return sum(1 for turn in transcript if turn["role"] == "assistant" and "42" in turn["content"])
