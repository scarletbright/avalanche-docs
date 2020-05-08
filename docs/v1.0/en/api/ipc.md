# IPC API

The IPC API allows users to create a UNIX domain socket for a blockchain to publish to.
When the blockchain accepts a vertex/block it will publish the vertex to the socket.

A node will only expose this API if it is started with [command-line argument](../references/command-line-interface.md) `api-ipcs-enabled=true`. 

## Format

This API uses the `json 2.0` RPC format.

## Endpoint

`/ext/ipcs`

## Methods

### ipcs.publishBlockchain

Register a blockchain so it publishes accepted vertices to a Unix domain socket.

#### Signature

```go
ipcs.publishBlockchain({blockchainID: string}) -> {url: string}
```

* `blockchainID` is the blockchain that will publish accepted vertices.
* `url` is the path of the Unix domain socket the vertices are published to.
  
#### Example Call

```json
curl -X POST --data '{
    "jsonrpc": "2.0",
    "method": "ipcs.publishBlockchain",
    "params":{
        "blockchainID":"GJABrZ9A6UQFpwjPU8MDxDd8vuyRoDVeDAXc694wJ5t3zEkhU"
    },
    "id": 1
}' -H 'content-type:application/json;' 127.0.0.1:9650/ext/ipcs
```

#### Example Response

```json
{
    "jsonrpc":"2.0",
    "result":{
        "url":"ipc:///tmp/GJABrZ9A6UQFpwjPU8MDxDd8vuyRoDVeDAXc694wJ5t3zEkhU.ipc"
    },
    "id":1
}
```

### ipcs.unpublishBlockchain

Deregister a blockchain so that it no longer publishes to a Unix domain socket.

#### Signature

```go
ipcs.unpublishBlockchain({blockchainID: string}) -> {success: bool}
```

* `blockchainID` is the blockchain that will no longer publish to a Unix domain socket.

#### Example Call

```json
curl -X POST --data '{
    "jsonrpc": "2.0",
    "method": "ipcs.unpublishBlockchain",
    "params":{
        "blockchainID":"GJABrZ9A6UQFpwjPU8MDxDd8vuyRoDVeDAXc694wJ5t3zEkhU"
    },
    "id": 1
}' -H 'content-type:application/json;' 127.0.0.1:9650/ext/ipcs
```

#### Example Response

```json
{
    "jsonrpc":"2.0",
    "result":{
        "success":true
    },
    "id":1
}
```