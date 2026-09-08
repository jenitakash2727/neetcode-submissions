class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:


        hashmap = {}

        for word in strs:#step1:-act,step 2:-pots ,step:-cat

            # word-a sort panni key create pannrom
            key = "".join(sorted(word))#step1:-act stringla podurom so "act",step2:-opst,step3:act
          

            if key in hashmap: #act in {'act',"pots",} so act irrukuthu

                hashmap[key].append(word) #ippo {'act'}.append (act) apponaa append naa list la apepnd panrom so athunala list kula podurom {'act':['act'],'opst':['pots']}
          
            else:
                hashmap[key] = [word] #step1: hashmap[key-act ]=[word-act] so {'act':['act']} step2:-hashmap[opst]=[pots] so {act:['act'],'opst':['pots']}
          

        return list(hashmap.values())
        