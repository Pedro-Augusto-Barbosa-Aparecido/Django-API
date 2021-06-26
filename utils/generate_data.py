import random
import string


def generate_slab_number(size=None, initial_format=None):
    if size and initial_format:
        slab = ''.join(random.choice(string.ascii_uppercase + string.digits) for _ in range(size))
        return f'{initial_format}{slab}'
    elif size and not initial_format:
        return ''.join(random.choice(string.ascii_uppercase + string.digits) for _ in range(size))
    else:
        return ''.join(random.choice(string.ascii_uppercase + string.digits) for _ in range(4))
