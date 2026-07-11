'''from collections import deque
class Solution:
    def isValid(self, s: str) -> bool:
        for p in range(len(s)):
            if p==0:
                q = deque(s[0])
            else:
                while q:
                    if s[p]=='(' or s[p]=='{' or s[p]=='[':
                        q.append(s[p])
                    else:
                        if s[p]==')' and q[-1]!='(':
                            return False
                        elif s[p]=='}' and q[-1]!='{':
                            return False
                        elif s[p]==']' and q[-1]!='[':
                            return False
                        q.pop()
        if not q:
            return True
        else:
            return False'''

class Solution:
    def isValid(self, s: str) -> bool:
        i=0
        a=[]
        for i in range(len(s)):
            if s[i]=='('or s[i]=='['or s[i]=='{':
                a.append(s[i])
            else:
                if not a:
                    return False
                top=a.pop()
                if s[i]==')'and top!='(':
                    return False
                if s[i]==']'and top!='[':
                    return False
                if s[i]=='}'and top!='{':
                    return False
        return len(a)==0