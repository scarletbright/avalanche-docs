# Adding a Validator to a Subnet

## Introduction

The [Default Subnet](../core-concepts/overview.md#what-are-subnets) is inherent to the Avalanche network and validates Avalanche's [built-in blockchains.](../core-concepts/overview.md#built-in-blockchains)

In this tutorial we'll add a node to the Default Subnet and to a non-default Subnet on the Avalanche Public Testnet.

The [Platform Chain (P-Chain)](../core-concepts/overview.md#the-p-chain) manages metadata about the Avalanche network.
This includes tracking which nodes are in which Subnets, which blockchains exist and which Subnets are validating which blockchains.
To add a validator we'll issue transactions to the P-Chain.

## Requirements

We assume that you've already done the [quickstart guide](../quickstart/ava-getting-started.md) and [subnet creation tutorial](../tutorials/create-a-subnet.md), and are familiar with the [Avalanche Network's architecture.](../core-concepts/overview.md)

## Connect to the Network

The node you're adding will need to be connected to the Avalanche Public Testnet.

To start your node and connect to the Avalanche Public Testnet, follow the quickstart guide.

## Add a Validator to the Default Subnet

To add a node the Default Subnet, we'll call [`platform.addDefaultSubnetValidator`](../api/platform.md#platformadddefaultsubnetvalidator).

This method's signature is:

```go
platform.addDefaultSubnetValidator(
    {
        nodeID: string,
        startTime: int,
        endTime: int,
        stakeAmount: int,
        rewardAddress: string,
        delegationFeeRate: int,
        username: string,
        password: string
    }
) -> {txID: string}
```

Let's go through and examine these arguments.

### `nodeID`

This is the node ID of the validator being added. To get your node's ID, call [`info.getNodeID`:](../api/info.md#infogetnodeid)

```json
curl -X POST --data '{
    "jsonrpc": "2.0",
    "method": "info.getNodeID",
    "params":{},
    "id": 1
}' -H 'content-type:application/json;' 127.0.0.1:9650/ext/info
```

The response has your node's ID:

```json
{
    "jsonrpc": "2.0",
    "result": {
        "nodeID": "nodeID-ARCLrphAHZ28xZEBfUL7SVAmzkTZNe1LK"
    },
    "id": 1
}
```

### `startTime` and `endTime`

When one issues a transaction to join the Default Subnet they specify the time they will enter (start validating) and leave (stop validating.)
The minimum duration that one can validate the Default Subnet is 24 hours, and the maximum duration is one year.
One can re-enter the Default Subnet after leaving, it's just that the maximum *continuous* duration is one year.
`startTime` and `endTime` are the Unix times when your validator will start and stop validating the Default Subnet, respectively. `startTime` must be in the future relative to the time the transaction is issued.

### `stakeAmount`

In order to validate the Default Subnet one must stake AVAX tokens.
This parameter defines the amount of AVAX staked.

### `rewardAddress`

When a validator stops validating the Default Subnet, they will receive a reward if they are sufficiently responsive and correct while they validated the Default Subnet. These tokens are sent to `rewardAddress`. The original stake will be sent back to an address controlled by `username`.

A validator's stake is never slashed, regardless of their behavior; they will always receive their stake back when they're done validating.

### `delegationFeeRate`

Avalanche allows for delegation of stake. This parameter is the percent fee this validator charges when others delegate stake to them, multiplied by 10,000.

For example, suppose a validator has `delegationFeeRate` 300,000 and someone delegates to this validator. When the delegation period is over, if the delegator is entitled to a reward, 30% of the reward (300,000 / 10,000) goes to the validator and 70% goes to the delegator.

### `username` and `password`

These parameters are the username and password of the user that pays the transaction fee, provides the staked AVAX and to whom the staked AVAX will be returned.

### Issue the Transaction

Now let's issue the transaction. We use the shell command `date` to compute the Unix time 10 minutes and 2 days in the future to use as the values of `startTime` and `endTime`, respectively.
(Note: If you're on a Mac, replace  `$(date` with `$(gdate`. If you don't have `gdate` installed, do `brew install coreutils`.)

```json
curl -X POST --data '{
    "jsonrpc": "2.0",
    "method": "platform.addDefaultSubnetValidator",
    "params": {
        "nodeID":"nodeID-ARCLrphAHZ28xZEBfUL7SVAmzkTZNe1LK",
        "startTime":'$(date --date="10 minutes" +%s)',
        "endTime":'$(date --date="2 days" +%s)',
        "stakeAmount":1000000,
        "rewardAddress":"P-Q4MzFZZDPHRPAHFeDs3NiyyaZDvxHKivf",
        "delegationFeeRate":100000,
        "username":"USERNAME",
        "password":"PASSWORD"
    },
    "id": 1
}' -H 'content-type:application/json;' 127.0.0.1:9650/ext/P
```

The response has the transaction ID:

```json
{
    "jsonrpc": "2.0",
    "result": {
        "txID": "6pb3mthunogehapzqmubmx6n38ii3lzytvdrxumovwkqftzls"
    },
    "id": 1
}
```

We can check the transaction's status by calling `platform.getTxStatus`:

```json
curl -X POST --data '{
    "jsonrpc": "2.0",
    "method": "platform.getTxStatus",
    "params": {
        "txID":"6pb3mthunogehapzqmubmx6n38ii3lzytvdrxumovwkqftzls"
    },
    "id": 1
}' -H 'content-type:application/json;' 127.0.0.1:9650/ext/P
```

The status should be `Committed`, meaning the transaction was successful. We can call [`platform.getPendingValidators`](../api/platform.md#platformgetpendingvalidators) and see that the node is now in the pending validator set for the Default Subnet:

```json
curl -X POST --data '{
    "jsonrpc": "2.0",
    "method": "platform.getPendingValidators",
    "params": {},
    "id": 1
}' -H 'content-type:application/json;' 127.0.0.1:9650/ext/P
```

The response should include the node we just added:

```json
{
    "jsonrpc": "2.0",
    "result": {
        "validators": [
            {
                "nodeID": "nodeID-ARCLrphAHZ28xZEBfUL7SVAmzkTZNe1LK",
                "startTime": "1584021450",
                "endtime": "1584121156",
                "stakeAmount": "1000000",
            }
        ] 
    },
    "id": 1
}
```

When the time reaches `1584021450`, this node will start validating the Default Subnet.
When it reaches `1584121156`, this node will stop validating the Default Subnet.
The staked AVAX will be returned to an address controlled by `username`, and the rewards, if any, will be given to `rewardAddress`.

## Add a Validator to a Non-default Subnet

Now let's add the same node to a non-default Subnet (that is, any Subnet other than the Default Subnet.)
The following will make more sense if you've already done this [tutorial on creating a Subnet.](../tutorials/create-a-subnet.md)

Suppose that the Subnet has ID `nTd2Q2nTLp8M9qv2VKHMdvYhtNWX7aTPa4SMEK7x7yJHbcWvr`, threshold 2, and its control keys belong to addresses `P-98vMGrh2nWNr8oDNKVK9jdxN1bwkeg4Jd` and `P-6UGRmWANxejv1uM5T8BiRR2VPFSk1aFWA`.

To add the validator, we'll call API method `addNonDefaultSubnetValidator`. Its signature is:

```go
platform.addNonDefaultSubnetValidator(
    {
        nodeID: string,
        subnetID: string,
        startTime: int,
        endTime: int,
        weight: int,
        username: string,
        password: string
    }
) -> {txID: string}
```

Let's examine the parameters:

### `nodeID`

This is the node ID of the validator being added to the subnet.
**This validator must validate the Default Subnet for the entire duration that it validates this Subnet.**

### `subnetID`

This is the ID of the subnet we're adding a validator to.

### `startTime` and `endTime`

Similar to above, these are the Unix times that the validator will start and stop validating the subnet. `startTime` must be at or after the time that the validator starts validating the Default Subnet, and `endTime` must be at or before the time that the validator stops validating the Default Subnet.

### `weight`

This is the validator's sampling weight for consensus. If the validator's weight is 1 and the cumulative weight of all validators in the subnet is 100, then this validator will be included in about 1 in every 100 samples during consensus.

### `username` and `password`

These parameters are the username and password of the user that pays the transaction fee. This user must hold a sufficient number of this Subnet's control keys in order to add a validator to this Subnet.

### Issue the Transaction

 We use the shell command `date` to compute the Unix time 10 minutes and 2 days in the future to use as the values of `startTime` and `endTime`, respectively.
(Note: If you're on a Mac, replace  `$(date` with `$(gdate`. If you don't have `gdate` installed, do `brew install coreutils`.)

```json
curl -X POST --data '{
    "jsonrpc": "2.0",
    "method": "platform.addNonDefaultSubnetValidator",
    "params": {
        "nodeID":"nodeID-ARCLrphAHZ28xZEBfUL7SVAmzkTZNe1LK",
        "subnetID":"nTd2Q2nTLp8M9qv2VKHMdvYhtNWX7aTPa4SMEK7x7yJHbcWvr",
        "startTime":'$(date --date="10 minutes" +%s)',
        "endTime":'$(date --date="2 days" +%s)',
        "weight":1,
        "username":"USERNAME",
        "password":"PASSWORD"
    },
    "id": 1
}' -H 'content-type:application/json;' 127.0.0.1:9650/ext/P
```

The response has the transaction ID:

```json
{
    "jsonrpc": "2.0",
    "result": {
        "txID": "2exafyvRNSE5ehwjhafBVt6CTntot7DFjsZNcZ54GSxBbVLcCm"
    },
    "id": 1
}
```

We can check the transaction's status by calling `platform.getTxStatus`:

```json
curl -X POST --data '{
    "jsonrpc": "2.0",
    "method": "platform.getTxStatus",
    "params": {
        "txID":"2exafyvRNSE5ehwjhafBVt6CTntot7DFjsZNcZ54GSxBbVLcCm"
    },
    "id": 1
}' -H 'content-type:application/json;' 127.0.0.1:9650/ext/P
```

The status should be `Committed`, meaning the transaction was successful. We can call [`platform.getPendingValidators`](../api/platform.md#platformgetpendingvalidators) and see that the node is now in the pending validator set for the Default Subnet. This time, we specify the subnet ID:

```json
curl -X POST --data '{
    "jsonrpc": "2.0",
    "method": "platform.getPendingValidators",
    "params": {"subnetID":"nTd2Q2nTLp8M9qv2VKHMdvYhtNWX7aTPa4SMEK7x7yJHbcWvr"},
    "id": 1
}' -H 'content-type:application/json;' 127.0.0.1:9650/ext/P
```

The response should include the node we just added:

```json
{
    "jsonrpc": "2.0",
    "result": {
        "validators": [
            {
                "nodeID": "nodeID-ARCLrphAHZ28xZEBfUL7SVAmzkTZNe1LK",
                "startTime":1584042912,
                "endTime":1584121156,
                "weight": "1"
            }
        ]
    },
    "id": 1
}
```

When the time reaches `1584042912`, this node will start validating this Subnet.
When it reaches `1584121156`, this node will stop validating this Subnet.