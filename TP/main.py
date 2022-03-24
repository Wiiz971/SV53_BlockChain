# fichier main.py
"""
une Blockchain basique sur Python

pip install ecdsa
"""

import hashlib
from ecdsa import SigningKey


class GeekCoinBlock:
    
    def __init__(self, previous_block_hash, transaction_list,signature,proof=1):

        self.previous_block_hash = previous_block_hash
        self.transaction_list = transaction_list

        self.block_data = f"{' - '.join(transaction_list)} - {previous_block_hash}"
        self.block_hash = hashlib.sha256(self.block_data.encode()).hexdigest()
        self.block_signature = signature
        self.proof = proof
    
class Blockchain:
    def __init__(self):
        self.chain = []
        self.generate_genesis_block()
        self.difficulty = 2

    
    def generate_genesis_block(self):
        self.chain.append(GeekCoinBlock("0", ['Genesis Block'],0))
    
        ##################### Construction de la preuve de travail ############################
   
    def proof_of_work(self, previous_proof):
         new_proof = 1
         check_proof = False
          
         while check_proof is False:
             hash_operation = hashlib.sha256(
                 str(new_proof**2 - previous_proof**2).encode()).hexdigest()
             if hash_operation[:5] == '00000':
                 check_proof = True
             else:
                 new_proof += 1
                  
         return new_proof
     
    def create_block_from_transaction(self, transaction_list):
        previous_block_hash = self.last_block.block_hash
        
        ##################### Insertion de la preuve de travail ############################
        previous_proof = self.last_block.proof
        
        proof = Blockchain().proof_of_work(previous_proof)
    
        ##################### Insertion d'une signature ############################
        
        message= f"{' - '.join(transaction_list)} - {previous_block_hash}"
        y = hashlib.sha256(message.encode()).hexdigest()
        y = y.encode()
        sk1 = SigningKey.generate() # clé privée
        sk_string = sk1.to_string()


        vk1 = sk1.verifying_key #clé publique
        y1 = sk1.sign(y) #signature
        assert vk1.verify(y1, y)
        
        #print ("Clee privee = %s \n Cle publique = %s \n Message chiffre = %s \n Signature = %s" %(sk_string.hex(),vk1.to_string("compressed").hex(),y.decode(),int.from_bytes(y1, byteorder = 'big')))
        
        self.chain.append(GeekCoinBlock(previous_block_hash, transaction_list,int.from_bytes(y1, byteorder = 'big'),proof))
    
    
    ##################### Verification de la validite de la chaine ############################
    
    def chain_valid(self, chain):
        previous_block = chain[0]
        block_index = 1
         
        while block_index < len(chain):
            block = chain[block_index]
            previous_code_message = f"{' - '.join(previous_block.transaction_list)} - {previous_block.previous_block_hash}"
            if block.previous_block_hash != hashlib.sha256(previous_code_message.encode()).hexdigest():
                return False
            
            previous_proof = previous_block.proof
            proof = block.proof
            hash_operation = hashlib.sha256(
                str(proof**2 - previous_proof**2).encode()).hexdigest()
             
            if hash_operation[:5] != '00000':
                return False
            previous_block = block
            block_index += 1
         
        return True
    
    ##################### Affichage de la chaine ############################
               
    def display_chain(self):        
        for i in range(len(self.chain)):
            print(f"Data {i + 1}: {self.chain[i].block_data}")
            print(f"Signature {i + 1}: {self.chain[i].block_signature}")
            print(f"Hash {i + 1}: {self.chain[i].block_hash}")
            print(f"Proof of work {i + 1}: {self.chain[i].proof}\n")
       
            
    ##################### Retour du dernier block ############################
    @property
    def last_block(self):
        return self.chain[-1]



############################### MAIN PROGRAM ######################################
t1 = "J'ai dépensé 5 € chez amazone"
t2 = "J'ai dépensé 70 € à Total"
t3 = "J'ai reçu 2100€ de salaire"
t4 = "J'ai fait 100€ de course à Auchan"
t5 = "J'ai payé 110€ de facture d'électricité"
t6 = "J'ai payé 30€ de facture de téléphone"


myblockchain = Blockchain()



myblockchain.create_block_from_transaction([t1, t2])
myblockchain.create_block_from_transaction([t3, t4])
myblockchain.create_block_from_transaction([t5, t6])

valid = myblockchain.chain_valid(myblockchain.chain)

#On verifie que la chaine est valide
if valid:
    print("La Blockchain est valide.\n\n")
    
    #Affichage du contenu de la chaine (block par block)
    myblockchain.display_chain()
else:
     print("La Blockchain n'est pas valide.")
     



 
    