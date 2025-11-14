import hashlib

def hash_password(password):
    # Encode the string, then hash it, then convert to hex
    hashed = hashlib.sha256(password.encode()).hexdigest()
    return hashed

# Example usage:
password = input("Enter your password: ")
print("SHA-256 Hash:", hash_password(password))
