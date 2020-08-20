[avalanche](../README.md) › [src/utils](../modules/src_utils.md) › [PersistanceOptions](src_utils.persistanceoptions.md)

# Class: PersistanceOptions

A class for defining the persistance behavior of this an API call.

## Hierarchy

* **PersistanceOptions**

## Index

### Constructors

* [constructor](src_utils.persistanceoptions.md#constructor)

### Properties

* [mergeRule](src_utils.persistanceoptions.md#protected-mergerule)
* [name](src_utils.persistanceoptions.md#protected-name)
* [overwrite](src_utils.persistanceoptions.md#protected-overwrite)

### Methods

* [getMergeRule](src_utils.persistanceoptions.md#getmergerule)
* [getName](src_utils.persistanceoptions.md#getname)
* [getOverwrite](src_utils.persistanceoptions.md#getoverwrite)

## Constructors

###  constructor

\+ **new PersistanceOptions**(`name`: string, `overwrite`: boolean, `mergeRule`: [MergeRule](../modules/src_utils.md#mergerule)): *[PersistanceOptions](src_utils.persistanceoptions.md)*

Defined in src/utils/persistenceoptions.ts:26

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
`mergeRule` | [MergeRule](../modules/src_utils.md#mergerule) | - | - |

**Returns:** *[PersistanceOptions](src_utils.persistanceoptions.md)*

## Properties

### `Protected` mergeRule

• **mergeRule**: *[MergeRule](../modules/src_utils.md#mergerule)* = "union"

Defined in src/utils/persistenceoptions.ts:11

___

### `Protected` name

• **name**: *string* = undefined

Defined in src/utils/persistenceoptions.ts:7

___

### `Protected` overwrite

• **overwrite**: *boolean* = false

Defined in src/utils/persistenceoptions.ts:9

## Methods

###  getMergeRule

▸ **getMergeRule**(): *[MergeRule](../modules/src_utils.md#mergerule)*

Defined in src/utils/persistenceoptions.ts:26

Returns the [MergeRule](../modules/src_utils.md#mergerule) of the instance

**Returns:** *[MergeRule](../modules/src_utils.md#mergerule)*

___

###  getName

▸ **getName**(): *string*

Defined in src/utils/persistenceoptions.ts:16

Returns the namespace of the instance

**Returns:** *string*

___

###  getOverwrite

▸ **getOverwrite**(): *boolean*

Defined in src/utils/persistenceoptions.ts:21

Returns the overwrite rule of the instance

**Returns:** *boolean*
