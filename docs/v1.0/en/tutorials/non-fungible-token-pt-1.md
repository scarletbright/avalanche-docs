# Creating A Non-Fungible Token&mdash;Part 1

## Introduction

Avalanche is a global financial network for the issuing and trading of all digital goods. On Avalanche these digital goods are represented as tokens and can be assets or utilities. Often times these tokens are interchangible or fungible. For example, imagine an `$EXAMPLE` token which is used in commerce. If you pay for an item using `$EXAMPLE` and the merchant gives you different `$EXAMPLE` in return as change that&rsquo;s the expected behavior for fungible tokens. They are interchangible and one `$EXAMPLE` is, for all intents-and-purposes, the same as all other `$EXAMPLE` tokens.

Avalanche also supports a unique type of token called a Non-fungible Token (NFT). NFTs are different than traditional tokens in the sense that they are not interchangible. They are non-fungible. For each issued NFT there will only ever be the single issued token. NFT's represent digital scarcity and may prove to have even greater utility than traditional tokens.

NFTs on Avalanche are extremely expressive and powerful. They start with an NFT family. This family has a name and a symbol. Each family has a number of groups that you decide when you create the family. You can issue individual NFTs to each of the groups. In this tutorial we'll see how that is done at a high level with AvalancheGo's RPC. In Part-2 we'll build up a custom NFT family using AvalancheJS.

This tutorial illustrates how to create a non-fungible asset using AvalancheGo's RPC. No units of the NFT exist when the asset is initialized, but more units may be minted. On asset creation we specify which sets of addresses may mint more NFTs of this family and group.

You may be wondering why we specify *sets* of addresses that can mint more units of the asset rather than a single address. The first reason is security. If only one address can mint more of the asset, and the private key for that address is lost, no more units can ever be minted. Similarly, if only one address can mint more of the asset, nothing stops the holder of that address from unilaterally minting as much as they want.

The second reason is flexibility. It's nice to be able to encode logic like, "Alice can unilaterally mint more units of this asset, or 2 of Dinesh, Ellin and Jamie can together mint more." Let's now create an NFT.

## Requirements

We assume that you've already done the [quickstart guide](../quickstart.md) and are familiar with the [Avalanche Network's architecture.](../core-concepts/overview.md) In this tutorial, we use [Avalanche's Postman collection](https://github.com/cgcardona/avalanche-postman-collection) to help us make API calls.

## Create the NFT Family

Our NFT will exist on the X-Chain, so to create our family we'll call `avm.createNFTAsset`, which is a method of the [X-Chain's API.](../api/avm.md)

The signature for this method is:

```go
avm.createNFTAsset({
    name: string,
    symbol: string,
    minterSets []{
        minters: []string,
        threshold: int
    },
    from: []string,
    changeAddr: string,
    username: string,
    password: string
}) ->
{
    assetID: string,
    changeAddr: string,
}
```

### Parameters

* `name` is a human-readable name for our NFT family. Not necessarily unique. Between 0 and 128 characters.
* `symbol` is a shorthand symbol for this NFT family. Between 0 and 4 characters. Not necessarily unique. May be omitted.
* `minterSets` is a list where each element specifies that `threshold` of the addresses in `minters` may together mint more of the asset by signing a minting transaction.
* Performing a transaction on the X-Chain require a transaction fee paid in AVAX. `username` and `password` denote the user paying the fee.
* `from` are the addresses that you want to use for this operation. If omitted, uses any of your addresses as needed.
* `changeAddr` is the address any change will be sent to. If omitted, change is sent to one of the addresses controlled by the user.

### Response

* `assetID` is the ID of the new asset that we'll have created.
* `changeAddr` in the result is the address where any change was sent.

Later in this example we'll mint NFT, so be sure to replace at least 1 address in the minter set with an address which your user controls.

