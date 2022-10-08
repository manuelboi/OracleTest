from web3 import Web3
import asyncio

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

'''
# METHOD TEST

# Build transaction
transaction = contract.functions.setInformation(string).buildTransaction(
    {"chainId": 5, "from": walletAddress, "nonce": nonce})

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
'''


# define function to handle events and print to the console
# You can also setup any action after listening to the event
def handle_event(event):
    print(Web3.toJSON(event))


# asynchronous defined function to loop
# this loop sets up an event filter and is looking for new entires for the "PairCreated" event
# this loop runs on a poll interval
async def log_loop(event_filter, poll_interval):
    while True:
        for PairCreated in event_filter.get_new_entries():
            handle_event(PairCreated)
        await asyncio.sleep(poll_interval)


# when main is called
# create a filter for the latest block and look for the "PairCreated" event for the uniswap factory contract
# run an async loop
# try to run the log_loop function above every 2 seconds
def main():
    event_filter = contract.events.informationRequestEvent.createFilter(fromBlock='latest')
    loop = asyncio.get_event_loop()
    try:
        loop.run_until_complete(
            asyncio.gather(
                log_loop(event_filter, 2)))
    finally:
        # close loop to free up system resources
        loop.close()


if __name__ == "__main__":
    main()
