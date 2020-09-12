---
title: "Avalanche Quickstart Guide"
excerpt: ""
---

# Quickstart Guide

The quickest way to learn about Avalanche is to run a node and interact with the network.

In this tutorial, which should take less than 10 minutes, we will:

* Install and run an Avalanche node
* Connect to the public test network
* Acquire and send AVAX, the Avalanche network's native token
* Start validating


If you run into any issues at all, **please check the [FAQ](faq.md)**
If your issue isn't addressed there, come ask for help on our [Discord Server!](https://chat.avalabs.org/)
We will work to get you through any problems.

## Requirements 

Avalanche is an incredibly lightweight protocol, so the minimum computer requirements are quite modest. 

* Hardware: CPU > 2 GHz, RAM > 4 GB, Storage > 10 GB free space.
* OS: Ubuntu == 18.04 or Mac OS X >= Catalina. (Ubuntu versions other than 18.04 may work but have not been tested.)
* Software: [Go](https://golang.org/doc/install) >= 1.13

Run `go version`. **It should be 1.13 or above.**
Run `echo $GOPATH`. **It should not be empty.**

## Run an Avalanche Node

Let's install AvalancheGo, the Go implementation of an Avalanche node, and connect to the Avalanche Public Testnet.

### Download AvalancheGo

The node is a binary program. You can either download the source code and then build the binary program, or you can download the pre-built binary.
You can do either of the below. You don't need to do both.

#### Download AvalancheGo Source Code

Download the AvalancheGo repository:

```sh
go get -v -d github.com/ava-labs/avalanchego/...
```

(Note to advanced users: AvalancheGo uses Go modules, so you can actually clone the [AvalancheGo repository](https://github.com/ava-labs/avalanchego) to locations other than your GOPATH.)

Change to the `avalanchego` directory:

```sh
cd $GOPATH/src/github.com/ava-labs/avalanchego
```

Build AvalancheGo:

```sh
./scripts/build.sh
```

The binary, named `avalanchego`, is in `avalanchego/build`. 

#### Download AvalancheGo Binary

Go to our [releases page](https://github.com/ava-labs/avalanchego/releases) and select the release you want (probably the latest one.)

Under `Assets`, select the appropriate file.

For MacOS:  
Download the file named `avalanche-osx-<VERSION>.zip`  
Unzip the file with `unzip avalanche-osx-<VERSION>.zip`  
The resulting folder, `avalanche-<VERSION>`, contains the binaries.  
You can run the node with `./avalanche-<VERSION>/avalanchego`

For Linux:  
Download the file named `avalanche-linux-<VERSION>.tar.gz`.  
Unzip the file with `tar -xvf avalanche-linux-<VERSION>.tar.gz`  
The resulting folder, `avalanche-<VERSION>`, contains the binaries.  
You can run the node with `./avalanche-<VERSION>/avalanchego`

### Start a Node and Connect to Test Network

The Avalanche test network is a sandbox Avalanche network where AVAX tokens are free.
You can use it to play around in a low-stakes environment.

To start a node and connect it to the Avalanche test net:

If you built from source:
```sh
./build/avalanchego
```

If you are using the released binaries:
```sh
./avalanche-<VERSION>/avalanchego
```

You can use `Ctrl + C` to kill the node.

When the node starts, it has to bootstrap (catch up with the rest of the network.)
This should take a few hours.
You will see logs about bootstrapping.
When a given chain is done bootstrapping, it will print a log like this:

`INFO [06-07|19:54:06] <X Chain> /snow/engine/avalanche/transitive.go#80: bootstrapping finished with 1 vertices in the accepted frontier`

To check if a given chain is done bootstrapping, call [info.isBootstrapped](api/info.md#infoisbootstrapped) like so:

```json
curl -X POST --data '{
    "jsonrpc":"2.0",
    "id"     :1,
    "method" :"info.isBootstrapped",
    "params": {
        "chain":"X"
    }
}' -H 'content-type:application/json;' 127.0.0.1:9650/ext/info
```

If this returns `true`, the chain is bootstrapped.

If you make an API call to a chain that is not done bootstrapping, it will return `API call rejected because chain is not done bootstrapping`.

If your node never finishes bootstrapping, contact us on [Discord.](https://chat.avalabs.org/)

## Create a Keystore User

Avalanche nodes provide a built-in **Keystore.**
The Keystore manages users and is a lot like a wallet.
A user is a password-protected identity that a client can use when interacting with blockchains.
**You should only create a keystore user on a node that you operate, as the node operator has access to your plaintext password.**
To create a user, call `keystore.createUser`:

```sh
curl -X POST --data '{
     "jsonrpc": "2.0",
     "id": 1,
     "method": "keystore.createUser",
     "params": {
         "username": "YOUR USERNAME HERE",
         "password": "YOUR PASSWORD HERE"
     }
}' -H 'content-type:application/json;' 127.0.0.1:9650/ext/keystore
```

The response should be:

```json
{
     "jsonrpc":"2.0",
     "result":{"success":true},
     "id":1
}
```

Now you have a user on this node.
Keystore data exists at the node level.
Users you create on one node's Keystore do not exist on
other nodes but you can import/export users to/from the Keystore.
See the [Keystore API](api/keystore.md) to see how.

## Create an Address

Avalanche is a network of heterogeneous blockchains.
One of these blockchains is the X-Chain, which acts as a decentralized platform for creating and trading digital assets.
(Think X for eXchanging assets.)

There's a special asset on the X-Chain called the [AVAX token](core-concepts/overview.md#the-x-chain). 
This is the native token of the Avalanche network, and transaction fees on the Avalanche network are paid in AVAX.

Let's acquire some AVAX tokens.
First, we'll need to create an address to hold them.

To create a new address on the X-Chain, call `avm.createAddress`, a method of the [X-Chain's API](api/avm.md):

```sh
curl -X POST --data '{
    "jsonrpc":"2.0",
    "id"     :2,
    "method" :"avm.createAddress",
    "params" :{
        "username":"YOUR USERNAME HERE",
        "password":"YOUR PASSWORD HERE"
    }
}' -H 'content-type:application/json;' 127.0.0.1:9650/ext/bc/X
```

If this call returns a 404 or hangs, your node probably isn't finished bootstrapping.

Note that we make this request to `127.0.0.1:9650/ext/bc/X`.
The `bc/X` portion signifies that the request is being sent to the blockchain whose ID (or alias) is `X` (ie the X-Chain.)

The response should look like this:

```json
{
    "jsonrpc":"2.0",
    "id":2,
    "result" :{
        "address":"X-avax1xeaj0h9uy7c5jn6fxjp0rg4g39jeh0hl27vf75"
    }
}
```

Your user now controls the address `X-avax1xeaj0h9uy7c5jn6fxjp0rg4g39jeh0hl27vf75` on the X-Chain.
To tell apart addresses on different chains, the Avalanche convention is for an address to include the ID or alias of the chain it exists on.
Hence, this address begins `X-`, denoting that it exists on the X-Chain.

## Use the Avalanche Faucet

Now let's use the Avalanche test net faucet to send some free AVAX to this address.
The faucet dispenses 100 000 000 nanoAVAX (nAVAX) each drop.

**This is only a test network, and AVAX on this network has no value.**

Go to the [test net faucet](https://faucet.avax.network/) and paste the address you just created to receive 100 000 000 nAVAX.

We can check an address's balance of a given asset by calling `avm.getBalance`, another method of the X-Chain's API.
Let's check that the faucet drip went through.

```sh
curl -X POST --data '{
    "jsonrpc":"2.0",
    "id"     :3,
    "method" :"avm.getBalance",
    "params" :{
        "address":"X-avax1xeaj0h9uy7c5jn6fxjp0rg4g39jeh0hl27vf75",
        "assetID"  :"AVAX"
    }
}' -H 'content-type:application/json;' 127.0.0.1:9650/ext/bc/X
```

Note that AVAX has the special ID `AVAX`. 
Usually an asset ID is an alphanumeric string.

The response should look like this:

```json
{
    "jsonrpc":"2.0",
    "id"     :3,
    "result" :{
        "balance":100000000,
        "utxoIDs": [
            {
                "txID": "x6vR85YPNRf5phpLAEC7Sd6Tq2PXWRt3AAHAK4BpjxyjRyhtu",
                "outputIndex": 0
            }
        ]
    }
}
```

## Send AVAX

Now let's send some AVAX:

```sh
curl -X POST --data '{
    "jsonrpc":"2.0",
    "id"     :5,
    "method" :"avm.send",
    "params" :{
        "username"   :"YOUR USERNAME HERE",
        "password"   :"YOUR PASSWORD HERE",
        "assetID"    :"AVAX",
        "amount"     :1000,
        "to"         :"X-avax1w4nt49gyv4e99ldqevy50l2kz55y9efghep0cs"
    }
}' -H 'content-type:application/json;' 127.0.0.1:9650/ext/bc/X
```

`amount` specifies the number of nAVAX to send.
A nAVAX (nanoAVAX) is the smallest increment of AVAX, and 1,000,000,000 nAVAX == 1 AVAX. 

When you send this request, the node will authenticate you using your username and password.
Then, it will look through all the private keys controlled by your user until it finds
enough nAVAX to satisfy the request.

The response contains the ID of this transaction:

```json
{
    "jsonrpc":"2.0",
    "id"     :5,
    "result" :{
        "txID":"2QouvFWUbjuySRxeX5xMbNCuAaKWfbk5FeEa2JmoF85RKLk2dD"
    }
}
```

`txID` is the ID of the send transaction we just sent to the network. It will be different for every invocation of `send`.

## Checking the Transaction Status

This send transaction will only take a second or two to finalize. We can check its status with `avm.getTxStatus`:

```sh
curl -X POST --data '{
    "jsonrpc":"2.0",
    "id"     :6,
    "method" :"avm.getTxStatus",
    "params" :{
        "txID":"2QouvFWUbjuySRxeX5xMbNCuAaKWfbk5FeEa2JmoF85RKLk2dD"
    }
}' -H 'content-type:application/json;' 127.0.0.1:9650/ext/bc/X
```

The response should indicate that the transaction was accepted:

```json
{
    "jsonrpc":"2.0",
    "id"     :6,
    "result" :{
        "status":"Accepted"
    }
}
```

You might also see that `status` is `Processing` if the network has not yet finalized the transaction.

Once you see that the transaction is `Accepted`, check the balance of the `to` address to see that it has the AVAX we sent:

```sh
curl -X POST --data '{
    "jsonrpc":"2.0",
    "id"     :7,
    "method" :"avm.getBalance",
    "params" :{
        "address":"X-avax1w4nt49gyv4e99ldqevy50l2kz55y9efghep0cs",
        "assetID"  :"AVAX"
    }
}' -H 'content-type:application/json;' 127.0.0.1:9650/ext/bc/X
```

The response should be:

```json
{
    "jsonrpc":"2.0",
    "id"     :7,
    "result" :{
        "balance":1000
    }
}
```

In the same fashion, we could check `X-avax1xeaj0h9uy7c5jn6fxjp0rg4g39jeh0hl27vf75` to see that AVAX we sent was deducted from its balance.

## Validate the Primary Network (Stake)

[Subnets](core-concepts/overview.md#what-are-subnets) are a powerful feature of the Avalanche network.
A Subnet is a set of validators that work to achieve consensus on a set of blockchains.

The Primary Network is inherent to the Avalanche network, and it validates Avalanche's [built-in blockchains](core-concepts/overview.md#built-in-blockchains).
Avalanche uses Proof-of-Stake, so to become a validator one needs to provide a stake, or bond, in AVAX tokens.

Let's add your node to the Primary Network.

### Create a P-Chain Address

The P-Chain (Platform Chain) manages metadata about the Avalanche network, including which nodes belong to which Subnets.
We create an address on the P-Chain by calling [`platform.createAddress`](api/platform.md#platformcreateaddress):

```sh
curl -X POST --data '{
    "jsonrpc": "2.0",
    "method": "platform.createAddress",
    "params": {
    	"username":"YOUR USERNAME HERE",
    	"password":"YOUR PASSWORD HERE"
    },
    "id": 1
}' -H 'content-type:application/json;' 127.0.0.1:9650/ext/P
```

Note that this API call is sent to the P-Chain (`127.0.0.1:9650/ext/P`) rather than the X-Chain (`127.0.0.1:9650/ext/X`).

The response contains the new address your user controls:

```json
{
    "jsonrpc": "2.0",
    "result": {
        "address": "P-avax1u8fe28yeftny3f4ewy6exc4d5832uhclf5mvur"
    },
    "id": 1
}
```

### Fund Your P-Chain Address

As mentioned before, in order validate the Primary Network, you need to stake some AVAX tokens.
Right now, your P-Chain address has no AVAX.
AVAX tokens are transferrable between the X-Chain (where you sent funds with the faucet) and the P-Chain.
Let's send some AVAX to your P-Chain address from the X-Chain.
The minimum stake amount on the test network is 10,000 nAVAX, so make sure you have at least this much AVAX in your X-Chain addresses.
(If you need more, use the faucet again.)

The first step in transferring AVAX from the X-Chain to P-Chain is to call `avm.exportAVAX`:

```sh
curl -X POST --data '{
    "jsonrpc":"2.0",
    "id"     :1,
    "method" :"avm.exportAVAX",
    "params" :{
        "to":"P-avax1u8fe28yeftny3f4ewy6exc4d5832uhclf5mvur",
        "amount": 20000,
    	"username":"YOUR USERNAME HERE",
    	"password":"YOUR PASSWORD HERE"
    }
}' -H 'content-type:application/json;' 127.0.0.1:9650/ext/bc/X
```

The response contains the transaction ID.
As before, you can check the transaction's status by calling `avm.getTxStatus`.

Once the transaction is completed, call `platform.importAVAX` to complete the transfer:

```sh
curl -X POST --data '{
    "jsonrpc": "2.0",
    "method": "platform.importAVAX",
    "params": {
        "to":"P-avax1u8fe28yeftny3f4ewy6exc4d5832uhclf5mvur",
        "sourceChain":"X",
    	"username":"YOUR USERNAME HERE",
    	"password":"YOUR PASSWORD HERE"
    },
    "id": 1
}' -H 'content-type:application/json;' 127.0.0.1:9650/ext/bc/P
```

The response contains the transaction ID:

```json
{
    "jsonrpc": "2.0",
    "result": {
        "txID": "ow2yyp9ZZVtxTYg6jAZJtnYetEwfu6UxKaw5hY6UAVbGnDwRN"
    },
    "id": 1
}
```

We can check the transaction's status with `platform.getTxStatus`:

```sh
curl -X POST --data '{
    "jsonrpc":"2.0",
    "id"     :1,
    "method" :"platform.getTxStatus",
    "params" :{
        "txID":"ow2yyp9ZZVtxTYg6jAZJtnYetEwfu6UxKaw5hY6UAVbGnDwRN"
    }
}' -H 'content-type:application/json;' 127.0.0.1:9650/ext/bc/P
```

It should be `Committed`, meaning the transfer is complete.

We can check the balance of the P-Chain address by calling `platform.getBalance`:

```sh
curl -X POST --data '{
    "jsonrpc": "2.0",
    "method": "platform.getBalance",
    "params":{
    	"address":"P-avax1u8fe28yeftny3f4ewy6exc4d5832uhclf5mvur"
    },
    "id": 1
}' -H 'content-type:application/json;' 127.0.0.1:9650/ext/bc/P
```

The response confirms that the funds are there:

```json
{
    "jsonrpc": "2.0",
    "result": {
        "balance": "20000"
    },
    "id": 1
}
```

Great! Now your P-Chain address has enough AVAX tokens to provide a stake.

### Issue the Transaction

To add a node the Primary Network, we'll call [`platform.addValidator`](api/platform.md#platformaddvalidator).

This method's signature is:

```go
platform.addValidator(
    {
        nodeID: string,
        startTime: int,
        endTime: int,
        stakeAmount: int,
        rewardAddress: string,
        delegationFeeRate: float,
        username: string,
        password: string
    }
) -> {txID: string}
```

Let's go through and examine these arguments.

### `nodeID`

This is the node ID of the validator being added. To get your node's ID, call [`info.getNodeID`:](api/info.md#infogetnodeid)

```json
curl -X POST --data '{
    "jsonrpc": "2.0",
    "method": "info.getNodeID",
    "params":{},
    "id": 1
}' -H 'content-type:application/json;' 127.0.0.1:9650/ext/info
```

The response has your node's ID:

```json
{
    "jsonrpc": "2.0",
    "result": {
        "nodeID": "NodeID-ARCLrphAHZ28xZEBfUL7SVAmzkTZNe1LK"
    },
    "id": 1
}
```

### `startTime` and `endTime`

When one issues a transaction to join the Primary Network they specify the time they will enter (start validating) and leave (stop validating.)
The minimum duration that one can validate the Primary Network is 24 hours, and the maximum duration is one year.
One can re-enter the Primary Network after leaving, it's just that the maximum *continuous* duration is one year.
`startTime` and `endTime` are the Unix times when your validator will start and stop validating the Primary Network, respectively. `startTime` must be in the future relative to the time the transaction is issued.

### `stakeAmount`

In order to validate the Primary Network one must stake AVAX tokens.
This parameter defines the amount of AVAX staked.

### `rewardAddress`

When a validator stops validating the Primary Network, they will receive a reward if they are sufficiently responsive and correct while they validated the Primary Network. These tokens are sent to `rewardAddress`. The original stake will be sent back to an address controlled by `username`.

A validator's stake is never slashed, regardless of their behavior; they will always receive their stake back when they're done validating.

### `delegationFeeRate`

Avalanche allows for delegation of stake. This parameter is the percent fee this validator charges when others delegate stake to them.
For example, if `delegationFeeRate` is `1.2345` and someone delegates to this validator, then when the delegation period is over, 1.2345% of the reward goes to the validator and the rest goes to the delegator.

### `username` and `password`

These parameters are the username and password of the user that pays the transaction fee, provides the staked AVAX and to whom the staked AVAX will be returned.

### Issue the Transaction

Now let's issue the transaction. We use the shell command `date` to compute the Unix time 10 minutes and 2 days in the future to use as the values of `startTime` and `endTime`, respectively.
(Note: If you're on a Mac, replace  `$(date` with `$(gdate`. If you don't have `gdate` installed, do `brew install coreutils`.)

```json
curl -X POST --data '{
    "jsonrpc": "2.0",
    "method": "platform.addValidator",
    "params": {
        "nodeID":"NodeID-ARCLrphAHZ28xZEBfUL7SVAmzkTZNe1LK",
        "startTime":'$(date --date="10 minutes" +%s)',
        "endTime":'$(date --date="2 days" +%s)',
        "stakeAmount":1000000,
        "rewardAddress":"P-avax1d4wfwrfgu4dkkyq7dlhx0lt69y2hjkjeejnhca",
        "delegationFeeRate":10,
        "username":"USERNAME",
        "password":"PASSWORD"
    },
    "id": 1
}' -H 'content-type:application/json;' 127.0.0.1:9650/ext/P
```

The response has the transaction ID:

```json
{
    "jsonrpc": "2.0",
    "result": {
        "txID": "6pb3mthunogehapzqmubmx6n38ii3lzytvdrxumovwkqftzls"
    },
    "id": 1
}
```

We can check the transaction's status by calling `platform.getTxStatus`:

```json
curl -X POST --data '{
    "jsonrpc": "2.0",
    "method": "platform.getTxStatus",
    "params": {
        "txID":"6pb3mthunogehapzqmubmx6n38ii3lzytvdrxumovwkqftzls"
    },
    "id": 1
}' -H 'content-type:application/json;' 127.0.0.1:9650/ext/P
```

The status should be `Committed`, meaning the transaction was successful.
We can call [`platform.getPendingValidators`](api/platform.md#platformgetpendingvalidators) and see that the node is now in the pending validator set for the Primary Network:

```json
curl -X POST --data '{
    "jsonrpc": "2.0",
    "method": "platform.getPendingValidators",
    "params": {},
    "id": 1
}' -H 'content-type:application/json;' 127.0.0.1:9650/ext/P
```

The response should include the node we just added:

```json
{
    "jsonrpc": "2.0",
    "result": {
        "validators": [
            {
                "nodeID": "NodeID-ARCLrphAHZ28xZEBfUL7SVAmzkTZNe1LK",
                "startTime": "1584021450",
                "endtime": "1584121156",
                "stakeAmount": "1000000",
            }
        ] 
    },
    "id": 1
}
```

When the time reaches `startTime`, this node will start validating the Primary Network.
When it reaches `endTime`, this node will stop validating the Primary Network.
The staked AVAX will be returned to an address controlled by `username`, and the rewards, if any, will be given to `rewardAddress`.
Then, if you want, you can rejoin the Primary Network.

## Next Steps

- [Learn more about Avalanche](core-concepts/overview.md)
- [Create and trade a new asset](tutorials/fixed-cap-asset.md)
- [Create a new blockchain](tutorials/create-a-blockchain.md)
- [Create a new, custom validator set (Subnet)](tutorials/create-a-subnet.md)
- [Explore our APIs](api/intro-apis.md)
- [Explore reference materials](references/cryptographic-primitives.md)
- [Read the whitepaper and other papers](papers/index.md)
