import random
from base import *

def get_hash_number():
    hashs = get_hashs_vac()
    
    hash = str(random.getrandbits(128))[:1]
    while(hash not in hashs):
        return hash
    
def checkNumber(number):
    if number:
        if number[0] == "8":
            if len(number)==11:
                return True
        
        if number[0:2]=="+7":
            if len(number)==12:
                return True
    return False




