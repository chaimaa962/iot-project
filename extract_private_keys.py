import json
import os
from eth_account import Account
from eth_keyfile import decode_keyfile_json

password = "123"

for i in range(1, 5):
    keystore_dir = f"node{i}_data/keystore"
    if not os.path.exists(keystore_dir):
        print(f"❌ Node {i}: pas de keystore")
        continue
    
    files = os.listdir(keystore_dir)
    if not files:
        print(f"❌ Node {i}: keystore vide")
        continue
    
    keystore_file = os.path.join(keystore_dir, files[0])
    
    try:
        with open(keystore_file, 'r') as f:
            keyfile = json.load(f)
        
        # Déchiffrer la clé privée
        private_key_bytes = decode_keyfile_json(keyfile, password)
        private_key_hex = private_key_bytes.hex()
        
        # Récupérer l'adresse
        address = files[0].split('--')[-1]
        
        print(f"\n{'='*60}")
        print(f"🔑 NŒUD {i}")
        print(f"{'='*60}")
        print(f"Adresse: 0x{address}")
        print(f"Clé privée: {private_key_hex}")
        print(f"Clé avec 0x: 0x{private_key_hex}")
        print(f"{'='*60}")
        
        # Sauvegarder dans un fichier
        with open(f"node{i}_private_key.txt", "w") as f:
            f.write(private_key_hex)
            
    except Exception as e:
        print(f"❌ Node {i}: {e}")

print("\n✅ Les clés privées ont été sauvegardées dans node*_private_key.txt")
