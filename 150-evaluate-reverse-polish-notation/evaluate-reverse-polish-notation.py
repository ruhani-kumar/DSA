class Solution:
    def operation(self, a, b, operator):
        if operator == '+':
            return a+b
        elif operator == '-':
            return a-b
        elif operator == '/':
            return int(a/b)
        elif operator == '*':
            return a*b
    def evalRPN(self, tokens: List[str]) -> int:
        st = []
        for t in tokens:
            if t == '+' or t == '-' or t == '/' or t == '*':
                b = st.pop()
                a = st.pop()
                op = t
                ans = self.operation(a, b, op)
                st.append(ans)
            else:
                st.append(int(t))
        return st.pop()
        