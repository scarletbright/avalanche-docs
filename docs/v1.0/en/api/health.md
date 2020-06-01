# Health API

This API can be used for measuring node health.

## Format

This API uses the `json 2.0` RPC format. For more information on making JSON RPC calls, see [here.](./issuing-api-calls.md)

## Endpoint

```http
/ext/health
```

## API Methods

### health.getLiveness
Get health check on this node.

#### Signature 
```go
health.getLiveness() -> {
    checks: {
        network.validators.heartbeat: {
            message: {
                heartbeat: int
            },
            timestamp: string,
            duration: int,
            contiguousFailures: int,
            timeOfFirstFailure: int
        }
    },
    healthy: bool
}
```

Note: timeOfFirstFailure will be null if this node has not failed.

#### Example Call
```json
curl -X POST --data '{
    "jsonrpc":"2.0",
    "id"     :1,
    "method" :"health.getLiveness"
}' -H 'content-type:application/json;' 127.0.0.1:9650/ext/health
```

#### Example Response

```json
{
   "jsonrpc":"2.0",
   "result":{
      "checks":{
         "network.validators.heartbeat":{
            "message":{
               "heartbeat":1591041377
            },
            "timestamp":"2020-06-01T15:56:18.554202-04:00",
            "duration":23201,
            "contiguousFailures":0,
            "timeOfFirstFailure":null
         }
      },
      "healthy":true
   },
   "id":1
}
```
