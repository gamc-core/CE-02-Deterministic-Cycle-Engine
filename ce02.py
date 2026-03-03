#!/usr/bin/env python3

import os
import json
import sys
from datetime import datetime

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

CONFIG_FILE = os.path.join(BASE_DIR, "config.json")
CYCLE_FILE = os.path.join(BASE_DIR, "cycle_closed.json")


def fail(message):
    print("ERROR:", message)
    sys.exit(1)


def load_config():
    if not os.path.exists(CONFIG_FILE):
        fail("Missing config.json")

    try:
        with open(CONFIG_FILE, "r") as f:
            config = json.load(f)
    except Exception:
        fail("Invalid JSON in config.json")

    if "threshold" not in config:
        fail("Missing 'threshold' in config.json")

    if "storage_path" not in config:
        fail("Missing 'storage_path' in config.json")

    if not isinstance(config["threshold"], int):
        fail("'threshold' must be integer")

    return config


def count_cells(storage_path):
    if not os.path.exists(storage_path):
        fail("Storage path not found")

    return len([
        f for f in os.listdir(storage_path)
        if f.endswith(".json")
    ])


def close_cycle(total, threshold):
    data = {
        "closed": True,
        "closed_at": datetime.utcnow().isoformat() + "Z",
        "final_total": total,
        "threshold": threshold
    }

    with open(CYCLE_FILE, "w") as f:
        json.dump(data, f, indent=2)

    print("CYCLE CLOSED")


def evaluate():
    # Si ya existe cierre, no reevalúa
    if os.path.exists(CYCLE_FILE):
        print("Status: CYCLE_CLOSED")
        return

    config = load_config()
    threshold = config["threshold"]
    storage_path = config["storage_path"]

    total = count_cells(storage_path)

    if total >= threshold:
        close_cycle(total, threshold)
    else:
        print("Total cells:", total)
        print("Threshold:", threshold)
        print("Status: STABLE")


if __name__ == "__main__":
    evaluate()