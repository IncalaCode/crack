import re

question_word_list = [
    "what",
    "where",
    "when",
    "how",
    "why",
    "did",
    "do",
    "does",
    "have",
    "has",
    "am",
    "is",
    "are",
    "can",
    "could",
    "may",
    "would",
    "will",
    "should",
    "didn't",
    "doesn't",
    "haven't",
    "isn't",
    "aren't",
    "can't",
    "couldn't",
    "wouldn't",
    "won't",
    "shouldn't",
    "?",
]


class QuestionChoice:
    def __init__(self, question, choices):
        self.question = question
        self.choices = choices


store = QuestionChoice()

stri = "What is the capital of France? a) Paris b) Berlin c)london What is the capital of France? a) Paris b) Berlin c)london"

while stri:
    text_words = stri.split()
    if any(word.lower() in question_word_list for word in text_words):
        question, sep, rest = stri.partition("?")
        choices = re.findall(r"\b[a-z]\b", rest)
        store.question = question.strip()
        store.choices = choices
    stri = rest.strip()

print(store.question)
print(store.choices)
