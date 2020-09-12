[avalanche](../README.md) › [Common-AssetAmount](../modules/common_assetamount.md) › [AssetAmount](common_assetamount.assetamount.md)

# Class: AssetAmount

Class for managing asset amounts in the UTXOSet fee calcuation

## Hierarchy

* **AssetAmount**

## Index

### Constructors

* [constructor](common_assetamount.assetamount.md#constructor)

### Properties

* [amount](common_assetamount.assetamount.md#protected-amount)
* [assetID](common_assetamount.assetamount.md#protected-assetid)
* [burn](common_assetamount.assetamount.md#protected-burn)
* [change](common_assetamount.assetamount.md#protected-change)
* [finished](common_assetamount.assetamount.md#protected-finished)
* [spent](common_assetamount.assetamount.md#protected-spent)

### Methods

* [getAmount](common_assetamount.assetamount.md#getamount)
* [getAssetID](common_assetamount.assetamount.md#getassetid)
* [getAssetIDString](common_assetamount.assetamount.md#getassetidstring)
* [getBurn](common_assetamount.assetamount.md#getburn)
* [getChange](common_assetamount.assetamount.md#getchange)
* [getSpent](common_assetamount.assetamount.md#getspent)
* [isFinished](common_assetamount.assetamount.md#isfinished)
* [spendAmount](common_assetamount.assetamount.md#spendamount)

## Constructors

###  constructor

\+ **new AssetAmount**(`assetID`: Buffer, `amount`: BN, `burn`: BN): *[AssetAmount](common_assetamount.assetamount.md)*

*Defined in [src/common/assetamount.ts:61](https://github.com/ava-labs/avalanche.js/blob/a2feb77/src/common/assetamount.ts#L61)*

**Parameters:**

Name | Type |
------ | ------ |
`assetID` | Buffer |
`amount` | BN |
`burn` | BN |

**Returns:** *[AssetAmount](common_assetamount.assetamount.md)*

## Properties

### `Protected` amount

• **amount**: *BN* = new BN(0)

*Defined in [src/common/assetamount.ts:16](https://github.com/ava-labs/avalanche.js/blob/a2feb77/src/common/assetamount.ts#L16)*

___

### `Protected` assetID

• **assetID**: *Buffer* = Buffer.alloc(32)

*Defined in [src/common/assetamount.ts:15](https://github.com/ava-labs/avalanche.js/blob/a2feb77/src/common/assetamount.ts#L15)*

___

### `Protected` burn

• **burn**: *BN* = new BN(0)

*Defined in [src/common/assetamount.ts:17](https://github.com/ava-labs/avalanche.js/blob/a2feb77/src/common/assetamount.ts#L17)*

___

### `Protected` change

• **change**: *BN* = new BN(0)

*Defined in [src/common/assetamount.ts:19](https://github.com/ava-labs/avalanche.js/blob/a2feb77/src/common/assetamount.ts#L19)*

___

### `Protected` finished

• **finished**: *boolean* = false

*Defined in [src/common/assetamount.ts:20](https://github.com/ava-labs/avalanche.js/blob/a2feb77/src/common/assetamount.ts#L20)*

___

### `Protected` spent

• **spent**: *BN* = new BN(0)

*Defined in [src/common/assetamount.ts:18](https://github.com/ava-labs/avalanche.js/blob/a2feb77/src/common/assetamount.ts#L18)*

## Methods

###  getAmount

▸ **getAmount**(): *BN*

*Defined in [src/common/assetamount.ts:30](https://github.com/ava-labs/avalanche.js/blob/a2feb77/src/common/assetamount.ts#L30)*

**Returns:** *BN*

___

###  getAssetID

▸ **getAssetID**(): *Buffer*

*Defined in [src/common/assetamount.ts:22](https://github.com/ava-labs/avalanche.js/blob/a2feb77/src/common/assetamount.ts#L22)*

**Returns:** *Buffer*

___

###  getAssetIDString

▸ **getAssetIDString**(): *string*

*Defined in [src/common/assetamount.ts:26](https://github.com/ava-labs/avalanche.js/blob/a2feb77/src/common/assetamount.ts#L26)*

**Returns:** *string*

___

###  getBurn

▸ **getBurn**(): *BN*

*Defined in [src/common/assetamount.ts:38](https://github.com/ava-labs/avalanche.js/blob/a2feb77/src/common/assetamount.ts#L38)*

**Returns:** *BN*

___

###  getChange

▸ **getChange**(): *BN*

*Defined in [src/common/assetamount.ts:42](https://github.com/ava-labs/avalanche.js/blob/a2feb77/src/common/assetamount.ts#L42)*

**Returns:** *BN*

___

###  getSpent

▸ **getSpent**(): *BN*

*Defined in [src/common/assetamount.ts:34](https://github.com/ava-labs/avalanche.js/blob/a2feb77/src/common/assetamount.ts#L34)*

**Returns:** *BN*

___

###  isFinished

▸ **isFinished**(): *boolean*

*Defined in [src/common/assetamount.ts:46](https://github.com/ava-labs/avalanche.js/blob/a2feb77/src/common/assetamount.ts#L46)*

**Returns:** *boolean*

___

###  spendAmount

▸ **spendAmount**(`amt`: BN): *boolean*

*Defined in [src/common/assetamount.ts:50](https://github.com/ava-labs/avalanche.js/blob/a2feb77/src/common/assetamount.ts#L50)*

**Parameters:**

Name | Type |
------ | ------ |
`amt` | BN |

**Returns:** *boolean*
