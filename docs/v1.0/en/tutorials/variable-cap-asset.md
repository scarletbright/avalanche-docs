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
* In the future, performing a transaction on an AVM instance will require a transaction fee (paid in AVAX tokens).
  `username` and `password` denote the user paying the transaction fee.
  That user will need to hold enough AVAX to pay the fee.
  Since there are no transaction fees right now, you can leave `username` and `password` blank.
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
        "username":"yourUsername",
        "password":"yourPassword"
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

First, we'll need to create an unsigned mint transaction.
Then, we'll need to sign it so that others can verify that the transaction
came from the minters specified when the asset was initialized.

### Create the Unsigned Transaction

We'll use `avm.createMintTx` to create the unsigned mint transaction.

* `to` is the address that will receive the newly minted shares.
  Replace `to` with an address your user controls so that later you'll be able to send
  some of the newly minted shares.
* `minters` are the addresses that will sign this transaction, thereby making it valid.
  Replace the address in `minters` with 2 addresses from the second minter set above.

```json
curl -X POST --data '{
    "jsonrpc":"2.0",
    "id"     : 1,
    "method" :"avm.createMintTx",
    "params" :{
        "amount":10000000,
        "assetID":"i1EqsthjiFTxunrj8WD2xFSrQ5p2siEKQacmCCB5qBFVqfSL2",
        "to":"X-3dj8tFUAv8zCF8nktYFvonJcRMv8H8ARJ",
        "minters":[
            "X-EMFBcgAKyToN7PSAaFkyTFhVmgXqK3BRG",
            "X-BuHCPN7JmzKJZnHrLgEvSo6pQeL1kivzM"
        ]
    }
}' -H 'content-type:application/json;' 127.0.0.1:9650/ext/bc/X
```

The response should look like this:

```json
{
    "jsonrpc":"2.0",
    "id"     :1,
    "result" :{
        "tx":"1112yKaDdxEJYZEdDc3gkmjksVUPSw1uE5iEBXgBJ8mtG5Hcdys1wfqbMewcGQiwrX4oARgu9RSouv7BfJwAimBHCPnELJ4s8mNrv7UCfShuVE6c7BzdRSKXZr1eLiBdpjZRfGBT5fV4CUxd31zuvpozJSYyGD8ugzejmz2s2peTb4pzCyCa9GL8hajP9wMcokH1hLW2KK9FCkMZ8fUHgABPvSQFHwFvEroYPqVNwetFdz39enBVcZF7xTajCU718NCeqYtMMApNmwJzXXejCTPAN1Uo4hKoeuRaAwQXJRvoVHK9iDq4DumFx84FYVCuKPF1C78Khd3qB2kNUoVm6fwt4aDd1A8pyBhNUkSweP4Bcdo4U3"
    }
}
```

### Sign the Transaction

The `minterSets` argument above specifies that the transaction can be made valid by signing it
with `X-No525ybWCY8jNwkPE8tcwwfFnQTWsL3aH`, or with 2 of `X-EMFBcgAKyToN7PSAaFkyTFhVmgXqK3BRG`,
`X-BuHCPN7JmzKJZnHrLgEvSo6pQeL1kivzM` and `X-AomEKCh7bDsh2rPMS8aq6jzG1Q3g3GMNh`.

To sign the transaction, we use `avm.signMintTx`. 
We specify that this signature is being provided by `X-EMFBcgAKyToN7PSAaFkyTFhVmgXqK3BRG`.

```json
curl -X POST --data '{
    "jsonrpc":"2.0",
    "id"     : 1,
    "method" :"avm.signMintTx",
    "params" :{
        "tx":"1112yKaDdxEJYZEdDc3gkmjksVUPSw1uE5iEBXgBJ8mtG5Hcdys1wfqbMewcGQiwrX4oARgu9RSouv7BfJwAimBHCPnELJ4s8mNrv7UCfShuVE6c7BzdRSKXZr1eLiBdpjZRfGBT5fV4CUxd31zuvpozJSYyGD8ugzejmz2s2peTb4pzCyCa9GL8hajP9wMcokH1hLW2KK9FCkMZ8fUHgABPvSQFHwFvEroYPqVNwetFdz39enBVcZF7xTajCU718NCeqYtMMApNmwJzXXejCTPAN1Uo4hKoeuRaAwQXJRvoVHK9iDq4DumFx84FYVCuKPF1C78Khd3qB2kNUoVm6fwt4aDd1A8pyBhNUkSweP4Bcdo4U3",
        "minter":"X-EMFBcgAKyToN7PSAaFkyTFhVmgXqK3BRG",
        "username":"yourUsername",
        "password":"yourPassword"
    }
}' -H 'content-type:application/json;' 127.0.0.1:9650/ext/bc/X
```

