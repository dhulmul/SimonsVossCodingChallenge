from fuzzywuzzy import fuzz
import re


def _is_partial_match(query_text, field_text):
    return query_text in field_text


def _is_full_match(query_text, field_text):
    my_regex = r"\b(?=\w)" + re.escape(query_text) + r"\b(?!\w)"
    if re.search(my_regex, field_text, re.IGNORECASE):
        return True
    return False


def _get_fuzzy_ratio(query_text, field_text):
    return fuzz.ratio(query_text, field_text)


def get_match_score(query_text, field_text):
    if _is_full_match(query_text, field_text):
        return 10
    elif _is_partial_match(query_text, field_text):
        return 1
    else:
        return _get_fuzzy_ratio(query_text, field_text)/100.0


print(get_match_score('head', 'heds office'))
# print('head' in 'head office')
# print(fuzz.ratio('head', 'headdfdf office'))
# print('head' in 'headdfdf office')