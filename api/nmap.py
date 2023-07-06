import socket
import netifaces
import subprocess
import xmltodict
import json

XML_PATH = "/home/cyberbox/data/nmapscan.xml"

def get_IP_NETMASK(interface):
    # Obtenez l'adresse IP
    ip = netifaces.ifaddresses(interface)[netifaces.AF_INET][0]['addr']

    # Obtenez le Netmask
    netmask = netifaces.ifaddresses(interface)[netifaces.AF_INET][0]['netmask']

    # Conversion du Netmask en format CIDR
    netmask = sum(bin(int(x)).count('1') for x in netmask.split('.'))

    # Concaténation de l'adresse IP et du Netmask
    IP_NETMASK = ip + '/' + '25'

    return IP_NETMASK

def nmap_call():
    # Obtenez le nom de l'interface réseau principale
    interface = netifaces.gateways()['default'][netifaces.AF_INET][1]

    # Obtenez l'adresse IP et le Netmask et stockez-les dans la variable IP_NETMASK
    IP_NETMASK = get_IP_NETMASK(interface)

    print(IP_NETMASK)

    # Commande Nmap à exécuter
    command = f"nmap -p1-100 -oX {XML_PATH} {IP_NETMASK}"

    # Exécution de la commande
    process = subprocess.Popen(command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)

    # Récupération de la sortie et des erreurs
    output, error = process.communicate()

    # Vérification du code de sortie
    if process.returncode == 0:
        print("Analyse Nmap terminée avec succès.")
        print("Résultats :")
        print(output.decode('utf-8'))
    else:
        print("Une erreur s'est produite lors de l'exécution de la commande Nmap :")
        print(error.decode('utf-8'))
        return []

    with open('/home/cyberbox/data/nmapscan.xml') as xml_file:
        data_dict = xmltodict.parse(xml_file.read())
        return json.dumps(data_dict, indent=4)

    return []
    # with open('outputnmapscan.json', 'w') as json_file:
    #     json_file.write(json_data)
