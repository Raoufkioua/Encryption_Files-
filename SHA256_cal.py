# Python program to find SHA256 hash string of a file
import hashlib
# To generate Unique ID name 
import uuid
 
def encrypt_sha256(filename):
    sha256_hash = hashlib.sha256()
    with open(filename,"rb") as f:
        File_name = uuid.uuid4()
        print(File_name)
    # Read and update hash string value in blocks of 4K
        for byte_block in iter(lambda: f.read(4096),b""):
            sha256_hash.update(byte_block)
        print(sha256_hash.hexdigest())
