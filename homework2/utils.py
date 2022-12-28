import random
import string


def get_random_string(k=10):
    l = random.choices(string.ascii_uppercase, k=k)
    return "".join(l)
