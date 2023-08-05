import os
import sys
import rsa

pk, sk = rsa.newkeys(512)

def encrypt_data(path: str) -> list:
    data = []
    for file_name in os.listdir(path):
        file_path = f'{path}/{file_name}'
        data.append(rsa.encrypt(file_name.encode(), pk))
        with open(file_path) as f:
            for line in f.readlines():
                if len(line) != 0:
                    data.append(rsa.encrypt(line.encode(), pk))    
    return data


def decrypt_data(data: list) -> list:
    tr = []
    for line in data:
        tr.append(rsa.decrypt(line, sk).decode())
    return tr


path = sys.argv[1]
data = encrypt_data(path)
print(decrypt_data(data))
