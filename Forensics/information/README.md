# PicoCTF2021 - information

## Description
Files can always be changed in a secret way. Can you find the flag? [cat.jpg](./cat.jpg)

## Solution
1. Analysed metadata of ```cat.jpg``` by running ```exiftool cat.jpg```
2. Under the ```License``` header, noticed a base64 value: ```cGljb0NURnt0aGVfbTN0YWRhdGFfMXNfbW9kaWZpZWR9```
3. Used [CyberChef](https://gchq.github.io/CyberChef/#recipe=From_Base64('A-Za-z0-9%2B/%3D',true,false)&input=Y0dsamIwTlVSbnQwYUdWZmJUTjBZV1JoZEdGZk1YTmZiVzlrYVdacFpXUjk) to decode string from base64

## Flag
picoCTF{the_m3tadata_1s_modified}
