class Solution:
    def reverseWords(self, s: str) -> str:
        s=s.strip()
        
        m=[]
        d=''
        for i in range(len(s)):
            if(s[i]==' '):
                if d != '':
                    m.append(d)
                d=''
            else:
                d+=s[i]
        m.append(d)
        l=0
        r=len(m)-1
        while(l<r):
            m[l],m[r]=m[r],m[l]
            l+=1
            r-=1
        return ' '.join(m)
    