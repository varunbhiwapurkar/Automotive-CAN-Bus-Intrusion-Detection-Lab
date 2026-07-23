# Automotive CAN Bus Intrusion Detection & Attack Simulation Lab

This repository provides a hands-on automotive cybersecurity lab to simulate and monitor CAN traffic on Linux using SocketCAN (`vcan0`), ICSim, `can-utils`, Wireshark, and a Python-based Intrusion Detection System (IDS).

## Lab Goals

- Simulate a vehicle CAN environment with `vcan0` and ICSim
- Capture and inspect CAN frames in Wireshark
- Emulate common CAN attacks:
  - Spoofing
  - Replay
  - Denial of Service (DoS/flooding)
- Detect anomalies with Python IDS rules:
  - Unauthorized CAN IDs
  - Abnormal message frequency
  - Malicious payload signatures
- Map detection/response outcomes to ISO/SAE 21434 and UNECE R155 controls

## Repository Structure

```text
.
├── attacks/
│   ├── dos_attack.py
│   ├── replay_attack.py
│   └── spoof_attack.py
├── diagrams/
│   └── can-lab-architecture.mmd
├── docs/
│   ├── architecture.md
│   └── standards_mapping.md
├── logs/
│   └── .gitkeep
├── screenshots/
│   └── .gitkeep
├── scripts/
│   ├── capture_can.sh
│   ├── run_icsim.sh
│   └── setup_vcan.sh
├── src/
│   └── can_ids/
│       ├── __init__.py
│       ├── config.py
│       ├── detector.py
│       ├── monitor.py
│       └── rules.py
├── tests/
│   └── test_detector.py
└── requirements.txt
```

## Prerequisites

- Linux host with SocketCAN support
- Python 3.10+
- `can-utils`
- `Wireshark`
- `ICSim` (from https://github.com/zombieCraig/ICSim)

## Quick Start

### 1. Install Python dependencies

```bash
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

### 2. Create virtual CAN interface

```bash
bash /home/runner/work/Automotive-Cybersecurity-Project/Automotive-Cybersecurity-Project/scripts/setup_vcan.sh
```

### 3. Start ICSim (optional if installed)

```bash
bash /home/runner/work/Automotive-Cybersecurity-Project/Automotive-Cybersecurity-Project/scripts/run_icsim.sh
```

### 4. Start IDS monitor

```bash
python -m src.can_ids.monitor --channel vcan0 --log /home/runner/work/Automotive-Cybersecurity-Project/Automotive-Cybersecurity-Project/logs/ids_alerts.log
```

### 5. Simulate attacks

```bash
python /home/runner/work/Automotive-Cybersecurity-Project/Automotive-Cybersecurity-Project/attacks/spoof_attack.py
python /home/runner/work/Automotive-Cybersecurity-Project/Automotive-Cybersecurity-Project/attacks/replay_attack.py
python /home/runner/work/Automotive-Cybersecurity-Project/Automotive-Cybersecurity-Project/attacks/dos_attack.py
```

### 6. Capture traffic in Wireshark

Use `vcan0` as capture interface, or run:

```bash
bash /home/runner/work/Automotive-Cybersecurity-Project/Automotive-Cybersecurity-Project/scripts/capture_can.sh
```

## IDS Detection Rules

- `unauthorized_id`: CAN ID not in approved list
- `abnormal_frequency`: frame rate exceeds ID-specific threshold
- `malicious_payload`: payload matches known malicious signatures

Thresholds and signatures are configurable in `src/can_ids/config.py`.

## Standards Alignment

See:

- `/home/runner/work/Automotive-Cybersecurity-Project/Automotive-Cybersecurity-Project/docs/architecture.md`
- `/home/runner/work/Automotive-Cybersecurity-Project/Automotive-Cybersecurity-Project/docs/standards_mapping.md`

## Future Enhancements

- React/Node.js dashboard for live IDS telemetry
- C-based hardened ECU simulation with message authentication
