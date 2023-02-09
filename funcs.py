def count_vowels(word):
    resp = 0
    vowels = ['a','e','i','o','u']
    for c in word:
        if c in vowels:
            resp = resp + 1
    return resp

def order(input, order):
    reverse = order == "desc"
    input.sort(reverse=reverse)
    return input
