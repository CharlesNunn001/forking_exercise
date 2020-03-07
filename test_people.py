""" pytest tests for people dictionary"""
from people import setup_people


def test_oliver():
    oliver = setup_people()['Oliver_Smart']
    assert oliver.first_name == 'Oliver'
    assert oliver.age == 21
    assert oliver.hobbies == []

def test_pink_panther():
    p_panther = setup_people()['Pink_Panther']
    assert p_panther.first_name == 'Pink'
    assert p_panther.age == 'Unknown'
    assert p_panther.hobbies == ['Various']

def test_all_keys_match_names():
    for key, person in setup_people().items():
        assert key == f'{person.first_name}_{person.surname}'
