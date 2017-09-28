# CORAAL-Aligner

Existing forced alignment performs notoriously poorly on African American Langauge (AAL, alternately 'African American English', AAE), in part English forced aligners are generally not trained on AAL, and in part because pronunciations in the pronouncing dictionaries used to train such aligners are based on "standard" (e.g., white) English pronunciations. 

This repository contains two pretrained forced alignment models for use with the Montreal Forced Aligner,
for speech in African American Language (AAL). Both models are trained on both the 1972 CORAAL (Washington) DC A and the 
2016 CORAAL (Washington) DC B interviews. 

**The first model, CORAAL1.zip**, is trained using the standard CMU Dictionary and phoneset. It performs quite well at finding correct word-level boundaries, however it has shortcomings with regards to AAL. Specifically, because it is looking for 'standard' pronunciations, it "finds" segments that may (1) not actually be present (e.g., "finding" an /r/ that was either vocalized or deleted), or (2) may be different in AAL (e.g., th-fronting that yields F AA1 V AH0 for "FATHER"). 

**The second model, CORAAL2.zip**, is trained using a novel phoneset that includes nasalized vowels (e.g., in
addition to strings like 'IH1 N', there is also 'IH~'), and includes AAL specific pronunciations. The model takes into account AAL phonology, and so has novel pronunciations *in addition* to the CMU Dictionary pronunciations. Phonological processes accounted for in the CORAAL2.zip model are:

- postvocalic r vocalization/deletion
- postvocalic l vocalization/deletion
- TH stopping
- TH fronting
- post- and intervocalic v deletion
- vowel nasalization
- word/syllable final obstruent deletion/debuccalization
- word final S/Z deletion
- T/D deletion (and debuccalization)

For example, in addition to the CMU Dictionary pronunciation of "northeast":

NORTHEAST N AO2 R TH IY1 S T

...there is also:

NORTHEAST N AO2 TH IY1 S T

NORTHEAST N AO2 F IY1 S T

NORTHEAST N AO2 TH IY1 S Q

NORTHEAST N A02 TH IY1 S

NORTHEAST N AO2 AH0 F IY1 S 

NORTHEAST N AO2 F IY1 S Q

NORTHEAST N AO2 F IY1 S 


...etc.

For this particular example, in one token the last pronunciation is what was actually said --- but CORAAL1 will 'find' an R and a T, and will assign F as TH. CORAAL2 should  correctly categorize the consonants here too. 

The python script used to generate the pronouncing dictionary from a standard pronouncing dictionary is shared here as **AAL_DICTIONARY.py**.

The code used to make the new pronouncing dictionary will be shared as an iPython notebook, allowing anyone to write their own script to modify the pronouncing dictionary used.

The dictionary is shared as **CORAAL_DC.dict**. Note, however, that it has only pronunciations for the words present in the CORAAL DCA and DCB interviews, and other researchers will likely find it profitable to modify the AAL_DICTIONARY.py to suit their needs.

**NOTE:** This is a work in progress. I have shared the current dictionary and aligner, but depending on your needs they may not be suitable without modification. I have done some accuracy checks, and it seems to categorize everything correctly, although there may be instances where, for instance, an unreleased stop is categorized as a glottal stop. The main goal -- accounting for AAL phonology so that vowel durations are more accurate (and not 'cut into' by absent segments...e.g., postvocalic /r/), was accomplished. Other researchers should be able to build on this code easily to investigate specific phenomena of interest. With regards to AAL phonology, CORAAL2.zip is "all" and CORAAL1.zip is "nothing." 
