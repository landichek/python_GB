"""Пользователь вводит текст(строка). Словом считается
последовательность непробельных символов идущих
подряд, слова разделены одним или большим числом
пробелов. Определите, сколько различных слов
содержится в этом тексте."""

text = input().split()
unique_words = set()
for word in text:
    unique_words.add(word.lower())
print(len(unique_words))

#Вариант 2:
print(len(set(text.lower())))