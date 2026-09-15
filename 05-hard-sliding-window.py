def longest_substring_k_distinct(s: str, k: int) -> int:
    """
    Approach: sliding window with a hashmap tracking char counts in
    the window. Expand right pointer; when distinct count exceeds k,
    shrink from the left until back within k.
    Time: O(n), Space: O(k).
    Edge cases handled explicitly:
      - k == 0: no window can ever be valid, return 0 immediately
        (this is the classic off-by-one trap — without this check,
        a naive sliding window can underflow or loop incorrectly).
      - empty string: loop body never executes, returns 0.
    """
    if k == 0 or not s:
        return 0

    counts = {}
    left = 0
    max_len = 0

    for right, ch in enumerate(s):
        counts[ch] = counts.get(ch, 0) + 1
        while len(counts) > k:
            left_ch = s[left]
            counts[left_ch] -= 1
            if counts[left_ch] == 0:
                del counts[left_ch]
            left += 1
        max_len = max(max_len, right - left + 1)

    return max_len
