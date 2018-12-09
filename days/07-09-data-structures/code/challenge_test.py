from challenge import (states, get_every_nth_state,
                       get_longest_state,
                       combine_state_names_and_abbreviations,
                       get_state_abbrev)


def test_get_every_nth_state():

    test_states = ['a', 'b', 'c', 'd', 'e', 'f']

    assert get_every_nth_state(states=test_states, n=3) == ['c', 'f']


def test_get_state_abbrev():

    assert get_state_abbrev(state_name='Alabama') == 'AL'

    assert get_state_abbrev(state_name='Warrshington') == 'N/A'


def test_get_longest_state():

    data = {'Washington': 'WA', 'ThisIsAReallyLongStateName': 'ZZ'}

    assert get_longest_state(data=data) == 'ThisIsAReallyLongStateName'


def test_combine_state_names_and_abbreviations():

    test_dict = {'c': 100, 'b': 2}
    test_list = ['z', 'y']
    test_result = [2, 100, 'y', 'z']

    assert combine_state_names_and_abbreviations(us_state_abbrev=test_dict,
                                                 states=test_list,
                                                 n=2) == test_result
