# Loic Defense Hacker - Outil DEFENSIF
# Pour proteger ton propre reseau / ton propre PC

import socket
import sys

def scanner_defensif(cible):
    print(f"[*] Scan defensif de {cible} ...")
    print("[*] Ports ouverts detectes :")
    for port in [21, 22, 23, 80, 443, 3306, 8080]:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.settimeout(1)
        try:
            resultat = s.connect_ex((cible, port))
            if resultat == 0:
                print(f"[+] Port {port} : OUVERT - A VERIFIER")
            else:
                print(f"[-] Port {port} : Ferme")
        except Exception as e:
            print(f"[!] Erreur port {port} : {e}")
        finally:
            s.close()
    print("[*] Scan termine. Securise les ports ouverts.")

if __name__ == "__main__":
    cible = input("Entre ton IP a proteger (ex: 127.0.0.1) : ")
    scanner_defensif(cible)
