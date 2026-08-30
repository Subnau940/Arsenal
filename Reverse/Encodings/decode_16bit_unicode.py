# ==========================================
# Template : Décodage 16-bits vers 2x8-bits
# ==========================================

chaine_encodee = '<INSERER_TA_CHAINE_ICI>'
resultat_clair = ""

for char in chaine_encodee:
    valeur = ord(char)
    
    # Extraction du 1er caractère (Octet de poids fort)
    # Mathématiquement : valeur // 256
    # En bit-à-bit    : valeur >> 8
    char1 = valeur // 256 
    
    # Extraction du 2eme caractère (Octet de poids faible)
    # Mathématiquement : valeur % 256
    # En bit-à-bit    : valeur & 0xFF
    char2 = valeur % 256  
    
    # Reconversion en texte et concaténation
    resultat_clair += chr(char1) + chr(char2)

print(resultat_clair)
