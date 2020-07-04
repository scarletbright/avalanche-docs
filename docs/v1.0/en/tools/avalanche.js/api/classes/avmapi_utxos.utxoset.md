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

*Defined in [src/apis/avm/utxos.ts:165](https://github.com/ava-labs/avalanche.js/blob/eabcc2f/src/apis/avm/utxos.ts#L165)*

#### Type declaration:

* \[ **address**: *string*\]: object

* \[ **utxoid**: *string*\]: BN

___

### `Protected` utxos

• **utxos**: *object*

*Defined in [src/apis/avm/utxos.ts:163](https://github.com/ava-labs/avalanche.js/blob/eabcc2f/src/apis/avm/utxos.ts#L163)*

#### Type declaration:

* \[ **utxoid**: *string*\]: [UTXO](avmapi_utxos.utxo.md)

## Methods

###  add

▸ **add**(`utxo`: [UTXO](avmapi_utxos.utxo.md) | string, `overwrite`: boolean): *[UTXO](avmapi_utxos.utxo.md)*

*Defined in [src/apis/avm/utxos.ts:192](https://github.com/ava-labs/avalanche.js/blob/eabcc2f/src/apis/avm/utxos.ts#L192)*

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

*Defined in [src/apis/avm/utxos.ts:229](https://github.com/ava-labs/avalanche.js/blob/eabcc2f/src/apis/avm/utxos.ts#L229)*

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

*Defined in [src/apis/avm/utxos.ts:449](https://github.com/ava-labs/avalanche.js/blob/eabcc2f/src/apis/avm/utxos.ts#L449)*

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

*Defined in [src/apis/avm/utxos.ts:557](https://github.com/ava-labs/avalanche.js/blob/eabcc2f/src/apis/avm/utxos.ts#L557)*

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

*Defined in [src/apis/avm/utxos.ts:598](https://github.com/ava-labs/avalanche.js/blob/eabcc2f/src/apis/avm/utxos.ts#L598)*

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

*Defined in [src/apis/avm/utxos.ts:683](https://github.com/ava-labs/avalanche.js/blob/eabcc2f/src/apis/avm/utxos.ts#L683)*

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

*Defined in [src/apis/avm/utxos.ts:374](https://github.com/ava-labs/avalanche.js/blob/eabcc2f/src/apis/avm/utxos.ts#L374)*

Gets the addresses in the [UTXOSet](avmapi_utxos.utxoset.md) and returns an array of [Buffer](https://github.com/feross/buffer).

**Returns:** *Array‹Buffer›*

___

###  getAllUTXOStrings

▸ **getAllUTXOStrings**(`utxoids`: Array‹string›): *Array‹string›*

*Defined in [src/apis/avm/utxos.ts:325](https://github.com/ava-labs/avalanche.js/blob/eabcc2f/src/apis/avm/utxos.ts#L325)*

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

*Defined in [src/apis/avm/utxos.ts:304](https://github.com/ava-labs/avalanche.js/blob/eabcc2f/src/apis/avm/utxos.ts#L304)*

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

*Defined in [src/apis/avm/utxos.ts:413](https://github.com/ava-labs/avalanche.js/blob/eabcc2f/src/apis/avm/utxos.ts#L413)*

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

*Defined in [src/apis/avm/utxos.ts:386](https://github.com/ava-labs/avalanche.js/blob/eabcc2f/src/apis/avm/utxos.ts#L386)*

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

*Defined in [src/apis/avm/utxos.ts:295](https://github.com/ava-labs/avalanche.js/blob/eabcc2f/src/apis/avm/utxos.ts#L295)*

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

*Defined in [src/apis/avm/utxos.ts:350](https://github.com/ava-labs/avalanche.js/blob/eabcc2f/src/apis/avm/utxos.ts#L350)*

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

*Defined in [src/apis/avm/utxos.ts:172](https://github.com/ava-labs/avalanche.js/blob/eabcc2f/src/apis/avm/utxos.ts#L172)*

Returns true if the [UTXO](avmapi_utxos.utxo.md) is in the UTXOSet.

**Parameters:**

Name | Type | Description |
------ | ------ | ------ |
`utxo` | [UTXO](avmapi_utxos.utxo.md) &#124; string | Either a [UTXO](avmapi_utxos.utxo.md) an AVA serialized string representing a UTXO  |

**Returns:** *boolean*

___

###  intersection

▸ **intersection**(`utxoset`: [UTXOSet](avmapi_utxos.utxoset.md)): *[UTXOSet](avmapi_utxos.utxoset.md)*

*Defined in [src/apis/avm/utxos.ts:669](https://github.com/ava-labs/avalanche.js/blob/eabcc2f/src/apis/avm/utxos.ts#L669)*

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

*Defined in [src/apis/avm/utxos.ts:650](https://github.com/ava-labs/avalanche.js/blob/eabcc2f/src/apis/avm/utxos.ts#L650)*

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

*Defined in [src/apis/avm/utxos.ts:732](https://github.com/ava-labs/avalanche.js/blob/eabcc2f/src/apis/avm/utxos.ts#L732)*

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

*Defined in [src/apis/avm/utxos.ts:247](https://github.com/ava-labs/avalanche.js/blob/eabcc2f/src/apis/avm/utxos.ts#L247)*

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

*Defined in [src/apis/avm/utxos.ts:277](https://github.com/ava-labs/avalanche.js/blob/eabcc2f/src/apis/avm/utxos.ts#L277)*

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

*Defined in [src/apis/avm/utxos.ts:697](https://github.com/ava-labs/avalanche.js/blob/eabcc2f/src/apis/avm/utxos.ts#L697)*

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

*Defined in [src/apis/avm/utxos.ts:712](https://github.com/ava-labs/avalanche.js/blob/eabcc2f/src/apis/avm/utxos.ts#L712)*

Set union between this set and a parameter.

**Parameters:**

Name | Type | Description |
------ | ------ | ------ |
`utxoset` | [UTXOSet](avmapi_utxos.utxoset.md) | The set to union  |

**Returns:** *[UTXOSet](avmapi_utxos.utxoset.md)*

A new UTXOSet containing the union
