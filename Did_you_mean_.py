""" You'll get an entered term (lowercase string) and an array of known words (also lowercase strings).
    Your task is to find out, which word from the dictionary is most similar to the entered one.
    The similarity is described by the minimum number of letters you have to add,
    remove or replace in order to get from the entered word to one of the dictionary.
    The lower the number of required changes, the higher the similarity between each two words.
"""


def levenshtein_distance(str1, str2):
    len_str1 = len(str1)
    len_str2 = len(str2)
    dp = [[0] * (len_str2 + 1) for _ in range(len_str1 + 1)]

    for i in range(len_str1 + 1):
        dp[i][0] = i

    for j in range(len_str2 + 1):
        dp[0][j] = j

    for i in range(1, len_str1 + 1):
        for j in range(1, len_str2 + 1):
            cost = 0 if str1[i - 1] == str2[j - 1] else 1
            dp[i][j] = min(
                dp[i - 1][j] + 1,  # вставка
                dp[i][j - 1] + 1,  # удаление
                dp[i - 1][j - 1] + cost  # замена
            )

    return dp[len_str1][len_str2]


class Dictionary:
    def __init__(self, words):
        self.words = words

    def find_most_similar(self, term):
        min_distance = float('inf')
        result = None

        for word in self.words:
            distance = levenshtein_distance(term, word)
            if distance < min_distance:
                min_distance = distance
                result = word
