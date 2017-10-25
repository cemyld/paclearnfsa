import random
def random_string(alphabet,length=1):
    return ''.join(random.choice(tuple(alphabet)) for _ in range(length))

def get_positive_input(fsa, length):
    rand_str = random_string(fsa.alphabet, length)
    if fsa.recognizes(rand_str):
        return rand_str
    return get_positive_input(fsa, length)
def get_negative_input(fsa, length):
    rand_str = random_string(fsa.alphabet, length)
    if not fsa.recognizes(rand_str):
        return rand_str
    return get_negative_input(fsa, length)
