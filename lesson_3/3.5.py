from random import choice

def get_jokes (nouns):
    smile = []
    for i in nouns:
        jokes = f'{choice(nouns)} {choice(adverbs)} {choice(adjectives)}'
        smile.append(jokes)
    return smile

nouns = ["автомобиль", "лес", "огонь", "город", "дом"]
adverbs = ["сегодня", "вчера", "завтра", "позавчера", "ночью"]
adjectives = ["веселый", "яркий", "зеленый", "утопичный", "мягкий"]
print(get_jokes (nouns))

