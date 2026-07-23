import unittest

from src.can_ids.config import IDSConfig
from src.can_ids.detector import CANFrame, CANIDSDetector


class DetectorTests(unittest.TestCase):
    def test_detects_unauthorized_id(self) -> None:
        detector = CANIDSDetector(IDSConfig(allowed_ids={0x100}))
        frame = CANFrame(arbitration_id=0x123, data=b"\x00\x01", timestamp=1.0)

        events = detector.evaluate(frame)

        self.assertTrue(any(event.rule == "unauthorized_id" for event in events))

    def test_detects_abnormal_frequency(self) -> None:
        config = IDSConfig(allowed_ids={0x100}, max_frequency_hz={0x100: 2.0}, sliding_window_seconds=1.0)
        detector = CANIDSDetector(config)

        frames = [
            CANFrame(arbitration_id=0x100, data=b"\x00", timestamp=1.0),
            CANFrame(arbitration_id=0x100, data=b"\x00", timestamp=1.2),
            CANFrame(arbitration_id=0x100, data=b"\x00", timestamp=1.3),
        ]

        all_events = [event for frame in frames for event in detector.evaluate(frame)]

        self.assertTrue(any(event.rule == "abnormal_frequency" for event in all_events))

    def test_detects_malicious_payload(self) -> None:
        config = IDSConfig(allowed_ids={0x100}, malicious_payload_signatures=(b"\xde\xad",))
        detector = CANIDSDetector(config)
        frame = CANFrame(arbitration_id=0x100, data=b"\x00\xde\xad\x01", timestamp=2.0)

        events = detector.evaluate(frame)

        self.assertTrue(any(event.rule == "malicious_payload" for event in events))


if __name__ == "__main__":
    unittest.main()
