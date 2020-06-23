import random
import wordlist
import re

E_PREFIX_RATE = 0.25
COMPANY = 'Amazon'

# in place Fisher Yates algorithm
def _shuffleArray(passed_list):

    for i in range(len(passed_list)):
        j = random.randint(i, len(passed_list) - 1)
        # swap
        t = passed_list[i]
        passed_list[i] = passed_list[j]
        passed_list[j] = t

    return passed_list


def _get_replacement(type_of_match):

    if type_of_match == 'noun':
        idx = random.randint(0, len(wordlist.noun) - 1)
        shuffled_list = _shuffleArray(wordlist.noun)
        random_noun = shuffled_list[idx]
        # give noun an e-prefix based on E_PREFIX_RATE
        if (random.random() < E_PREFIX_RATE) and random_noun[:2] != 'e-':
            random_noun = 'e-' + random_noun

        return random_noun

    elif type_of_match == 'verb':
        idx = random.randint(0, len(wordlist.verb) - 1)
        shuffled_list = _shuffleArray(wordlist.verb)
        random_verb = shuffled_list[idx]
        return random_verb

    elif type_of_match == 'adjective':
        idx = random.randint(0, len(wordlist.adjective) - 1)
        shuffled_list = _shuffleArray(wordlist.adjective)
        random_adjective = shuffled_list[idx]
        return random_adjective

    elif type_of_match == 'comapny':
        # make user provide it 
        return COMPANY

    else:
        # type is terminal
        if random.random() < 0.5:
            random_terminal = '.'
        else:
            random_terminal = '!'

        return random_terminal


def _getWord(data):
    regex = r"""\{[-_a-z]+?\}"""
    matches = re.finditer(regex, data, re.IGNORECASE | re.VERBOSE)
    match_list = [i.group() for i in matches]
    replacement_list = []
    for match in match_list:
        type_of_match = match[1:-1]
        replacement_list.append(_get_replacement(type_of_match))

    for i in range(len(match_list)):
        data = data.replace(str(match_list[i]), replacement_list[i])

    return data


def getName():

    idx_first = random.randint(0, len(wordlist.first_name) - 1)
    idx_last = random.randint(0, len(wordlist.last_name) - 1)
    shuffled_first = _shuffleArray(wordlist.first_name)
    shuffled_last = _shuffleArray(wordlist.last_name)

    return f'{shuffled_first[idx_first]} {shuffled_last[idx_last]}'


def 


