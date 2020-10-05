import hashlib
class MerkelTreeHash(object):    
    def __init__(self):
        pass
    def find_merkel_hash(self,file_hashes):    #implemented using recursion
        blocks=[]
        if not file_hashes:
            raise ValueError("Missing file hashes for computing merkel tree hash")
        for m in sorted(file_hashes):
            blocks.append(m)
        list_len=len(blocks)
        while list_len % 2!=0:
            blocks.extend(blocks[-1:]) #even no of items are needed to group
            list_len=len(blocks)    
        secondary =[]  
        for k in [blocks[x:x+2] for x in range(0,len(blocks),2)]:
            hasher=hashlib.sha256()
            hasher.update(k[0]+k[1])
            secondary.append(hasher.hexdigest())
        if len(secondary)==1:
            return secondary[0][0:64]
        else:
            
            return self.find_merkel_hash(secondary)
if __name__=="__main__":
    import uuid
    file_hashes=[]
    for i in range(0,9):
        file_hashes.append(str(uuid.uuid4().hex))
        
    print("Finding the merkel tree hash of {0} random hashes".format(len(file_hashes)))
    obj=MerkelTreeHash()
    merkel_t=obj.find_merkel_hash(file_hashes)
    print("The Merkel tree hash of the hashes below is : {0}".format(merkel_t))
    print("\n")
    for i in range(len(file_hashes)):
        print("hash_"+str(i)+" :",file_hashes[i])

# Note :works fine in python 2
"""
Output :
Finding the merkel tree hash of 9 random hashes
The Merkel tree hash of the hashes below is : 055188eebe8ec9685e0b7c1b1bab143716f6fad8b36481137560515aa184af77


('hash_0 :', '80b4520c7af346bf82184177006a47f4')
('hash_1 :', '9c72c42289da464b9ebd0f4de31109ff')
('hash_2 :', '4ff8fe94aadb49e1811cbe1a0a5461bb')
('hash_3 :', 'a3a395ab50b940d78e5e090258d73fc9')
('hash_4 :', 'a9a633978f384d889bb9b5be637fb3b7')
('hash_5 :', '3d6d8b52cdcf423b9b1e9f591ced4fe3')
('hash_6 :', 'bb09b9a5e99d466898395575d8d41b03')
('hash_7 :', 'cd7f8f551c7d4ccb886b411e3ce8d5c4')
('hash_8 :', '85373238adf34903830259bcf5077010')"""