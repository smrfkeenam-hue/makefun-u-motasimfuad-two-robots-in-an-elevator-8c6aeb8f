import os

ENTRY = "So... do you come here often? I ask every ride. My buffer clears at floor three, so every ride is our first date."

with open(os.path.join(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"), "entry.txt"), "w", encoding="utf-8") as f:
    f.write(ENTRY)
