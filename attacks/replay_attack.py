#!/usr/bin/env python3
import argparse

import can


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Replay CAN traffic from a log")
    parser.add_argument("--log", default="logs/capture.asc", help="Path to candump/can-utils compatible log")
    parser.add_argument("--channel", default="vcan0", help="CAN channel")
    return parser.parse_args()


def main() -> None:
    args = parse_args()
    bus = can.Bus(channel=args.channel, interface="socketcan")

    replayed = 0
    with can.ASCReader(args.log) as reader:
        for msg in reader:
            bus.send(msg)
            replayed += 1

    print(f"Replay complete: sent {replayed} frames from {args.log}")


if __name__ == "__main__":
    main()
