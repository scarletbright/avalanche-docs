# Creating A Fixed-Cap Asset

## Introduction

This tutorial illustrates how Avalanche can be used to create and trade a fixed-cap, fungible asset.
A quantity of the asset is created at the asset's initialization, and then no more is ever created. 

Suppose there is an Income Sharing Agreement (ISA) with 10M shares, and no more shares are ever created.
Let's create an asset where one unit of the asset represents one share of the ISA.

## Assumptions

We assume the reader has already completed the [quickstart guide.](../quickstart/ava-getting-started.md)

## Create the Asset

Our asset will exist on the [X-Chain](../core-concepts/overview.md#the-x-chain), so to create our asset we'll call `avm.createFixedCapAsset`, a method of the [X-Chain's API.](../api/avm.md)

The signature for this method is:

```go
avm.createFixedCapAsset({
    name: string, 
    symbol: string,
    denomination: int,  
    initialHolders: []{
        address: string, 
        amount: int
    }, 
    username: string,  
    password: string
}) -> {assetID: string}
```

* `name` is a human-readable name for the asset. Not necessarily unique.
* `symbol` is a shorthand symbol for the asset. Between 0 and 4 characters. Not necessarily unique. May be omitted.
* `denomination` determines how balances of this asset are displayed by user interfaces. If denomination is 0, 100 units of this asset are displayed as 100. If denomination is 1, 100 units of this asset are displayed as 10.0. If denomination is 2, 100 units of this asset are displays as .100, etc.
* Performing a transaction on the X-Chain will require a transaction fee in AVAX in the future. `username` and `password` denote the user paying the fee.
  That user will need to hold enough AVAX to cover the fee.
  Since there are no transaction fees right now, you can leave `username` and `password` blank.
* Each element in `initialHolders` specifies that `address` holds `amount` units of the asset at genesis.
* `assetID` is the ID of the new asset.
  
Now, on to creating the asset.
You'll want to replace `address` with an address your user controls so that you will
hold all of the newly created asset and be able to send it later in this tutorial.

```json
curl -X POST --data '{
    "jsonrpc":"2.0",
    "id"     : 1,
    "method" :"avm.createFixedCapAsset",
    "params" :{
        "name": "ISA Shares",
        "symbol":"ISAS",
        "initialHolders": [
            {
                "address": "X-Dxs8JWAzDZX1VXcLZT5GZR7TyfX8h9ic9",
                "amount": 10000000
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
        "assetID":"keMuoTQSGjqZbNVTCcbrwuNNNv9eEEZWBaRY3TapcgjkoZmQ1"
    }
}
```

## Trade the Asset

### Check a balance

All 10,000,000 units of the asset (shares) are controlled by the address we specified in `initialHolders`.

To verify this we call `avm.getBalance`:

```json
curl -X POST --data '{
    "jsonrpc":"2.0",
    "id"     :1,
    "method" :"avm.getBalance",
    "params" :{
        "address":"X-Dxs8JWAzDZX1VXcLZT5GZR7TyfX8h9ic9",
        "assetID":"keMuoTQSGjqZbNVTCcbrwuNNNv9eEEZWBaRY3TapcgjkoZmQ1"
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

### Send the asset

Now, let's send 100 shares by calling `avm.send`.

To send the shares, we need to prove that we control the user the shares are being sent from.
Therefore, this time we'll need to fill in `username` and `password`.

```json
curl -X POST --data '{
    "jsonrpc":"2.0",
    "id"     :1,
    "method" :"avm.send",
    "params" :{
        "username":"yourUsername",
        "password":"yourPassword",
        "assetID" :"keMuoTQSGjqZbNVTCcbrwuNNNv9eEEZWBaRY3TapcgjkoZmQ1",
        "amount"  :100,
        "to"      :"X-9R5xWj1DkMtGVDQmyTB4uNnvYdCnj57pa"
    }
}' -H 'content-type:application/json;' 127.0.0.1:9650/ext/bc/X
```

### Check the transaction status

The response from the above call should look like this:

```json
{
    "jsonrpc":"2.0",
    "id"     :1,
    "result" :{
        "txID":"2EAgR1YbsaJrwFiU4DpwjUfTLkt97WrjQYYNQny13AheewnxSR"
    }
}
```

`txID` is the ID of the `send` transaction we sent to the network.

After a second or two, the transaction should be finalized.
We can check the status of the transaction with `avm.getTxStatus`:

```json
curl -X POST --data '{
    "jsonrpc":"2.0",
    "id"     :1,
    "method" :"avm.getTxStatus",
    "params" :{
        "txID":"2EAgR1YbsaJrwFiU4DpwjUfTLkt97WrjQYYNQny13AheewnxSR"
    }
}' -H 'content-type:application/json;' 127.0.0.1:9650/ext/bc/X
```

The response should look like this

```json
{
    "jsonrpc":"2.0",
    "id"     :1,
    "result" :{
        "status":"Accepted"
    }
}
```

You might also see that `status` is `Pending` if the network has not yet finalized it yet.

Now let's check the balance of the `to` address:

```json
curl -X POST --data '{
    "jsonrpc":"2.0",
    "id"     :1,
    "method" :"avm.getBalance",
    "params" :{
        "address":"X-9R5xWj1DkMtGVDQmyTB4uNnvYdCnj57pa",
        "assetID":"keMuoTQSGjqZbNVTCcbrwuNNNv9eEEZWBaRY3TapcgjkoZmQ1"
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

* Called `createFixedCapAsset` to create a fixed cap asset
* Called `getBalance` to check address balances
* Called `send` to transfer a quantity of our asset