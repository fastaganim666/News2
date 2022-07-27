from django import template


register = template.Library()

STOP_WORDS = ("Новый", "новый")

@register.filter()
def stop_words(text):
    for word in STOP_WORDS:
        text = text.replace(word, word[0] + ('*' * (len(word) - 1)))
    return f'{text}'