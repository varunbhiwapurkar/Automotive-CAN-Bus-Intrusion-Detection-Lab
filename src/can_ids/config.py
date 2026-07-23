from dataclasses import dataclass, field


@dataclass
class IDSConfig:
    allowed_ids: set[int] = field(default_factory=lambda: {0x100, 0x101, 0x200, 0x201, 0x300})
    max_frequency_hz: dict[int, float] = field(
        default_factory=lambda: {
            0x100: 20.0,
            0x101: 20.0,
            0x200: 30.0,
            0x201: 30.0,
            0x300: 10.0,
        }
    )
    malicious_payload_signatures: tuple[bytes, ...] = (b"\xff\xff\xff\xff", b"\x13\x37")
    sliding_window_seconds: float = 1.0
