import hashlib 
msg=input("Enter the Message :")
hash_value = hashlib.sha256(msg.encode()) 
print("hash_value :",hash_value,"\n")
print("The hexadecimal equivalent 32-bit hash of SHA256 is : ") 
print(hash_value.hexdigest())
"""
Output :
Enter the Message :I love Blockchain
hash_value : <sha256 HASH object @ 0x05F41788> 

The hexadecimal equivalent 32-bit hash of SHA256 is : 
01298a37f6c0cacbd84251eff5281994e5ab0085a33baa3eb46dc52ef9695a47  """