```json
curl -X POST --data '{
    "jsonrpc":"2.0",
    "id"     : 1,
    "method" :"avm.createNFTAsset",
    "params" :{
        "name":"Family",
        "symbol":"FAM",
        "minterSets":[
            {
                "minters": [
                    "X-avax1ghstjukrtw8935lryqtnh643xe9a94u3tc75c7"
                ],
                "threshold": 1
            }
        ],
        "from":["X-avax1ghstjukrtw8935lryqtnh643xe9a94u3tc75c7"],
        "changeAddr":"X-avax1ghstjukrtw8935lryqtnh643xe9a94u3tc75c7",
        "username":"USERNAME GOES HERE",
        "password":"PASSWORD GOES HERE"
    }
}' -H 'content-type:application/json;' 127.0.0.1:9650/ext/bc/X
```

The response should look like this:

```json
{
    "jsonrpc":"2.0",
    "id"     :1,
    "result" :{
        "assetID":"2X1YV4jpGpqezvj2khQdj1yEiXU1dCwsJ7DmNhQRyZZ7j9oYBp",
        "changeAddr":"X-avax1ghstjukrtw8935lryqtnh643xe9a94u3tc75c7"
    }
}
```

A couple things to take note of. First, in addition to creating an NFT family, AvalancheGo's `avm.createNFTAsset` also creates a group for each of the `minterSets` which are passed in. Second, take note of the `assetID` which is returned in the response. This is the `assetID` of the newly created NFT family and you'll need it later to issue NFTs.

## Confirm newly created NFT Mint Output

NFT outputs don't show up in calls to `avm.getBalance` or `avn.getAllBalances`. To see your NFTs you have to call `avm.getUTXOs` and then parse the utxo to check for the type ID. NFT Mint Outputs have a type id of `00 00 00 0a` in hexidecimal or `10` in decimal and NFT Transfer Outputs have a type id of `00 00 00 0b` hexdecimal or `11` in decimal.

```json
curl -X POST --data '{
    "jsonrpc":"2.0",
    "id"     : 1,
    "method" :"avm.getUTXOs",
    "params" :{
        "addresses":["X-avax1ghstjukrtw8935lryqtnh643xe9a94u3tc75c7"],
        "limit": 5
    }
}' -H 'content-type:application/json;' 127.0.0.1:9650/ext/bc/X
```

The response contains the transaction's ID:

```json
{
    "jsonrpc":"2.0",
    "id"     :1,
    "result" :{
        "numFetched": "2",
        "utxos": [
            "116VhGCxiSL4GrMPKHkk9Z92WCn2i4qk8qdN3gQkFz6FMEbHo82Lgg8nkMCPJcZgpVXZLQU6MfYuqRWfzHrojmcjKWbfwqzZoZZmvSjdD3KJFsW3PDs5oL3XpCHq4vkfFy3q1wxVY8qRc6VrTZaExfHKSQXX1KnC",
            "11cxRVipJgtuHy1ZJ6qM7moAf3GveBD9PjHeZMkhk7kjizdGUu5RxZqhViaWh8dJa9jT9sS62xy73FubMAxAy8b542v3k8frTnVitUagW9YhTMLmZ6nE48Z9qXB2V9HHzCuFH1xMvUEj33eNWv5wsP3JvmywkwkQW9WLM"
        ],
        "endIndex": {
            "address": "X-avax1ghstjukrtw8935lryqtnh643xe9a94u3tc75c7",
            "utxo": "2iyUVo8XautXpZwVfp5vhSh4ASWbo67zmHbtx7SUJg2Qa8BHtr"
        }
    }
}
```

`avm.getUTXOs` returns 2 UTXOs. Let's take the first one, `116VhGCxiSL4GrMPKHkk9Z92WCn2i4qk8qdN3gQkFz6FMEbHo82Lgg8nkMCPJcZgpVXZLQU6MfYuqRWfzHrojmcjKWbfwqzZoZZmvSjdD3KJFsW3PDs5oL3XpCHq4vkfFy3q1wxVY8qRc6VrTZaExfHKSQXX1KnC`, and decode it to confirm that it's an NFT Mint Output.

