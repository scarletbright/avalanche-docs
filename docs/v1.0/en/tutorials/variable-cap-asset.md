# Creating A Variable-Cap Asset

## Introduction

This tutorial illustrates how to create a variable-cap, fungible asset.
No units of the asset exist when the asset is initialized, but more units
of the asset may be minted.
On asset creation we specify which sets of addresses may mint more units.

You may be wondering why we specify *sets* of addresses that can mint more units of the asset 
rather than a single address.


The first reason is security. If only one address can mint more of the asset, and
the private key for that address is lost, no more units can ever be minted. Similarly, if only one
address can mint more of the asset, nothing stops the holder of that address from unilaterally
minting as much as they want.

The second reason is flexibility. It's nice to be able to encode logic like, "Alice can unilaterally mint more units of this asset, or 2 of Dinesh, Ellin and Jamie can together mint more."

Suppose that we want to issue an asset that represents shares of a corporation.
No shares exist to start with, but more shares may be created later.
Let's create such an asset.

## Assumptions

We assume the reader has already completed the [quickstart guide.](../quickstart/ava-getting-started.md)

## Create the Asset

Our asset will exist on the X-Chain, so to create our asset we'll call `avm.createVariableCapAsset`, which is a method of the [X-Chain's API.](../api/avm.md)

The signature for this method is:

```go
avm.createVariableCapAsset({
    name: string,
    symbol: string,
    minterSets []{
        minters: []string,
        threshold: int
    },
    username: string,
    password: string
}) -> {assetID: string}
```

* `name` is a human-readable name for our asset. Not necessarily unique. Between 0 and 128 characters.
* `symbol` is a shorthand symbol for this asset. Between 0 and 4 characters. Not necessarily unique. May be omitted.
* `minterSets` is a list where each element specifies that `threshold` of the addresses
  in `minters` may together mint more of the asset by signing a minting transaction.
* Performing a transaction on the X-Chain require a transaction fee paid in AVAX. `username` and `password` denote the user paying the fee.
* `assetID` is the ID of the new asset that we'll have created.


Later in this example we'll mint more shares, so be sure to replace at least 2 addresses
in the second minter set with addresses your user controls.

```json
curl -X POST --data '{
    "jsonrpc":"2.0",
    "id"     : 1,
    "method" :"avm.createVariableCapAsset",
    "params" :{
        "name":"Corp. Shares",
        "symbol":"CS",
        "minterSets":[
            {
                "minters": [
                    "X-No525ybWCY8jNwkPE8tcwwfFnQTWsL3aH"
                ],
                "threshold": 1
            },
            {
                "minters": [
                    "X-EMFBcgAKyToN7PSAaFkyTFhVmgXqK3BRG",
                    "X-BuHCPN7JmzKJZnHrLgEvSo6pQeL1kivzM",
                    "X-AomEKCh7bDsh2rPMS8aq6jzG1Q3g3GMNh"
                ],
                "threshold": 2
            }
        ],
        "username":"USERNAME GOES HERE",
        "password":"PASSWORD GOES HERE"
    }
}' -H 'content-type:application/json;' 127.0.0.1:9650/ext/bc/X
```

The response should look like this:

```json
{
    "jsonrpc":"2.0",
    "id"     :1,
    "result" :{
        "assetID":"i1EqsthjiFTxunrj8WD2xFSrQ5p2siEKQacmCCB5qBFVqfSL2"
    }
}
```

## Mint the Asset

Right now 0 shares exist. Let's mint 10M shares.

### Create the Unsigned Transaction

We'll use `avm.mint` to mint the shares.

* `amount` is the number of shares that will be created.
* `assetID` is the ID of the asset we're creating more of.
* `to` is the address that will receive the newly minted shares. Replace `to` with an address your user controls so that later you'll be able to send some of the newly minted shares.
* `username` must be a user that holds keys giving it permission to mint more of this asset. That is, it controls at least *threshold* keys for one of the minter sets we specified above.

