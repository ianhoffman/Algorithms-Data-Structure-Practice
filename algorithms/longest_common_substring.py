def LCS(s, t):
    cache = {}

    def LCS_helper(i, j):
        if (i, j) in cache:
            return cache[(i, j)]

        if i < 0 or j < 0:
            lcs = 0
        else:
            lcs = max(
                bool(s[i] == t[j]) + LCS_helper(i - 1, j - 1),
                LCS_helper(i - 1, j),
                LCS_helper(i, j - 1)
            )

        cache[(i, j)] = lcs
        return lcs

    return LCS_helper(len(s) - 1, len(t) - 1)


if __name__ == '__main__':
    print(LCS('ABCDGH', 'AEDFHR'))
    print(LCS('AGGTAB', 'GXTXAYB'))

