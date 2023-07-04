import subprocess
import socket
XML_PATH = "../log/scan-hackathon.xml"



def nmap_call ():
    # Obtenir l'adresse IP de la machine
    ip_address = socket.gethostbyname(socket.gethostname())
    print("Adresse IP de la machine :", ip_address)

    # Obtenir le sous-réseau de l'adresse IP
    subnet = '.'.join(ip_address.split('.')[:3]) + '.0/24'
    print("Analyse du réseau !")

    # Commande Nmap à exécuter
    command = f"nmap -F -oX {XML_PATH} {subnet}"

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