# Python3 ,By :- amreen.s
# Que. Defanging an IP Address

class Solution:
    def defangIPaddr(self, address: str) -> str:
        return address.replace('.','[.]')
