class Solution:
    def countCoveredBuildings(self, n: int, buildings: List[List[int]]) -> int:
        # Convert building list to a set for O(1) lookup
        bset = {(x, y) for x, y in buildings}

        # Maps for quick check of buildings in same row or column
        rows = {}
        cols = {}

        for x, y in buildings:
            if x not in rows:
                rows[x] = []
            rows[x].append(y)

            if y not in cols:
                cols[y] = []
            cols[y].append(x)

        # Sort row/column lists so we can check neighbors
        for r in rows:
            rows[r].sort()
        for c in cols:
            cols[c].sort()

        covered = 0

        for x, y in buildings:
            ys = rows[x]
            xs = cols[y]

            # Find positions in sorted lists
            import bisect
            yi = bisect.bisect_left(ys, y)
            xi = bisect.bisect_left(xs, x)

            has_left = yi > 0
            has_right = yi < len(ys) - 1
            has_above = xi > 0
            has_below = xi < len(xs) - 1

            if has_left and has_right and has_above and has_below:
                covered += 1

        return covered
