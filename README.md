# CORAAL-Aligner
This repository will, when finished, have two pretrained forced alignment models for use with the Montreal Forced Aligner,
for speech in African American Language (AAL). Both models are trained on both the 1972 CORAAL (Washington) DC A and the 
2016 CORAAL (Washington) DC B interviews. The first model, CORAAL1.zip, is trained using the standard CMU Dictionary and phoneset. 

The second model, CORAAL2.zip, is trained using a novel phoneset that includes nasalized vowels (e.g., in
addition to strings like 'IH1 N', there is also 'IH~'). The model takes into account AAL phonology, and so has novel pronunciations 
*in addition* to the CMU Dictionary pronunciations. Phonological processes accounted for in the CORAAL2.zip model are:

- postvocalic r vocalization/deletion
- postvocalic l vocalization/deletion
- TH stopping
- TH fronting
- post- and intervocalic v deletion
- vowel nasalization
- TH deletion in "them"
- sibilant fortition (wasn't --> wadn't) (to come)
- word/syllable final obstruent deletion/debuccalization (to come)

For example, in addition to the CMU Dictionary pronunciation of "northeast":

NORTHEAST N AO2 R TH IY1 S T

...there is also:

NORTHEAST N AO2 TH IY1 S T

NORTHEAST N AO2 F IY1 S T

NORTHEAST N AO2 TH IY1 S 

NORTHEAST N AO2 AH0 F IY1 S 

NORTHEAST N AO2 F IY1 S 


...etc.

For this particular example, in one token the last pronunciation is what was actually said --- but CORAAL1 will 'find' an R and a T, and will assign F as TH. CORAAL2 should  correctly categorize the consonants here too.

The code used to make the new pronouncing dictionary will be shared as AAL.py

The dictionary is shared as AAL.dict.
