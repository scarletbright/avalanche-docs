[avalanche](../README.md) › [API-AVM-MinterSet](../modules/api_avm_minterset.md) › [MinterSet](api_avm_minterset.minterset.md)

# Class: MinterSet

Class for representing a threshold and set of minting addresses in Avalanche.

**`typeparam`** including a threshold and array of addresses

## Hierarchy

* **MinterSet**

## Index

### Constructors

* [constructor](api_avm_minterset.minterset.md#constructor)

### Properties

* [minters](api_avm_minterset.minterset.md#protected-minters)
* [threshold](api_avm_minterset.minterset.md#protected-threshold)

### Methods

* [_cleanAddresses](api_avm_minterset.minterset.md#protected-_cleanaddresses)
* [getMinters](api_avm_minterset.minterset.md#getminters)
* [getThreshold](api_avm_minterset.minterset.md#getthreshold)

## Constructors

###  constructor

\+ **new MinterSet**(`threshold`: number, `minters`: Array‹string | Buffer›): *[MinterSet](api_avm_minterset.minterset.md)*

Defined in src/apis/avm/minterset.ts:48

**Parameters:**

Name | Type | Description |
------ | ------ | ------ |
`threshold` | number | The number of signatures required to mint more of an asset by signing a minting transaction |
`minters` | Array‹string &#124; Buffer› | Array of addresss which are authorized to sign a minting transaction  |

**Returns:** *[MinterSet](api_avm_minterset.minterset.md)*

## Properties

### `Protected` minters

• **minters**: *Array‹Buffer›* = []

Defined in src/apis/avm/minterset.ts:22

___

### `Protected` threshold

• **threshold**: *number*

Defined in src/apis/avm/minterset.ts:21

## Methods

### `Protected` _cleanAddresses

▸ **_cleanAddresses**(`addresses`: Array‹string | Buffer›): *Array‹Buffer›*

Defined in src/apis/avm/minterset.ts:38

**Parameters:**

Name | Type |
------ | ------ |
`addresses` | Array‹string &#124; Buffer› |

**Returns:** *Array‹Buffer›*

___

###  getMinters

▸ **getMinters**(): *Array‹Buffer›*

Defined in src/apis/avm/minterset.ts:34

Returns the minters.

**Returns:** *Array‹Buffer›*

___

###  getThreshold

▸ **getThreshold**(): *number*

Defined in src/apis/avm/minterset.ts:27

Returns the threshold.

**Returns:** *number*
