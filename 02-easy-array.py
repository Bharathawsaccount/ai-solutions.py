def merge_intervals(intervals: list[list[int]]) -> list[list[int]]:
    """
    Approach: sort by start time, then walk through merging any
    interval whose start <= current merged interval's end.
    Time: O(n log n) for the sort, Space: O(n) for the output.
    Edge cases handled: empty list returns []; touching intervals
    ([1,4],[4,5]) are treated as overlapping (<=, not <).
    """
    if not intervals:
        return []
    intervals.sort(key=lambda x: x[0])
    merged = [intervals[0]]
    for start, end in intervals[1:]:
        last = merged[-1]
        if start <= last[1]:
            last[1] = max(last[1], end)
        else:
            merged.append([start, end])
    return merged
