# System Health Checker (Python CLI)

A lightweight Python command-line tool that simulates common DevOps / sysadmin health checks by scanning:
- application logs for **ERROR** and **WARNING**
- disk usage output against a configurable **threshold**
- service status listings for **stopped** services

The tool prints a structured report with an overall status summary.

---

## What it Checks

### ✅ Log Check (`app.log`)
- Counts ERROR and WARNING lines
- Prints flagged entries with clear markers

### ✅ Disk Check (`df.txt`)
- Parses filesystem usage percentages
- Alerts when usage is **>= threshold**

### ✅ Service Check (`services.txt`)
- Flags services not in `running` state
- Counts stopped services

---

## Files Included

- `script.py` — main CLI tool
- `app.log` — sample log file
- `df.txt` — sample disk report
- `services.txt` — sample services status list

---

## How to Run

From the repo directory:

```bash
python script.py

Follow the prompts:
disk threshold %
run logs? (y/n)
run disk? (y/n)
run services? (y/n)

--------EXAMPLE OUTPUT------------

=== System Health Checker ===
-- Log Check --
🚨 ERROR db connection failed
⚠️ WARNING memory high

-- Disk Check --
🚨 DISK HIGH: /dev/sdc1 88 %

-- Service Check --
⚠️ SERVICE DOWN: postgres stopped

=== Overall Status ===
🚨 ATTENTION NEEDED — issues found: 6
