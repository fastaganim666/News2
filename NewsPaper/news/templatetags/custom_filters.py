from django import template


register = template.Library()

STOP_WORDS = ("Новый", "новый", 'Пост', 'пост')

@register.filter()
def censor(text):
    for word in STOP_WORDS:
        text = text.replace(word, word[0] + ('*' * (len(word) - 1)))
    return f'{text}'