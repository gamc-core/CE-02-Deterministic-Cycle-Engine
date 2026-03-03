# CE-02 — Deterministic Cycle Engine

Minimal deterministic structural cycle over JSON structural units..

No creation.
No mutation.
No optimization.

---

## What It Does

CE-02:
	•	Reads frozen structural cells from CE01.
	•	Evaluates a quantitative threshold.
	•	Creates cycle_closed.json when threshold is reached.
	•	Maintains irreversible closure within the current execution context.

---

## What It Is Not
	•	Database
	•	Monitoring system
	•	Adaptive controller
	•	AI engine
	•	Workflow automation tool

---

## Requirements

Python 3.9+
No external dependencies.

---

## Usage

From project root:

python ce02.py

Behavior
	•	If total cells < threshold → returns STABLE
	•	If total cells ≥ threshold → creates cycle_closed.json
	•	If cycle is closed → returns CYCLE_CLOSED

Edit config.json to define:

- threshold
- storage_path(directory containing.json files)

Ensure the directory defined in storage_path exists and contains .json files before execution.

---

See CONTRACT.md for formal definition.

License: MIT