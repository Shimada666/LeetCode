# -*- coding: utf-8 -*-
from typing import List


class Solution:
    def defangIPaddr(self, address: str) -> str:
        return address.replace('.', '[.]')
