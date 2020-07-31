# Credits tracker network
by Pedro Freitas and Mardel Faria


## General comments:

In our fictious world, we have 5 power plants, some of them making use of clean energy sources, and others not. We simulated a few daily readings for energy generation for each of the companies. We also created some additional data that might lead to interesting observations, like geographical location. Having the data ready, we also did a simpler dataset (converting time to integers and removing unnecessary columns) to be loaded into the blockchain.

We used the ganache development environment for our DApp. We ran the network on HTTP://127.0.0.1:9545.

We also wrote smart contract in solidity that stores the sensors reading in our blockchain. We chose to use the python package web3py to interact with our blockchain. We did not choose to create a user interface because in our solution data is loaded automatically from sensor readings. 

The python script runs the following tasks:
	- Connect to the blockchain
	- Load the compiled contract's ABI and Bytecode into the blockchain
	- Load data to the blockchain
	- Read entries

The analytics part of the project was made using R Flexdashboard. It is a dashboard to follow to power generation of the plants over time. 



## Instructions:

1 - Quick start a new ganache network on HTTP://127.0.0.1:9545.
2 - Run the web3_code.py to load the contract into the blockchain, store data, and retrieve information. We recommend to run it line by line.
3 - Open ./dashboard/dashboard.html to see the dashboard created in R Shiny. It can also be found on https://rpubs.com/ppfreitas/creditsdash.



## Main files dictionary:

1 - Credits.Sol: Smart contract we wrote to store the sensor readings. Initially we wanted it to do transactions between accounts automatically, but we were having a hard time for it to compile (apparentely is not so simple to transfer ether to the contracts account);

2 - web3_code.py: Python script to interact with the blockchain

3 - ./dashboard/dashboard.html: R Flexdashboard dashboard. It can also be found on https://rpubs.com/ppfreitas/creditsdash.

4 - slides_analytics.pdf: Pitch slides.

5 - ./credits_contract/: We don't use this folder for anything other than extracting the ABI and bytecode of the compiled contract.



## What went wrong:

1 - We did not achieve to write the contract to do the credit transfer automatically. Right now, the contract exists only to store data.


