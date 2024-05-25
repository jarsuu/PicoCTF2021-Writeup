# PicoCTF2021 - tunn3l v1s10n

## Description
We found this [file](./tunn3l_v1s10n). Recover the flag.

## Solution
1. Analysed the hex content of the file by running command: `hexdump -C tunn3l_v1s10n | head`
2. `42 4d` file signature is a bitmap file
3. Opening the image by running command: `display tunn3l_v1s10n ` shows a somewhat cropped image with text of "noflag{sorry}"
4. From [this site](https://www.ece.ualberta.ca/~elliott/ee552/studentAppNotes/2003_w/misc/bmp_file_format/bmp_file_format.htm), it says that the width and height of bitmaps occur at byte 18 and 22 respectively
5. Created duplicate of original file as `tunn3l_v1s10n_copy`
6. Edited the hex content of the file by running command: `hexedit tunn3l_v1s10n_copy`
7. Changed the height bytes from `32 01` to `32 03` to extend the height of the image
8. Opened up image again running command: `display tunn3l_v1s10n_copy`
which contained the flag

## Flag
picoCTF{qu1t3_a_v13w_2020}