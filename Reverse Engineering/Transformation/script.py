enc_flag = open("enc", "r").read().strip()
flag = ""

for i in enc_flag:
    # 16 bits per char
    combined = ord(i)
    
    # first 8 bits >> 8
    high = (combined & 0xff00) >> 8
    
    # last 8 bits
    low = combined & 0x00ff
    
    flag += chr(high) + chr(low)

print(flag)
    