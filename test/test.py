from datetime import datetime, timezone                                
local_time = datetime.now(timezone.utc).astimezone()
print(local_time.isoformat())