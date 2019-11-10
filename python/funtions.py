#!\workspace\python37\python

# How to import important libraries 

import hashlib
import os
import binascii

# Create a function that has only one parameter 

def testing(r):
    print(r)

# Testing the fuction

testing("this output")

# Definition how to create a hash of a password adding salt

def hash_password(password):
    """Hash a password for storing."""
    salt = hashlib.sha256(os.urandom(60)).hexdigest().encode('ascii')
    pwdhash = hashlib.pbkdf2_hmac('sha512', password.encode('utf-8'), salt, 100000)
    pwdhash = binascii.hexlify(pwdhash)
    return (salt + pwdhash).decode('ascii')
 
# Autenticate user

def verify_password(stored_password, provided_password):
    """Verify a stored password against one provided by user"""
    salt = stored_password[:64]
    stored_password = stored_password[64:]
    pwdhash = hashlib.pbkdf2_hmac('sha512', provided_password.encode('utf-8'), salt.encode('ascii'), 100000)
    pwdhash = binascii.hexlify(pwdhash).decode('ascii')
    return pwdhash == stored_password

# Print the result 

stored_password = hash_password('Clave')

print(stored_password)

print(verify_password(stored_password, 'Clave'))

print(verify_password(stored_password, 'MalaClave'))
