def read_ip(line):
    return [int(elem) for elem in line.split(".")]

def read_ips():
    lst = []
    with open('ips.txt') as fh:
        for line in fh.readlines():
            lst.append(read_ip(line))
    return lst
