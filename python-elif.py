byte1 = 4
byte2 = 192
byte3 = 9
byte4 = 0

if byte1 < 0 or byte1 > 255 or byte2 < 0 or byte2 > 255 or byte3 < 0 or byte3 > 255 or byte4 < 0 or byte4 > 0:
    print("byte 1 tot byte 4 stellen samen geen geldig IP-adres voor")
elif byte1 == 10 or (byte1 == 172 and byte2 >= 16 and byte2 <= 31) or (byte1 == 192 and byte2 == 168):
    print("byte 1 tot byte 4 stellen samen een geldig IP-adres in het privébereik voor")
else:
    print("byte 1 tot byte 4 stellen samen een geldig IP-adres in het publieke bereik voor")
