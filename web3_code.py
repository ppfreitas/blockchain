#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jun  7 01:23:12 2020

@author: pedro
"""
from web3 import Web3
import pandas as pd
import json

# development blockchain url
ganache_url = 'HTTP://127.0.0.1:9545'

# connect to bc
web3 = Web3(Web3.HTTPProvider(ganache_url))

# check if connected
web3.isConnected()

# retrieve all acounts
accounts = web3.eth.accounts
'''
# initiate cos names
companies_names = ['Solar Generation SA','Green Energy Co',
                   'Coal is Life','Thermal Gen', 'Go Green']
# associate one account to a name
comp_accounts = dict(zip(companies_names,accounts[-5:]))

# define private keys
private_keys = ['085d6ddf86c6c39412ac8b918535102fe44a9466911223a7c1b0659a7e5b0433', #index5
                 '53cc9809b4bc426b911b6e1a124e93bb200af6734467b9b463e6cab08fea80a1', #index6
                 '460c153a0f7bb413b8ce189c72d098563f647678dbaa041b2935bb9ee70ff8c4', #index7
                 'd6835c7dbf47be4733b537bfdbe9d64077ec246b81ab814e2f9457b5a347e26a', #index8
                 'e1c0fd218b2702d138e6af692dbd6c87d88e4cd3ecb4120bd56672ef2aecac93'] #index9

# associate keys to a name
comp_keys = dict(zip(companies_names,private_keys))
'''
# this is the contract after truffle compilation
build_abi2 = json.loads('[{"inputs": [],"payable": false,"stateMutability": "nonpayable","type": "constructor"},{"constant": true,"inputs": [{"internalType": "uint256", "name": "", "type": "uint256"}], "name": "readings", "outputs": [{ "internalType": "uint256", "name": "time", "type": "uint256"},{ "internalType": "uint256", "name": "sensor_id", "type": "uint256"}, {"internalType": "uint256", "name": "energy", "type": "uint256" }],    "payable": false, "stateMutability": "view", "type": "function"},{ "constant": true, "inputs": [], "name": "trans_id", "outputs": [{ "internalType": "uint256", "name": "", "type": "uint256"}], "payable": false, "stateMutability": "view", "type": "function"}, { "constant": false, "inputs": [{ "internalType": "uint256", "name": "_time", "type": "uint256" }, {"internalType": "uint256", "name": "_sensor", "type": "uint256"}, { "internalType": "uint256", "name": "_mwh", "type": "uint256"}], "name": "addReading", "outputs": [], "payable": false, "stateMutability": "nonpayable", "type": "function"}, { "constant": true, "inputs": [{ "internalType": "uint256", "name": "_trans_id", "type": "uint256"}], "name": "getReadInfo", "outputs": [{"internalType": "uint256", "name": "", "type": "uint256"}, { "internalType": "uint256", "name": "", "type": "uint256"}, {"internalType": "uint256", "name": "", "type": "uint256"}], "payable": false, "stateMutability": "view", "type": "function"}]')
byte_code2 = '0x608060405234801561001057600080fd5b506001808190555060405180606001604052806000815260200160008152602001600081525050610271806100466000396000f3fe608060405234801561001057600080fd5b506004361061004c5760003560e01c80630cc2c9da14610051578063949c88cc1461006f578063d5da886d146100bf578063e87c22481461010f575b600080fd5b610059610151565b6040518082815260200191505060405180910390f35b61009b6004803603602081101561008557600080fd5b8101908080359060200190929190505050610157565b60405180848152602001838152602001828152602001935050505060405180910390f35b6100eb600480360360208110156100d557600080fd5b81019080803590602001909291905050506101ab565b60405180848152602001838152602001828152602001935050505060405180910390f35b61014f6004803603606081101561012557600080fd5b810190808035906020019092919080359060200190929190803590602001909291905050506101d5565b005b60015481565b60008060008060008581526020019081526020016000206000015460008086815260200190815260200160002060010154600080878152602001908152602001600020600201549250925092509193909250565b60006020528060005260406000206000915090508060000154908060010154908060020154905083565b600160008154809291906001019190505550604051806060016040528084815260200183815260200182815250600080600154815260200190815260200160002060008201518160000155602082015181600101556040820151816002015590505050505056fea265627a7a72315820b65347214bb8990876d474522def4ded22ffe0791d424c43ce70d3f06e5124a564736f6c63430005100032'

#import json
#build_abi = json.loads('[{"constant": true,"inputs": [], "name": "amount", "outputs": [{ "internalType": "uint256", "name": "", "type": "uint256" }], "payable": false, "stateMutability": "view", "type": "function"}, { "constant": true, "inputs": [ { "internalType": "uint256", "name": "", "type": "uint256" }], "name": "readings", "outputs": [ {"internalType": "uint256", "name": "time", "type": "uint256"}, {"internalType": "uint256", "name": "energy", "type": "uint256" }, {"internalType": "bool", "name": "polluting", "type": "bool" }], "payable": false, "stateMutability": "view", "type": "function"}, {"constant": true, "inputs": [], "name": "trans_id", "outputs": [ { "internalType": "uint256", "name": "", "type": "uint256" }], "payable": false, "stateMutability": "view", "type": "function"}, {"constant": false, "inputs": [{ "internalType": "uint256", "name": "_time", "type": "uint256" }, {"internalType": "uint256", "name": "_mwh", "type": "uint256" }, {"internalType": "bool", "name": "_polluting", "type": "bool"}], "name": "addReading", "outputs": [], "payable": true, "stateMutability": "payable", "type": "function"}]')

# define contracts account
web3.eth.defaultAccount = accounts[0]

# deploy contract
Credits = web3.eth.contract(abi = build_abi2, bytecode = byte_code2)
tx_hash = Credits.constructor().transact()
tx_receipt = web3.eth.waitForTransactionReceipt(tx_hash)

contract = Credits(address=tx_receipt['contractAddress'])

# read simulated simplified simulated data
df = pd.read_csv('data_simple.csv')

# write 50 first data in blockchain
for i in range(50):
    date = int(df.iloc[i][1])
    sensor_id = int(df.iloc[i][2])
    sensor_reading = int(df.iloc[i][3])
    # store data into blockchain
    contract.functions.addReading(date,sensor_id,sensor_reading).transact()

# read 50 first data in blockchain
for trans_id in range(50):
    print(contract.functions.getReadInfo(trans_id).call())


