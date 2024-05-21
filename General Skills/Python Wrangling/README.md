# PicoCTF2021 - Python Wrangling

## Description
Python scripts are invoked kind of like programs in the Terminal... Can you run [this Python script](./ende.py) using [this password](./pw.txt) to get [the flag](./flag.txt.en)?

## Solution
1. Inspected ```ende.py```, the usage shows: ```"Usage: "+ sys.argv[0] +" (-e/-d) [file]"``` and to decrypt a file: ```"'$ python "+ sys.argv[0] +" -d pole.txt'\n"```
2. ```flag.txt.en``` is the encrypted file to be passed in so run: ```python ende.py -d flag.txt.en```
3. When prompted with the password, extracted the password from ```pw.txt``` and inputted it: ```67c6cc9667c6cc9667c6cc9667c6cc96```
4. The program decrypted ```flag.txt.en``` giving the flag

## Flag
picoCTF{4p0110_1n_7h3_h0us3_67c6cc96}
