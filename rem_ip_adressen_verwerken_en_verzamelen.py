def verzamel_ip_adressen():
    result = []
    ip = input("Wat is het volgende IP-adres? Duw meteen op enter om af te sluiten.\n").strip()
    while ip != "":
        result.append(ip)
        ip = input("Wat is het volgende IP-adres? Duw meteen op enter om af te sluiten.\n").strip()
    return result
