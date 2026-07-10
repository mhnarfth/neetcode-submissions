class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        A = {}
        for s in strs:

            # joining the sorted chars of the string 
            sorted_s = "".join (sorted(s))

            #checking if the key exists 
            if sorted_s not in A:
                A[sorted_s] = []

            A[sorted_s].append(s)

        return list(A.values())