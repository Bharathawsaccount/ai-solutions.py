def first_unique_char(s: str) -> int:
    """
    Approach: count frequency of each char, then scan again to find
    the first one with count == 1.
    Time: O(n), Space: O(1) — at most 26 lowercase letters.
    Edge cases handled: empty string returns -1 immediately.
    """
    if not s:
        return -1
    counts = {}
    for ch in s:
        counts[ch] = counts.get(ch, 0) + 1
    for i, ch in enumerate(s):
        if counts[ch] == 1:
            return i
    return -1
