"""Funções para manipular."""

def count_vowels(word):
    """Função para contar vogais."""
    resp = 0
    vowels = ['a','e','i','o','u']
    for char in word:
        if char in vowels:
            resp = resp + 1
    return resp

def order(words_arr, order_option):
    """Função para ordenar palavras."""
    reverse = order_option == "desc"
    words_arr.sort(reverse=reverse)
    return words_arr
