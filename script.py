print("=== System Health Checker ===")

DISK_THRESHOLD = int(input("Disk alert threshold % (example 85): "))
run_logs = input("Check logs? (y/n): ").strip().lower() == "y"
run_disk = input("Check disk? (y/n): ").strip().lower() == "y"
run_svc = input("Check services? (y/n): ").strip().lower() == "y"

#---- Initialize counters (always defined)-----
issues_found = 0
errors = 0
warnings = 0
disk_alerts= 0
stopped = 0

# -------------- LOG CHECK ----------------
if run_logs:
  print("\n-- Log Check --")
  log_file = "app.log"

  try:
      with open(log_file) as f:
        for line in f:
            line = line.strip()
            if "ERROR" in line:
                errors += 1
                print("🚨", line)
            elif "WARNING" in line:
                warnings += 1
                print("⚠️", line)

  except FileNotFoundError:
    print("❌ Missing file:", log_file)

  print("log Errors:", errors)
  print("Log Warnings:", warnings)
  issues_found += errors + warnings

# ------------- DISK CHECK -------------
if run_disk:
  print("\n-- Disk Check --")
  disk_file = "df.txt"
 
  try:
      with open(disk_file) as f:
        lines = f.read().strip().split("\n")

      for line in lines[1:]: #skip header
        parts = line.split()
        fs = parts[0]
        use = int(parts[1].replace("%", ""))

        if use >= DISK_THRESHOLD:
         disk_alerts += 1
         print("🚨 DISK HIGH:", fs, use, "%")

  except FileNotFoundError:
   print("❌ Missing file:", disk_file)

  print("Disk Alerts:", disk_alerts)
  issues_found += disk_alerts

# ------------ SERVICE CHECK -----------
if run_svc:
    print("\n-- Service Check --")
    svc_file = "services.txt"
  
    try:
      with open(svc_file) as f:
          for line in f:
              line = line.strip()
              if not line:
                continue

              name, status = line.split()
              if status.lower() != "running":
                stopped += 1
                print("⚠️ SERVICE DOWN:", name, status)
               
    except FileNotFoundError:
      print("❌ Missing file:", svc_file)

print("Stopped Services:", stopped)
issues_found += stopped

# --------------- Overall -----------------
print("\n=== Overall Status ===")
if issues_found == 0:
  print("✅ HEALTHY")
else:
  print("🚨 ATTENTION NEEDED - issues found:", issues_found)
