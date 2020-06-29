# EVM API

This document describes the API of the C-Chain, which is an instance of the Ethereum Virtual Machine (EVM.)

Note: Ethereum has its own notion of `networkID` and `chainID`. The C-Chain uses `1` and `43110` for these values, respectively. These have no relationship to Avalanche's view of networkID and chainID, and are purely internal to the C-Chain. 

## Methods

This API is identical to Geth's API except that it only supports the following services:

* `web3_`
* `net_`
* `eth_`
* `personal_`

You can interact with these services the same exact way you'd interact with Geth.
See [Geth's RPC Documentation](https://github.com/ethereum/wiki/wiki/JSON-RPC) for a full description of this API.


## JSON-RPC Endpoints

To interact with C-Chain (the main EVM instance on Avalanche):

```http
/ext/bc/C/rpc
```

To interact with other instances of the EVM:

```http
/ext/bc/blockchainID/rpc
```

where `blockchainID` is the ID of the blockchain running the EVM.

## WebSocket-RPC Endpoints

To interact with C-Chain (the main EVM instance on Avalanche):

```http
/ext/bc/C/ws
```

To interact with other instances of the EVM:

```http
/ext/bc/blockchainID/ws
```

where `blockchainID` is the ID of the blockchain running the EVM.

## Examples

### Getting an account's balance

#### Call

```json
curl -X POST --data '{
    "jsonrpc": "2.0",
    "method": "eth_getBalance",
    "params": [
        "0x820891f8b95daf5ea7d7ce7667e6bba2dd5c5594",
        "latest"
    ],
    "id": 1
}' -H 'Content-Type: application/json' \
   -H 'cache-control: no-cache' \
   127.0.0.1:9650/ext/bc/C/rpc 
```

#### Response

```json
{
    "jsonrpc": "2.0",
    "id": 1,
    "result": "0x0"
}
```

### Send a raw transaction

#### Call

```json
curl -X POST --data '{
    "id": 1,
    "jsonrpc": "2.0",
    "method": "eth_sendRawTransaction",
    "params": [
        "0xf869808082520894a4e0aa1263542f6a3b6af0cf2a25008c2631eaf6872386f26fc1000080830150f0a03004a3aa8f417cdaff0539fc6fdbb17fafa6388b98fc5bb04cb9bf5e9acfc361a05354b602c07b9e341c247d631775f1a94d7eb306ba199e22011cde6958dd7835"
    ]
}' -H 'Content-Type: application/json' \
   -H 'cache-control: no-cache' \
   127.0.0.1:9650/ext/bc/C/rpc 
```

#### Response

```json
{
    "jsonrpc": "2.0",
    "id": 1,
    "error": {
        "code": -32000,
        "message": "insufficient funds for gas * price + value"
    }
}
```