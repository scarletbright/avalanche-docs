[avalanche](../README.md) › [API-AVM-Operations](../modules/api_avm_operations.md) › [NFTMintOperation](api_avm_operations.nftmintoperation.md)

# Class: NFTMintOperation

An [Operation](api_avm_operations.operation.md) class which specifies a NFT Mint Op.

## Hierarchy

* [Operation](api_avm_operations.operation.md)

  ↳ **NFTMintOperation**

## Index

### Constructors

* [constructor](api_avm_operations.nftmintoperation.md#constructor)

### Properties

* [groupID](api_avm_operations.nftmintoperation.md#protected-groupid)
* [outputOwners](api_avm_operations.nftmintoperation.md#protected-outputowners)
* [payload](api_avm_operations.nftmintoperation.md#protected-payload)
* [sigCount](api_avm_operations.nftmintoperation.md#protected-sigcount)
* [sigIdxs](api_avm_operations.nftmintoperation.md#protected-sigidxs)

### Methods

* [addSignatureIdx](api_avm_operations.nftmintoperation.md#addsignatureidx)
* [fromBuffer](api_avm_operations.nftmintoperation.md#frombuffer)
* [getCredentialID](api_avm_operations.nftmintoperation.md#getcredentialid)
* [getOperationID](api_avm_operations.nftmintoperation.md#getoperationid)
* [getOutputOwners](api_avm_operations.nftmintoperation.md#getoutputowners)
* [getPayload](api_avm_operations.nftmintoperation.md#getpayload)
* [getPayloadBuffer](api_avm_operations.nftmintoperation.md#getpayloadbuffer)
* [getSigIdxs](api_avm_operations.nftmintoperation.md#getsigidxs)
* [toBuffer](api_avm_operations.nftmintoperation.md#tobuffer)
* [toString](api_avm_operations.nftmintoperation.md#tostring)
* [comparator](api_avm_operations.nftmintoperation.md#static-comparator)

## Constructors

###  constructor

\+ **new NFTMintOperation**(`groupID`: number, `payload`: Buffer, `outputOwners`: Array‹[OutputOwners](common_output.outputowners.md)›): *[NFTMintOperation](api_avm_operations.nftmintoperation.md)*

*Overrides [Operation](api_avm_operations.operation.md).[constructor](api_avm_operations.operation.md#constructor)*

*Defined in [src/apis/avm/ops.ts:419](https://github.com/ava-labs/avalanche.js/blob/a2feb77/src/apis/avm/ops.ts#L419)*

An [Operation](api_avm_operations.operation.md) class which contains an NFT on an assetID.

**Parameters:**

Name | Type | Default | Description |
------ | ------ | ------ | ------ |
`groupID` | number | undefined | The group to which to issue the NFT Output |
`payload` | Buffer | undefined | A [Buffer](https://github.com/feross/buffer) of the NFT payload |
`outputOwners` | Array‹[OutputOwners](common_output.outputowners.md)› | undefined | An array of outputOwners  |

**Returns:** *[NFTMintOperation](api_avm_operations.nftmintoperation.md)*

## Properties

### `Protected` groupID

• **groupID**: *Buffer* = Buffer.alloc(4)

*Defined in [src/apis/avm/ops.ts:316](https://github.com/ava-labs/avalanche.js/blob/a2feb77/src/apis/avm/ops.ts#L316)*

___

### `Protected` outputOwners

• **outputOwners**: *Array‹[OutputOwners](common_output.outputowners.md)›* = []

*Defined in [src/apis/avm/ops.ts:318](https://github.com/ava-labs/avalanche.js/blob/a2feb77/src/apis/avm/ops.ts#L318)*

___

### `Protected` payload

• **payload**: *Buffer*

*Defined in [src/apis/avm/ops.ts:317](https://github.com/ava-labs/avalanche.js/blob/a2feb77/src/apis/avm/ops.ts#L317)*

___

### `Protected` sigCount

• **sigCount**: *Buffer* = Buffer.alloc(4)

*Inherited from [Operation](api_avm_operations.operation.md).[sigCount](api_avm_operations.operation.md#protected-sigcount)*

*Defined in [src/apis/avm/ops.ts:38](https://github.com/ava-labs/avalanche.js/blob/a2feb77/src/apis/avm/ops.ts#L38)*

___

### `Protected` sigIdxs

• **sigIdxs**: *Array‹[SigIdx](common_signature.sigidx.md)›* = []

*Inherited from [Operation](api_avm_operations.operation.md).[sigIdxs](api_avm_operations.operation.md#protected-sigidxs)*

*Defined in [src/apis/avm/ops.ts:40](https://github.com/ava-labs/avalanche.js/blob/a2feb77/src/apis/avm/ops.ts#L40)*

## Methods

###  addSignatureIdx

▸ **addSignatureIdx**(`addressIdx`: number, `address`: Buffer): *void*

*Inherited from [Operation](api_avm_operations.operation.md).[addSignatureIdx](api_avm_operations.operation.md#addsignatureidx)*

*Defined in [src/apis/avm/ops.ts:60](https://github.com/ava-labs/avalanche.js/blob/a2feb77/src/apis/avm/ops.ts#L60)*

Creates and adds a [SigIdx](common_signature.sigidx.md) to the [Operation](api_avm_operations.operation.md).

**Parameters:**

Name | Type | Description |
------ | ------ | ------ |
`addressIdx` | number | The index of the address to reference in the signatures |
`address` | Buffer | The address of the source of the signature  |

**Returns:** *void*

___

###  fromBuffer

▸ **fromBuffer**(`bytes`: Buffer, `offset`: number): *number*

*Overrides [Operation](api_avm_operations.operation.md).[fromBuffer](api_avm_operations.operation.md#frombuffer)*

*Defined in [src/apis/avm/ops.ts:360](https://github.com/ava-labs/avalanche.js/blob/a2feb77/src/apis/avm/ops.ts#L360)*

Popuates the instance from a [Buffer](https://github.com/feross/buffer) representing the [NFTMintOperation](api_avm_operations.nftmintoperation.md) and returns the updated offset.

**Parameters:**

Name | Type | Default |
------ | ------ | ------ |
`bytes` | Buffer | - |
`offset` | number | 0 |

**Returns:** *number*

___

###  getCredentialID

▸ **getCredentialID**(): *number*

*Overrides [Operation](api_avm_operations.operation.md).[getCredentialID](api_avm_operations.operation.md#abstract-getcredentialid)*

*Defined in [src/apis/avm/ops.ts:330](https://github.com/ava-labs/avalanche.js/blob/a2feb77/src/apis/avm/ops.ts#L330)*

Returns the credential ID.

**Returns:** *number*

___

###  getOperationID

▸ **getOperationID**(): *number*

*Overrides [Operation](api_avm_operations.operation.md).[getOperationID](api_avm_operations.operation.md#abstract-getoperationid)*

*Defined in [src/apis/avm/ops.ts:323](https://github.com/ava-labs/avalanche.js/blob/a2feb77/src/apis/avm/ops.ts#L323)*

Returns the operation ID.

**Returns:** *number*

___

###  getOutputOwners

▸ **getOutputOwners**(): *Array‹[OutputOwners](common_output.outputowners.md)›*

*Defined in [src/apis/avm/ops.ts:353](https://github.com/ava-labs/avalanche.js/blob/a2feb77/src/apis/avm/ops.ts#L353)*

Returns the outputOwners.

**Returns:** *Array‹[OutputOwners](common_output.outputowners.md)›*

___

###  getPayload

▸ **getPayload**(): *Buffer*

*Defined in [src/apis/avm/ops.ts:337](https://github.com/ava-labs/avalanche.js/blob/a2feb77/src/apis/avm/ops.ts#L337)*

Returns the payload.

**Returns:** *Buffer*

___

###  getPayloadBuffer

▸ **getPayloadBuffer**(): *Buffer*

*Defined in [src/apis/avm/ops.ts:344](https://github.com/ava-labs/avalanche.js/blob/a2feb77/src/apis/avm/ops.ts#L344)*

Returns the payload's raw [Buffer](https://github.com/feross/buffer) with length prepended, for use with [PayloadBase](utils_payload.payloadbase.md)'s fromBuffer

**Returns:** *Buffer*

___

###  getSigIdxs

▸ **getSigIdxs**(): *Array‹[SigIdx](common_signature.sigidx.md)›*

*Inherited from [Operation](api_avm_operations.operation.md).[getSigIdxs](api_avm_operations.operation.md#getsigidxs)*

*Defined in [src/apis/avm/ops.ts:47](https://github.com/ava-labs/avalanche.js/blob/a2feb77/src/apis/avm/ops.ts#L47)*

Returns the array of [SigIdx](common_signature.sigidx.md) for this [Operation](api_avm_operations.operation.md)

**Returns:** *Array‹[SigIdx](common_signature.sigidx.md)›*

___

###  toBuffer

▸ **toBuffer**(): *Buffer*

*Overrides [Operation](api_avm_operations.operation.md).[toBuffer](api_avm_operations.operation.md#tobuffer)*

*Defined in [src/apis/avm/ops.ts:382](https://github.com/ava-labs/avalanche.js/blob/a2feb77/src/apis/avm/ops.ts#L382)*

Returns the buffer representing the [NFTMintOperation](api_avm_operations.nftmintoperation.md) instance.

**Returns:** *Buffer*

___

###  toString

▸ **toString**(): *string*

*Overrides [Operation](api_avm_operations.operation.md).[toString](api_avm_operations.operation.md#tostring)*

*Defined in [src/apis/avm/ops.ts:417](https://github.com/ava-labs/avalanche.js/blob/a2feb77/src/apis/avm/ops.ts#L417)*

Returns a base-58 string representing the [NFTMintOperation](api_avm_operations.nftmintoperation.md).

**Returns:** *string*

___

### `Static` comparator

▸ **comparator**(): *function*

*Inherited from [Operation](api_avm_operations.operation.md).[comparator](api_avm_operations.operation.md#static-comparator)*

*Defined in [src/apis/avm/ops.ts:104](https://github.com/ava-labs/avalanche.js/blob/a2feb77/src/apis/avm/ops.ts#L104)*

**Returns:** *function*

▸ (`a`: [Operation](api_avm_operations.operation.md), `b`: [Operation](api_avm_operations.operation.md)): *0 | 1 | -1*

**Parameters:**

Name | Type |
------ | ------ |
`a` | [Operation](api_avm_operations.operation.md) |
`b` | [Operation](api_avm_operations.operation.md) |
