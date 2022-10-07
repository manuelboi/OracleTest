from web3 import Web3


# Configure Infura
w3 = Web3(Web3.HTTPProvider("https://goerli.infura.io/v3/a2d3ce8effcf445b8fea9dad109c9150"))
assert w3.isConnected()

# Contract infos
contractAddress = '0x7396949Df940541fD27c04ddE1a2eD9816Aa4242'
contractABI = '[{"inputs": [],"name": "informationRequest","outputs": [],"stateMutability": "nonpayable",' \
              '"type": "function"},{"inputs": [],"stateMutability": "nonpayable","type": "constructor"},{"anonymous": ' \
              'false,"inputs": [],"name": "informationRequestEvent","type": "event"},{"inputs": [{"internalType": ' \
              '"string","name": "information","type": "string"}],"name": "setInformation","outputs": [],' \
              '"stateMutability": "nonpayable","type": "function"},{"inputs": [],"name": "getInformation","outputs": ' \
              '[{"internalType": "string","name": "","type": "string"}],"stateMutability": "view","type": "function"}] '

# Wallet infos
walletAddress = '0x2f2a3bE0f87D2EC706576b457b527eBF1E38d168'
privateKey = ''
nonce = w3.eth.getTransactionCount(walletAddress)


# Contract instance create and link
contract = w3.eth.contract(address=contractAddress, abi=contractABI)

string = 'Information'

# METHOD TEST

# Build transaction
transaction = contract.functions.setInformation(string).buildTransaction({"chainId": 5, "from": walletAddress, "nonce": nonce})

# Sign transaction
signedTransaction = w3.eth.account.sign_transaction(transaction, private_key=privateKey)

# Send transaction
sentTransaction = w3.eth.send_raw_transaction(signedTransaction.rawTransaction)

# Wait for transaction receipt
transactionReceipt = w3.eth.wait_for_transaction_receipt(sentTransaction)
print(transactionReceipt)


# FUNCTION TEST

# Read from smart contract test
information = contract.functions.getInformation().call()
assert (information == string)
