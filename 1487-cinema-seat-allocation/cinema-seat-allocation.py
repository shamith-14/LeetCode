class Solution:
    def maxNumberOfFamilies(self, n, reservedSeats):
        rows = {}

        for row, seat in reservedSeats:
            rows[row] = rows.get(row, 0) | (1 << seat)

        answer = (n - len(rows)) * 2

        left = (1 << 2) | (1 << 3) | (1 << 4) | (1 << 5)
        middle = (1 << 4) | (1 << 5) | (1 << 6) | (1 << 7)
        right = (1 << 6) | (1 << 7) | (1 << 8) | (1 << 9)

        for reserved in rows.values():
            count = 0

            if reserved & left == 0:
                count += 1

            if reserved & right == 0:
                count += 1

            if count == 0 and reserved & middle == 0:
                count = 1

            answer += count

        return answer