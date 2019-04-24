import collections


def max_val_in_window(stream, window_size):
    q = collections.deque()
    windows = []
    s_len = len(stream)
    pos = 0

    while q or pos < s_len:
        if pos < s_len:
            el = stream[pos]
            q.append(el)
            pos += 1

        if len(q) > window_size or pos >= s_len:
            q.popleft()

        if q:
            windows.append(max(q))

    return windows


if __name__ == '__main__':
    print(max_val_in_window([1.3, 2.5, 3.7, 1.4, 2.6, 2.2, 1.7, 1.7], 3))

