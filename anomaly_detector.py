import json

with open("examples/sample_validation.json") as f:
    result = json.load(f)

failed = result["statistics"]["unsuccessful_expectations"]
total = result["statistics"]["evaluated_expectations"]

failure_rate = failed / total

if failure_rate > 0.3:
    severity = "HIGH"
elif failure_rate > 0.1:
    severity = "MEDIUM"
else:
    severity = "LOW"

print("Evaluated Expectations:", total)
print("Failed Expectations:", failed)
print(f"Failure Rate: {failure_rate:.2%}")
print("Severity:", severity)
