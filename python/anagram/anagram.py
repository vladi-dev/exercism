def detect_anagrams(given, candidates):
    detected = []

    for candidate in candidates:

        if len(candidate) != len(given) or candidate.lower() == given.lower():
            continue

        x = list(candidate.lower())
        y = list(given.lower())

        is_anagram = 0 == len([char for char in y if char not in x or x.remove(char)])

        if is_anagram:
            detected.append(''.join(candidate))

    return detected
