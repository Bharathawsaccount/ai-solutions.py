def group_anagrams(words: list[str]) -> list[list[str]]:
    """
    Approach: use sorted-letters as a hashmap key — anagrams share
    the same sorted form. Preserve insertion order via dict (Python 3.7+).
    Time: O(n * k log k) where k = max word length, Space: O(n * k).
    Edge cases handled: empty string "" sorts to "" and groups with itself;
    single-char words group alone if no match.
    """
    groups = {}
    for word in words:
        key = "".join(sorted(word))
        groups.setdefault(key, []).append(word)
    return list(groups.values())
