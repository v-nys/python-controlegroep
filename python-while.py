number_of_host_addresses = 7 # naar eigen keuze, test wat opties uit
number_of_host_bits = 1
available_host_addresses = 0
while available_host_addresses < number_of_host_addresses and number_of_host_bits < 33:
    number_of_host_bits += 1
    available_host_addresses = (available_host_addresses + 2) * 2 - 2
if number_of_host_bits >= 33:
    print("Je hebt meer hostbits nodig dan er bits in een IPv4-adres zijn.")
else:
    print("Je hebt " + str(number_of_host_bits) + " bits nodig")
