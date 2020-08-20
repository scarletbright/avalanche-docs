[avalanche](../README.md) › [API-PlatformVM-UTXOs](../modules/api_platformvm_utxos.md) › [AssetAmountDestination](api_platformvm_utxos.assetamountdestination.md)

# Class: AssetAmountDestination

## Hierarchy

* **AssetAmountDestination**

## Index

### Constructors

* [constructor](api_platformvm_utxos.assetamountdestination.md#constructor)

### Properties

* [amountkey](api_platformvm_utxos.assetamountdestination.md#protected-amountkey)
* [amounts](api_platformvm_utxos.assetamountdestination.md#protected-amounts)
* [change](api_platformvm_utxos.assetamountdestination.md#protected-change)
* [changeAddresses](api_platformvm_utxos.assetamountdestination.md#protected-changeaddresses)
* [destinations](api_platformvm_utxos.assetamountdestination.md#protected-destinations)
* [inputs](api_platformvm_utxos.assetamountdestination.md#protected-inputs)
* [outputs](api_platformvm_utxos.assetamountdestination.md#protected-outputs)
* [senders](api_platformvm_utxos.assetamountdestination.md#protected-senders)

### Methods

* [addAssetAmount](api_platformvm_utxos.assetamountdestination.md#addassetamount)
* [addChange](api_platformvm_utxos.assetamountdestination.md#addchange)
* [addInput](api_platformvm_utxos.assetamountdestination.md#addinput)
* [addOutput](api_platformvm_utxos.assetamountdestination.md#addoutput)
* [assetExists](api_platformvm_utxos.assetamountdestination.md#assetexists)
* [canComplete](api_platformvm_utxos.assetamountdestination.md#cancomplete)
* [getAllOutputs](api_platformvm_utxos.assetamountdestination.md#getalloutputs)
* [getAmounts](api_platformvm_utxos.assetamountdestination.md#getamounts)
* [getAssetAmount](api_platformvm_utxos.assetamountdestination.md#getassetamount)
* [getChangeAddresses](api_platformvm_utxos.assetamountdestination.md#getchangeaddresses)
* [getChangeOutputs](api_platformvm_utxos.assetamountdestination.md#getchangeoutputs)
* [getDestinations](api_platformvm_utxos.assetamountdestination.md#getdestinations)
* [getInputs](api_platformvm_utxos.assetamountdestination.md#getinputs)
* [getOutputs](api_platformvm_utxos.assetamountdestination.md#getoutputs)
* [getSenders](api_platformvm_utxos.assetamountdestination.md#getsenders)

## Constructors

###  constructor

\+ **new AssetAmountDestination**(`destinations`: Array‹Buffer›, `senders`: Array‹Buffer›, `changeAddresses`: Array‹Buffer›): *[AssetAmountDestination](api_platformvm_utxos.assetamountdestination.md)*

Defined in src/apis/platformvm/utxos.ts:225

**Parameters:**

Name | Type |
------ | ------ |
`destinations` | Array‹Buffer› |
`senders` | Array‹Buffer› |
`changeAddresses` | Array‹Buffer› |

**Returns:** *[AssetAmountDestination](api_platformvm_utxos.assetamountdestination.md)*

## Properties

### `Protected` amountkey

• **amountkey**: *object*

Defined in src/apis/platformvm/utxos.ts:154

___

### `Protected` amounts

• **amounts**: *Array‹[AssetAmount](api_platformvm_utxos.assetamount.md)›* = []

Defined in src/apis/platformvm/utxos.ts:150

___

### `Protected` change

• **change**: *Array‹[TransferableOutput](api_platformvm_outputs.transferableoutput.md)›* = []

Defined in src/apis/platformvm/utxos.ts:157

___

### `Protected` changeAddresses

• **changeAddresses**: *Array‹Buffer›* = []

Defined in src/apis/platformvm/utxos.ts:153

___

### `Protected` destinations

• **destinations**: *Array‹Buffer›* = []

Defined in src/apis/platformvm/utxos.ts:151

___

### `Protected` inputs

• **inputs**: *Array‹[TransferableInput](api_platformvm_inputs.transferableinput.md)›* = []

Defined in src/apis/platformvm/utxos.ts:155

___

### `Protected` outputs

• **outputs**: *Array‹[TransferableOutput](api_platformvm_outputs.transferableoutput.md)›* = []

Defined in src/apis/platformvm/utxos.ts:156

___

### `Protected` senders

• **senders**: *Array‹Buffer›* = []

Defined in src/apis/platformvm/utxos.ts:152

## Methods

###  addAssetAmount

▸ **addAssetAmount**(`assetID`: Buffer, `amount`: BN, `burn`: BN): *void*

Defined in src/apis/platformvm/utxos.ts:159

**Parameters:**

Name | Type |
------ | ------ |
`assetID` | Buffer |
`amount` | BN |
`burn` | BN |

**Returns:** *void*

___

###  addChange

▸ **addChange**(`output`: [TransferableOutput](api_platformvm_outputs.transferableoutput.md)): *void*

Defined in src/apis/platformvm/utxos.ts:173

**Parameters:**

Name | Type |
------ | ------ |
`output` | [TransferableOutput](api_platformvm_outputs.transferableoutput.md) |

**Returns:** *void*

___

###  addInput

▸ **addInput**(`input`: [TransferableInput](api_platformvm_inputs.transferableinput.md)): *void*

Defined in src/apis/platformvm/utxos.ts:165

**Parameters:**

Name | Type |
------ | ------ |
`input` | [TransferableInput](api_platformvm_inputs.transferableinput.md) |

**Returns:** *void*

___

###  addOutput

▸ **addOutput**(`output`: [TransferableOutput](api_platformvm_outputs.transferableoutput.md)): *void*

Defined in src/apis/platformvm/utxos.ts:169

**Parameters:**

Name | Type |
------ | ------ |
`output` | [TransferableOutput](api_platformvm_outputs.transferableoutput.md) |

**Returns:** *void*

___

###  assetExists

▸ **assetExists**(`assetHexStr`: string): *boolean*

Defined in src/apis/platformvm/utxos.ts:197

**Parameters:**

Name | Type |
------ | ------ |
`assetHexStr` | string |

**Returns:** *boolean*

___

###  canComplete

▸ **canComplete**(): *boolean*

Defined in src/apis/platformvm/utxos.ts:217

**Returns:** *boolean*

___

###  getAllOutputs

▸ **getAllOutputs**(): *Array‹[TransferableOutput](api_platformvm_outputs.transferableoutput.md)›*

Defined in src/apis/platformvm/utxos.ts:213

**Returns:** *Array‹[TransferableOutput](api_platformvm_outputs.transferableoutput.md)›*

___

###  getAmounts

▸ **getAmounts**(): *Array‹[AssetAmount](api_platformvm_utxos.assetamount.md)›*

Defined in src/apis/platformvm/utxos.ts:177

**Returns:** *Array‹[AssetAmount](api_platformvm_utxos.assetamount.md)›*

___

###  getAssetAmount

▸ **getAssetAmount**(`assetHexStr`: string): *[AssetAmount](api_platformvm_utxos.assetamount.md)*

Defined in src/apis/platformvm/utxos.ts:193

**Parameters:**

Name | Type |
------ | ------ |
`assetHexStr` | string |

**Returns:** *[AssetAmount](api_platformvm_utxos.assetamount.md)*

___

###  getChangeAddresses

▸ **getChangeAddresses**(): *Array‹Buffer›*

Defined in src/apis/platformvm/utxos.ts:189

**Returns:** *Array‹Buffer›*

___

###  getChangeOutputs

▸ **getChangeOutputs**(): *Array‹[TransferableOutput](api_platformvm_outputs.transferableoutput.md)›*

Defined in src/apis/platformvm/utxos.ts:209

**Returns:** *Array‹[TransferableOutput](api_platformvm_outputs.transferableoutput.md)›*

___

###  getDestinations

▸ **getDestinations**(): *Array‹Buffer›*

Defined in src/apis/platformvm/utxos.ts:181

**Returns:** *Array‹Buffer›*

___

###  getInputs

▸ **getInputs**(): *Array‹[TransferableInput](api_platformvm_inputs.transferableinput.md)›*

Defined in src/apis/platformvm/utxos.ts:201

**Returns:** *Array‹[TransferableInput](api_platformvm_inputs.transferableinput.md)›*

___

###  getOutputs

▸ **getOutputs**(): *Array‹[TransferableOutput](api_platformvm_outputs.transferableoutput.md)›*

Defined in src/apis/platformvm/utxos.ts:205

**Returns:** *Array‹[TransferableOutput](api_platformvm_outputs.transferableoutput.md)›*

___

###  getSenders

▸ **getSenders**(): *Array‹Buffer›*

Defined in src/apis/platformvm/utxos.ts:185

**Returns:** *Array‹Buffer›*
