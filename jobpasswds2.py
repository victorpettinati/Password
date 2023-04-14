import hashlib, json, os

f = open("passwords.json", "a")
f.write("")
f.close()

# Lire les lignes d'un fichier et les stocker dans une liste
with open('passwords.json', 'r') as fichier:
    elements = fichier.readlines()

found_duplicate = False

for i in range(len(elements)):
    for j in range(i + 1, len(elements)):
        if elements[i] == elements[j]:
            found_duplicate = True
            break
    if found_duplicate:
        break

if found_duplicate:
    print("Il existe au moins deux éléments identiques dans le tableau.")
else:
    print("Aucun élément identique trouvé dans le tableau.")

password = input("Veuillez saisir un mot de passe: \n ")
return_val= True
rep = os.path.dirname((__file__))
chemin = os.path.join(rep,"passwords.json")

if len(password) < 8:
    print("Le mot de passe doit avoir une longueur minimale de 8 caractères")
    return_val= False
elif not any(mot.isupper() for mot in password):
    print("Le mot de passe doit contenir au moins une lettre majuscule")
    return_val= False
elif not any(mot.islower() for mot in password):
    print("Le mot de passe doit contenir au moins une lettre minuscule")
    return_val= False
elif not any(mot.isdigit() for mot in password):
    print("Le mot de passe doit contenir au moins un chiffre")
    return_val= False
elif not any(mot in ['!', '@','?', '#', '$', '%', '^', '&', '*', '(', ')', '-', '_', '+', '=', '.'] for mot in password):
    print("Le mot de passe doit contenir au moins un caractère spécial")
    return_val= False
else:
    return_val= True
    print("Le mot de passe est sécurisé ! :" + password)

password_bytes = password.encode('utf-8')
hash_object = hashlib.sha256(password_bytes)
hash_hex = hash_object.hexdigest()
print( hash_hex)
with open(chemin, "a") as f:
    json.dump(hash_hex, f)
    f.write("\n")