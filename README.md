Hi!! Would you like to build a small blockchain on your own? Here is a basic guide through which follows on developing a simple blockchain using python and its libraries. 
Lets first understand the term “BlockChain”. 

A Blockchain is simply a ledger that keeps a permanent record of all the transactions that take place sequentially in a secure, and unchangeable manner. It is a chain of ‘Blocks’ which consists of information and each and every block records all the recent transactions. Once a block is completed it will be added to the blockchain and so on. 
A ledger means a file that grows constantly. In the definition, it says as secure which means the Blockchain uses very advanced cryptography to make sure that the information is protected inside the blockchain. Once you enter any data to a block and that block is added to the Blockchain network it cannot be changed again. 
So now let's follow the simple steps on creating a blockchain.

Step 01- import hashlib library and create the Block Class.  

Hashlib module implements a common interface to different secure hash and message digest algorithms.It  Included secure hash algorithms such as SHA1, SHA224, SHA256, SHA384, and SHA512.
In the Block class, we create a constructor and accept parameters of ‘previous hash’ and the ‘transaction’. We assign those two values to 2 variables and join the values and assign them to a new variable called ‘string_to_hash’.  Then we convert the value in ‘string_to_hash’ to a hash value using the sha256 algorithm.
hash= transaction + hash of the previous block

Step 02- Let's create Blocks and add up to the Blockchain.

The first block of a blockchain is called “Genesis Block”. So we create an instance of Block class and assign a default value as “0000000” as the ‘previous hash’ and assign a transaction called “kavindu sent 7 BTC to kasun”. So this is will together generate a new hash which will become the previous hash for the second block. 
As above you can create many blocks as you want and add up it to the chain. All the blocks in the chain are connected through the hashes. You can see the generated hashes as the output. 

See! It is very easy and simple. I hope this article would encourage you to build your own blockchain. 




