from typing import List


class Solution:
    def threeConsecutiveOdds(self, arr: List[int]) -> bool:
        for i in range(0, len(arr)-2):
            if arr[i] % 2 != 0 and arr[i+1] % 2 != 0 and arr[i+2] % 2 != 0:
                return True
        return False


def main():
    arr = [2, 6, 4, 1]
    assert Solution().threeConsecutiveOdds(arr) is False

    arr = [1, 2, 34, 3, 4, 5, 7, 23, 12]
    assert Solution().threeConsecutiveOdds(arr) is True


if __name__ == '__main__':
    main()
