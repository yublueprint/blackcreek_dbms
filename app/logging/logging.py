import datetime
import os

class Logger:
    def __init__(self, filename="app.log", max_bytes=1024*1024, backup_count=3):
        self.filename = filename
        self.max_bytes = max_bytes
        self.backup_count = backup_count

    def log(self, message):
        self._rotate_if_needed()
        timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        with open(self.filename, "a") as f:
            f.write(f"[{timestamp}] {message}\n")

    def _rotate_if_needed(self):
        if os.path.exists(self.filename) and os.path.getsize(self.filename) >= self.max_bytes:
            for i in range(self.backup_count, 0, -1):
                backup_file = f"{self.filename}.{i}"
                prev_file = f"{self.filename}.{i-1}" if i > 1 else self.filename
                if os.path.exists(prev_file):
                    os.rename(prev_file, backup_file)