class Solution:
    def getHint(self, secret, guess):
        
        bulls = 0
        cows = 0
      
        #lst = []
        dg = {}
        ds = {}

        for i, g in enumerate(guess):
            if g in dg:
                dg[g] += 1
            else:
                dg[g] = 1
            
            s = secret[i]
            if s in ds:
                ds[s] += 1
            else:
                ds[s] = 1
            
            if g == s:
                bulls += 1
                ds[s] -= 1
                dg[g] -= 1
                if dg[g] == 0:
                    del dg[g]
                if ds[s] == 0:
                    del ds[s]                    
        for key in dg:
            if key in ds:
                cows += min(ds[key], dg[key])
                
        return f"{bulls}A{cows}B"


sol = Solution()

print(sol.getHint("1807", "7810"))
print(sol.getHint("1123", "0111"))
print(sol.getHint("1122", "2211"))
