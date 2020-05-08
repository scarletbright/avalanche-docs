# Feature Pipeline

## Subnet Creation

Currently there is only one subnet (the default subnet.) We want to allow users to create their own subnets, which may impose requirements upon those that validate the subnet.

## Governable Transaction Fees

Fees are essential for DDoS protection. Right now they’re being statically set at a fixed rate. Fees are already part of the Platform Chain, and we will be making that a governance parameter. We are also exploring a more flexible fee structure for the AVA token DAG.

## Cedrus Upgrade

Cedrus is a write-optimized database we're developing to replace LevelDB and thereby increase disk write speed. We do this because most reads are batched and loaded in-memory, but the writes are frequent.  A database built to optimize for writes rather than reads will noticeably improve node efficiency.

## Subnet Incentives

Some subnets will want a method for incentivising validators in the AVA platform to validate for their network. To assist with this, the Platform chain will offer a method to incentivize validators in AVA from a budget allocated to the subnetwork. This budget can increase as needed to keep validators checking the subnetworks.

## Atomic Commitment Across Blockchains

An advantage of the AVA platform is that blockchains are all using the same underlying protocol for consensus on their transactions. This enables transactions to atomically commit across multiple blockchains. These atomic commitments provide the capability for AVA validators to verify transactions across two or more blockchains. We envision atomic commitments as the primary mechanism for token transfer across the AVA platform.

## Expand Governance Parameters

Currently, the Platform chain has one governable parameter, time. The rest of the parameters are currently hard-coded for testing. We are going to add the ability to change them. This includes specifying how much each parameter can change, based on the last time they were modified.

## NAT Traversal

Our current library for peer-to-peer communication, salticidae, does not support NAT traversal. The lack of this feature makes it more difficult for nodes to run in heavily virtualized environments. It is essential we enable this functionality to enable development across a wider variety of network environments.  

## Pruning

Our current implementation stores the entire transaction history. We plan to implement various pruning algorithms.

## Node Reputation

We plan to add the ability for validators to track the uptime and virtuousness of other validators on the network. Currently, validators always vote to provide staking rewards to a validator leaving the staking set. Once uptime and virtuousness is tracked, a validator can vote to deny staking rewards for the validators which are not adhering to the promises made when they staked their AVA. Doing so improves the quality of service of stakers on the network.

## Blockchain Sandboxing

It’s important that blockchains not operate outside of their expected environment. We want to give developers freedom to create the blockchain they want, but we also must protect the network from malware threats. Our sandboxing solution will do just that.

## Improve Build Process (inc. static linking salticidae)

Our current build process includes the salticidae library. Salticidae is a highly efficient C++ p2p networking library and serves us well as it interfaces with any client implementation that can utilize C++ libraries. However, the build process needs expanding. We must support Windows, Mac OS X, various Linux and Unix distributions, and potentially other platforms including mobile. For this to work, we must be able to create statically linked version of the salticidae library or add the library to modern package management systems so they can be installed (a la homebrew or apt-get). This will improve our cross-platform capability, which is essential for reaching the widest audience of developers and validators.

## Memory Management

We want to improve our garbage collection pressure by re-using memory wherever possible will give our nodes significant performance gains and free up computation cycles for validating transactions. We will improve the memory management across the entire stack, especially focusing on snow consensus and snow consensus engines.

## Transaction Mempool (Staking)

In the Snowman protocol, if a block was rejected, the transactions that it contained are not necessarily invalid. We will place these transactions into a mempool and attempt to re-issue them so they are not dropped along with rejected blocks. This improves user experience as transactions are published across the network.

## Frosty Consensus Protocol

This is a leadered version of snowman consensus. The generic snowman implementation is a leaderless snowman consensus. This has a decrease in liveness guarantee but doesn’t depend on a leader. The leadered version of Snowman, dubbed “Frosty”, has an increase in liveness and is more performant.

## Explore BLS

We’re going to look into the possibility of changing addressing from secp256k1 with ECDSA to BLS. We are aware of the codebase implementing BLS in Golang here: [https://github.com/herumi/bls](https://github.com/herumi/bls). We’re going to consider the possibility of the switch as well as gauging the performance change. This study will lead us to decide if we will implement BLS for mainnet or stick with ECDSA.

## Addressing and PK Representation Changes

The current addressing system mimics the Bitcoin address system. We’re going to augment our system in the following way:
Add Reed-Solomon codes to private keys in addition to the checksum.
Add prefix byte for private key similar to WIF for the purpose of determining if a key is mainnet, testnet, or other ([https://en.bitcoin.it/wiki/Wallet_import_format](https://en.bitcoin.it/wiki/Wallet_import_format))
Add a prefix for versioning addresses of the format bytes(AVA + version#)

## Additional Features

* HD Mnemonic Wallet
* AVA Wallet GUI
* AVA Network Monitoring
* AVA DAG Explorer
* AVA Chain Explorer
* Binary Consensus on DAG
* Self-signing RPC Package (WASM?)
