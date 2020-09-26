# Timestamp API

This API allows clients to interact with the Timestamp Chain.

The Timestamp Chain is a timestamp server.
Each block contains a 32 byte payload and the timestamp when the block was created.

The [genesis data](./platform.md#platfrombuildgenesis) for a new instance of the Timestamp Chain is the genesis block's 32 byte payload.

## Endpoint

`/ext/timestamp`

## Methods

### timestamp.getBlock

Get a block by its ID. If no ID is provided, get the latest block.

#### Signature

```go
timestamp.getBlock({id: string}) ->
    {
        id: string,
        data: string,
        timestamp: int,
        parentID: string
    }
```

* `id` is the ID of the block being retrieved. If omitted from arguments, gets the latest block.
* `data` is the base 58 (with checksum) representation of the block's 32 byte payload.
* `timestamp` is the Unix timestamp when this block was created.
* `parentID` is the block's parent.

#### Example Call

```json
curl -X POST --data '{
    "jsonrpc": "2.0",
    "method": "timestamp.getBlock",
    "params":{
    	"id":"xqQV1jDnCXDxhfnNT7tDBcXeoH2jC3Hh7Pyv4GXE1z1hfup5K"
    },
    "id": 1
}' -H 'content-type:application/json;' 127.0.0.1:9650/ext/bc/timestamp
```

#### Example Response

```json
{
    "jsonrpc": "2.0",
    "result": {
        "timestamp": "1581717416",
        "data": "11111111111111111111111111111111LpoYY",
        "id": "xqQV1jDnCXDxhfnNT7tDBcXeoH2jC3Hh7Pyv4GXE1z1hfup5K",
        "parentID": "22XLgiM5dfCwTY9iZnVk8ZPuPe3aSrdVr5Dfrbxd3ejpJd7oef"
    },
    "id": 1
}
```

### timestamp.proposeBlock

Propose the creation of a new block.

#### Signature

```go
timestamp.proposeBlock({data: string}) -> {success: bool}
```

* `data` is the base 58 (with checksum) representation of the proposed block's 32 byte payload.

#### Example Call

```json
curl -X POST --data '{
    "jsonrpc": "2.0",
    "method": "timestamp.proposeBlock",
    "params":{
    	"data":"SkB92YpWm4Q2iPnLGCuDPZPgUQMxajqQQuz91oi3xD984f8r"
    },
    "id": 1
}' -H 'content-type:application/json;' 127.0.0.1:9650/ext/bc/timestamp

```

#### Example Response

```json
{
    "jsonrpc": "2.0",
    "result": {
        "Success": true
    },
    "id": 1
}
```
