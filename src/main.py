import os
import sys

import requests
from dotenv import load_dotenv

load_dotenv()  # .env 로딩


def http_ok() -> bool:
    return requests.get("https://httpbin.org/get", timeout=10).status_code == 200


if __name__ == "__main__":
    print("Hello, CODEX!")
    print("Python:", sys.version)
    print("API_KEY:", os.getenv("API_KEY", "(not set)"))
    print("HTTP 200?:", http_ok())
