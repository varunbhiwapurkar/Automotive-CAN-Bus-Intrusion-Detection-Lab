from collections import defaultdict, deque
from typing import TYPE_CHECKING

from .config import IDSConfig

if TYPE_CHECKING:
    from .detector import CANFrame


def is_unauthorized_id(frame: "CANFrame", config: IDSConfig) -> bool:
    return frame.arbitration_id not in config.allowed_ids


def has_malicious_payload(frame: "CANFrame", config: IDSConfig) -> bool:
    payload = frame.data
    return any(signature in payload for signature in config.malicious_payload_signatures)


class FrequencyTracker:
    def __init__(self, window_seconds: float) -> None:
        self.window_seconds = window_seconds
        self._timestamps: dict[int, deque[float]] = defaultdict(deque)

    def is_abnormal(self, frame: "CANFrame", config: IDSConfig) -> bool:
        threshold = config.max_frequency_hz.get(frame.arbitration_id)
        if threshold is None:
            return False

        timestamps = self._timestamps[frame.arbitration_id]
        timestamps.append(frame.timestamp)
        cutoff = frame.timestamp - self.window_seconds
        while timestamps and timestamps[0] < cutoff:
            timestamps.popleft()

        current_rate = len(timestamps) / self.window_seconds
        return current_rate > threshold
