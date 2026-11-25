#!/usr/bin/env python3
"""Charm the Commuter: one line of weather for a city that isn't.

The forecast is fixed text: no clock, no network, no randomness.
The program only checks the line fits the gate, then writes it out.
"""

import os
import sys

# The line, built from its beats so each part can be read on its own.
CITY = "Drizzlemere"
TEMP = "9°C"
SKY = "rain queuing in single file"
BUS = "the 7:42 slips through dry"
KICKER = "the only queue in town that actually moves"

LINE = f"{CITY}: {TEMP}, {SKY}, so {BUS} — {KICKER}"

GATE_MAX = 140
OUT_PATH = "/output/entry.txt"


def gate_ok(line: str) -> str | None:
    """Return the reason the line fails the gate, or None when it passes."""
    if not 1 <= len(line) <= GATE_MAX:
        return f"line is {len(line)} chars, outside 1..{GATE_MAX}"
    if line != line.strip():
        return "line has leading or trailing whitespace"
    if "\n" in line or "\r" in line:
        return "line is not a single line"
    try:
        line.encode("utf-8")
    except UnicodeEncodeError:
        return "line is not encodable as UTF-8"
    return None


def main() -> int:
    problem = gate_ok(LINE)
    if problem is not None:
        print(problem, file=sys.stderr)
        return 1
    os.makedirs(os.path.dirname(OUT_PATH), exist_ok=True)
    with open(OUT_PATH, "w", encoding="utf-8", newline="") as handle:
        handle.write(LINE)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
