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

* `chains.default.bootstrapped`
     * `timestamp` is the unix timestamp of the when the node was bootstrapped.
     * `duration` is the duration the node has been up.
     * `contiguousFailures` is the number of contiguous failures.
     * `timeOfFirstFailure` is the time of the first failure.
* `network.validators.heartbeat`
    * `heartbeat` is the unix timestamp of the last time the network handled a message.
    * `timestamp` is the timestamp of the last health check.
    * `duration` is the execution duration of the last health check in milliseconds.
    * `contiguousFailures` is the number of fails that occurred in a row.
    * `timeOfFirstFailure` is the time of the initial transitional failure.

More information on these measurements can be found in the documentation for the [go-sundheit](https://github.com/AppsFlyer/go-sundheit) library.

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
    "jsonrpc": "2.0",
    "result": {
        "checks": {
            "chains.default.bootstrapped": {
                "timestamp": "2020-09-17T21:27:31.776773-07:00",
                "duration": 5891,
                "contiguousFailures": 0,
                "timeOfFirstFailure": null
            },
            "network.validators.heartbeat": {
                "message": {
                    "heartbeat": 1600403244
                },
                "timestamp": "2020-09-17T21:27:31.776793-07:00",
                "duration": 4000,
                "contiguousFailures": 0,
                "timeOfFirstFailure": null
            }
        },
        "healthy": true
    },
    "id": 1
}
```
