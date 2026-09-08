class Solution:
    def isAnagram(self, s: str, t: str) -> bool:

            # length same illa na anagram illa
        if len(s) != len(t):
            return False

        hashmap = {}

        # s string character count
        for ch in s:#step1:-a  3step2:-c #step3:a
            if ch in hashmap: #a in {a:1,c:2} so a irrukuthu
                hashmap[ch] += 1 #_appo a add prnom +=1 a:1+1={a:2}
            else:
                hashmap[ch] = 1 #step1(a:1)#step2:(a:1,c:2)

        # t string character count reduce
        for ch in t: # step4:-c,step 5:-a,step 6:a

            if ch not in hashmap: #step 4:-c  hashmapla ilalana false appo c irrukuthu ,step5:-a hashapla  illaa flase but a irrukuthu appo false,step 6:- a irrukuthu hashmap appo false
                return False

            hashmap[ch] -= 1 #step4:- {c:1-1=c:0}so {c:0} #step5:-{c:1,a:2-1=1} so{c:0,a:1},step 6:-{c:0,a:1-1=0} so  {c:0,a:0}

        # ella count um 0 aaganum
        for value in hashmap.values():
            if value != 0: #hashmap value o la irrukuthu appo false varathu
                return False

        return True #yes all values zero la irrukuthu so true

            