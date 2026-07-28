# Replay Attack

## Objective

Demonstrate a CAN replay attack using previously captured legitimate traffic.

## Procedure

1. Captured legitimate CAN traffic using:

```bash
candump -L vcan0 > replay_left_indicator.log
```

2. Generated normal left indicator activity using the ICSim control panel.

3. Replayed the captured traffic using:

```bash
canplayer -I replay_left_indicator.log
```

## Result

The left indicator blinked without using the legitimate control panel.

## Observation

The replayed CAN traffic was accepted by the simulator because the CAN protocol does not provide built-in message freshness or replay protection.