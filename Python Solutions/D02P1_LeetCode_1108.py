# Python3 ,By :- Shridhan jadhav
# Que. Defanging an IP Address

class Solution:
    def defangIPaddr(self, address: str) -> str:
        return address.replace('.','[.]')
    
