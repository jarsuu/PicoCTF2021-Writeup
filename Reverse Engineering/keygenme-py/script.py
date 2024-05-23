import hashlib

# extracted from keygenme-trial.py
key_part_static1_trial = "picoCTF{1n_7h3_|<3y_of_"
key_part_static2_trial = "}"
bUsername_trial = b"MORTON"

# order of indexes to extract from SHA256 hash
indexes = [4, 5, 3, 6, 2, 7, 1, 8]

hashed_username = hashlib.sha256(bUsername_trial).hexdigest()

key_part_dynamic_trial = ""
for i in indexes:
    key_part_dynamic_trial += hashed_username[i]
    
# combine key parts
key = key_part_static1_trial + key_part_dynamic_trial + key_part_static2_trial
print(key)



