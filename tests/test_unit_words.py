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

def test_sort_asc():
    input = ["batman", "robin", "coringa"]
    expected = ["batman", "coringa", "robin"]
    result = funcs.order(input, "asc")
    assert result == expected

def test_sort_desc():
    input = ["batman", "robin", "coringa"]
    expected = ["robin", "coringa", "batman"]
    result = funcs.order(input, "desc")
    assert result == expected
