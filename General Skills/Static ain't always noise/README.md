# PicoCTF2021 - Static ain't always noise

## Description
Can you look at the data in this binary: [static](./static)? This [BASH script](./ltdis.sh) might help!

## Solution
1. Noted that ```ltdis.sh``` takes in a binary file and dissassembles it to assemby code, hence ```echo "Attempting disassembly of $1 ..."```
2. Ran ```./ltdis.sh static``` (ensure you have execute permissions which you can get by ```chmod +x ltdis.sh```) which displayed output:
```
Attempting disassembly of static ...
Disassembly successful! Available at: static.ltdis.x86_64.txt
Ripping strings from binary with file offsets...
Any strings found in static have been written to static.ltdis.strings.txt with file offset
```
3. Suspected flag was a string located in ```static.ltdis.strings.txt```
4. Extracted the flag by running command: ```cat static.ltdis.strings.txt | grep -Eo "picoCTF{.+}"```

## Flag
picoCTF{d15a5m_t34s3r_f6c48608}