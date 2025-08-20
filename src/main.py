import sys, requests
print("Hello, CODEX!")
print("Python:", sys.version)
print("HTTP 200?:", requests.get("https://httpbin.org/get").status_code == 200)
