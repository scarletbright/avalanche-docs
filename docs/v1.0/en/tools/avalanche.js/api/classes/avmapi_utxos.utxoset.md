[avalanche](../README.md) › [AVMAPI-UTXOs](../modules/avmapi_utxos.md) › [UTXOSet](avmapi_utxos.utxoset.md)

# Class: UTXOSet

Class representing a set of [UTXO](avmapi_utxos.utxo.md)s.

## Hierarchy

* **UTXOSet**

## Index

### Properties

* [addressUTXOs](avmapi_utxos.utxoset.md#protected-addressutxos)
* [utxos](avmapi_utxos.utxoset.md#protected-utxos)

### Methods

* [add](avmapi_utxos.utxoset.md#add)
* [addArray](avmapi_utxos.utxoset.md#addarray)
* [buildBaseTx](avmapi_utxos.utxoset.md#buildbasetx)
* [buildCreateAssetTx](avmapi_utxos.utxoset.md#buildcreateassettx)
* [buildNFTTransferTx](avmapi_utxos.utxoset.md#buildnfttransfertx)
* [difference](avmapi_utxos.utxoset.md#difference)
* [getAddresses](avmapi_utxos.utxoset.md#getaddresses)
* [getAllUTXOStrings](avmapi_utxos.utxoset.md#getallutxostrings)
* [getAllUTXOs](avmapi_utxos.utxoset.md#getallutxos)
* [getAssetIDs](avmapi_utxos.utxoset.md#getassetids)
* [getBalance](avmapi_utxos.utxoset.md#getbalance)
* [getUTXO](avmapi_utxos.utxoset.md#getutxo)
* [getUTXOIDs](avmapi_utxos.utxoset.md#getutxoids)
* [includes](avmapi_utxos.utxoset.md#includes)
* [intersection](avmapi_utxos.utxoset.md#intersection)
* [merge](avmapi_utxos.utxoset.md#merge)
* [mergeByRule](avmapi_utxos.utxoset.md#mergebyrule)
* [remove](avmapi_utxos.utxoset.md#remove)
* [removeArray](avmapi_utxos.utxoset.md#removearray)
* [symDifference](avmapi_utxos.utxoset.md#symdifference)
* [union](avmapi_utxos.utxoset.md#union)

## Properties

### `Protected` addressUTXOs

• **addressUTXOs**: *object*

*Defined in [apis/avm/utxos.ts:154](https://github.com/ava-labs/avalanche.js/blob/3888064/src/apis/avm/utxos.ts#L154)*

#### Type declaration:

* \[ **address**: *string*\]: object

* \[ **utxoid**: *string*\]: BN

___

### `Protected` utxos

• **utxos**: *object*

*Defined in [apis/avm/utxos.ts:153](https://github.com/ava-labs/avalanche.js/blob/3888064/src/apis/avm/utxos.ts#L153)*

#### Type declaration:

* \[ **utxoid**: *string*\]: [UTXO](avmapi_utxos.utxo.md)

## Methods

###  add

▸ **add**(`utxo`: [UTXO](avmapi_utxos.utxo.md) | string, `overwrite`: boolean): *[UTXO](avmapi_utxos.utxo.md)*

*Defined in [apis/avm/utxos.ts:181](https://github.com/ava-labs/avalanche.js/blob/3888064/src/apis/avm/utxos.ts#L181)*

Adds a UTXO to the UTXOSet.

**Parameters:**

Name | Type | Default | Description |
------ | ------ | ------ | ------ |
`utxo` | [UTXO](avmapi_utxos.utxo.md) &#124; string | - | Either a [UTXO](avmapi_utxos.utxo.md) an AVA serialized string representing a UTXO |
`overwrite` | boolean | false | If true, if the UTXOID already exists, overwrite it... default false  |

**Returns:** *[UTXO](avmapi_utxos.utxo.md)*

A [UTXO](avmapi_utxos.utxo.md) if one was added and undefined if nothing was added.

___

###  addArray

▸ **addArray**(`utxos`: Array‹string | [UTXO](avmapi_utxos.utxo.md)›, `overwrite`: boolean): *Array‹[UTXO](avmapi_utxos.utxo.md)›*

*Defined in [apis/avm/utxos.ts:218](https://github.com/ava-labs/avalanche.js/blob/3888064/src/apis/avm/utxos.ts#L218)*

Adds an array of [UTXO](avmapi_utxos.utxo.md)s to the [UTXOSet](avmapi_utxos.utxoset.md).

**Parameters:**

Name | Type | Default | Description |
------ | ------ | ------ | ------ |
`utxos` | Array‹string &#124; [UTXO](avmapi_utxos.utxo.md)› | - | - |
`overwrite` | boolean | false | If true, if the UTXOID already exists, overwrite it... default false  |

**Returns:** *Array‹[UTXO](avmapi_utxos.utxo.md)›*

An array of UTXOs which were added.

___

###  buildBaseTx

▸ **buildBaseTx**(`networkid`: number, `blockchainid`: Buffer, `amount`: BN, `toAddresses`: Array‹Buffer›, `fromAddresses`: Array‹Buffer›, `changeAddresses`: Array‹Buffer›, `assetID`: Buffer, `asOf`: BN, `locktime`: BN, `threshold`: number, `outputID`: number): *[UnsignedTx](avmapi_transactions.unsignedtx.md)*

*Defined in [apis/avm/utxos.ts:438](https://github.com/ava-labs/avalanche.js/blob/3888064/src/apis/avm/utxos.ts#L438)*

Creates an [UnsignedTx](avmapi_transactions.unsignedtx.md) wrapping a [BaseTx](avmapi_transactions.basetx.md). For more granular control, you may create your own
[UnsignedTx](avmapi_transactions.unsignedtx.md) wrapping a [BaseTx](avmapi_transactions.basetx.md) manually (with their corresponding [TransferableInput](avmapi_inputs.transferableinput.md)s and [TransferableOutput](avmapi_outputs.transferableoutput.md)s).

**Parameters:**

Name | Type | Default | Description |
------ | ------ | ------ | ------ |
`networkid` | number | - | The number representing NetworkID of the node |
`blockchainid` | Buffer | - | The [Buffer](https://github.com/feross/buffer) representing the BlockchainID for the transaction |
`amount` | BN | - | The amount of AVA to be spent in $nAVA |
`toAddresses` | Array‹Buffer› | - | The addresses to send the funds |
`fromAddresses` | Array‹Buffer› | - | The addresses being used to send the funds from the UTXOs [Buffer](https://github.com/feross/buffer) |
`changeAddresses` | Array‹Buffer› | - | The addresses that can spend the change remaining from the spent UTXOs |
`assetID` | Buffer | - | - |
`asOf` | BN | UnixNow() | Optional. The timestamp to verify the transaction against as a [BN](https://github.com/indutny/bn.js/) |
`locktime` | BN | new BN(0) | Optional. The locktime field created in the resulting outputs |
`threshold` | number | 1 | Optional. The number of signatures required to spend the funds in the resultant UTXO |
`outputID` | number | AVMConstants.SECPOUTPUTID | Optional. The outputID used for this transaction, must implement AmountOutput, default AVMConstants.SECPOUTPUTID  |

**Returns:** *[UnsignedTx](avmapi_transactions.unsignedtx.md)*

An unsigned transaction created from the passed in parameters.

___

###  buildCreateAssetTx

▸ **buildCreateAssetTx**(`networkid`: number, `blockchainid`: Buffer, `avaAssetID`: Buffer, `fee`: BN, `feeSenderAddresses`: Array‹Buffer›, `initialState`: [InitialStates](avmapi_types.initialstates.md), `name`: string, `symbol`: string, `denomination`: number): *[UnsignedTx](avmapi_transactions.unsignedtx.md)*

*Defined in [apis/avm/utxos.ts:538](https://github.com/ava-labs/avalanche.js/blob/3888064/src/apis/avm/utxos.ts#L538)*

Creates an unsigned transaction. For more granular control, you may create your own
[[TxCreateAsset]] manually (with their corresponding [TransferableInput](avmapi_inputs.transferableinput.md)s, [TransferableOutput](avmapi_outputs.transferableoutput.md)s).

**Parameters:**

Name | Type | Description |
------ | ------ | ------ |
`networkid` | number | The number representing NetworkID of the node |
`blockchainid` | Buffer | The [Buffer](https://github.com/feross/buffer) representing the BlockchainID for the transaction |
`avaAssetID` | Buffer | - |
`fee` | BN | The amount of AVA to be paid for fees, in $nAVA |
`feeSenderAddresses` | Array‹Buffer› | The addresses to send the fees |
`initialState` | [InitialStates](avmapi_types.initialstates.md) | The [InitialStates](avmapi_types.initialstates.md)that represent the intial state of a created asset |
`name` | string | String for the descriptive name of the asset |
`symbol` | string | String for the ticker symbol of the asset |
`denomination` | number | Optional number for the denomination which is 10^D. D must be >= 0 and <= 32. Ex: $1 AVA = 10^9 $nAVA  |

**Returns:** *[UnsignedTx](avmapi_transactions.unsignedtx.md)*

An unsigned transaction created from the passed in parameters.

___

###  buildNFTTransferTx

▸ **buildNFTTransferTx**(`networkid`: number, `blockchainid`: Buffer, `feeAssetID`: Buffer, `fee`: BN, `feeSenderAddresses`: Array‹Buffer›, `toAddresses`: Array‹Buffer›, `fromAddresses`: Array‹Buffer›, `utxoids`: Array‹string›, `asOf`: BN, `locktime`: BN, `threshold`: number): *[UnsignedTx](avmapi_transactions.unsignedtx.md)*

*Defined in [apis/avm/utxos.ts:571](https://github.com/ava-labs/avalanche.js/blob/3888064/src/apis/avm/utxos.ts#L571)*

Creates an unsigned NFT transfer transaction. For more granular control, you may create your own
[NFTTransferOperation](avmapi_operations.nfttransferoperation.md) manually (with their corresponding [TransferableInput](avmapi_inputs.transferableinput.md)s, [TransferableOutput](avmapi_outputs.transferableoutput.md)s, and [[TransferOperation]]s).

**Parameters:**

Name | Type | Default | Description |
------ | ------ | ------ | ------ |
`networkid` | number | - | The number representing NetworkID of the node |
`blockchainid` | Buffer | - | The [Buffer](https://github.com/feross/buffer) representing the BlockchainID for the transaction |
`feeAssetID` | Buffer | - | The assetID for the AVA fee to be paid |
`fee` | BN | - | The amount of AVA to be paid for fees, in $nAVA |
`feeSenderAddresses` | Array‹Buffer› | - | The addresses to send the fees |
`toAddresses` | Array‹Buffer› | - | An array of [Buffer](https://github.com/feross/buffer)s which indicate who recieves the NFT |
`fromAddresses` | Array‹Buffer› | - | An array for [Buffer](https://github.com/feross/buffer) who owns the NFT |
`utxoids` | Array‹string› | - | An array of strings for the NFTs being transferred |
`asOf` | BN | UnixNow() | Optional. The timestamp to verify the transaction against as a [BN](https://github.com/indutny/bn.js/) |
`locktime` | BN | new BN(0) | Optional. The locktime field created in the resulting outputs |
`threshold` | number | 1 | Optional. The number of signatures required to spend the funds in the resultant UTXO |

**Returns:** *[UnsignedTx](avmapi_transactions.unsignedtx.md)*

An unsigned transaction created from the passed in parameters.

___

###  difference

▸ **difference**(`utxoset`: [UTXOSet](avmapi_utxos.utxoset.md)): *[UTXOSet](avmapi_utxos.utxoset.md)*

*Defined in [apis/avm/utxos.ts:656](https://github.com/ava-labs/avalanche.js/blob/3888064/src/apis/avm/utxos.ts#L656)*

Set difference between this set and a parameter.

**Parameters:**

Name | Type | Description |
------ | ------ | ------ |
`utxoset` | [UTXOSet](avmapi_utxos.utxoset.md) | The set to difference  |

**Returns:** *[UTXOSet](avmapi_utxos.utxoset.md)*

A new UTXOSet containing the difference

___

###  getAddresses

▸ **getAddresses**(): *Array‹Buffer›*

*Defined in [apis/avm/utxos.ts:363](https://github.com/ava-labs/avalanche.js/blob/3888064/src/apis/avm/utxos.ts#L363)*

Gets the addresses in the [UTXOSet](avmapi_utxos.utxoset.md) and returns an array of [Buffer](https://github.com/feross/buffer).

**Returns:** *Array‹Buffer›*

___

###  getAllUTXOStrings

▸ **getAllUTXOStrings**(`utxoids`: Array‹string›): *Array‹string›*

*Defined in [apis/avm/utxos.ts:316](https://github.com/ava-labs/avalanche.js/blob/3888064/src/apis/avm/utxos.ts#L316)*

Gets all the [UTXO](avmapi_utxos.utxo.md)s as strings, optionally that match with UTXOIDs in an array.

**Parameters:**

Name | Type | Default | Description |
------ | ------ | ------ | ------ |
`utxoids` | Array‹string› | undefined | An optional array of UTXOIDs, returns all [UTXO](avmapi_utxos.utxo.md)s if not provided  |

**Returns:** *Array‹string›*

An array of [UTXO](avmapi_utxos.utxo.md)s as AVA serialized strings.

___

###  getAllUTXOs

▸ **getAllUTXOs**(`utxoids`: Array‹string›): *Array‹[UTXO](avmapi_utxos.utxo.md)›*

*Defined in [apis/avm/utxos.ts:295](https://github.com/ava-labs/avalanche.js/blob/3888064/src/apis/avm/utxos.ts#L295)*

Gets all the [UTXO](avmapi_utxos.utxo.md)s, optionally that match with UTXOIDs in an array

**Parameters:**

Name | Type | Default | Description |
------ | ------ | ------ | ------ |
`utxoids` | Array‹string› | undefined | An optional array of UTXOIDs, returns all [UTXO](avmapi_utxos.utxo.md)s if not provided  |

**Returns:** *Array‹[UTXO](avmapi_utxos.utxo.md)›*

An array of [UTXO](avmapi_utxos.utxo.md)s.

___

###  getAssetIDs

▸ **getAssetIDs**(`addresses`: Array‹Buffer›): *Array‹Buffer›*

*Defined in [apis/avm/utxos.ts:401](https://github.com/ava-labs/avalanche.js/blob/3888064/src/apis/avm/utxos.ts#L401)*

Gets all the Asset IDs, optionally that match with Asset IDs in an array

**Parameters:**

Name | Type | Default |
------ | ------ | ------ |
`addresses` | Array‹Buffer› | undefined |

**Returns:** *Array‹Buffer›*

An array of [Buffer](https://github.com/feross/buffer) representing the Asset IDs.

___

###  getBalance

▸ **getBalance**(`addresses`: Array‹Buffer›, `assetID`: Buffer | string, `asOf`: BN): *BN*

*Defined in [apis/avm/utxos.ts:376](https://github.com/ava-labs/avalanche.js/blob/3888064/src/apis/avm/utxos.ts#L376)*

Returns the balance of a set of addresses in the UTXOSet.

**Parameters:**

Name | Type | Default | Description |
------ | ------ | ------ | ------ |
`addresses` | Array‹Buffer› | - | An array of addresses |
`assetID` | Buffer &#124; string | - | Either a [Buffer](https://github.com/feross/buffer) or an AVA serialized representation of an AssetID |
`asOf` | BN | undefined | The timestamp to verify the transaction against as a [BN](https://github.com/indutny/bn.js/)  |

**Returns:** *BN*

Returns the total balance as a [BN](https://github.com/indutny/bn.js/).

___

###  getUTXO

▸ **getUTXO**(`utxoid`: string): *[UTXO](avmapi_utxos.utxo.md)*

*Defined in [apis/avm/utxos.ts:284](https://github.com/ava-labs/avalanche.js/blob/3888064/src/apis/avm/utxos.ts#L284)*

Gets a [UTXO](avmapi_utxos.utxo.md) from the [UTXOSet](avmapi_utxos.utxoset.md) by its UTXOID.

**Parameters:**

Name | Type | Description |
------ | ------ | ------ |
`utxoid` | string | String representing the UTXOID  |

**Returns:** *[UTXO](avmapi_utxos.utxo.md)*

A [UTXO](avmapi_utxos.utxo.md) if it exists in the set.

___

###  getUTXOIDs

▸ **getUTXOIDs**(`addresses`: Array‹Buffer›, `spendable`: boolean): *Array‹string›*

*Defined in [apis/avm/utxos.ts:341](https://github.com/ava-labs/avalanche.js/blob/3888064/src/apis/avm/utxos.ts#L341)*

Given an address or array of addresses, returns all the UTXOIDs for those addresses

**Parameters:**

Name | Type | Default | Description |
------ | ------ | ------ | ------ |
`addresses` | Array‹Buffer› | undefined | - |
`spendable` | boolean | true | If true, only retrieves UTXOIDs whose locktime has passed  |

**Returns:** *Array‹string›*

An array of addresses.

___

###  includes

▸ **includes**(`utxo`: [UTXO](avmapi_utxos.utxo.md) | string): *boolean*

*Defined in [apis/avm/utxos.ts:161](https://github.com/ava-labs/avalanche.js/blob/3888064/src/apis/avm/utxos.ts#L161)*

Returns true if the [UTXO](avmapi_utxos.utxo.md) is in the UTXOSet.

**Parameters:**

Name | Type | Description |
------ | ------ | ------ |
`utxo` | [UTXO](avmapi_utxos.utxo.md) &#124; string | Either a [UTXO](avmapi_utxos.utxo.md) an AVA serialized string representing a UTXO  |

**Returns:** *boolean*

___

###  intersection

▸ **intersection**(`utxoset`: [UTXOSet](avmapi_utxos.utxoset.md)): *[UTXOSet](avmapi_utxos.utxoset.md)*

*Defined in [apis/avm/utxos.ts:641](https://github.com/ava-labs/avalanche.js/blob/3888064/src/apis/avm/utxos.ts#L641)*

Set intersetion between this set and a parameter.

**Parameters:**

Name | Type | Description |
------ | ------ | ------ |
`utxoset` | [UTXOSet](avmapi_utxos.utxoset.md) | The set to intersect  |

**Returns:** *[UTXOSet](avmapi_utxos.utxoset.md)*

A new UTXOSet containing the intersection

___

###  merge

▸ **merge**(`utxoset`: [UTXOSet](avmapi_utxos.utxoset.md), `hasUTXOIDs`: Array‹string›): *[UTXOSet](avmapi_utxos.utxoset.md)*

*Defined in [apis/avm/utxos.ts:622](https://github.com/ava-labs/avalanche.js/blob/3888064/src/apis/avm/utxos.ts#L622)*

Returns a new set with copy of UTXOs in this and set parameter.

**Parameters:**

Name | Type | Default | Description |
------ | ------ | ------ | ------ |
`utxoset` | [UTXOSet](avmapi_utxos.utxoset.md) | - | The [UTXOSet](avmapi_utxos.utxoset.md) to merge with this one |
`hasUTXOIDs` | Array‹string› | undefined | Will subselect a set of [UTXO](avmapi_utxos.utxo.md)s which have the UTXOIDs provided in this array, defults to all UTXOs  |

**Returns:** *[UTXOSet](avmapi_utxos.utxoset.md)*

A new UTXOSet that contains all the filtered elements.

___

###  mergeByRule

▸ **mergeByRule**(`utxoset`: [UTXOSet](avmapi_utxos.utxoset.md), `mergeRule`: [MergeRule](../modules/avmapi_types.md#mergerule)): *[UTXOSet](avmapi_utxos.utxoset.md)*

*Defined in [apis/avm/utxos.ts:709](https://github.com/ava-labs/avalanche.js/blob/3888064/src/apis/avm/utxos.ts#L709)*

Merges a set by the rule provided.

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

Name | Type | Description |
------ | ------ | ------ |
`utxoset` | [UTXOSet](avmapi_utxos.utxoset.md) | The set to merge by the MergeRule |
`mergeRule` | [MergeRule](../modules/avmapi_types.md#mergerule) | The [MergeRule](../modules/avmapi_types.md#mergerule) to apply  |

**Returns:** *[UTXOSet](avmapi_utxos.utxoset.md)*

A new UTXOSet containing the merged data

___

###  remove

▸ **remove**(`utxo`: [UTXO](avmapi_utxos.utxo.md) | string): *[UTXO](avmapi_utxos.utxo.md)*

*Defined in [apis/avm/utxos.ts:236](https://github.com/ava-labs/avalanche.js/blob/3888064/src/apis/avm/utxos.ts#L236)*

Removes a [UTXO](avmapi_utxos.utxo.md) from the [UTXOSet](avmapi_utxos.utxoset.md) if it exists.

**Parameters:**

Name | Type | Description |
------ | ------ | ------ |
`utxo` | [UTXO](avmapi_utxos.utxo.md) &#124; string | Either a [UTXO](avmapi_utxos.utxo.md) an AVA serialized string representing a UTXO  |

**Returns:** *[UTXO](avmapi_utxos.utxo.md)*

A [UTXO](avmapi_utxos.utxo.md) if it was removed and undefined if nothing was removed.

___

###  removeArray

▸ **removeArray**(`utxos`: Array‹string | [UTXO](avmapi_utxos.utxo.md)›): *Array‹[UTXO](avmapi_utxos.utxo.md)›*

*Defined in [apis/avm/utxos.ts:266](https://github.com/ava-labs/avalanche.js/blob/3888064/src/apis/avm/utxos.ts#L266)*

Removes an array of [UTXO](avmapi_utxos.utxo.md)s to the [UTXOSet](avmapi_utxos.utxoset.md).

**Parameters:**

Name | Type |
------ | ------ |
`utxos` | Array‹string &#124; [UTXO](avmapi_utxos.utxo.md)› |

**Returns:** *Array‹[UTXO](avmapi_utxos.utxo.md)›*

An array of UTXOs which were removed.

___

###  symDifference

▸ **symDifference**(`utxoset`: [UTXOSet](avmapi_utxos.utxoset.md)): *[UTXOSet](avmapi_utxos.utxoset.md)*

*Defined in [apis/avm/utxos.ts:671](https://github.com/ava-labs/avalanche.js/blob/3888064/src/apis/avm/utxos.ts#L671)*

Set symmetrical difference between this set and a parameter.

**Parameters:**

Name | Type | Description |
------ | ------ | ------ |
`utxoset` | [UTXOSet](avmapi_utxos.utxoset.md) | The set to symmetrical difference  |

**Returns:** *[UTXOSet](avmapi_utxos.utxoset.md)*

A new UTXOSet containing the symmetrical difference

___

###  union

▸ **union**(`utxoset`: [UTXOSet](avmapi_utxos.utxoset.md)): *[UTXOSet](avmapi_utxos.utxoset.md)*

*Defined in [apis/avm/utxos.ts:687](https://github.com/ava-labs/avalanche.js/blob/3888064/src/apis/avm/utxos.ts#L687)*

Set union between this set and a parameter.

**Parameters:**

Name | Type | Description |
------ | ------ | ------ |
`utxoset` | [UTXOSet](avmapi_utxos.utxoset.md) | The set to union  |

**Returns:** *[UTXOSet](avmapi_utxos.utxoset.md)*

A new UTXOSet containing the union
