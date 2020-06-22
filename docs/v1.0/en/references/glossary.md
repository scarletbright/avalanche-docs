# Glossary

## Address

An address is a notion that exists in certain blockchain-based applications for transferring value. 
Addresses hold value and value is transferred between addresses. Real-life entities control addresses 
and the value held in them by holding a private key, a secret piece of information that allows them 
to transfer value from them.

## AVA

AVA is the AVA network's native asset. It has two special uses on the AVA network:

* Validators must [stake](../core-concepts/overview.md#what-is-staking) AVA
* Transaction fees will be paid in AVA

## [Avalanche](../core-concepts/overview.md#what-is-avalanche)

Avalanche is a family of consensus protocols used by blockchains on the AVA network.
Avalanche-based protocols allow computers to agree on a large set of information very quickly and with high security.

## AVA Virtual Machine

The AVA Virtual Machine is one of the AVA network's built-in virtual machines. 
It defines an application for creating and trading smart assets.
In a slight abuse of notation, we also call the main instance of the AVM 
"the AVM" since this is the one people almost always use.

## Blockchain

A blockchain is an append-only ledger. Blockchains have the special property that nobody can re-write old sections of the ledger. 
Applications, such as payments systems, can be built atop blockchains. 

## CB58

CB58 is a format used to represent keys, addresses, and other binary values in web wallets and APIs.
It uses 58 lowercase letters, uppercase letters, and digits so values are easier to read and write.
CB58 is similar to [Base58Check], but uses a different checksum algorithm.

[Base58Check]: https://en.bitcoin.it/wiki/Base58Check_encoding

## Consensus Protocol

A consensus protocol is an algorithm, or series of steps, that a set of computers follow in order to reach agreement on some piece of information.
In a payments system, for example, the computers follow a protocol to agree on who has how much money.

## Gecko

Gecko is the Go implementation of an AVA node.

## Node

A node is a computer participating in the AVA network.

## Smart Digital Assets

A smart digital asset is a digital representation of a real-world thing such as an equity, bond, money etc.
They can have a complex ruleset that defines their behavior and how they are handled.
This ruleset can include things like, "can't be traded until next year," for example.

## [Subnetwork](../core-concepts/overview.md#what-are-subnets)

A subnetwork (or subnet) is a set of nodes that validate a set of blockchains.

## Transaction

A transaction queries or modifies the state of a blockchain.

## Validator

A validator is a node participating in the consensus protocol.
Validators work together to achieve consensus as to which transactions have taken place on a blockchain.

## [Virtual Machines](../core-concepts/overview.md#what-are-virtual-machines)

A Virtual Machine defines the application-level logic of a blockchain.
In technical terms, it defines a state machine.
It specifies the state that is held, the state transition function, and the transactions that clients can issue in order to query/modify the state.
Developers create Virtual Machines that implements some functionality and then create a blockchain that runs the Virtual Machine.
Every blockchain runs (is an instance of) a Virtual Machine.  