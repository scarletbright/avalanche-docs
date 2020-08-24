# Transfer AVAX tokens between the P-Chain and X-Chain

## Introduction

AVAX tokens exist on both the X-Chain, where they can be traded, and the P-Chain, where they can be provided as a stake when validating the Default Subnet.

Avalanche supports **atomic swaps** of AVAX between the X-Chain and P-chain.
(In the future Avalanche will support more generic atomic swaps between chains.)

In this tutorial we'll send AVAX tokens from the X-Chain to the P-chain and back.

## Requirements

We assume that you've already done the [quickstart guide](../quickstart/ava-getting-started.md) and are familiar with the [Avalanche Network's architecture.](../core-concepts/overview.md)

We assume your node is connected to the Public Testnet.

## Export AVAX from the X-Chain to the P-Chain

Of course, in order to send AVAX you need to have some AVAX!
Use the [Public Tesnet Faucet](https://faucet.avax.network/) to send some AVAX to an X-Chain address you hold, just like in the quickstart guide.

To send the AVAX, call the X-Chain's [`exportAVAX`](../api/avm.md#avmexportavax) method.

Your call should look like this:

```json
curl -X POST --data '{
    "jsonrpc":"2.0",
    "id"     :1,
    "method" :"avm.exportAVAX",
    "params" :{
        "to":"P-avax1wkmfja9ve3lt3n9ye4qp3l3gj9k2mz7ep45j7q",
        "amount": 500,
        "username":"myUsername",
        "password":"myPassword"
    }
}' -H 'content-type:application/json;' 127.0.0.1:9650/ext/bc/X
```

where `to` is the address of a P-Chain address you hold.
(See [here](../api/platform.md#platformcreateaddress) for instructions on creating a new P-Chain address.)

The response should look like this:

```json
{
    "jsonrpc": "2.0",
    "result": {
        "txID": "MqEaeWc4rfkw9fhRMuMTN7KUTNpFmh9Fd7KSre1ZqTsTQG73h"
    },
    "id": 1
}
```

We can verify that this transaction was accepted by calling `getTxStatus`:

```json
curl -X POST --data '{
    "jsonrpc": "2.0",
    "method": "avm.getTxStatus",
    "params":{
        "txID":"MqEaeWc4rfkw9fhRMuMTN7KUTNpFmh9Fd7KSre1ZqTsTQG73h"
    },
    "id": 1
}' -H 'content-type:application/json;' 127.0.0.1:9650/ext/bc/X
```

Which shows our transaction is accepted:

```json
{
    "jsonrpc": "2.0",
    "result": {
        "status": "Accepted"
    },
    "id": 1
}
```

We can also call [`getBalance`](../api/avm.md#avmgetbalance) to check that the AVAX was deducted from an address held by our user:

```json
curl -X POST --data '{
    "jsonrpc":"2.0",
    "id"     :1,
    "method" :"avm.getBalance",
    "params" :{
        "address":"X-ADDRESSGOESHERE",
        "assetID":"AVAX"
    }
}' -H 'content-type:application/json;' 127.0.0.1:9650/ext/bc/X
```

(If your user controls multiple X-Chain addresses, the AVAX may have been sent from any combination of them.)

## Import AVAX to the P-Chain from the X-Chain

Our transfer isn't done just yet.
We need to call the P-Chain's [`importAVAX`](../api/platform.md#platformimportavax) method to finish the transfer.

Your call should look like this:

```json
curl -X POST --data '{
    "jsonrpc": "2.0",
    "method": "platform.importAVAX",
    "params": {
        "to":"P-avax1wkmfja9ve3lt3n9ye4qp3l3gj9k2mz7ep45j7q",
        "sourceChain":"X",
        "username":"myUsername",
        "password":"myPassword",
    },
    "id": 1
}' -H 'content-type:application/json;' 127.0.0.1:9650/ext/bc/P
```

This returns the transaction ID:

```json
{
    "jsonrpc": "2.0",
    "result": {
        "txID": "2sxo3ySETZ4xzXqAtgsUvZ5pdkqG4SML4c7Z7NoKLZcp77YNXC"
    },
    "id": 1
}
```

We can check that the transaction was accepted with:


```json
curl -X POST --data '{
    "jsonrpc":"2.0",
    "id"     :1,
    "method" :"avm.getTxStatus",
    "params" :{
        "txID":"2sxo3ySETZ4xzXqAtgsUvZ5pdkqG4SML4c7Z7NoKLZcp77YNXC"
    }
}' -H 'content-type:application/json;' 127.0.0.1:9650/ext/bc/X
```

It should be `Committed`, meaning the transfer is complete.
We can also check the balance of the address with:


```json
curl -X POST --data '{
    "jsonrpc": "2.0",
    "method": "platform.getBalance",
    "params":{
        "address":"P-avax1wkmfja9ve3lt3n9ye4qp3l3gj9k2mz7ep45j7q"
    },
    "id": 1
}' -H 'content-type:application/json;' 127.0.0.1:9650/ext/bc/P
```

The response should look like this:

```json
{
    "jsonrpc": "2.0",
    "result": {
        "balance": "20000",
        "utxoIDs": [
            {
                "txID": "2sxo3ySETZ4xzXqAtgsUvZ5pdkqG4SML4c7Z7NoKLZcp77YNXC",
                "outputIndex": 0
            }
        ]
    },
    "id": 84
}
```

Woo! We successfully moved AVAX from the X-Chain to the P-Chain.
Now we can use the AVAX held by this P-Chain address to provide a stake in order to validate the Default Subnet.

## Export AVAX from the P-Chain to the X-Chain

Now let's move AVAX on the P-Chain back to the X-Chain.

To do so, call [`platform.exportAVAX`](../api/platform.md#platformexportavax):

```json
curl -X POST --data '{
    "jsonrpc": "2.0",
    "method": "platform.exportAVAX",
    "params": {
        "to":"X-avax1fjn5rffqvny7uk3tjegjs6snwjs3hhgcpcxfax",
        "amount":250,
        "username":"myUsername",
        "password":"myPassword"
    },
    "id": 1
}' -H 'content-type:application/json;' 127.0.0.1:9650/ext/P
```

where `to` is the X-Chain address the AVAX is being sent to.

Just as before, this returns the transaction ID, and we can check that the transaction was committed with another call to `platform.getTxStatus`.

## Import AVAX to the X-Chain from the P-Chain

To finish our transfer from the P-Chain to the X-Chain, call `avm.importAVAX`:

```json
curl -X POST --data '{
    "jsonrpc":"2.0",
    "id"     :1,
    "method" :"avm.importAVAX",
    "params" :{
        "to":"X-avax1fjn5rffqvny7uk3tjegjs6snwjs3hhgcpcxfax",
        "sourceChain":"P",
        "username":"myUsername",
        "password":"myPassword"
    }
}' -H 'content-type:application/json;' 127.0.0.1:9650/ext/bc/X
```

Note that `to` is the same address specified in our call to `platform.exportAVAX`.

Just as before, we can call `avm.getBalance` to verify the funds were received.

## Wrapping Up

That's it! Now you can swap AVAX back and forth between the X-Chain and P-Chain.
In the future Avalanche will support more generalized atomic swaps between chains.