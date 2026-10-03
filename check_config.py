import json
from pathlib import Path


settings_path = Path("local.settings.json")

with settings_path.open("r", encoding="utf-8") as file:
    settings = json.load(file)

connection_string = settings["Values"]["SQL_CONNECTION_STRING"]

parts = {}

for item in connection_string.split(";"):
    if "=" in item:
        key, value = item.split("=", 1)
        parts[key.strip().lower()] = value.strip()

print("Driver:", parts.get("driver"))
print("Server:", parts.get("server"))
print("Database:", parts.get("database"))
print("UID:", repr(parts.get("uid")))
print("PWD configured:", bool(parts.get("pwd")))
print("Encrypt:", parts.get("encrypt"))
print("TrustServerCertificate:", parts.get("trustservercertificate"))