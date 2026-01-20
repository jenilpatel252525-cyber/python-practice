def isIPv4(ip):
    parts = ip.split('.')
    if len(parts) != 4:
        return False
    for p in parts:
        # must be digits only
        if not p.isdigit():
            return False
        # no leading zeros unless single digit 0
        if len(p) > 1 and p[0] == '0':
            return False
        # range check
        if not 0 <= int(p) <= 255:
            return False
    return True


def isIPv6(ip):
    parts = ip.split(':')
    if len(parts) != 8:
        return False

    valid_hex = set("0123456789abcdefABCDEF")  # ✅ using a set
    for p in parts:
        if not (1 <= len(p) <= 4):
            return False
        if not all(c in valid_hex for c in p):
            return False
    return True


def validIPAddress(queryIP):
    if queryIP.count('.') == 3 and isIPv4(queryIP):
        return "IPv4"
    elif queryIP.count(':') == 7 and isIPv6(queryIP):
        return "IPv6"
    else:
        return "Neither"


# 🔹 Examples
print(validIPAddress("172.16.254.1"))                 # IPv4
print(validIPAddress("2001:0db8:85a3:0:0:8A2E:0370:7334"))  # IPv6
print(validIPAddress("256.256.256.256"))              # Neither
print(validIPAddress("192.168.01.1"))                 # Neither
print(validIPAddress("2001:0db8:85a3::8A2E:037j:7334")) # Neither
