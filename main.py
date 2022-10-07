from web3 import Web3


# Configuring Infura
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


# Contract instance creating and linking
contract = w3.eth.contract(address=contractAddress, abi=contractABI)

# Reading from smart contract
information = contract.functions.getInformation().call()
assert (information == "TestInformation")
