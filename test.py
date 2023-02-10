import re


with open("data.txt", 'r') as f:
    list = f.readlines()

for i in range(len(list)):
    list[i] = list[i][:-1].lower()


def tokenize(text):
    return re.findall(r'\w+', text.lower())


with open("twitter_comments.txt", 'r') as f:
    sentences = f.readlines()

# sentence = "abbo you abbo-up, boong-witted, scruffy-looking nerfherder!"

for sentence in sentences:
    tokens = tokenize(sentence)
    print(tokens)

    # Rate: number of occurrences normalized by total number
    degree_of_profanity = sum(1 for t in tokens if t in list) / len(tokens)
    print(degree_of_profanity)