```json
curl -X POST --data '{
    "jsonrpc":"2.0",
    "id"     : 1,
    "method" :"avm.mint",
    "params" :{
        "amount":10000000,
        "assetID":"i1EqsthjiFTxunrj8WD2xFSrQ5p2siEKQacmCCB5qBFVqfSL2",
        "to":"X-3dj8tFUAv8zCF8nktYFvonJcRMv8H8ARJ",
        "username":"USERNAME GOES HERE",
        "password":"PASSWORD GOES HERE"
    }
}' -H 'content-type:application/json;' 127.0.0.1:9650/ext/bc/X
```

The response contains the transaction's ID:

```json
{
    "jsonrpc":"2.0",
    "id"     :1,
    "result" :{
        "txID":"E1gqPbkziu8AutqccRa9ioPWyEF3Vd7eMjDJ3UshjQPpLoREZ"
    }
}
```

We can check the status of the transaction we've just sent to the network using `avm.getTxStatus`: 

```json
curl -X POST --data '{
    "jsonrpc":"2.0",
    "id"     : 1,
    "method" :"avm.getTxStatus",
    "params" :{
        "txID":"E1gqPbkziu8AutqccRa9ioPWyEF3Vd7eMjDJ3UshjQPpLoREZ"
    }
}' -H 'content-type:application/json;' 127.0.0.1:9650/ext/bc/X
```

This should give:

```json
{
    "jsonrpc": "2.0",
    "result": {
        "status": "Accepted"
    },
    "id": 1
}
```

## Trade the Asset

### Check a Balance

All 10M shares are controlled by the `to` address we specified in `mint`. 
To verify this we'll use `avm.getBalance`:

```json
curl -X POST --data '{
    "jsonrpc":"2.0",
    "id"     :1,
    "method" :"avm.getBalance",
    "params" :{
        "address":"X-3dj8tFUAv8zCF8nktYFvonJcRMv8H8ARJ",
        "assetID":"i1EqsthjiFTxunrj8WD2xFSrQ5p2siEKQacmCCB5qBFVqfSL2"
    }
}' -H 'content-type:application/json;' 127.0.0.1:9650/ext/bc/X
```

The response confirms that our asset creation was successful, and that the expected address holds all 10,000,000 shares:

```json
{
    "jsonrpc":"2.0",
    "id"     :1,
    "result" :{
        "balance":10000000
    }
}
```

### Send the Asset

Let's send 100 shares to another address by using `avm.send`.

To send the shares, we need to prove that we control the address the shares are being sent from (`X-3dj8tFUAv8zCF8nktYFvonJcRMv8H8ARJ`).
Therefore, this time we'll need to fill in `username` and `password`.

To send the 100 shares:

```json
curl -X POST --data '{
    "jsonrpc":"2.0",
    "id"     :1,
    "method" :"avm.send",
    "params" :{
        "username":"USERNAME GOES HERE",
        "password":"PASSWORD GOES HERE",
        "assetID" :"i1EqsthjiFTxunrj8WD2xFSrQ5p2siEKQacmCCB5qBFVqfSL2",
        "amount"  :100,
        "to"      :"X-LzAcZRDqv3GFsvszqFo22SNKLvFKwKknk"
    }
}' -H 'content-type:application/json;' 127.0.0.1:9650/ext/bc/X
```

Let's check the balances of the `to` address:

```json
curl -X POST --data '{
    "jsonrpc":"2.0",
    "id"     :1,
    "method" :"avm.getBalance",
    "params" :{
        "address":"X-LzAcZRDqv3GFsvszqFo22SNKLvFKwKknk",
        "assetID":"i1EqsthjiFTxunrj8WD2xFSrQ5p2siEKQacmCCB5qBFVqfSL2"
    }
}' -H 'content-type:application/json;' 127.0.0.1:9650/ext/bc/X
```

The response should be:

```json
{
    "jsonrpc":"2.0",
    "id"     :1,
    "result" :{
        "balance":100
    }
}
```

## Wrapping up

In this tutorial, we:

* Used  `createVariableCapAsset` to create a variable-cap asset that represents shares.
* Used  `mint` to mint more units of an asset.
* Used  `getBalance` to check address balances.
* Used  `send` to transfer shares.
