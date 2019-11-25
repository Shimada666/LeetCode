from typing import List


class Solution:
    def distributeCandies(self, candies: int, num_people: int) -> List[int]:
        res = [0] * num_people
        cnt = 1
        i = 0
        while candies >= 0:
            if cnt > candies:
                res[i % num_people] += candies
            else:
                res[i % num_people] += cnt
            candies -= cnt
            cnt += 1
            i += 1
        return res


if __name__ == '__main__':
    print(Solution().distributeCandies(10, 3))
