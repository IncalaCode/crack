import re

stri = "What is the capital of France? a) Paris b) Berlin c)london What is the capital of France? a) Paris b) Berlin c)london"

question_word_list = [
    "what", "where", "when", "how", "why", "who", "which", "whom", "whose", 
    "whither", "whence", "whenceforth", "did", "do", "does", "have", "has", "am", 
    "is", "are", "can", "could", "may", "would", "will", "should", "must",
    "didn't", "doesn't", "haven't", "isn't", "aren't", "can't", "couldn't",
    "wouldn't", "won't", "shouldn't", "?"
]

class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_end_of_word = False

class Trie:
    def __init__(self):
        self.root = TrieNode()
    
    def insert(self, word):
        node = self.root
        for char in word:
            if char not in node.children:
                node.children[char] = TrieNode()
            node = node.children[char]
        node.is_end_of_word = True
    
    def search(self, word):
        node = self.root
        for char in word:
            if char not in node.children:
                return False
            node = node.children[char]
        return node is not None and node.is_end_of_word


class q_c:

    def set_question(self, question):
        self.question = question

    def set_choice(self, choice):
        self.choice = choice

    def get_question(self, question):
        return self.question

    def get_choice(self, choice):
        return self.choice




def input():
    for word in question_word_list:
         trie.insert(word)

input()

q_c_list = []

while stri != "":
    if part := re.split(fr"[{ any(
        word in question_word_list for word in stri
    )}][\.\?]\s*", stri, 1):
        obj_qc = q_c()
        obj_qc.set_question(part[0])
        if part := re.split(r"\s*([a-z])\)\s*", part[1], 1):
            obj_qc.set_choice(part[0])
        else:
            obj_qc.set_choice("")
    q_c_list.append(obj_qc)

    if len(part) < 0:
        stri = part[1]
    else:
        stri = ""
