import datetime, os

R = "\033[91m"  # Rouge
V = "\033[92m"  # Vert
J = "\033[93m"  # Jaune
B = "\033[94m"  # Bleu
C = "\033[96m"  # Cyan
W = "\033[0m"   # Blanc

os.makedirs("rapports", exist_ok=True)

def save(titre, resultat):
    heure = datetime.datetime.now().strftime("%Y-%m-%d_%H-%M")
    with open(f"rapports/{heure}_{titre}.txt", "w") as f:
        f.write(resultat)
    print(f"{V}[+] Rapport sauvegardé dans rapports/{W}")

print(f"{R}=================================================={W}")
print(f"{C}   LOIC DEFENSE HACKER - IA DE DEFENSE V2{W}")
print(f"{J}   Je ne pirate pas, je PROTEGE.{W}")
print(f"{R}=================================================={W}")
print(f"{V}1 - Analyser un lien suspect")
print(f"2 - Analyser un message suspect")
print(f"3 - Analyser un numero suspect")
print(f"4 - Quitter{W}")

choix = input(f"\n{B}Boss, que veux-tu analyser ? : {W}")

if choix == "1":
    url = input("Colle le lien : ")
    score = 0
    if "bit.ly" in url or "tinyurl" in url: score += 40
    if "free" in url or "gagne" in url: score += 30
    if "http://" in url: score += 20
    if "login" in url or "verif" in url: score += 10
    print(f"{R if score>=50 else J}Score de danger : {score}/100{W}")
    if score >= 50:
        print(f"{R}[!] DANGER : Ne clique PAS, probable phishing !{W}")
    else:
        print(f"{V}[*] Risque faible, mais vérifie sur VirusTotal{W}")
    save("lien", f"URL: {url}\nScore: {score}")

elif choix == "2":
    msg = input("Colle le message : ").lower()
    mots = ["gagne", "code", "urgent", "bloqué", "clique", "whatsapp", "cadeau", "transfert"]
    trouve = [m for m in mots if m in msg]
    score = len(trouve)*15
    print(f"{J}Mots d'arnaque trouvés : {trouve}{W}")
    print(f"{R if score>=45 else V}Score arnaque : {score}/100{W}")
    save("message", f"Message: {msg}\nScore: {score}")

elif choix == "3":
    num = input("Colle le numero : ")
    print(f"{C}[*] Lance pour analyse complete :{W}")
    print(f"phoneintel --info {num} | lolcat")
    save("numero", f"Numero: {num}")

else:
    print(f"{V}A plus Boss, reste protégé.{W}")

