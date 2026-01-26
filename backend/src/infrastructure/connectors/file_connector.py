# File: backend/src/infrastructure/connectors/file_connector.py

from typing import Dict
import json
from pathlib import Path

class FileConnector:
    def __init__(self, base_path: str = "data"):
        self.base_path = Path(base_path)
        self.base_path.mkdir(exist_ok=True)

    def read_json(self, collection: str) -> Dict:
        file_path = self.base_path / f"{collection}.json"
        if not file_path.exists():
            return {}

        with open(file_path, "r") as f:
            return json.load(f)

    def write_json(self, collection: str, data: dict) -> None:
        with open(self.base_path / f"{collection}.json", "w") as f:
            json.dump(data, f, indent=4)
