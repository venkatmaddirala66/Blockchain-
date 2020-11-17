import hashlib
import time
def node(r_t,d_ac,Blocks,temp,t_stamp,t_id,d_amt,db,c):   #used recursion to create nodes easily
    c+=1
    name=input("Name:")   #name refers to account holder
    amt=int(input("amount :"))  #initial amnt
    r_t.append((name,amt))    
    d_ac.append("initial")
    c_ac.append(name)
    c_amt.append(amt)
    d_amt.append(amt)
    db.append(0)
    t_stamp.append(time.time())
    msg=name+str(amt)+d_ac[0] 
    result = hashlib.sha256(msg.encode())
    tr=result.hexdigest()
    temp.append(tr)
    t_id.append(tr)
    print("want to add new node enter 1 ,else enter 0")
    create=int(input())
    if create==1:
            node(r_t,d_ac,Blocks,temp,t_stamp,t_id,d_amt,db,c)

            
def transactions(d_t,d_ac,tmp,t_stamp,start,t_limit,t_id,d_amt,db):
    s=input("enter sender :")
    r=input("enter receiver:")
    amount=int(input("enter amount :"))
    db.append(amount)   #list for debited amnt
    if amount<=d_t[s]:  #condition for checking amnt is available or not
        d_t[s]=d_t[s]-amount
        d_t[r]=d_t[r]+amount
        d_ac.append(s)
        c_ac.append(r)
        c_amt.append(d_t[r])  
        d_amt.append(d_t[s])
        print("Transaction is Successful")
    else:
        print("Invalid transaction")
    msg=s+str(amount)+r           #i used sender,rec,amt collectively as a parameters to generate hash
    result = hashlib.sha256(msg.encode())  #sha256 has algo is used
    tr=result.hexdigest()      # tr is transaction hash
    tmp.append(tr)
    t_id.append(tr)
    t_stamp.append(time.time())  
    if t_limit < 60:   # time limit is set to 60 min   
        t_limit = time.time() - start
        print("Transaction request :")
        req=int(input())
        if req==1:
            transactions(d_t,d_ac,tmp,t_stamp,start,t_limit,t_id,d_amt,db)
    else:
        new_Block_create(Blocks,tmp)
        tmp.clear()
        print("Transaction request :")
        req=int(input())
        if req==1:
            transactions(d_t,d_ac,tmp,t_stamp,start,t_limit,t_id,d_amt,db)
    
def ledger_of_transactions(d_ac,c_ac,c_amt,d_amt,Blocks,t_id,t_stamp,db,c):  #contains record of transactions
    print("\n")
    print("Debited_ac"," "*10,"Credited_ac"," "*10,"Debited amount"," "*10,"Balance"," "*10,"T_stamp")
    for i in range(len(c_ac)):
        print(d_ac[i]," "*15,c_ac[i]," "*15,db[i]," "*15,c_amt[i]," "*20,t_stamp[i])
        print("\n")
    print("\n")
    print("Accounts and their current balance after all trasactions")
    print("\n")
    print("Account"," "*10,"Balance"," "*10,"Trasaction_id")
    for i in range(c,len(c_ac)):
        if d_ac[i]!="initial":
                    print(d_ac[i]," "*15,d_amt[i]," "*10,t_id[i])  
                    print("\n")
                    print(c_ac[i]," "*15,c_amt[i]," "*10,t_id[i])

def new_Block_create(Blocks,tmp):   #function to create newblock after 1hr 
        Blocks.append(tmp)          #its actual implemenation is in transaction() fn
        print("new Block is created")

class Block_hash(object):  #Block hash class used for finding merkel root    
    def __init__(self):
        pass
    def find_merkel_hash(self,Block):
        blocks=[]
        if not Block:
            raise ValueError("Missing file hashes for computing merkel tree hash")
        for m in sorted(Block):
            blocks.append(m)
        list_len=len(blocks)
        while list_len % 2!=0:
            blocks.extend(blocks[-1:]) #even no of items are needed to group
            list_len=len(blocks)    
        secondary =[]  
        for k in [blocks[x:x+2] for x in range(0,len(blocks),2)]:
            hasher=hashlib.sha256()
            hasher.update(k[0].encode()+k[1].encode())
            secondary.append(hasher.hexdigest())
        if len(secondary)==1:
            return secondary[0][0:64]
        else:
            
            return self.find_merkel_hash(secondary)

class link:     #link class takes each block data for transactions
    def __init__(self, data): 
        self.data = data  # Assign data 
        self.next = None  # Initialize next as null
class Blockchain:   #this class used to form chain
    def __init__(self): 
        self.head = None
    def printList(self):     #printlist() used to retrieve blocks in chain
        temp = self.head 
        while (temp): 
            print (temp.data) 
            temp = temp.next
    
if __name__=="__main__":
    r_t=[]
    d_ac=[]    #debited ac
    c_ac=[]    #credited ac
    c_amt=[]   #credited amount
    Blocks=[]  
    temp=[]
    tmp=[]
    t_id=[]    #transaction id
    d_amt=[]   #debited amount
    t_stamp=[] #timestamp
    db=[]       
    t_limit=0  #time limit initally 0 and it is limit upto 1hr =60min 
    c=0
    start = time.time()   #time now
    print("Create nodes in Blockchain N/W")
    node(r_t,d_ac,Blocks,temp,t_stamp,t_id,d_amt,db,c) 
    d_t=dict(r_t)
    Blocks.append(temp)
    print("Transaction request :")   #to do transaction press 1 else 0
    req=int(input())
    if req==1:
        transactions(d_t,d_ac,tmp,t_stamp,start,t_limit,t_id,d_amt,db)
        ledger_of_transactions(d_ac,c_ac,c_amt,d_amt,Blocks,t_id,t_stamp,db,c)
    else:
        ledger_of_transactions(d_ac,c_ac,c_amt,d_amt,Blocks,t_id,t_stamp,db,c)
    merkel_t=[]
    obj=Block_hash() 
    for i in range(len(Blocks)):
        if Blocks[i]!=[]:
            merkel_t.append(obj.find_merkel_hash(Blocks[i]))
    #print(merkel_t)            #use this print to see block hashes
    b=Blockchain()
    #linking blocks using linkedlist
    s=[0]*len(Blocks)
    for i in range(len(Blocks)):
        if i==0:
            b.head=link(Blocks[i])
        else:
            s[i]=link(Blocks[i])
    for i in range(len(Blocks)):
        if i==0:
            b.head.next=s[i+1]
        elif i!=len(Blocks)-1:
            s[i].next=s[i+1]
        else:
            s[i].next=None   
    #print("Blockchain is :")
    #print(b.printList())    #use this print to see blocks and their transactions
    print("Hence Blockchain is created")