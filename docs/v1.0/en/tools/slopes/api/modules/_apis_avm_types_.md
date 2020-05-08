[slopes - v1.4.3](../README.md) › [Globals](../globals.md) › ["apis/avm/types"](_apis_avm_types_.md)

# External module: "apis/avm/types"

## Index

### Classes

* [AVMConstants](../classes/_apis_avm_types_.avmconstants.md)
* [Address](../classes/_apis_avm_types_.address.md)
* [InitialStates](../classes/_apis_avm_types_.initialstates.md)
* [SigIdx](../classes/_apis_avm_types_.sigidx.md)
* [Signature](../classes/_apis_avm_types_.signature.md)

### Type aliases

* [MergeRule](_apis_avm_types_.md#mergerule)

### Functions

* [UnixNow](_apis_avm_types_.md#unixnow)

## Type aliases

###  MergeRule

Ƭ **MergeRule**: *"intersection" | "differenceSelf" | "differenceNew" | "symDifference" | "union" | "unionMinusNew" | "unionMinusSelf" | "ERROR"*

*Defined in [apis/avm/types.ts:199](https://github.com/ava-labs/slopes/blob/709e172/src/apis/avm/types.ts#L199)*

Rules used when merging sets

## Functions

###  UnixNow

▸ **UnixNow**(): *BN*

*Defined in [apis/avm/types.ts:211](https://github.com/ava-labs/slopes/blob/709e172/src/apis/avm/types.ts#L211)*

Function providing the current UNIX time using a [BN](https://github.com/indutny/bn.js/)

**Returns:** *BN*
