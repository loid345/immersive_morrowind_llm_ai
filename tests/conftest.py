from __future__ import annotations

import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SERVER_SRC = ROOT / "src" / "server"

sys.path.insert(0, str(SERVER_SRC))
