[avalanche](../README.md) › [API-AVM-UTXOs](../modules/api_avm_utxos.md) › [AssetAmountDestination](api_avm_utxos.assetamountdestination.md)

# Class: AssetAmountDestination

## Hierarchy

* **AssetAmountDestination**

## Index

### Constructors

* [constructor](api_avm_utxos.assetamountdestination.md#constructor)

### Properties

* [amountkey](api_avm_utxos.assetamountdestination.md#protected-amountkey)
* [amounts](api_avm_utxos.assetamountdestination.md#protected-amounts)
* [change](api_avm_utxos.assetamountdestination.md#protected-change)
* [changeAddresses](api_avm_utxos.assetamountdestination.md#protected-changeaddresses)
* [destinations](api_avm_utxos.assetamountdestination.md#protected-destinations)
* [inputs](api_avm_utxos.assetamountdestination.md#protected-inputs)
* [outputs](api_avm_utxos.assetamountdestination.md#protected-outputs)
* [senders](api_avm_utxos.assetamountdestination.md#protected-senders)

### Methods

* [addAssetAmount](api_avm_utxos.assetamountdestination.md#addassetamount)
* [addChange](api_avm_utxos.assetamountdestination.md#addchange)
* [addInput](api_avm_utxos.assetamountdestination.md#addinput)
* [addOutput](api_avm_utxos.assetamountdestination.md#addoutput)
* [assetExists](api_avm_utxos.assetamountdestination.md#assetexists)
* [canComplete](api_avm_utxos.assetamountdestination.md#cancomplete)
* [getAllOutputs](api_avm_utxos.assetamountdestination.md#getalloutputs)
* [getAmounts](api_avm_utxos.assetamountdestination.md#getamounts)
* [getAssetAmount](api_avm_utxos.assetamountdestination.md#getassetamount)
* [getChangeAddresses](api_avm_utxos.assetamountdestination.md#getchangeaddresses)
* [getChangeOutputs](api_avm_utxos.assetamountdestination.md#getchangeoutputs)
* [getDestinations](api_avm_utxos.assetamountdestination.md#getdestinations)
* [getInputs](api_avm_utxos.assetamountdestination.md#getinputs)
* [getOutputs](api_avm_utxos.assetamountdestination.md#getoutputs)
* [getSenders](api_avm_utxos.assetamountdestination.md#getsenders)

## Constructors

###  constructor

\+ **new AssetAmountDestination**(`destinations`: Array‹Buffer›, `senders`: Array‹Buffer›, `changeAddresses`: Array‹Buffer›): *[AssetAmountDestination](api_avm_utxos.assetamountdestination.md)*

Defined in src/apis/avm/utxos.ts:230

**Parameters:**

Name | Type |
------ | ------ |
`destinations` | Array‹Buffer› |
`senders` | Array‹Buffer› |
`changeAddresses` | Array‹Buffer› |

**Returns:** *[AssetAmountDestination](api_avm_utxos.assetamountdestination.md)*

## Properties

### `Protected` amountkey

• **amountkey**: *object*

Defined in src/apis/avm/utxos.ts:159

___

### `Protected` amounts

• **amounts**: *Array‹[AssetAmount](api_avm_utxos.assetamount.md)›* = []

Defined in src/apis/avm/utxos.ts:155

___

### `Protected` change

• **change**: *Array‹[TransferableOutput](api_avm_outputs.transferableoutput.md)›* = []

Defined in src/apis/avm/utxos.ts:162

___

### `Protected` changeAddresses

• **changeAddresses**: *Array‹Buffer›* = []

Defined in src/apis/avm/utxos.ts:158

___

### `Protected` destinations

• **destinations**: *Array‹Buffer›* = []

Defined in src/apis/avm/utxos.ts:156

___

### `Protected` inputs

• **inputs**: *Array‹[TransferableInput](api_avm_inputs.transferableinput.md)›* = []

Defined in src/apis/avm/utxos.ts:160

___

### `Protected` outputs

• **outputs**: *Array‹[TransferableOutput](api_avm_outputs.transferableoutput.md)›* = []

Defined in src/apis/avm/utxos.ts:161

___

### `Protected` senders

• **senders**: *Array‹Buffer›* = []

Defined in src/apis/avm/utxos.ts:157

## Methods

###  addAssetAmount

▸ **addAssetAmount**(`assetID`: Buffer, `amount`: BN, `burn`: BN): *void*

Defined in src/apis/avm/utxos.ts:164

**Parameters:**

Name | Type |
------ | ------ |
`assetID` | Buffer |
`amount` | BN |
`burn` | BN |

**Returns:** *void*

___

###  addChange

▸ **addChange**(`output`: [TransferableOutput](api_avm_outputs.transferableoutput.md)): *void*

Defined in src/apis/avm/utxos.ts:178

**Parameters:**

Name | Type |
------ | ------ |
`output` | [TransferableOutput](api_avm_outputs.transferableoutput.md) |

**Returns:** *void*

___

###  addInput

▸ **addInput**(`input`: [TransferableInput](api_avm_inputs.transferableinput.md)): *void*

Defined in src/apis/avm/utxos.ts:170

**Parameters:**

Name | Type |
------ | ------ |
`input` | [TransferableInput](api_avm_inputs.transferableinput.md) |

**Returns:** *void*

___

###  addOutput

▸ **addOutput**(`output`: [TransferableOutput](api_avm_outputs.transferableoutput.md)): *void*

Defined in src/apis/avm/utxos.ts:174

**Parameters:**

Name | Type |
------ | ------ |
`output` | [TransferableOutput](api_avm_outputs.transferableoutput.md) |

**Returns:** *void*

___

###  assetExists

▸ **assetExists**(`assetHexStr`: string): *boolean*

Defined in src/apis/avm/utxos.ts:202

**Parameters:**

Name | Type |
------ | ------ |
`assetHexStr` | string |

**Returns:** *boolean*

___

###  canComplete

▸ **canComplete**(): *boolean*

Defined in src/apis/avm/utxos.ts:222

**Returns:** *boolean*

___

###  getAllOutputs

▸ **getAllOutputs**(): *Array‹[TransferableOutput](api_avm_outputs.transferableoutput.md)›*

Defined in src/apis/avm/utxos.ts:218

**Returns:** *Array‹[TransferableOutput](api_avm_outputs.transferableoutput.md)›*

___

###  getAmounts

▸ **getAmounts**(): *Array‹[AssetAmount](api_avm_utxos.assetamount.md)›*

Defined in src/apis/avm/utxos.ts:182

**Returns:** *Array‹[AssetAmount](api_avm_utxos.assetamount.md)›*

___

###  getAssetAmount

▸ **getAssetAmount**(`assetHexStr`: string): *[AssetAmount](api_avm_utxos.assetamount.md)*

Defined in src/apis/avm/utxos.ts:198

**Parameters:**

Name | Type |
------ | ------ |
`assetHexStr` | string |

**Returns:** *[AssetAmount](api_avm_utxos.assetamount.md)*

___

###  getChangeAddresses

▸ **getChangeAddresses**(): *Array‹Buffer›*

Defined in src/apis/avm/utxos.ts:194

**Returns:** *Array‹Buffer›*

___

###  getChangeOutputs

▸ **getChangeOutputs**(): *Array‹[TransferableOutput](api_avm_outputs.transferableoutput.md)›*

Defined in src/apis/avm/utxos.ts:214

**Returns:** *Array‹[TransferableOutput](api_avm_outputs.transferableoutput.md)›*

___

###  getDestinations

▸ **getDestinations**(): *Array‹Buffer›*

Defined in src/apis/avm/utxos.ts:186

**Returns:** *Array‹Buffer›*

___

###  getInputs

▸ **getInputs**(): *Array‹[TransferableInput](api_avm_inputs.transferableinput.md)›*

Defined in src/apis/avm/utxos.ts:206

**Returns:** *Array‹[TransferableInput](api_avm_inputs.transferableinput.md)›*

___

###  getOutputs

▸ **getOutputs**(): *Array‹[TransferableOutput](api_avm_outputs.transferableoutput.md)›*

Defined in src/apis/avm/utxos.ts:210

**Returns:** *Array‹[TransferableOutput](api_avm_outputs.transferableoutput.md)›*

___

###  getSenders

▸ **getSenders**(): *Array‹Buffer›*

Defined in src/apis/avm/utxos.ts:190

**Returns:** *Array‹Buffer›*
