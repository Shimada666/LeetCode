# -*- coding: utf-8 -*-
"""
    :author: Shimada666
    :url: https://github.com/shimada666
    :copyright: © 2020 Shimada666 <Shimada666@foxmail.com>
    :license: MIT, see LICENSE for more details.
"""


class Solution:
    def dayOfTheWeek(self, day: int, month: int, year: int) -> str:
        import datetime
        dic = {1: 'Monday', 2: 'Tuesday', 3: 'Wednesday', 4: 'Thursday',
               5: 'Friday', 6: 'Saturday', 0: 'Sunday'}
        week_num = int(datetime.datetime(year, month, day).strftime("%w"))
        return dic[week_num]
