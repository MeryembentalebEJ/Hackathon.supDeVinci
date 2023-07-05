import json
import re

def extract_ip(data, ip_addresses):
    # Pattern regex pour identifier une adresse IP
    ip_pattern = re.compile(
        r"\b(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\b"
    )

    if isinstance(data, dict):
        for key, value in data.items():
            if key == "@addr" and ip_pattern.match(value):
                ip_addresses.append(value)
            elif isinstance(value, (dict, list)):
                extract_ip(value, ip_addresses)
    elif isinstance(data, list):
        for item in data:
            extract_ip(item, ip_addresses)

# Ouvrez votre fichier json
with open('outputnmapscan.json') as f:
    data = json.load(f)

# Liste pour stocker toutes les adresses IP trouvées
ip_addresses = []

# Extrayez les adresses IP
extract_ip(data, ip_addresses)

# Écrivez toutes les adresses IP trouvées dans un nouveau fichier texte
with open('ipaddresses.txt', 'w') as f:
    for ip in ip_addresses:
        f.write(ip + '\n')