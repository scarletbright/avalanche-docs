[avalanche](../README.md) › [API-AVM-UTXOs](../modules/api_avm_utxos.md) › [AssetAmount](api_avm_utxos.assetamount.md)

# Class: AssetAmount

Class for managing asset amounts in the UTXOSet fee calcuation

## Hierarchy

* **AssetAmount**

## Index

### Constructors

* [constructor](api_avm_utxos.assetamount.md#constructor)

### Properties

* [amount](api_avm_utxos.assetamount.md#protected-amount)
* [assetID](api_avm_utxos.assetamount.md#protected-assetid)
* [burn](api_avm_utxos.assetamount.md#protected-burn)
* [change](api_avm_utxos.assetamount.md#protected-change)
* [finished](api_avm_utxos.assetamount.md#protected-finished)
* [spent](api_avm_utxos.assetamount.md#protected-spent)

### Methods

* [getAmount](api_avm_utxos.assetamount.md#getamount)
* [getAssetID](api_avm_utxos.assetamount.md#getassetid)
* [getAssetIDString](api_avm_utxos.assetamount.md#getassetidstring)
* [getBurn](api_avm_utxos.assetamount.md#getburn)
* [getChange](api_avm_utxos.assetamount.md#getchange)
* [getSpent](api_avm_utxos.assetamount.md#getspent)
* [isFinished](api_avm_utxos.assetamount.md#isfinished)
* [spendAmount](api_avm_utxos.assetamount.md#spendamount)

## Constructors

###  constructor

\+ **new AssetAmount**(`assetID`: Buffer, `amount`: BN, `burn`: BN): *[AssetAmount](api_avm_utxos.assetamount.md)*

Defined in src/apis/avm/utxos.ts:144

**Parameters:**

Name | Type |
------ | ------ |
`assetID` | Buffer |
`amount` | BN |
`burn` | BN |

**Returns:** *[AssetAmount](api_avm_utxos.assetamount.md)*

## Properties

### `Protected` amount

• **amount**: *BN* = new BN(0)

Defined in src/apis/avm/utxos.ts:99

___

### `Protected` assetID

• **assetID**: *Buffer* = Buffer.alloc(32)

Defined in src/apis/avm/utxos.ts:98

___

### `Protected` burn

• **burn**: *BN* = new BN(0)

Defined in src/apis/avm/utxos.ts:100

___

### `Protected` change

• **change**: *BN* = new BN(0)

Defined in src/apis/avm/utxos.ts:102

___

### `Protected` finished

• **finished**: *boolean* = false

Defined in src/apis/avm/utxos.ts:103

___

### `Protected` spent

• **spent**: *BN* = new BN(0)

Defined in src/apis/avm/utxos.ts:101

## Methods

###  getAmount

▸ **getAmount**(): *BN*

Defined in src/apis/avm/utxos.ts:113

**Returns:** *BN*

___

###  getAssetID

▸ **getAssetID**(): *Buffer*

Defined in src/apis/avm/utxos.ts:105

**Returns:** *Buffer*

___

###  getAssetIDString

▸ **getAssetIDString**(): *string*

Defined in src/apis/avm/utxos.ts:109

**Returns:** *string*

___

###  getBurn

▸ **getBurn**(): *BN*

Defined in src/apis/avm/utxos.ts:121

**Returns:** *BN*

___

###  getChange

▸ **getChange**(): *BN*

Defined in src/apis/avm/utxos.ts:125

**Returns:** *BN*

___

###  getSpent

▸ **getSpent**(): *BN*

Defined in src/apis/avm/utxos.ts:117

**Returns:** *BN*

___

###  isFinished

▸ **isFinished**(): *boolean*

Defined in src/apis/avm/utxos.ts:129

**Returns:** *boolean*

___

###  spendAmount

▸ **spendAmount**(`amt`: BN): *boolean*

Defined in src/apis/avm/utxos.ts:133

**Parameters:**

Name | Type |
------ | ------ |
`amt` | BN |

**Returns:** *boolean*