The result should look like this:

```json
{
    "jsonrpc":"2.0",
    "id"     :1,
    "result" :{
        "tx":"111DodqUkFYB5DCHpPtzwmfEur9TnNRK8G7AvJixtMXhvKybf3FY4FZimmwxvA2RkqpQGBi7Dad161ZX3DZ6pohH7fUM1G9N57b43k29rWRyqcZw3r2Gj24KhC8FTbWJGAVAdVRg1biufVgD5apRq7tuz5uCMCFpCifqjkYdeAj7R15nENQiknTqHaTMWzY7UGxwMgbo1HfQmraDnUELnHWpJ9sCi5tnFVY97MtCGg15tyPyeXQRVPvdFtB3FCrFhPct3KEGiwxukhHSgb9xs66oTgcnJJLgSxmwgS6tFNvMVFJJqA7gtMyXnDU3do7gSJzKhrvofgPFMVw62J8AhqLCSWWkqnFrV4eDTTEWyoUUomEkXhsioy839UmdcE1u7fnc8kHCJ2hMfDMcKgLihyYVJDmBD87phm1hSFuWGHSNZruBBRktCSFWHFZCBEZxLHu221PLiDL3RmsKXHA5PJxk9gzw7eQm9qRFJ5AEPzDzN2f6P1mXZRC8co8MeqkBDApKXftrqGgw5szYifwsr7KSZXFmEhyxqjsEVKFDncR6he"
    }
}
```

Let's sign the partially signed transaction with the signature of
`X-BuHCPN7JmzKJZnHrLgEvSo6pQeL1kivzM`.

```json
curl -X POST --data '{
    "jsonrpc":"2.0",
    "id"     : 1,
    "method" :"avm.signMintTx",
    "params" :{
        "tx":"111DodqUkFYB5DCHpPtzwmfEur9TnNRK8G7AvJixtMXhvKybf3FY4FZimmwxvA2RkqpQGBi7Dad161ZX3DZ6pohH7fUM1G9N57b43k29rWRyqcZw3r2Gj24KhC8FTbWJGAVAdVRg1biufVgD5apRq7tuz5uCMCFpCifqjkYdeAj7R15nENQiknTqHaTMWzY7UGxwMgbo1HfQmraDnUELnHWpJ9sCi5tnFVY97MtCGg15tyPyeXQRVPvdFtB3FCrFhPct3KEGiwxukhHSgb9xs66oTgcnJJLgSxmwgS6tFNvMVFJJqA7gtMyXnDU3do7gSJzKhrvofgPFMVw62J8AhqLCSWWkqnFrV4eDTTEWyoUUomEkXhsioy839UmdcE1u7fnc8kHCJ2hMfDMcKgLihyYVJDmBD87phm1hSFuWGHSNZruBBRktCSFWHFZCBEZxLHu221PLiDL3RmsKXHA5PJxk9gzw7eQm9qRFJ5AEPzDzN2f6P1mXZRC8co8MeqkBDApKXftrqGgw5szYifwsr7KSZXFmEhyxqjsEVKFDncR6he",
        "minter":"X-BuHCPN7JmzKJZnHrLgEvSo6pQeL1kivzM",
        "username":"yourUsername",
        "password":"yourPassword"
    }
}' -H 'content-type:application/json;' 127.0.0.1:9650/ext/bc/X
```

The result should look like this:

