class Solution:
    def reverseVowels(self, a: str) -> str:
        a=list(a)
        l=0
        r=len(a)-1
        while l<r:
            if a[l] not in 'AEIOUaeiou':
                l+=1
            elif a[r] not in 'AEIOUaeiou':
                r-=1
            else:
                a[l],a[r]=a[r],a[l]
                l+=1
                r-=1
        return ''.join(a)