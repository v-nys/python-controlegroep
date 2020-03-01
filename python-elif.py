byte1 = 4
byte2 = 192
byte3 = 9
byte4 = 0

if byte1 < 0 or byte1 > 255 or byte2 < 0 or byte2 > 255 or byte3 < 0 or byte3 > 255 or byte4 < 0 or byte4 > 0:
    print("de vier bytes vormen geen geldig IPv4-adres")
elif byte1 == 10:
    print("de vier bytes vormen een IPv4-adres in het bereik 10.0.0.0/8")
else:
    print("de vier bytes vormen een IPv4-adres buiten het bereik 10.0.0.0/8")
