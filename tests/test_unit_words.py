import funcs

def test_vowel_count_batman():
    input = "batman"
    vowels = funcs.count_vowels(input)
    assert vowels == 2

def test_vowel_count_robin():
    input = "robin"
    vowels = funcs.count_vowels(input)
    assert vowels == 2

def test_vowel_count_coringa():
    input = "coringa"
    vowels = funcs.count_vowels(input)
    assert vowels == 3
