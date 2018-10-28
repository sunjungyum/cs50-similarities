from nltk.tokenize import sent_tokenize


def lines(a, b):
    """Return lines in both a and b"""

    lines = []

    # Splits both strings into lines separated by "\n"
    alist = a.split("\n")
    blist = b.split("\n")

    # Traverses through the lines in a
    for line in alist:
        # Checks if line is also in b and makes sure that it wasn't appended already
        if (line in blist) and (line not in lines):
            lines.append(line)

    return lines


def sentences(a, b):
    """Return sentences in both a and b"""

    sentences = []

    # Splits both strings into sentences
    alist = sent_tokenize(a)
    blist = sent_tokenize(b)

    # Traverses through the sentences in a
    for sentence in alist:
        # Checks if sentence is also in b and makes sure that it wasn't appended already
        if (sentence in blist) and (sentence not in sentences):
            sentences.append(sentence)

    return sentences


def createsubs(a, n):
    createdsubs = []

    # Stops traversing when there are no more substrings of length n left
    for i in range(len(a) - n + 1):
        createdsubs.append(a[i:(i + n)])

    return createdsubs


def substrings(a, b, n):
    """Return substrings of length n in both a and b"""

    substrings = []

    # Splits both strings into substrings of length n using a helper function
    alist = createsubs(a, n)
    blist = createsubs(b, n)

    # Traverses through the substrings in a
    for substring in alist:
        # Checks if substring is also in b and makes sure that it wasn't appended already
        if (substring in blist) and (substring not in substrings):
            substrings.append(substring)

    return substrings