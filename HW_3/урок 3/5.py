def get_jokes(n):
    import random
    nouns = ["автомобиль", "лес", "огонь", "город", "дом"]
    adverbs = ["сегодня", "вчера", "завтра", "позавчера", "ночью"]
    adjectives = ["веселый", "яркий", "зеленый", "утопичный", "мягкий"]
    list_joke = []
    while n > 0:
        joke = random.choice(nouns) + ' ' + random.choice(adverbs) + ' ' + random.choice(adjectives)
        list_joke.append(joke)
        n = n - 1
    if n == 0:
        joke = random.choice(nouns) + ' ' + random.choice(adverbs) + ' ' + random.choice(adjectives)
        list_joke.append(joke)
    return print(list_joke, ' ')

get_jokes(5)
