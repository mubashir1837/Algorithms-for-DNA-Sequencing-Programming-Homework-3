def overlap(a, b, min_length=3):
    """Return length of longest suffix of 'a' matching prefix of 'b'."""
    start = 0
    while True:
        start = a.find(b[:min_length], start)
        if start == -1:
            return 0
        if b.startswith(a[start:]):
            return len(a) - start
        start += 1
