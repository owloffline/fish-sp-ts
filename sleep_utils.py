import random
import time


def sleep_rand(min_seconds, max_seconds):
    # Generate a random duration between min_seconds and max_seconds
    sleep_duration = random.uniform(min_seconds, max_seconds)
    
    # Sleep for the generated duration
    time.sleep(sleep_duration)