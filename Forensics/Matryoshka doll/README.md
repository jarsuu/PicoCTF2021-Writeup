# PicoCTF2021 - Matryoshka doll

## Description
Matryoshka dolls are a set of wooden dolls of decreasing size placed one inside another. What's the final one? Image: [this](./dolls.jpg)

## Solution
1. Used [foremost](https://www.kali.org/tools/foremost/) to extract hidden content initially from ```dolls.jp``` by running command: ```foremost dolls.jpg```
2. ```cd output```
3. ```ouput``` folder contained the ```zip``` folder with a .zip file
4. unzipped the file which extracts a ```base_images``` folder
5. ```cd base_images```
6. ```base_images``` folder contained a .jpg file
7. Ran ```foremost [.jpg file]``` and repeated the cycle from Step 2 until the bottom layer
8. The bottom layer contained ```flag.txt``` holding the [flag](./output/base_images/output/base_images/output/base_images/output/flag.txt)

## Flag
picoCTF{ac0072c423ee13bfc0b166af72e25b61}