First we convert the Base58Check encoded string which is returned from `avm.getUTXOs` in to hex. The following CB58 string:

```zsh
116VhGCxiSL4GrMPKHkk9Z92WCn2i4qk8qdN3gQkFz6FMEbHo82Lgg8nkMCPJcZgpVXZLQU6MfYuqRWfzHrojmcjKWbfwqzZoZZmvSjdD3KJFsW3PDs5oL3XpCHq4vkfFy3q1wxVY8qRc6VrTZaExfHKSQXX1KnC
```

gets converted to the following hex:

```zsh
00 00 04 78 f2 39 8d d2 16 3c 34 13 2c e7 af a3 1f 0a c5 03 01 7f 86 3b f4 db 87 ea 55 53 c5 2d 7b 57 00 00 00 01 04 78 f2 39 8d d2 16 3c 34 13 2c e7 af a3 1f 0a c5 03 01 7f 86 3b f4 db 87 ea 55 53 c5 2d 7b 57 00 00 00 0a 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 01 00 00 00 01 3c b7 d3 84 2e 8c ee 6a 0e bd 09 f1 fe 88 4f 68 61 e1 b2 9c
```

Now we can decompose the hex in to the UTXO's indivdual components:

```zsh
NFT Mint Output

CodecID: 00 00
TXID: 04 78 f2 39 8d d2 16 3c 34 13 2c e7 af a3 1f 0a c5 03 01 7f 86 3b f4 db 87 ea 55 53 c5 2d 7b 57
Output Index: 00 00 00 01
AssetID: 04 78 f2 39 8d d2 16 3c 34 13 2c e7 af a3 1f 0a c5 03 01 7f 86 3b f4 db 87 ea 55 53 c5 2d 7b 57
TypeID: 00 00 00 0a
GroupID: 00 00 00 00
Locktime: 00 00 00 00 00 00 00 00
Threshold: 00 00 00 01
Address Count: 00 00 00 01
Addresses[0]: 3c b7 d3 84 2e 8c ee 6a 0e bd 09 f1 fe 88 4f 68 61 e1 b2 9c
```

