[avalanche](../README.md) › [API-PlatformVM-UTXOs](../modules/api_platformvm_utxos.md) › [AssetAmount](api_platformvm_utxos.assetamount.md)

# Class: AssetAmount

Class for managing asset amounts in the UTXOSet fee calcuation

## Hierarchy

* **AssetAmount**

## Index

### Constructors

* [constructor](api_platformvm_utxos.assetamount.md#constructor)

### Properties

* [amount](api_platformvm_utxos.assetamount.md#protected-amount)
* [assetID](api_platformvm_utxos.assetamount.md#protected-assetid)
* [burn](api_platformvm_utxos.assetamount.md#protected-burn)
* [change](api_platformvm_utxos.assetamount.md#protected-change)
* [finished](api_platformvm_utxos.assetamount.md#protected-finished)
* [spent](api_platformvm_utxos.assetamount.md#protected-spent)

### Methods

* [getAmount](api_platformvm_utxos.assetamount.md#getamount)
* [getAssetID](api_platformvm_utxos.assetamount.md#getassetid)
* [getAssetIDString](api_platformvm_utxos.assetamount.md#getassetidstring)
* [getBurn](api_platformvm_utxos.assetamount.md#getburn)
* [getChange](api_platformvm_utxos.assetamount.md#getchange)
* [getSpent](api_platformvm_utxos.assetamount.md#getspent)
* [isFinished](api_platformvm_utxos.assetamount.md#isfinished)
* [spendAmount](api_platformvm_utxos.assetamount.md#spendamount)

## Constructors

###  constructor

\+ **new AssetAmount**(`assetID`: Buffer, `amount`: BN, `burn`: BN): *[AssetAmount](api_platformvm_utxos.assetamount.md)*

Defined in src/apis/platformvm/utxos.ts:139

**Parameters:**

Name | Type |
------ | ------ |
`assetID` | Buffer |
`amount` | BN |
`burn` | BN |

**Returns:** *[AssetAmount](api_platformvm_utxos.assetamount.md)*

## Properties

### `Protected` amount

• **amount**: *BN* = new BN(0)

Defined in src/apis/platformvm/utxos.ts:94

___

### `Protected` assetID

• **assetID**: *Buffer* = Buffer.alloc(32)

Defined in src/apis/platformvm/utxos.ts:93

___

### `Protected` burn

• **burn**: *BN* = new BN(0)

Defined in src/apis/platformvm/utxos.ts:95

___

### `Protected` change

• **change**: *BN* = new BN(0)

Defined in src/apis/platformvm/utxos.ts:97

___

### `Protected` finished

• **finished**: *boolean* = false

Defined in src/apis/platformvm/utxos.ts:98

___

### `Protected` spent

• **spent**: *BN* = new BN(0)

Defined in src/apis/platformvm/utxos.ts:96

## Methods

###  getAmount

▸ **getAmount**(): *BN*

Defined in src/apis/platformvm/utxos.ts:108

**Returns:** *BN*

___

###  getAssetID

▸ **getAssetID**(): *Buffer*

Defined in src/apis/platformvm/utxos.ts:100

**Returns:** *Buffer*

___

###  getAssetIDString

▸ **getAssetIDString**(): *string*

Defined in src/apis/platformvm/utxos.ts:104

**Returns:** *string*

___

###  getBurn

▸ **getBurn**(): *BN*

Defined in src/apis/platformvm/utxos.ts:116

**Returns:** *BN*

___

###  getChange

▸ **getChange**(): *BN*

Defined in src/apis/platformvm/utxos.ts:120

**Returns:** *BN*

___

###  getSpent

▸ **getSpent**(): *BN*

Defined in src/apis/platformvm/utxos.ts:112

**Returns:** *BN*

___

###  isFinished

▸ **isFinished**(): *boolean*

Defined in src/apis/platformvm/utxos.ts:124

**Returns:** *boolean*

___

###  spendAmount

▸ **spendAmount**(`amt`: BN): *boolean*

Defined in src/apis/platformvm/utxos.ts:128

**Parameters:**

Name | Type |
------ | ------ |
`amt` | BN |

**Returns:** *boolean*
