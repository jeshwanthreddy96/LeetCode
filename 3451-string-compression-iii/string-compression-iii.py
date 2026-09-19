class Solution(object):
    def compressedString(self, word):
        op = {}
        ch = []
        z = "" 
        for i in word:
            if not ch or i != ch[-1] or op[i] == 9:
                if ch:
                    z += str(op[ch[-1]]) + ch[-1]
                ch.append(i)
                op[i] = 1
            else:
                op[i] += 1
        if ch:
            z += str(op[ch[-1]]) + ch[-1]         
        return z
