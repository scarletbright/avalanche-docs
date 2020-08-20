# Glossary

## Address

An address is a notion that exists in certain blockchain-based applications for transferring value. 
Addresses hold value and value is transferred between addresses. Real-life entities control addresses 
and the value held in them by holding a private key, a secret piece of information that allows them 
to transfer value from them.

The Avalanche platform is not prescriptive about addressing schemes. Each VM may select its own addressing scheme. 

The Avlanche C-Chain follows the EVM addressing system. 

The Avalanche X-Chain and P-Chain use their own addressing system. The 33-byte public key of the Secp256k1 keypair is hashed once using SHA256 and then hashed again using RIPEMD160, producing a byte array of length 20. This byte array is the address. Additional information about the raw-binary implementation of addressing on the default subnet can be found in [cryptographic primitives](../cryptographic-primitives/#secp256k1-addresses). 

There are conventions in the Avalanche platform for distributing readable addresses. All addresses are [CB58 encoded](#cb58). By convention the blockchainID for the address is prepended to the address in the format `chainID-address`. Aliases for chainID may be used as well. Example:

```
/* P-Chain address */
P-avax1am4w6hfrvmh3akduzkjthrtgtqafalce6an8cr

/* C-Chain address */
C-0x820891f8b95daf5ea7d7ce7667e6bba2dd5c5594

/* X-Chain address */
X-avax1kj06lhgx84h39snsljcey3tpc046ze68mek3g5

/* Same address on a different chain */
P-avax1kj06lhgx84h39snsljcey3tpc046ze68mek3g5

/* Same address, using the chainID instead of the chain alias */
11111111111111111111111111111111LpoYY-avax1kj06lhgx84h39snsljcey3tpc046ze68mek3g5
```

## AVAX

AVAX is the Avalanche network's native asset. It has two special uses on the Avalanche network:

* Validators must [stake](../core-concepts/overview.md#what-is-staking) AVAX
* Transaction fees will be paid in AVAX

## [Avalanche Consensus](../core-concepts/overview.md#what-is-avalanche)

Avalanche is a family of consensus protocols used by blockchains on the Avalanche network.
Avalanche-based protocols allow computers to agree on a large set of information very quickly and with high security.

## Avalanche Virtual Machine

The Avalanche Virtual Machine is one of the Avalanche network's built-in virtual machines. 
It defines an application for creating and trading smart assets.
In a slight abuse of notation, we also call the main instance of the AVM 
"the AVM" since this is the one people almost always use.

## Blockchain

A blockchain is an append-only ledger. Blockchains have the special property that nobody can re-write old sections of the ledger. 
Applications, such as payments systems, can be built atop blockchains. 

## CB58

CB58 is a format used to represent keys, addresses, and other binary values in web wallets and APIs. CB58 is the concatenation of the data bytes and a checksum. The checksum is created by taking the last four bytes of the SHA256 hash of the data bytes. 

This concatenated output is then mapped to a base-58 string. It uses 58 lowercase letters, uppercase letters, and digits so values are easier to read and write. The alphabet for the base-58 conversion is:

`123456789ABCDEFGHJKLMNPQRSTUVWXYZabcdefghijkmnopqrstuvwxyz`

A full implementation of the base-58 format [can be found in Avalanche.js](https://github.com/ava-labs/avalanche.js/blob/eabcc2f23091be98d3db9d6bc0655c6faa7a3c3e/src/utils/bintools.ts#L19)

CB58 is similar to [Base58Check], but uses a different checksum algorithm.

[Base58Check]: https://en.bitcoin.it/wiki/Base58Check_encoding

## Consensus Protocol

A consensus protocol is an algorithm, or series of steps, that a set of computers follow in order to reach agreement on some piece of information.
In a payments system, for example, the computers follow a protocol to agree on who has how much money.

## Gecko

Gecko is the Go implementation of an Avalanche node.

## Node

A node is a computer participating in the Avalanche network.

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