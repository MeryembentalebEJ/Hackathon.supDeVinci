import subprocess

def run_metasploit(ip):
    command = f"msfconsole -x 'use auxiliary/scanner/portscan/tcp;set RHOSTS {ip};run'"
    process = subprocess.Popen(command, stdout=subprocess.PIPE, shell=True)
    output, error = process.communicate()

    return output

# Lire le fichier avec les adresses IP
with open('ipaddresses.txt', 'r') as f:
    ip_addresses = f.read().splitlines()

# Ouvrir le fichier de résultats en mode 'écriture'
with open('results.txt', 'w') as result_file:
    # Lancer Metasploit pour chaque adresse IP
    for ip in ip_addresses:
        output = run_metasploit(ip)
        # Écrire les résultats dans le fichier
        result_file.write(f"Results for {ip}:\n")
        result_file.write(output.decode() + '\n')

print("Scan Metasploit terminé. Les résultats ont été écrits dans 'results.txt'.")