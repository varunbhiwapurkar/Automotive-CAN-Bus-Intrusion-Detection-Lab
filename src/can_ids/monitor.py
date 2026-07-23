import argparse
import logging

import can

from .detector import CANFrame, CANIDSDetector


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="CAN IDS monitor")
    parser.add_argument("--channel", default="vcan0", help="SocketCAN interface (default: vcan0)")
    parser.add_argument("--bustype", default="socketcan", help="python-can bus type (default: socketcan)")
    parser.add_argument("--log", default="logs/ids_alerts.log", help="Path to IDS alert log file")
    return parser.parse_args()


def setup_logger(log_path: str) -> logging.Logger:
    logger = logging.getLogger("can_ids")
    logger.setLevel(logging.INFO)
    logger.handlers.clear()

    stream_handler = logging.StreamHandler()
    file_handler = logging.FileHandler(log_path)

    formatter = logging.Formatter("%(asctime)s %(levelname)s %(message)s")
    stream_handler.setFormatter(formatter)
    file_handler.setFormatter(formatter)

    logger.addHandler(stream_handler)
    logger.addHandler(file_handler)
    return logger


def run() -> None:
    args = parse_args()
    logger = setup_logger(args.log)
    detector = CANIDSDetector()

    logger.info("Starting CAN IDS monitor on channel=%s bustype=%s", args.channel, args.bustype)

    with can.Bus(channel=args.channel, interface=args.bustype) as bus:
        for msg in bus:
            frame = CANFrame(arbitration_id=msg.arbitration_id, data=bytes(msg.data), timestamp=msg.timestamp)
            events = detector.evaluate(frame)
            for event in events:
                logger.warning("%s id=0x%X details=%s", event.rule, event.arbitration_id, event.details)


if __name__ == "__main__":
    run()
