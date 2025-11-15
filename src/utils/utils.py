import os
from config import PARENT_PATH


def load_envs():
    env_path = os.path.join(PARENT_PATH, ".env")
    with open(env_path, "r") as f:
        for line in f:
            line = line.strip()
            if line and not line.startswith("#") and "=" in line:
                key, value = line.split("=", 1)
                value = value.strip().strip('"').strip("'")
                print(f"export {key}='{value}'")
