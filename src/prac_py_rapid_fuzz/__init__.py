def lcs_length(s1, s2):
    m, n = len(s1), len(s2)
    dp = [[0] * (n + 1) for _ in range(m + 1)]
    for i in range(m):
        for j in range(n):
            if s1[i] == s2[j]:
                dp[i + 1][j + 1] = dp[i][j] + 1
            else:
                dp[i + 1][j + 1] = max(dp[i + 1][j], dp[i][j + 1])
    return dp[m][n]


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
