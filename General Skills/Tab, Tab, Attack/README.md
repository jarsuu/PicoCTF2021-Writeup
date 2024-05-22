# PicoCTF2021 - Tab, Tab, Attack

## Description
Using tabcomplete in the Terminal will add years to your life, esp. when dealing with long rambling directory structures and filenames: [Addadshashanammu.zip](./Addadshashanammu.zip)

## Solution
1. Unzipped ```Addadshashanammu.zip```
2. Repeatedly ran ``cd`` through the folder until the bottom layer containing a binary file called ```fang-of-haynekhtnamet```
3. Extracted the flag from the binary file running command: ```cat fang-of-haynekhtnamet | grep -aEo "picoC
TF{.+}"```

## Alternative Solution
1. Found non-folder files by running command:  ```find Addadshashanammu/ -type f```
2. Ouput containing file: ```Addadshashanammu/Almurbalarammi/Ashalmimilkala/Assurnabitashpi/Maelkashishi/Onnissiralis/Ularradallaku/fang-of-haynekhtnamet```
3. Checked file type by running command: ```file Addadshashanammu/Almurbalarammi/Ashalmimilkala/Assurnabitashpi/Maelkashishi/Onnissiralis/Ularradallaku/fang-of-haynekhtnamet```, which indicated it was in ELF format hence a binary file
4. Extracted flag by running command: ```cat Addadshashanammu/Almurbalarammi/Ashalmimilkala/Assurnabitashpi/Maelkashishi/Onnissiralis/Ularradallaku/fang-of-haynekhtnamet | grep -aEo "picoCTF{.+}"```

## Flag
picoCTF{l3v3l_up!_t4k3_4_r35t!_76266e38}