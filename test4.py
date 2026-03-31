from datetime import datetime, timezone

s="2026-03-28 03:04:23+00:00"

dt=datetime.fromisoformat(s)
timestamp = dt.timestamp()

td=datetime.now(timezone.utc)
timestamp2 = td.timestamp()

print(f"in hours: {int((timestamp2 - timestamp)/60/60)}")
