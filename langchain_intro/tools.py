import random
import time


def get_current_wait_time(hospital: str) -> int | str:
    """Dummy function to simulate getting current wait times."""

    if hospital not in ["A", "B", "C", "D"]:
        return f"Hospital {hospital} not found."

    time.sleep(1)

    return random.randint(0, 10000)
