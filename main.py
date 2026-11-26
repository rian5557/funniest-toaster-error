import os

MESSAGE = "ERROR: Crumb tray full. So is my patience. Please empty one of us."
OUTPUT_PATH = os.path.join("/output", "entry.txt")


def render_message():
    # The whole entry is this one line, exactly as the toaster would show it.
    return MESSAGE.strip()


def main():
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8") as f:
        f.write(render_message() + "\n")


if __name__ == "__main__":
    main()
