# Admin API

This API can be used for measuring node health and debugging.

## Format

This API uses the `json 2.0` RPC format. For more information on making JSON RPC calls, see [here.](./issuing-api-calls.md)

## Endpoint

```http
/ext/admin
```

## API Methods

### admin.getNodeID
Get the ID of this node.

#### Signature 
```go
admin.getNodeID() -> {nodeID: string}
```

#### Example Call
```json
curl -X POST --data '{
    "jsonrpc":"2.0",
    "id"     :1,
    "method" :"admin.getNodeID"
}' -H 'content-type:application/json;' 127.0.0.1:9650/ext/admin
```

#### Example Response

```json
{
    "jsonrpc": "2.0",
    "result": {
        "nodeID": "5mb46qkSBj81k9g9e4VFjGGSbaaSLFRzD"
    },
    "id": 1
}
```

### admin.peers
Get the peers this node is connected to.

#### Signature 
```go
admin.peers() -> {peers:[]string}
```

#### Example Call
```json
curl -X POST --data '{
    "jsonrpc":"2.0",
    "id"     :1,
    "method" :"admin.peers"
}' -H 'content-type:application/json;' 127.0.0.1:9650/ext/admin
```

#### Example Response

```json
{
    "jsonrpc":"2.0",
    "id"     :1,
    "result" :{
        "peers":[
          {
             "ip":"206.189.137.87:9651",
             "publicIP":"206.189.137.87:9651",
             "id":"8PYXX47kqLDe2wD4oPbvRRchcnSzMA4J4",
             "version":"avalanche/0.5.0",
             "lastSent":"2020-06-01T15:23:02Z",
             "lastReceived":"2020-06-01T15:22:57Z"
          },
          {
             "ip":"158.255.67.151:9651",
             "publicIP":"158.255.67.151:9651",
             "id":"C14fr1n8EYNKyDfYixJ3rxSAVqTY3a8BP",
             "version":"avalanche/0.5.0",
             "lastSent":"2020-06-01T15:23:02Z",
             "lastReceived":"2020-06-01T15:22:34Z"
          },
          {
             "ip":"83.42.13.44:9651",
             "publicIP":"83.42.13.44:9651",
             "id":"LPbcSMGJ4yocxYxvS2kBJ6umWeeFbctYZ",
             "version":"avalanche/0.5.0",
             "lastSent":"2020-06-01T15:23:02Z",
             "lastReceived":"2020-06-01T15:22:55Z"
          }
        ]
    }
}
```

### admin.getNetworkID

Get the ID of the network this node is participating in.

#### Signature 
```go
admin.getNetworkID() -> {networkID:int}
```

#### Example Call
```json
curl -X POST --data '{
    "jsonrpc":"2.0",
    "id"     :1,
    "method" :"admin.getNetworkID"
}' -H 'content-type:application/json;' 127.0.0.1:9650/ext/admin
```

#### Example Response

```json
{
    "jsonrpc":"2.0",
    "id"     :1,
    "result" :{
        "networkID":"2"
    }
}
```

### admin.alias

Assign an API an alias, a different endpoint for the API.
The original endpoint will still work.
This change only affects this node; other nodes will not know about this alias.

#### Signature 
```go
admin.alias(endpoint:string, alias:string) -> {success:bool}
```

* `endpoint` is the original endpoint of the API. `endpoint` should only include the part of the endpoint after `/ext/`.
* The API being aliased can now be called at `ext/alias`.

#### Example Call
```json
curl -X POST --data '{
    "jsonrpc":"2.0",
    "id"     :1,
    "method" :"admin.alias",
    "params": {
        "alias":"myAlias",
        "endpoint":"bc/x"
    }
}' -H 'content-type:application/json;' 127.0.0.1:9650/ext/admin
```

#### Example Response

```json
{
    "jsonrpc":"2.0",
    "id"     :1,
    "result" :{
        "success":true
    }
}
```

Now, calls to the X-Chain can be made to either `/ext/bc/X` or, equivalently, to `/ext/myAlias`.

### admin.aliasChain

Give a blockchain an alias, a different name that can be used any place the blockchain's ID is used.

#### Signature 
```go
admin.aliasChain(
    {
        chain:string,
        alias:string
    }
) -> {success:bool}
```

* `chain` is the blockchain's ID.
* `alias` can now be used in place of the blockchain's ID (in API endpoints, for example.)

