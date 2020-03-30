#!/usr/bin/env python
# coding: utf-8

# In[4]:


import hashlib
# Blocks are connected using a hash
# hash= transaction + hash of the previous block


# In[5]:


class Block:
    def __init__(self,previous_hash,transaction):
        self.transaction=transaction
        self.previous_hash=previous_hash
        string_to_hash="".join(transaction)+previous_hash
        self.block_hash=hashlib.sha256(string_to_hash.encode()).hexdigest()


# In[6]:


# Here we create 3 Blocks
# Genesis block is the first block in the blockchain     

genesis_block=Block("0000000",["kavindu sent 5 BTC to kasun"]) # Here 00000 is just a number because we dont' have a previous block
print("Blcok hash of Genises Block:")
print(genesis_block.block_hash)

second_block= Block(genesis_block.block_hash, ["kasun sent 5 BTC to Indunil",
                                               "Lakshan sent 5 BTC to layya"])
print("Blcok hash of Second Block:")
print(second_block.block_hash)


Third_block= Block(genesis_block.block_hash, ["Kavindu sent 9 BTC to Indunil",
                                               "Kavinda sent 5 BTC to Dushan"])
print("Blcok hash of Third Block:")
print(Third_block.block_hash)


# In[ ]:





# In[ ]:




