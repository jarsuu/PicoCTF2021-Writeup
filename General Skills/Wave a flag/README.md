# PicoCTF2021 - Wave a flag

## Description
Can you invoke help flags for a tool or binary? [This program](./warm) has extraordinarily helpful information...

## Solution
1. Outputted the text contents of binary file ```warm``` running ```strings warm```
2. Attempted to extract the flag from the text content dump using ```grep```
3. Extracted the flag by running ```strings warm | grep -oE "picoCTF{.+}"```

## Flag
picoCTF{b1scu1ts_4nd_gr4vy_30e77291}