```json
{
    "jsonrpc":"2.0",
    "id"     :1,
    "result" :{
        "tx":"111DodqUkFYB5DCHpPtzwmfEur9TnNRK8G7AvJixtMXhvKybf3FY4FZimmwxvA2RkqpQGBi7Dad161ZX3DZ6pohH7fUM1G9N57b43k29rWRyqcZw3r2Gj24KhC8FTbWJGAVAdVRg1biufVgD5apRq7tuz5uCMCFpCifqjkYdeAj7R15nENQiknTqHaTMWzY7UGxwMgbo1HfQmraDnUELnHWpJ9sCi5tnFVY97MtCGg15tyPyeXQRVPvdFtB3FCrFhPct3KEGiwxukhHSgb9xs66oTgcnJJLgSxmwgS6tFNvMVFJJqA7gtMyXnDU3do7gSJzKhrvofgPFMVw62J8AhqLCSWWkqnFrV4eDTTEWyoUUomEkXhsioy839UmdcE1u7fnc8kHCJ2hMfDMcKgLihyYVJDmBD87phm1hSFuWGHSNZruBBRktCSFWHFZCBEZxLHu221PLiDL3RmsKckXp87ywsGT9SDfXjjRuHFq3fmpaDXSYZrGuW3XpFScs8r4Ho1aHmiGdsLUVH1BbWaGkPDTCxMMhDaVDfMMLeLT2ULQyjA"
    }
}
```

### Issue the Signed Transaction

When we created this asset, we specified that more of it could be minted with
the signatures of 2 of: `X-EMFBcgAKyToN7PSAaFkyTFhVmgXqK3BRG`, `X-BuHCPN7JmzKJZnHrLgEvSo6pQeL1kivzM`,
and `X-AomEKCh7bDsh2rPMS8aq6jzG1Q3g3GMNh`.
We've now signed the transaction with the signatures of the first two addresses,
so this transaction is ready to be sent to the network.

To send the signed transaction to the network, thereby minting more shares, we use `avm.issueTx`:

```json
curl -X POST --data '{
    "jsonrpc":"2.0",
    "id"     : 1,
    "method" :"avm.issueTx",
    "params" :{
        "tx":"111DodqUkFYB5DCHpPtzwmfEur9TnNRK8G7AvJixtMXhvKybf3FY4FZimmwxvA2RkqpQGBi7Dad161ZX3DZ6pohH7fUM1G9N57b43k29rWRyqcZw3r2Gj24KhC8FTbWJGAVAdVRg1biufVgD5apRq7tuz5uCMCFpCifqjkYdeAj7R15nENQiknTqHaTMWzY7UGxwMgbo1HfQmraDnUELnHWpJ9sCi5tnFVY97MtCGg15tyPyeXQRVPvdFtB3FCrFhPct3KEGiwxukhHSgb9xs66oTgcnJJLgSxmwgS6tFNvMVFJJqA7gtMyXnDU3do7gSJzKhrvofgPFMVw62J8AhqLCSWWkqnFrV4eDTTEWyoUUomEkXhsioy839UmdcE1u7fnc8kHCJ2hMfDMcKgLihyYVJDmBD87phm1hSFuWGHSNZruBBRktCSFWHFZCBEZxLHu221PLiDL3RmsKckXp87ywsGT9SDfXjjRuHFq3fmpaDXSYZrGuW3XpFScs8r4Ho1aHmiGdsLUVH1BbWaGkPDTCxMMhDaVDfMMLeLT2ULQyjA"
    }
}' -H 'content-type:application/json;' 127.0.0.1:9650/ext/bc/X
```

The result should look like this:

```json
{
    "jsonrpc":"2.0",
    "id"     :1,
    "result" :{
        "txID":"2W5AZ3w94dteqXHvsAkw8FfDcZHSf8F93Qsn3pBsqLTM3RBGRG"
    }
}
```

We can check the status of the transaction we've just sent to the network using
`avm.getTxStatus.` We omit this step here.

## Trade the Asset

### Check a Balance

All 10M shares are controlled by the `to` address we specified `createMintTx`. 
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
        "username":"yourUsername",
        "password":"yourPassword",
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
* Used  `getBalance` to check address balances.
* Used  `send` to transfer shares.
* Used  `createMintTx` to create an unsigned transaction to mint more shares.
* Used `signMintTx` twice to sign the unsigned transaction with `threshold` minter signatures.
* Used `issueTx` to send the signed transaction to the network, thus minting more shares.

It's important to note that even though in this tutorial all of the minter addresses were controlled
by one user, this is not necessarily the case.
In practice, it makes more sense for each minter address to be controlled by a *different* user because this is more secure.
A variable-cap asset that can be minted with only one user's signatures has a single point of failure.