Note that the `TypeID` is `00 00 00 0a` which is the correct type id for an [NFT Mint Output](../references/avm-transaction-serialization.md/#nft-mint-output). Also note that the `GroupID` is `00 00 00 00`. This `GroupID` was created based on the number of `MinterSet`s which I passed in to `avm.createNFTAsset`.

## Mint the Asset

Now that we have an NFT family and a group for the single `MinterSet` we're able to mint some NFTs to the group. To do that we call `avm.mintNFT` and pass in the following parameters.

* `assetID` is the ID of the NFT we're creating more of.
* `payload` is an arbitrary CB58 encoded payload of up to 1024 bytes.
* `to` is the address that will receive the newly minted NFT. Replace `to` with an address your user controls so that later you'll be able to send some of the newly minted NFT.
* `from` are the addresses that you want to use for this operation. If omitted, uses any of your addresses as needed.
* `changeAddr` is the address any change will be sent to. If omitted, change is sent to one of the addresses controlled by the user.
* `username` must be a user that holds keys giving it permission to mint more of this NFT. That is, it controls at least *threshold* keys for one of the minter sets we specified above.
* `password` is the valid password for `username`

```json
curl -X POST --data '{
    "jsonrpc":"2.0",
    "id"     : 1,
    "method" :"avm.mintNFT",
    "params" :{
        "assetID":"2yF5DPhRj4JvadN27xE8CGbkmpziFWs641zsEnZ2U9Tsp17fj",
        "payload":"2EWh72jYQvEJF9NLk",
        "to":"X-avax1a202a8pu5w4vnerwzp84j68yknm6lf47drfsdv",
        "from": ["X-avax1a202a8pu5w4vnerwzp84j68yknm6lf47drfsdv"],
        "changeAddr": "X-avax1a202a8pu5w4vnerwzp84j68yknm6lf47drfsdv",
        "username":"USERNAME GOES HERE",
        "password":"PASSWORD GOES HERE"
    }
}' -H 'content-type:application/json;' 127.0.0.1:9650/ext/bc/X
```

The response contains the transaction's ID:

```json
{
    "jsonrpc":"2.0",
    "id"     :1,
    "result" :{
        "txID":"x4fKx95KirTvqWCeiPZfnjB4xFdrTduymRKMouXTioXojdnUm",
        "changeAddr": "X-avax1turszjwn05lflpewurw96rfrd3h6x8flgs5uf8"
    }
}
```

Similar to the previous step, we can now confirm that an NFT was minted by calling `avm.getUTXOs` and parsing the UTXO to confirm that we now have an [NFT Transfer Output](../references/avm-transaction-serialization/#nft-transfer-output).

```json
curl -X POST --data '{
    "jsonrpc":"2.0",
    "id"     : 1,
    "method" :"avm.getUTXOS",
    "params" :{
        "addresses":["X-avax1ghstjukrtw8935lryqtnh643xe9a94u3tc75c7"],
        "limit": 5"
    }
}' -H 'content-type:application/json;' 127.0.0.1:9650/ext/bc/X
```

This should give:

```json
{
    "jsonrpc": "2.0",
    "result": {
        "numFetched": "2",
        "utxos": [
            "11Do4RK6FchGXeoycKujR7atm3tvBz3qc64uoipCc5J74Sj1U4orM6vbBGSES8hnjgjZava9oPgmnbHxh2mBKjeXdvAqTRtYMHEacrveSzKgk7F8h8xi8JB9CddoiX8nbjZMYt1keGo5Rvpjh8dGymDWwRbV1FdnG5uDiiyU8uidc3P24",
            "11JL98R9yVoCaekrzP2PoCKJfCTin6vhTWU4h9TxqevEUnhiMo2j7F4DHxRpHq6BnFnHGAajhmiXgrdfUbbNd1izmdLVMwqe3UCTJWWLaJ6XUZ46R243T8NdhKXXJWC9GvcjFYMyiKRWvVnvFt7duzq8P8D53uhv1QfdQ9"
        ],
        "endIndex": {
            "address": "X-avax1ghstjukrtw8935lryqtnh643xe9a94u3tc75c7",
            "utxo": "2qs3A1sBhVjFcXqRADJ7AorvoawVgMkNdgJi8eYNPABMKmdBYq"
        }
    },
    "id": 1
}
```

Again, similar to the previous step we can now decode the CB58 encoded UTXO to hexidecimal and then decompose it to it's individual components to confirm that we have the correct UTXO and type.

First we convert the Base58Check encoded string which is returned from `avm.getUTXOs` in to hex. The following CB58 string:

```zsh
11Do4RK6FchGXeoycKujR7atm3tvBz3qc64uoipCc5J74Sj1U4orM6vbBGSES8hnjgjZava9oPgmnbHxh2mBKjeXdvAqTRtYMHEacrveSzKgk7F8h8xi8JB9CddoiX8nbjZMYt1keGo5Rvpjh8dGymDWwRbV1FdnG5uDiiyU8uidc3P24
```

gets converted to the following hex:

```zsh
00 00 7d 07 0d 1e fe a6 4e 45 09 05 c6 11 ee b1 cf 61 9f 21 22 eb 17 db aa ea 9a fe 2d ff 17 be 27 6b 00 00 00 01 04 78 f2 39 8d d2 16 3c 34 13 2c e7 af a3 1f 0a c5 03 01 7f 86 3b f4 db 87 ea 55 53 c5 2d 7b 57 00 00 00 0b 00 00 00 00 00 00 00 08 41 56 41 20 4c 61 62 73 00 00 00 00 00 00 00 00 00 00 00 01 00 00 00 01 3c b7 d3 84 2e 8c ee 6a 0e bd 09 f1 fe 88 4f 68 61 e1 b2 9c
```

Now we can decompose the hex in to the UTXO's indivdual components:

```zsh
NFT Mint Output

CodecID: 00 00
TXID: 7d 07 0d 1e fe a6 4e 45 09 05 c6 11 ee b1 cf 61 9f 21 22 eb 17 db aa ea 9a fe 2d ff 17 be 27 6b
Output Index: 00 00 00 01
AssetID: 04 78 f2 39 8d d2 16 3c 34 13 2c e7 af a3 1f 0a c5 03 01 7f 86 3b f4 db 87 ea 55 53 c5 2d 7b 57
TypeID: 00 00 00 0b
GroupID: 00 00 00 00
Payload Length: 00 00 00 08
Payload: 41 56 41 20 4c 61 62 73
Locktime: 00 00 00 00 00 00 00 00
Threshold: 00 00 00 01
Address Count: 00 00 00 01
Addresses[0]: 3c b7 d3 84 2e 8c ee 6a 0e bd 09 f1 fe 88 4f 68 61 e1 b2 9c
```

Note that the `TypeID` is `00 00 00 0b` which is the correct type id for an [NFT Transfer Output](../references/avm-transaction-serialization.md/#nft-transfer-output). Also note that the Payload is included.

## Send the NFT

Lastly, you are now able to send the NFT to anyone. To do that you use AvalancheGo's `avm.sendNFT` RPC endpoint.

```json
curl -X POST --data '{
    "jsonrpc":"2.0",
    "id"     :1,
    "method" :"avm.sendNFT",
    "params" :{
        "assetID" :"i1EqsthjiFTxunrj8WD2xFSrQ5p2siEKQacmCCB5qBFVqfSL2",
        "from"    : ["X-avax1ghstjukrtw8935lryqtnh643xe9a94u3tc75c7"],
        "to"      :"X-avax1ghstjukrtw8935lryqtnh643xe9a94u3tc75c7",
        "groupID" : 0,
        "changeAddr": "X-avax1ghstjukrtw8935lryqtnh643xe9a94u3tc75c7",
        "username":"USERNAME GOES HERE",
        "password":"PASSWORD GOES HERE"
    }
}' -H 'content-type:application/json;' 127.0.0.1:9650/ext/bc/X
```

The response confirms that our NFT Transfer Operation was successful:

```json
{
    "jsonrpc":"2.0",
    "id"     :1,
    "result" :{
        "txID": "txtzxcrzPx1sn38HWKU9PB52EpbpXCegbdHNxPNAYd9ZvezJq",
        "changeAddr": "X-avax1ghstjukrtw8935lryqtnh643xe9a94u3tc75c7"0
    }
}
```

You can call `avm.getUTXOs` for the address which you sent the NFT to and decompose the returned UTXO, after converting from CB58 to hex, to confirm that there is a UTXO with type id `00 00 00 0b` in hex or `11` in decimal.

## Wrapping up

Blockchain technology and tokenomics represent a radical new way of representing digital assets. Non-fungible tokens allow scarce assets to be tokenized. In this tutorial, we:

* Used  `createNFTAsset` to create a non-fungible asset family and group.
* Used  `mintNFT` to mint units of an NFT to the group.
* Used  `getUTXOs` to fetch UTXOs for an address. We then converted the CB58 encoded UTXO to hex and decomposed it to it's individual components.
* Used  `sendNFT` to transfer NFTs between addresses.

In [Part 2](./non-fungible-token-pt-2) of this series we'll go more in depth by using AvalancheJS to create a protocol for our NFT payload and by issuing to multiple groups.
