# CAN ID Map

## Project
Automotive CAN Bus Intrusion Detection & Attack Simulation Lab

## Baseline Capture

- Interface: `vcan0`
- Tool: Wireshark + SocketCAN
- Simulator: ICSim
- Capture Type: Normal vehicle operation

---

## Observations

- Successfully captured CAN traffic from the virtual CAN interface (`vcan0`).
- CAN traffic is continuously transmitted even when no controls are pressed.
- Each CAN frame contains:
  - CAN Identifier (ID)
  - Data Length Code (DLC)
  - Data Payload
- Vehicle actions (acceleration, indicators, locking/unlocking) modify CAN traffic.
- This baseline capture will be used for comparison during attack simulations.

---

## Known CAN IDs


|---------|----------|--------|
| CAN ID | Function | Status |
|---------|----------|--------|
| 0x188 | Left Indicator | Verified |

| TBD | To be identified during attack analysis | Pending |

---

## Notes

The CAN ID mapping will be expanded during the spoofing, replay, and DoS attack phases as message functions are experimentally verified.