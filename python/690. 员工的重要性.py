# -*- coding: utf-8 -*-
from typing import List

"""
# Employee info
class Employee:
    def __init__(self, id, importance, subordinates):
        # It's the unique id of each node.
        # unique id of this employee
        self.id = id
        # the importance value of this employee
        self.importance = importance
        # the id of direct subordinates
        self.subordinates = subordinates
"""


class Solution:
    def __init__(self):
        self.res = 0

    def getImportance(self, employees, id):
        """
        :type employees: Employee
        :type id: int
        :rtype: int
        """

        hashmap = dict()

        for employee in employees:
            hashmap[employee.id] = [employee.importance, employee.subordinates]

        def dfs(subs):
            for sub in subs:
                self.res += hashmap[sub][0]
                dfs(hashmap[sub][1])

        dfs([id])
        return self.res
