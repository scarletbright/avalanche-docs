[avalanche](../README.md) › [AVMAPI-Types](avmapi_types.md)

# Module: AVMAPI-Types

## Index

### Classes

* [AVMConstants](../classes/avmapi_types.avmconstants.md)
* [Address](../classes/avmapi_types.address.md)
* [InitialStates](../classes/avmapi_types.initialstates.md)
* [SigIdx](../classes/avmapi_types.sigidx.md)
* [Signature](../classes/avmapi_types.signature.md)
* [UTXOID](../classes/avmapi_types.utxoid.md)

### Type aliases

* [MergeRule](avmapi_types.md#mergerule)

### Functions

* [UnixNow](avmapi_types.md#unixnow)

## Type aliases

###  MergeRule

Ƭ **MergeRule**: *"intersection" | "differenceSelf" | "differenceNew" | "symDifference" | "union" | "unionMinusNew" | "unionMinusSelf" | "ERROR"*

*Defined in [apis/avm/types.ts:268](https://github.com/ava-labs/avalanche.js/blob/4d26b45/src/apis/avm/types.ts#L268)*

Rules used when merging sets

## Functions

###  UnixNow

▸ **UnixNow**(): *BN*

*Defined in [apis/avm/types.ts:280](https://github.com/ava-labs/avalanche.js/blob/4d26b45/src/apis/avm/types.ts#L280)*

Function providing the current UNIX time using a [BN](https://github.com/indutny/bn.js/)

**Returns:** *BN*
