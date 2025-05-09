BLACKLIST = {"192.168.1.10", "10.0.0.5"}

def es_maliciosa(ip):
    return ip in BLACKLIST

if __name__ == "__main__":
    ip = input("Introduce una dirección IP: ")
    if es_maliciosa(ip):
        print(f"La IP {ip} es MALICIOSA.")
    else:
        print(f"La IP {ip} es SEGURA.")
