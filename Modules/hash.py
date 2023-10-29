import sys
import hashlib

def hashfun():
    # This function takes the input of a file and calculates the md5 and sha1 hash.
    # Outputs the value back on to the terminal

    filename = input("Enter the file name:")

    with open(filename, "rb") as f:
        bytes = f.read()
        readable_hash =  hashlib.md5(bytes).hexdigest();
        readable_hash2 = hashlib.sha1(bytes).hexdigest();

        print("========================================")
        print("MD5 hash value  :" + readable_hash)
        print("SHA1 hash value :" + readable_hash2)
        print("========================================")

    sys.stdout.write('### Returning back to main page ####')