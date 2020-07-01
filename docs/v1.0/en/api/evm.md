# EVM API

This document describes the API of the C-Chain, which is an instance of the Ethereum Virtual Machine (EVM.)

Note: Ethereum has its own notion of `networkID` and `chainID`. The C-Chain uses `1` and `43110` for these values, obtained using the `net_version` and `eth_chainId` methods shown below. These have no relationship to AVA's view of networkID and chainID, and are purely internal to the C-Chain. 

## Methods

This API is identical to Geth's API except that it only supports the following services:

* `web3_`
* `net_`
* `eth_`
* `personal_`
* `txpool_`

You can interact with these services the same exact way you'd interact with Geth.
See the [Ethereum Wiki's JSON-RPC Documentation](https://eth.wiki/json-rpc/API) and [Geth's JSON-RPC Documentation](https://geth.ethereum.org/docs/rpc/server) for a full description of this API.


## JSON-RPC Endpoints

To interact with C-Chain (the main EVM instance on AVA):

```http
/ext/bc/C/rpc
```

To interact with other instances of the EVM:

```http
/ext/bc/blockchainID/rpc
```

where `blockchainID` is the ID of the blockchain running the EVM.

## WebSocket-RPC Endpoints

To interact with C-Chain (the main EVM instance on AVA):

```http
/ext/bc/C/ws
```

To interact with other instances of the EVM:

```http
/ext/bc/blockchainID/ws
```

where `blockchainID` is the ID of the blockchain running the EVM.

## Examples

### Getting the current client version

#### Call

```json
curl -X POST --data '{
    "jsonrpc": "2.0",
    "method": "web3_clientVersion",
    "params": [],
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
    "result": "Athereum 1.0"
}
```

### Getting the network ID

#### Call

```json
curl -X POST --data '{
    "jsonrpc": "2.0",
    "method": "net_version",
    "params": [],
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
    "result": "1"
}
```

### Getting the chain ID

Not well documented in JSON-RPC references. See instead [EIP694](https://github.com/ethereum/EIPs/issues/694)

#### Call

```json
curl -X POST --data '{
    "jsonrpc": "2.0",
    "method": "eth_chainId",
    "params": [],
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
    "result": "0xa866"
}
```

### Getting the most recent block number

#### Call

```json
curl -X POST --data '{
    "jsonrpc": "2.0",
    "method": "eth_blockNumber",
    "params": [],
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
    "result": "0x10f"
}
```

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
### Getting count of pending transactions

"Pending" transactions will be non-zero during periods of heavy network use. "Queued" transactions indicate transactions have been submitted with nonce values ahead of the next expected value for an address, which places them on hold until a transaction with the next expected nonce value is submitted.

#### Call

```json
curl -X POST --data '{
    "jsonrpc": "2.0",
    "method": "txpool_status",
    "params": [],
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
    "result": {
        "pending": "0x2f",
        "queued": "0x0"
    }
}
```
