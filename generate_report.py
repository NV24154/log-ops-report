import json

level_counts = {}
service_counts = {}
error_samples = []

with open("clean_logs_l4.txt", "r", encoding="utf-8") as f:
    for line in f:
        line = line.strip()

        if not line:
            continue

        parts = [p.strip() for p in line.split("|")]
        ts, level, service, msg = parts

        level_counts[level] = level_counts.get(level, 0) + 1

        service_counts[service] = service_counts.get(service, 0) + 1

        if level == "ERROR":
            error_samples.append(line)

summary = {
    "level_counts": level_counts,
    "service_counts": service_counts
}

with open("summary_l4.json", "w", encoding="utf-8") as f:
    json.dump(summary, f, indent=2)

report_text = "INCIDENT MINI-REPORT\n\n"

for level, count in level_counts.items():
    report_text += f"{level}: {count}\n"

report_text += "\nTop services:\n"

for service, count in service_counts.items():
    report_text += f"{service}: {count}\n"

report_text += "\nSample ERROR logs:\n"

for line in error_samples[:5]:
    report_text += f"{line}\n"

with open("incident_report_l4.txt", "w", encoding="utf-8") as f:
    f.write(report_text)

print("Report generated successfully.")
