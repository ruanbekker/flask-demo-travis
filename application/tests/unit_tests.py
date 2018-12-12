from types import StringType

word = 'foobar'

def dummy_test_string_type():
    assert type(word) is StringType

def dummy_test_string_value():
    assert (word) == 'foobar'
