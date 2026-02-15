def lcs_length(s1, s2):
    # Ensure s2 is the shorter string to optimize space
    if len(s1) < len(s2):
        s1, s2 = s2, s1
    
    m, n = len(s1), len(s2)
    
    # dp array for the current row, initialized to all zeros
    # dp[j] will store the LCS length of s1[:i+1] and s2[:j+1]
    # from the previous iteration (i-1)
    dp = [0] * (n + 1)

    for i in range(m): # Iterate through s1 (longer string)
        diag_prev = 0 # Stores dp[i][j] (value from previous row, previous column)
        for j in range(n): # Iterate through s2 (shorter string)
            temp = dp[j+1] # Save dp[i][j+1] (value from previous row, current column)
            if s1[i] == s2[j]:
                dp[j+1] = diag_prev + 1
            else:
                dp[j+1] = max(dp[j], dp[j+1])
            diag_prev = temp # Update diag_prev for the next column calculation

    return dp[n]


def indel_distance(s1, s2):
    lcs = lcs_length(s1, s2)
    return len(s1) + len(s2) - 2 * lcs


def _norm_distance(dist, lensum):
    if lensum == 0:
        return 100.0
    score = 100.0 - 100.0 * float(dist) / float(lensum)
    return score if score > 0 else 0.0


def main(s1: str, s2: str) -> int:

    if not s1 or not s2:
        return 0

    tokens_a = set(s1.split())
    tokens_b = set(s2.split())

    if not tokens_a or not tokens_b:
        return 0

    intersect = tokens_a.intersection(tokens_b)
    diff_ab = tokens_a.difference(tokens_b)
    diff_ba = tokens_b.difference(tokens_a)

    if intersect and (not diff_ab or not diff_ba):
        return 100

    diff_ab_joined = " ".join(sorted(list(diff_ab)))
    diff_ba_joined = " ".join(sorted(list(diff_ba)))
    intersect_joined = " ".join(sorted(list(intersect)))

    sect_len = len(intersect_joined)
    ab_len = len(diff_ab_joined)
    ba_len = len(diff_ba_joined)

    has_sect = 1 if sect_len > 0 else 0

    sect_ab_len = sect_len + has_sect + ab_len
    sect_ba_len = sect_len + has_sect + ba_len

    dist1 = indel_distance(diff_ab_joined, diff_ba_joined)
    result = _norm_distance(dist1, sect_ab_len + sect_ba_len)

    if not sect_len:
        return int(result)

    sect_ab_dist = has_sect + ab_len
    sect_ab_ratio = _norm_distance(sect_ab_dist, sect_len + sect_ab_len)

    sect_ba_dist = has_sect + ba_len
    sect_ba_ratio = _norm_distance(sect_ba_dist, sect_len + sect_ba_len)

    final_score = max(result, sect_ab_ratio, sect_ba_ratio)

    return int(final_score)
