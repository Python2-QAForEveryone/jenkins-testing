import random
import string


def generate_random_string(number_of_symbols):
    return ''.join(random.choices(string.ascii_letters, k=number_of_symbols))


def generate_random_int(number_of_symbols):
    return ''.join(random.choices(string.digits, k=number_of_symbols))


def generate_random_string_and_int(number_of_symbols):
    return ''.join(random.choices(string.ascii_letters + string.digits, k=number_of_symbols))


def generate_random_special_symbol(number_of_symbols):
    return ''.join(random.choices(string.punctuation, k=number_of_symbols))