#### Example Call
```json
curl -X POST --data '{
    "jsonrpc":"2.0",
    "id"     :1,
    "method" :"admin.aliasChain",
    "params": {
        "chain":"sV6o671RtkGBcno1FiaDbVcFv2sG5aVXMZYzKdP4VQAWmJQnM",
        "alias":"myBlockchainAlias"
    }
}' -H 'content-type:application/json;' 127.0.0.1:9650/ext/admin
```

#### Example Response

```json
{
    "jsonrpc":"2.0",
    "id"     :1,
    "result" :{
        "success":true
    }
}
```

Now, instead of interacting with the blockchain whose ID is `sV6o671RtkGBcno1FiaDbVcFv2sG5aVXMZYzKdP4VQAWmJQnM` by making API calls to `/ext/bc/sV6o671RtkGBcno1FiaDbVcFv2sG5aVXMZYzKdP4VQAWmJQnM`, one can also make calls to `ext/bc/myBlockchainAlias`.

### admin.getBlockchainID

Given a blockchain's alias, get its ID. (See `avm.aliasChain` for more context.)

#### Signature 
```go
admin.getBlockchainID({alias:string}) -> {blockchainID:string}
```

#### Example Call
```json
curl -X POST --data '{
    "jsonrpc":"2.0",
    "id"     :1,
    "method" :"admin.getBlockchainID",
    "params": {
        "alias":"X"
    }
}' -H 'content-type:application/json;' 127.0.0.1:9650/ext/admin
```

#### Example Response

```json
{
    "jsonrpc":"2.0",
    "id"     :1,
    "result" :{
        "blockchainID":"sV6o671RtkGBcno1FiaDbVcFv2sG5aVXMZYzKdP4VQAWmJQnM"
    }
}
```

### admin.startCPUProfiler

Start profiling the CPU utilization of the node. Will write the profile to the specified file on stop.

#### Signature
```go
admin.startCPUProfiler({fileName:string}) -> {success:bool}
```

where `fileName` is the name of the file to write the profile to.

#### Example Call

```json
curl -X POST --data '{
    "jsonrpc":"2.0",
    "id"     :1,
    "method" :"admin.startCPUProfiler",
    "params" :{
        "fileName":"cpu.profile"
    }
}' -H 'content-type:application/json;' 127.0.0.1:9650/ext/admin
```

#### Example Response
```json
{
    "jsonrpc":"2.0",
    "id"     :1,
    "result" :{
        "success":true
    }
}
```

### admin.stopCPUProfiler
Stop the CPU profile that was previously started.

#### Signature
```go
admin.stopCPUProfiler() -> {success:bool}
```

#### Example Call
```json
curl -X POST --data '{
    "jsonrpc":"2.0",
    "id"     :1,
    "method" :"admin.stopCPUProfiler"
}' -H 'content-type:application/json;' 127.0.0.1:9650/ext/admin
```

#### Example Response
```json
{
    "jsonrpc":"2.0",
    "id"     :1,
    "result" :{
        "success":true
    }
}
```

### admin.memoryProfile
Dump the current memory footprint of the node to the specified file.

#### Signature
```go
admin.memoryProfile({fileName:string}) -> {success:bool}
```

where `fileName` is the name of the file to dump the information into.

#### Example Call

```json
curl -X POST --data '{
    "jsonrpc":"2.0",
    "id"     :1,
    "method" :"admin.memoryProfile",
    "params" :{
        "fileName":"mem.profile"
    }
}' -H 'content-type:application/json;' 127.0.0.1:9650/ext/admin
```

#### Example Response
```json
{
    "jsonrpc":"2.0",
    "id"     :1,
    "result" :{
        "success":true
    }
}
```

### admin.lockProfile
Dump the mutex statistics of the node to the specified file.

#### Signature
```go
admin.lockProfile({fileName:string}) -> {success:bool}
```

where `fileName` is the name of the file to dump the information into.


#### Example Call

```json
curl -X POST --data '{
    "jsonrpc":"2.0",
    "id"     :1,
    "method" :"admin.lockProfile",
    "params" :{
        "fileName":"lock.profile"
    }
}' -H 'content-type:application/json;' 127.0.0.1:9650/ext/admin
```

#### Example Response

```json
{
    "jsonrpc":"2.0",
    "id"     :1,
    "result" :{
        "success":true
    }
}
```
