from dataclasses import dataclass

from .config import IDSConfig
from .rules import FrequencyTracker, has_malicious_payload, is_unauthorized_id


@dataclass(frozen=True)
class CANFrame:
    arbitration_id: int
    data: bytes
    timestamp: float


@dataclass(frozen=True)
class DetectionEvent:
    rule: str
    arbitration_id: int
    timestamp: float
    details: str


class CANIDSDetector:
    def __init__(self, config: IDSConfig | None = None) -> None:
        self.config = config or IDSConfig()
        self._frequency_tracker = FrequencyTracker(self.config.sliding_window_seconds)

    def evaluate(self, frame: CANFrame) -> list[DetectionEvent]:
        events: list[DetectionEvent] = []

        if is_unauthorized_id(frame, self.config):
            events.append(
                DetectionEvent(
                    rule="unauthorized_id",
                    arbitration_id=frame.arbitration_id,
                    timestamp=frame.timestamp,
                    details=f"CAN ID 0x{frame.arbitration_id:X} is not in allow-list",
                )
            )

        if self._frequency_tracker.is_abnormal(frame, self.config):
            events.append(
                DetectionEvent(
                    rule="abnormal_frequency",
                    arbitration_id=frame.arbitration_id,
                    timestamp=frame.timestamp,
                    details=f"CAN ID 0x{frame.arbitration_id:X} exceeded expected message rate",
                )
            )

        if has_malicious_payload(frame, self.config):
            events.append(
                DetectionEvent(
                    rule="malicious_payload",
                    arbitration_id=frame.arbitration_id,
                    timestamp=frame.timestamp,
                    details=f"CAN ID 0x{frame.arbitration_id:X} payload matched malicious signature",
                )
            )

        return events
