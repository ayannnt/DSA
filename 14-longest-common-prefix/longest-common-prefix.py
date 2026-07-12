class Solution(object):
    def longestCommonPrefix(self, strs):
        a = strs[0]
        b= ''
        for i in range(len(a)):
            b+=a[i]
            for j in range(1, len(strs)):
                if b not in strs[j][:i+1]:
                    b = b[:len(b)-1]
                    break
            if len(b)==i:
                break
            
                

        return b


        """
        :type strs: List[str]
        :rtype: str
        """
        