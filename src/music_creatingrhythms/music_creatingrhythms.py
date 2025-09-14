import math
import random
import sys

class Rhythms:
    def __init__(
        self,
        verbose=False,
    ):
        self.verbose = verbose

    def b2int(self, binary_str):
        nbit = len(binary_str)
        intervals = []
        j = 0
        while j < nbit:
            k = 1
            j += 1
            while j < nbit and binary_str[j] != '1':
                k += 1
                j += 1
            intervals.append(k)
        return intervals

    def cfcv(self, *terms):
        p0, p1 = 0, 1
        q0, q1 = 1, 0
        for t in terms:
            p2 = t * p1 + p0
            q2 = t * q1 + q0
            p0, p1 = p1, p2
            q0, q1 = q1, q2
        return [p2, q2]

    def cfsqrt(self, n):
        A = 0
        B = 1
        a0 = int(math.isqrt(n))
        a = a0
        terms = [a]
        if a * a < n:
            while True:
                A = B * a - A
                B = (n - A * A) // B
                a = (a0 + A) // B
                terms.append(a)
                if a == 2 * a0:
                    break
        return terms

    def chsequl(self, t, p, q, n=None):
        if t not in ('u', 'l'):
            raise ValueError("Type must be 'u' or 'l'")
        n = n or (p + q)
        word = []
        i = 0
        while i < n:
            word.append(1 if t == 'u' else 0)
            i += 1
            x, y = p, q
            while x != y and i < n:
                if x > y:
                    word.append(1)
                    y += q
                else:
                    word.append(0)
                    x += p
                i += 1
            if x == y and i < n:
                word.append(0 if t == 'u' else 1)
                i += 1
        return word

    def comp(self, n):
        compositions = []
        def _compose(n, p, k, parts):
            if n == 0:
                compositions.append(parts + [p])
                return
            _compose(n - 1, 1, k + 1, parts + [p])
            _compose(n - 1, p + 1, k, parts)
        _compose(n - 1, 1, 0, [])
        return compositions

    def compa(self, n, *intervals):
        compositions = []
        def _allowed(p):
            return p in intervals
        def _composea(n, p, k, parts):
            if n == 0:
                if _allowed(p):
                    compositions.append(parts + [p])
                return
            if _allowed(p):
                _composea(n - 1, 1, k + 1, parts + [p])
            _composea(n - 1, p + 1, k, parts)
        _composea(n - 1, 1, 0, [])
        return compositions

    def compam(self, n, m, *intervals):
        compositions = []
        def _allowed(p):
            return p in intervals
        def _composeam(n, p, k, m, parts):
            if n == 0:
                if k == m and _allowed(p):
                    compositions.append(parts + [p])
                return
            if k < m and _allowed(p):
                _composeam(n - 1, 1, k + 1, m, parts + [p])
            _composeam(n - 1, p + 1, k, m, parts)
        _composeam(n - 1, 1, 0, m - 1, [])
        return compositions

    def compm(self, n, m):
        compositions = []
        def _composem(n, p, k, m, parts):
            if n == 0:
                if k == m:
                    compositions.append(parts + [p])
                return
            if k < m:
                _composem(n - 1, 1, k + 1, m, parts + [p])
            _composem(n - 1, p + 1, k, m, parts)
        _composem(n - 1, 1, 0, m - 1, [])
        return compositions

    def compmrnd(self, n, m):
        j = 1
        mp = m - 1
        np = n - 1
        compositions = []
        while mp > 0:
            p = mp * (sys.maxsize // np)
            if random.randint(0, sys.maxsize) < p:
                compositions.append(j)
                mp -= 1
                j = 1
            else:
                j += 1
            np -= 1
        compositions.append(j + np)
        return compositions

    def comprnd(self, n):
        if not n:
            return [0]
        import random
        compositions = []
        p = 1
        for i in range(1, n):
            if random.randint(0, 1) % 2 == 0:
                p += 1
            else:
                compositions.append(p)
                p = 1
        compositions.append(p)
        return compositions

    def count_digits(self, digit, n):
        if isinstance(n, (list, tuple)):
            return sum(1 for i in n if i == digit)
        else:
            return str(n).count(str(digit))

    def count_ones(self, n):
        return self.count_digits(1, n)

    def count_zeros(self, n):
        return self.count_digits(0, n)

    def de_bruijnX(self, n):
        def debruijn(k, n):
            a = [0] * k * n
            sequence = []
            def db(t, p):
                if t > n:
                    if n % p == 0:
                        for j in range(1, p + 1):
                            sequence.append(a[j])
                else:
                    a[t] = a[t - p]
                    db(t + 1, p)
                    for j in range(a[t - p] + 1, k):
                        a[t] = j
                        db(t + 1, t)
            db(1, 1)
            return sequence
        seq = debruijn(2, n)
        return seq

    def neckbin(self, k, l, n, b, dbs, idbs):
        if k > n:
            if n % l == 0:
                for i in range(l):
                    dbs[idbs[0] + i] = 0 if b[i + 1] == 0 else 1
                idbs[0] += l
        else:
            b[k] = b[k - l]
            if b[k] == 1:
                self.neckbin(k + 1, l, n, b, dbs, idbs)
                b[k] = 0
                self.neckbin(k + 1, k, n, b, dbs, idbs)
            else:
                self.neckbin(k + 1, l, n, b, dbs, idbs)

    def de_bruijn(self, n):
        ndbs = 1 << n
        idbs = [0]
        b = [0] * (n + 2)
        b[0] = 1
        dbs = [''] * (ndbs + 1)
        self.neckbin(1, 1, n, b, dbs, idbs)
        return dbs[:-1]

    def euclid(self, n, m):
        intercept = 1
        slope = n / m
        pattern = [0] * m
        for y in range(1, n + 1):
            idx = int(round((y - intercept) / slope))
            pattern[idx] = 1
        return pattern

    def int2b(self, intervals):
        sequences = []
        for i in intervals:
            bitstring = []
            for j in i:
                bits = '1' + '0' * (j - 1)
                bitstring.extend([int(b) for b in bits])
            sequences.append(bitstring)
        return sequences

    def invert_at(self, n, parts):
        head = parts[:n]
        tail = [0 if x else 1 for x in parts[n:]]
        return head + tail

    def neck(self, n):
        necklaces = []
        parts = [1]
        i = [0]
        self._neckbin(n, 1, 1, i, necklaces, parts)
        return necklaces

    def _neckbin(self, n, k, l, i, necklaces, parts):
        if k > n:
            if n % l == 0:
                necklaces.append([parts[j] for j in range(1, n + 1)])
                i[0] += 1
        else:
            if len(parts) <= k:
                parts.append(0)
            parts[k] = parts[k - l]
            if parts[k] == 1:
                self._neckbin(n, k + 1, l, i, necklaces, parts)
                parts[k] = 0
                self._neckbin(n, k + 1, k, i, necklaces, parts)
            else:
                self._neckbin(n, k + 1, l, i, necklaces, parts)

    def necka(self, n, *intervals):
        necklaces = []
        parts = [1]
        i = [0]
        self._neckbina(n, 1, 1, 1, i, necklaces, parts, intervals)
        return necklaces

    def _neckbina(self, n, k, l, p, i, necklaces, parts, intervals):
        def _allowed(p, intervals):
            return p in intervals
        if k > n:
            if (n % l == 0) and _allowed(p, intervals) and p <= n:
                necklaces.append([parts[j] for j in range(1, n + 1)])
                i[0] += 1
        else:
            if len(parts) <= k:
                parts.append(0)
            parts[k] = parts[k - l]
            if parts[k] == 1:
                if _allowed(p, intervals) or k == 1:
                    self._neckbina(n, k + 1, l, 1, i, necklaces, parts, intervals)
                parts[k] = 0
                self._neckbina(n, k + 1, k, p + 1, i, necklaces, parts, intervals)
            else:
                self._neckbina(n, k + 1, l, p + 1, i, necklaces, parts, intervals)

    def neckam(self, n, m, *intervals):
        necklaces = []
        parts = [1]
        i = [0]
        self._neckbinam(n, 1, 1, 0, 1, m, i, necklaces, parts, intervals)
        return necklaces

    def _neckbinam(self, n, k, l, q, p, m, i, necklaces, parts, intervals):
        def _allowed(p, intervals):
            return p in intervals
        if k > n:
            if (n % l == 0) and _allowed(p, intervals) and p <= n and q == m:
                necklaces.append([parts[j] for j in range(1, n + 1)])
                i[0] += 1
        else:
            if len(parts) <= k:
                parts.append(0)
            parts[k] = parts[k - l]
            if parts[k] == 1:
                if _allowed(p, intervals) or k == 1:
                    self._neckbinam(n, k + 1, l, q + 1, 1, m, i, necklaces, parts, intervals)
                parts[k] = 0
                self._neckbinam(n, k + 1, k, q, p + 1, m, i, necklaces, parts, intervals)
            else:
                self._neckbinam(n, k + 1, l, q, p + 1, m, i, necklaces, parts, intervals)

    def neckm(self, n, m):
        necklaces = []
        parts = [1]
        i = [0]
        self._neckbinm(n, 1, 1, 0, m, i, necklaces, parts)
        return necklaces

    def _neckbinm(self, n, k, l, p, m, i, necklaces, parts):
        if k > n:
            if (n % l == 0) and (p == m):
                necklaces.append([parts[j] for j in range(1, n + 1)])
                i[0] += 1
        else:
            if len(parts) <= k:
                parts.append(0)
            parts[k] = parts[k - l]
            if parts[k] == 1:
                self._neckbinm(n, k + 1, l, p + 1, m, i, necklaces, parts)
                parts[k] = 0
                self._neckbinm(n, k + 1, k, p, m, i, necklaces, parts)
            else:
                self._neckbinm(n, k + 1, l, p, m, i, necklaces, parts)

    def partition(self, n, p, m, parts, result):
        if n == 0:
            result.append(parts[:m] + [p])
            return
        if n < 0:
            return
        parts[m] = p
        self.partition(n - p, p, m + 1, parts, result)
        self.partition(n - 1, p + 1, m, parts, result)

    def part(self, n):
        parts = [0] * n
        result = []
        self.partition(n - 1, 1, 0, parts, result)
        return result

    def parta(self, n, *parts):
        allowed = set(parts)
        return [p for p in self.part(n) if all(x in allowed for x in p)]
