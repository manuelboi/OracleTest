from web3 import Web3
# from web3.auto import w3
import json
import pprint

# Trying EIP20_ABI
EIP20_ABI = json.loads('[{"constant":true,"inputs":[],"name":"name","outputs":[{"name":"","type":"string"}],'
                       '"payable":false,"stateMutability":"view","type":"function"},{"constant":false,"inputs":[{'
                       '"name":"_spender","type":"address"},{"name":"_value","type":"uint256"}],"name":"approve",'
                       '"outputs":[{"name":"","type":"bool"}],"payable":false,"stateMutability":"nonpayable",'
                       '"type":"function"},{"constant":true,"inputs":[],"name":"totalSupply","outputs":[{"name":"",'
                       '"type":"uint256"}],"payable":false,"stateMutability":"view","type":"function"},'
                       '{"constant":false,"inputs":[{"name":"_from","type":"address"},{"name":"_to",'
                       '"type":"address"},{"name":"_value","type":"uint256"}],"name":"transferFrom","outputs":[{'
                       '"name":"","type":"bool"}],"payable":false,"stateMutability":"nonpayable","type":"function"},'
                       '{"constant":true,"inputs":[],"name":"decimals","outputs":[{"name":"","type":"uint8"}],'
                       '"payable":false,"stateMutability":"view","type":"function"},{"constant":true,"inputs":[{'
                       '"name":"_owner","type":"address"}],"name":"balanceOf","outputs":[{"name":"",'
                       '"type":"uint256"}],"payable":false,"stateMutability":"view","type":"function"},'
                       '{"constant":true,"inputs":[],"name":"symbol","outputs":[{"name":"","type":"string"}],'
                       '"payable":false,"stateMutability":"view","type":"function"},{"constant":false,"inputs":[{'
                       '"name":"_to","type":"address"},{"name":"_value","type":"uint256"}],"name":"transfer",'
                       '"outputs":[{"name":"","type":"bool"}],"payable":false,"stateMutability":"nonpayable",'
                       '"type":"function"},{"constant":true,"inputs":[{"name":"_owner","type":"address"},'
                       '{"name":"_spender","type":"address"}],"name":"allowance","outputs":[{"name":"",'
                       '"type":"uint256"}],"payable":false,"stateMutability":"view","type":"function"},'
                       '{"anonymous":false,"inputs":[{"indexed":true,"name":"_from","type":"address"},'
                       '{"indexed":true,"name":"_to","type":"address"},{"indexed":false,"name":"_value",'
                       '"type":"uint256"}],"name":"Transfer","type":"event"},{"anonymous":false,"inputs":[{'
                       '"indexed":true,"name":"_owner","type":"address"},{"indexed":true,"name":"_spender",'
                       '"type":"address"},{"indexed":false,"name":"_value","type":"uint256"}],"name":"Approval",'
                       '"type":"event"}]')

# Contract address and abi
address = '0xa688D975311CFC7e634B8877dC508B527eF4566E'
abi = json.loads('[{"inputs": [],"name": "informationRequest","outputs": [],"stateMutability": "nonpayable", '
                 '"type": "function"},{"inputs": [],"stateMutability": "nonpayable","type": "constructor"},'
                 '{"anonymous": false,"inputs": [],"name": "informationRequestEvent","type": "event"},{"inputs": [{'
                 '"internalType": "string","name": "information","type": "string"}],"name": "storeInformation",'
                 '"outputs": [],"stateMutability": "nonpayable","type": "function"},{"inputs": [],'
                 '"name": "_information","outputs": [{"internalType": "string","name": "","type": "string"}],'
                 '"stateMutability": "view","type": "function"}]')

finalAbi = abi + EIP20_ABI

# Connect to infura
w3 = Web3(Web3.HTTPProvider("https://mainnet.infura.io/v3/a2d3ce8effcf445b8fea9dad109c9150"))

# Create contract instance
contract = w3.eth.contract(address=address, abi=finalAbi)
# Test connection
print(w3.isConnected())

# Link to wallet?
nonce = w3.eth.get_transaction_count('0xb8f8597067bB30cA102869d6dc0e1ddb1a58D4c6')
# Wallet private key
private_key = "private_key"

# Test contract link
# print(contract.get_function_by_name('storeInformation'))

# Building transaction
transaction = contract.functions.transfer(
    address,
    1,
).build_transaction({
    'chainId': 1,
    'gas': 70000,
    'maxFeePerGas': w3.toWei('2', 'gwei'),
    'maxPriorityFeePerGas': w3.toWei('1', 'gwei'),
    'nonce': nonce,
})

# Transaction signing
signed_transaction = w3.eth.account.sign_transaction(transaction, private_key=private_key)

w3.eth.send_raw_transaction(signed_transaction.rawTransaction)

# contract.functions.storeInformation('Information').transfer()
# receipt = w3.eth.wait_for_transaction_receipt(transaction)
# print("Transaction receipt mined:")
# pprint.pprint(dict(receipt))
