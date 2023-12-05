def read_file(filename: str) -> list:
    """
    This function opens the file reads the file and splits it by ' '
    :param filename: Name of the file to open
    :return:
    """
    return open(filename, 'r', encoding='UTF-8').read().split(' ')


def remove_punctuation_and_numbers(words: list, punctuation: list, numbers: list) -> list:
    """
    Remove punctuation and numbers from a list of words.
    This is done by iterating through each character in
    each word and checking whether it is in the punctuation list or the number list.
    :param words: List where the text is
    :param punctuation: List where the punctuation is
    :param numbers: List where the numbers are
    :return:
    """
    punctuation_set = set(punctuation)
    numbers_set = set(numbers)
    words_aux = []
    for w in words:
        w_aux = ''.join(c for c in w if c not in punctuation_set and c not in numbers_set)
        words_aux.append(w_aux)
    return words_aux


def count_words(words: list) -> dict:
    """
    Count words
    :param words: List where the text is
    :return: Return of the counting dictionary
    """
    dict_word = {}
    for w in words:
        if w in dict_word:
            dict_word[w] = dict_word[w] + 1
        else:
            dict_word[w] = 1
    return dict_word


def remove_words(words: list, stopwords: list) -> list:
    """

    :param words: List where the text is
    :param stopwords: List where the stop words are
    :return: List of the text without then stop words
    """
    return [word for word in words if word not in stopwords]


def calculate_absolute_frequency(words: list):
    """
    Calculate Absolute Frequency
    :param words: List where the text is
    :return:the word_count dictionary, which contains the count of each word,
     and total_words, which is the total number of words in the text.
    """
    word_count = {}
    total_words = len(words)
    for word in words:
        if word in word_count:
            word_count[word] += 1
        else:
            word_count[word] = 1
    return word_count, total_words


def calculate_relative_frequency(word_count: dict, total_words: int) -> dict:
    """

    :param word_count: A dictionary containing the count of each word in the text.
    :param total_words: The total number of words in the text.
    :return: A new dictionary in which each word is mapped to its corresponding relative frequency.
    """
    return {word: count / total_words for word, count in word_count.items()}


def words_in_frequency_range(word_count: dict, min_frequency: int, max_frequency: int) -> list:
    """

    :param word_count: A dictionary containing the count of each word in the text.
    :param min_frequency: Minimum frequency of the word
    :param max_frequency: Maximum frequency of the word
    :return: A new dictionary in which each word is mapped to its corresponding
     frequency in the defined range.
    """
    return [word for word, count in word_count.items() if min_frequency <= count <= max_frequency]


def words_in_relative_frequency_range(relative_frequency: dict, min_frequency: float, max_frequency: float) -> list:
    """

    :param relative_frequency:
    :param min_frequency: Minimum frequency of the word
    :param max_frequency: Maximum frequency of the word
    :return: The function returns a list containing all the words whose relative frequencies
     are within the specified range.
    """
    return [word for word, freq in relative_frequency.items() if min_frequency <= freq <= max_frequency]
