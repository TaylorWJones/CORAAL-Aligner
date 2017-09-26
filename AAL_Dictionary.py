#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Sep 26 22:08:03 2017

@author: py
"""

#%%
import re

#%%
print("Importing CMU dictionary.")

file = open("/Users/py/Prosodylab-Aligner/CORAAL-Aligner/CORAAL2.dict")
f = file.read()

wordsindict = str.splitlines(f)
file.close()
#%%

print("Importing spoken corpus.")
file2 = open("/Users/py/Desktop/CORAAL/CORAAL_DC/alltextfiles.txt")
f2 = file2.read()
wordsincorpus = str.splitlines(f2)
file2.close()

#%%
print("Finding intersection of CMU dict and spoken corpus. This may take a moment.")
wordsincorpus = [line.split() for line in wordsincorpus]

#%%

wic = []
wic = [item for sublist in wordsincorpus for item in sublist] #makes flat list
#%%

wic = sorted(set(wic)) # eliminates duplicates

#%%

certain = [word for word in wic if '/' not in word] # eliminates guesses between slashes
non_num = [word for word in certain if word.isalpha() == True ] #eliminates numbers

#%%
non_num = [word.upper() for word in non_num]

#%%

wordlist = [word for word in wordsindict if word.split()[0] in non_num] #assigns final corpus

#%%
print("sub-dictionary created, cleaning up.")
print("Now to start with the phonological processes.")

del wordsincorpus, wic, certain, non_num

#%%
# assign helpful arpabet characters to list.

arpa_vowels = ['AA0', 'AA1', 'AA2', 'AE0', 'AE1', 'AE2', 'AH0', 'AH1',
               'AH2', 'AO0', 'AO1', 'AO2', 'AW0', 'AW1', 'AW2', 'AY0', 
               'AY1', 'AY2', 'EH0', 'EH1', 'EH2',
               'EY0', 'EY1', 'EY2', 'IH0', 'IH1', 'IH2', 'IY0', 'IY1',
               'IY2', 'OW0', 'OW1', 'OW2', 'OY0', 'OY1', 'OY2', 'UH0',
               'UH1', 'UH2', 'UW0', 'UW1', 'UW2']

arpa_cons = ['B', 'CH', 'D', 'DH', 'F', 'G', 'HH', 'JH', 'K', 'L', 'M', 
             'N', 'NG', 'P', 'R', 'S', 'SH', 'T', 'TH', 'V', 'W', 'Y', 
             'Z', 'ZH']
             
arpa_rs = ['ER0', 'ER1', 'ER2']             

arpa_obs = ['P', 'T', 'K', 'B', 'D', 'G']
arpa_v_obs = ['B', 'D', 'G']

arpa_vless_obs = ['P', 'T', 'K']   

arpa_v_cons = ['B', 'D', 'F','JH', 'K', 'L', 'M', 
             'N', 'NG', 'R', 'V', 'W', 'Y', 
             'Z', 'ZH']

arpa_vless_cons = ['CH', 'F', 'HH', 'K', 'P', 'S', 'SH', 'T', 'TH',]           


nasals = ['N', 'M', 'NG'] 
nas_vowels = [vowel + '~' for vowel in arpa_vowels]


#%%

new_words = []

# SYLLABIC R

for word in wordlist:
    for r in arpa_rs:
        if r in word:
            print("Syllabic R: \n")
            print("Word is: " + word)
            new_word = re.sub(r, 'AH0', word)
            new_word2 = re.sub(r, 'AH0 R', word)
            print("NEW word is: " + new_word)
            print("NEW word 2 is: " + new_word2 + '\n')
            new_words.append(new_word)
            new_words.append(new_word2)
            
new_words1 = list(sorted(list(set(new_words))))
wordlist = list(sorted(list(set(wordlist + new_words1))))

        
#%%

new_words = []

# POSTVOCALIC R (DELETION)
for word in wordlist:
    for vowel in arpa_vowels:
        if str(vowel + ' R') in word:
            print("Postvocalic R Deletion: \n")
            print("Word is: " + word)
            new_word = re.sub(str(vowel + ' R'), str(vowel), word)
            print("NEW word is: " + new_word + "\n")
            new_words.append(new_word)
            


new_words1 = list(sorted(list(set(new_words))))
wordlist = list(sorted(list(set(wordlist + new_words1))))


#%%

new_words = []

# POSTVOCALIC R (VOCALIZATION)
for word in wordlist:
    for vowel in arpa_vowels:
        if str(vowel + ' R') in word:
            print("Postvocalic R Vocalization: \n")
            print("Word is: " + word)
            new_word = re.sub(str(vowel + ' R'), str(vowel + ' AH0'), word)
            print("NEW word is: " + new_word + "\n")
            new_words.append(new_word)


new_words1 = list(sorted(list(set(new_words))))
wordlist = list(sorted(list(set(wordlist + new_words1))))

     
#%%

new_words = []

# POSTVOCALIC L (DELETION)
for word in wordlist:
    for vowel in arpa_vowels:
        if str(vowel + ' L') in word:
            print("Postvocalic L deletion: \n")
            print("Word is: " + word)
            #new_word = ' '.join(replace([vowel, 'L'], vowel , word.split()))
            new_word = re.sub(str(vowel + ' L'), vowel, word)
            print("NEW word is: " + new_word + "\n")
            new_words.append(new_word)
 

new_words1 = list(sorted(list(set(new_words))))
wordlist = list(sorted(list(set(wordlist + new_words1))))
                 
#%%
new_words = []

# POSTVOCALIC L (VOCALIZATION)
for word in wordlist:
    for vowel in arpa_vowels:
        if str(vowel + ' L') in word:
            print("Postvocalic L vocalization: \n")
            print("Word is: " + word)
            new_word = re.sub(str(vowel + ' L'), str(vowel + ' UW0'), word)
            print("NEW word is: " + new_word + "\n")
            new_words.append(new_word)
            

new_words1 = list(sorted(list(set(new_words))))
wordlist = list(sorted(list(set(wordlist + new_words1))))
                             
#%%

new_words = []
# TH stopping
for word in wordlist:
    if ' TH ' in word:
        print("TH stopping: \n")
        print("word is: " + word)
        new_word = re.sub(' TH ', ' T ', word)
        print("NEW word is: " + new_word + '\n')
        new_words.append(new_word)   
        

new_words1 = list(sorted(list(set(new_words))))
wordlist = list(sorted(list(set(wordlist + new_words1))))
                         
#%%
new_words = []
# (Voiced) TH (DH) stopping

for word in wordlist:
    if ' DH ' in word:
        print("DH stopping: \n")
        print("word is: " + word)
        new_word = re.sub(' DH ', ' D ', word)
        print("NEW word is: " + new_word + '\n')
        new_words.append(new_word)  


new_words1 = list(sorted(list(set(new_words))))
wordlist = list(sorted(list(set(wordlist + new_words1))))
                         

#%% 
new_words = []
# TH fronting
#
for word in wordlist:
   if 'TH' in word.split() and word.split()[1] != 'TH':
       print("TH fronting: \n")
       print("word is: " + word)
       new_word = re.sub(' TH', ' F', word)
       print("NEW word is: " + new_word + '\n')     
       new_words.append(new_word)
       

new_words1 = list(sorted(list(set(new_words))))
wordlist = list(sorted(list(set(wordlist + new_words1))))
                        




#%% 
new_words = []
# (voiced) TH (DH) fronting

for word in wordlist:
   if 'DH' in word.split() and word.split()[1] != 'DH':
       print("DH fronting: \n")
       print("word is: " + word)
       #new_word = ' '.join(replace(['DH'], 'V' , word.split()))
       new_word = re.sub('DH', 'V', word)
       print("NEW word is: " + new_word + '\n')
       #wordlist.insert(wordlist.index(word)+1, new_word)
       new_words.append(new_word)
       
new_words1 = list(sorted(list(set(new_words))))
wordlist = list(sorted(list(set(wordlist + new_words1))))       
       
#%%
new_words = []
# post and intervocalic V deletion
# NOTE: MUST COME AFTER VOICED TH (DH) FRONTING AS 
# FRONTING ***FEEDS*** THIS PHONOLOGICAL PROCESS

for word in wordlist:
    for vowel in arpa_vowels:
        if str(vowel + ' V') in word:
            print("Post and intervocalic V deletion: \n")
            print("word is: " + word )
            new_word = re.sub(' V', '', word )
            print("NEW word is: " + new_word + '\n')
            new_words.append(new_word)
            
new_words1 = list(sorted(list(set(new_words))))
wordlist = list(sorted(list(set(wordlist + new_words1))))            
            
#%%
new_words = []
# vowel nasalization:
    

for word in wordlist:
    for vowel in arpa_vowels:
        for nasal in nasals:
            if str(vowel + ' ' +  nasal) in word:
                print("Word is: " + word)
                new_word = re.sub(str(vowel + ' ' + nasal), str(vowel + '~ ' + nasal), word)
                print("New word is: " + new_word)
                new_words.append(new_word)
                new_word2 = re.sub(str(vowel + ' ' + nasal), str(vowel + '~'), word)
                print("New word 2 is: " + new_word2 + '\n')
                if '~G' not in new_word2:
                    new_words.append(new_word2)

new_words1 = sorted(list(set(new_words)))
wordlist = sorted(list(set(wordlist + new_words1)))       
            
            
            
#%% 
new_words = []

# SIMPLE INTERVOCALIC STOP DEBUCCALIZATION
   
for word in wordlist:
    for vowel in arpa_vowels + nas_vowels:
        for obs in arpa_obs:
            if str(vowel + ' ' + obs + ' ' + vowel) in word:
                print("Intervocalic stop debuccalization: \n")
                print("Word is: " + word)
                new_word = re.sub(str(vowel + ' ' + obs), str(vowel + ' Q'), word)
                print("NEW word is: " + new_word + '\n')
                new_words.append(new_word)
                
                
new_words1 = sorted(set(new_words))
wordlist = sorted(set(wordlist + new_words1))    
#               

#%%
new_words = []
# word final S

for word in wordlist:
    if word.endswith('S') == True:
        print("Word final S deletion: \n")
        print("Word is: " + word)
        new_word = re.sub(' S$', '', word)
        print("NEW word is: " + new_word + '\n')
        new_words.append(new_word)
    if word.endswith('Z') == True:
        print("Word final Z deletion: \n")
        print("Word is: " + word)
        new_word2 = re.sub(' Z$', '', word)
        print("NEW word is: " + new_word2 + '\n')
        new_words.append(new_word2)

             
new_words1 = sorted(set(new_words))
wordlist = sorted(set(wordlist + new_words1))

#%%
new_words = []
# word final debuccalization/deletion:
    
for word in wordlist:
    for obs in arpa_obs:
        if word.endswith(' ' + obs) == True:
            print("Word final debuccalization/deletion: \n")
            print("Word is: " + word)
            new_word = re.sub(' ' + obs, ' Q', word)
            print("NEW word is: " + new_word)
            new_word2 = re.sub(' '+ obs, '', word)
            print("NEW word is: " + new_word2 + '\n')
            new_words.append(new_word)
            new_words.append(new_word2)
            
    
new_words1 = sorted(set(new_words))
wordlist = sorted(set(wordlist + new_words1))


   
#%%


new_words = []
## T/D (DEBUCCALIZATION AND) DELETION:
#
## POSTVOCALIC V C(C) DEBUCCALIZATION AND DELTION --- VOICELESS

for word in wordlist:
    for vowel in arpa_vowels + nas_vowels:
        for coda in arpa_vless_cons:
            for stop in arpa_vless_obs:
                if str(vowel + ' ' + coda + ' ' + stop) in word:
                    print("T/D deletion (voiceless): \n")
                    print("Word is: " + word)
                    new_word = re.sub(str(vowel + ' ' + coda + ' ' + stop),str(vowel + ' ' + coda + ' Q'), word)
                    print("NEW word is: " + new_word)
                    new_word2 = re.sub(str(vowel + ' ' + coda + ' ' + stop),str(vowel + ' ' + coda + ''), word)
                    print("NEW word 2 is: " + new_word2 + '\n')
                    new_words.append(new_word)
                    new_words.append(new_word2)
                    

new_words1 = sorted(set(new_words))
wordlist = sorted(set(wordlist + new_words1))

#%%
new_words = []
##POSTVOCALIC V C(C) DEBUCCALIZATION AND DELTION --- VOICED

for word in wordlist:
    for vowel in arpa_vowels + nas_vowels:
        for coda in arpa_v_cons:
            for stop in arpa_v_obs:
                if str(vowel + ' ' + coda + ' ' + stop) in word:
                    print("T/D deletion (voiced): \n")
                    print("Word is: " + word)
                    new_word = re.sub(str(vowel + ' ' + coda + ' ' + stop),str(vowel + ' ' + coda + ' Q'), word)
                    print("NEW word is: " + new_word)
                    new_word2 = re.sub(str(vowel + ' ' + coda + ' ' + stop),str(vowel + ' ' + coda + ''), word)
                    print("NEW word 2 is: " + new_word2 + '\n')
                    new_words.append(new_word)
                    new_words.append(new_word2)
                    

new_words1 = sorted(set(new_words))
wordlist = sorted(set(wordlist + new_words1))

#%%
new_words = []
# vowel nasalization:
    

for word in wordlist:
    for vowel in arpa_vowels:
        for nasal in nasals:
            if str(vowel + ' ' +  nasal) in word:
                print("Word is: " + word)
                new_word = re.sub(str(vowel + ' ' + nasal), str(vowel + '~ ' + nasal), word)
                print("New word is: " + new_word)
                new_words.append(new_word)
                new_word2 = re.sub(str(vowel + ' ' + nasal), str(vowel + '~'), word)
                print("New word 2 is: " + new_word2 + '\n')
                new_words.append(new_word2)

new_words1 = sorted(list(set(new_words)))
wordlist = sorted(list(set(wordlist + new_words1)))       
            

#%% 
print("Finished adding items, now making list without doubled phones\n" * 100)

#%%

new_words = [] 
# remove cruft with repeated adjacent vowels
for word in wordlist:
    for vowel in arpa_vowels + nas_vowels:
        if str(vowel + ' ' + vowel) not in word:
            print("adding: " + word)
            new_words.append(word)

new_wordlist = sorted(set(new_words))


new_words = []    
# remove cruft with repeated adjacent S (common after cluster reduction)
for word in new_wordlist:
    for vowel in arpa_vowels:
        if str(vowel + ' ' + vowel) not in word and 'S S$' not in word:
            print("Adding: " + word)
            new_words.append(word)

new_words1 = sorted(set(new_words))
new_wordlist1 = sorted(set(new_wordlist + new_words1))

#%%
final_dict = [word for word in new_wordlist1 if len(word.split()) > 1]

  
#%%

print("writing to output file\n" * 20)


#%%


with open("/Users/py/Desktop/AALang.dict", 'w') as dickt:
    for line in final_dict:
        print("Writing to file: " + line)
        dickt.write(line + '\n')
  
print("length of new dictionary is: " + str(len(final_dict)))
