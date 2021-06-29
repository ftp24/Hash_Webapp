import hashlib
def MD5(password="hello"):
    hash_md5=hashlib.md5(str(password).encode('utf-8'))
    hex=hash_md5.hexdigest()
    return hex

def SHA1(password="hello"):
    hash_sha1=hashlib.sha1(str(password).encode('utf-8'))
    hex=hash_sha1.hexdigest()
    return hex

def SHA2(password="hello"):
    hash_sha2=hashlib.sha256(str(password).encode('utf-8'))
    hex=hash_sha2.hexdigest()
    return hex
