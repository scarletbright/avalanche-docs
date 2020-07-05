[avalanche](../README.md) › [AVMAPI](../modules/avmapi.md) › [PersistanceOptions](avmapi.persistanceoptions.md)

# Class: PersistanceOptions

A class for defining the persistance behavior of this an API call.

## Hierarchy

* **PersistanceOptions**

## Index

### Constructors

* [constructor](avmapi.persistanceoptions.md#constructor)

### Properties

* [mergeRule](avmapi.persistanceoptions.md#protected-mergerule)
* [name](avmapi.persistanceoptions.md#protected-name)
* [overwrite](avmapi.persistanceoptions.md#protected-overwrite)

### Methods

* [getMergeRule](avmapi.persistanceoptions.md#getmergerule)
* [getName](avmapi.persistanceoptions.md#getname)
* [getOverwrite](avmapi.persistanceoptions.md#getoverwrite)

## Constructors

###  constructor

\+ **new PersistanceOptions**(`name`: string, `overwrite`: boolean, `mergeRule`: [MergeRule](../modules/avmapi_types.md#mergerule)): *[PersistanceOptions](avmapi.persistanceoptions.md)*

*Defined in [src/apis/avm/api.ts:46](https://github.com/ava-labs/avalanche.js/blob/eabcc2f/src/apis/avm/api.ts#L46)*

**`remarks`** 
The merge rules are as follows:
  * "intersection" - the intersection of the set
  * "differenceSelf" - the difference between the existing data and new set
  * "differenceNew" - the difference between the new data and the existing set
  * "symDifference" - the union of the differences between both sets of data
  * "union" - the unique set of all elements contained in both sets
  * "unionMinusNew" - the unique set of all elements contained in both sets, excluding values only found in the new set
  * "unionMinusSelf" - the unique set of all elements contained in both sets, excluding values only found in the existing set

**Parameters:**

Name | Type | Default | Description |
------ | ------ | ------ | ------ |
`name` | string | - | The namespace of the database the data |
`overwrite` | boolean | false | True if the data should be completey overwritten |
`mergeRule` | [MergeRule](../modules/avmapi_types.md#mergerule) | - | - |

**Returns:** *[PersistanceOptions](avmapi.persistanceoptions.md)*

## Properties

### `Protected` mergeRule

• **mergeRule**: *[MergeRule](../modules/avmapi_types.md#mergerule)* = "union"

*Defined in [src/apis/avm/api.ts:31](https://github.com/ava-labs/avalanche.js/blob/eabcc2f/src/apis/avm/api.ts#L31)*

___

### `Protected` name

• **name**: *string* = undefined

*Defined in [src/apis/avm/api.ts:27](https://github.com/ava-labs/avalanche.js/blob/eabcc2f/src/apis/avm/api.ts#L27)*

___

### `Protected` overwrite

• **overwrite**: *boolean* = false

*Defined in [src/apis/avm/api.ts:29](https://github.com/ava-labs/avalanche.js/blob/eabcc2f/src/apis/avm/api.ts#L29)*

## Methods

###  getMergeRule

▸ **getMergeRule**(): *[MergeRule](../modules/avmapi_types.md#mergerule)*

*Defined in [src/apis/avm/api.ts:46](https://github.com/ava-labs/avalanche.js/blob/eabcc2f/src/apis/avm/api.ts#L46)*

Returns the [MergeRule](../modules/avmapi_types.md#mergerule) of the instance

**Returns:** *[MergeRule](../modules/avmapi_types.md#mergerule)*

___

###  getName

▸ **getName**(): *string*

*Defined in [src/apis/avm/api.ts:36](https://github.com/ava-labs/avalanche.js/blob/eabcc2f/src/apis/avm/api.ts#L36)*

Returns the namespace of the instance

**Returns:** *string*

___

###  getOverwrite

▸ **getOverwrite**(): *boolean*

*Defined in [src/apis/avm/api.ts:41](https://github.com/ava-labs/avalanche.js/blob/eabcc2f/src/apis/avm/api.ts#L41)*

Returns the overwrite rule of the instance

**Returns:** *boolean*
