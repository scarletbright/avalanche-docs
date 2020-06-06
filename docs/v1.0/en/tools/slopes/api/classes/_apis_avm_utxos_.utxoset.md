[slopes - v1.7.3](../README.md) › ["apis/avm/utxos"](../modules/_apis_avm_utxos_.md) › [UTXOSet](_apis_avm_utxos_.utxoset.md)

# Class: UTXOSet

Class representing a set of [UTXO](_apis_avm_utxos_.utxo.md)s.

## Hierarchy

* **UTXOSet**

## Index

### Properties

* [addressUTXOs](_apis_avm_utxos_.utxoset.md#protected-addressutxos)
* [utxos](_apis_avm_utxos_.utxoset.md#protected-utxos)

### Methods

* [add](_apis_avm_utxos_.utxoset.md#add)
* [addArray](_apis_avm_utxos_.utxoset.md#addarray)
* [difference](_apis_avm_utxos_.utxoset.md#difference)
* [getAddresses](_apis_avm_utxos_.utxoset.md#getaddresses)
* [getAllUTXOStrings](_apis_avm_utxos_.utxoset.md#getallutxostrings)
* [getAllUTXOs](_apis_avm_utxos_.utxoset.md#getallutxos)
* [getAssetIDs](_apis_avm_utxos_.utxoset.md#getassetids)
* [getBalance](_apis_avm_utxos_.utxoset.md#getbalance)
* [getUTXO](_apis_avm_utxos_.utxoset.md#getutxo)
* [getUTXOIDs](_apis_avm_utxos_.utxoset.md#getutxoids)
* [includes](_apis_avm_utxos_.utxoset.md#includes)
* [intersection](_apis_avm_utxos_.utxoset.md#intersection)
* [makeBaseTx](_apis_avm_utxos_.utxoset.md#makebasetx)
* [makeCreateAssetTx](_apis_avm_utxos_.utxoset.md#makecreateassettx)
* [makeNFTTransferTx](_apis_avm_utxos_.utxoset.md#makenfttransfertx)
* [merge](_apis_avm_utxos_.utxoset.md#merge)
* [mergeByRule](_apis_avm_utxos_.utxoset.md#mergebyrule)
* [remove](_apis_avm_utxos_.utxoset.md#remove)
* [removeArray](_apis_avm_utxos_.utxoset.md#removearray)
* [symDifference](_apis_avm_utxos_.utxoset.md#symdifference)
* [union](_apis_avm_utxos_.utxoset.md#union)

## Properties

### `Protected` addressUTXOs

• **addressUTXOs**: *object*

*Defined in [apis/avm/utxos.ts:154](https://github.com/ava-labs/slopes/blob/48cc94f/src/apis/avm/utxos.ts#L154)*

#### Type declaration:

* \[ **address**: *string*\]: object

* \[ **utxoid**: *string*\]: BN

___

### `Protected` utxos

• **utxos**: *object*

*Defined in [apis/avm/utxos.ts:153](https://github.com/ava-labs/slopes/blob/48cc94f/src/apis/avm/utxos.ts#L153)*

#### Type declaration:

* \[ **utxoid**: *string*\]: [UTXO](_apis_avm_utxos_.utxo.md)

## Methods

###  add

▸ **add**(`utxo`: [UTXO](_apis_avm_utxos_.utxo.md) | string, `overwrite`: boolean): *[UTXO](_apis_avm_utxos_.utxo.md)*

*Defined in [apis/avm/utxos.ts:181](https://github.com/ava-labs/slopes/blob/48cc94f/src/apis/avm/utxos.ts#L181)*

Adds a UTXO to the UTXOSet.

**Parameters:**

Name | Type | Default | Description |
------ | ------ | ------ | ------ |
`utxo` | [UTXO](_apis_avm_utxos_.utxo.md) &#124; string | - | Either a [UTXO](_apis_avm_utxos_.utxo.md) an AVA serialized string representing a UTXO |
`overwrite` | boolean | false | If true, if the UTXOID already exists, overwrite it... default false  |

**Returns:** *[UTXO](_apis_avm_utxos_.utxo.md)*

A [UTXO](_apis_avm_utxos_.utxo.md) if one was added and undefined if nothing was added.

___

###  addArray

▸ **addArray**(`utxos`: Array‹string | [UTXO](_apis_avm_utxos_.utxo.md)›, `overwrite`: boolean): *Array‹[UTXO](_apis_avm_utxos_.utxo.md)›*

*Defined in [apis/avm/utxos.ts:218](https://github.com/ava-labs/slopes/blob/48cc94f/src/apis/avm/utxos.ts#L218)*

Adds an array of [UTXO](_apis_avm_utxos_.utxo.md)s to the [UTXOSet](_apis_avm_utxos_.utxoset.md).

**Parameters:**

Name | Type | Default | Description |
------ | ------ | ------ | ------ |
`utxos` | Array‹string &#124; [UTXO](_apis_avm_utxos_.utxo.md)› | - | - |
`overwrite` | boolean | false | If true, if the UTXOID already exists, overwrite it... default false  |

**Returns:** *Array‹[UTXO](_apis_avm_utxos_.utxo.md)›*

An array of UTXOs which were added.

___

###  difference

▸ **difference**(`utxoset`: [UTXOSet](_apis_avm_utxos_.utxoset.md)): *[UTXOSet](_apis_avm_utxos_.utxoset.md)*

*Defined in [apis/avm/utxos.ts:656](https://github.com/ava-labs/slopes/blob/48cc94f/src/apis/avm/utxos.ts#L656)*

Set difference between this set and a parameter.

**Parameters:**

Name | Type | Description |
------ | ------ | ------ |
`utxoset` | [UTXOSet](_apis_avm_utxos_.utxoset.md) | The set to difference  |

**Returns:** *[UTXOSet](_apis_avm_utxos_.utxoset.md)*

A new UTXOSet containing the difference

___

###  getAddresses

▸ **getAddresses**(): *Array‹Buffer›*

*Defined in [apis/avm/utxos.ts:363](https://github.com/ava-labs/slopes/blob/48cc94f/src/apis/avm/utxos.ts#L363)*

Gets the addresses in the [UTXOSet](_apis_avm_utxos_.utxoset.md) and returns an array of [Buffer](https://github.com/feross/buffer).

**Returns:** *Array‹Buffer›*

___

###  getAllUTXOStrings

▸ **getAllUTXOStrings**(`utxoids`: Array‹string›): *Array‹string›*

*Defined in [apis/avm/utxos.ts:316](https://github.com/ava-labs/slopes/blob/48cc94f/src/apis/avm/utxos.ts#L316)*

Gets all the [UTXO](_apis_avm_utxos_.utxo.md)s as strings, optionally that match with UTXOIDs in an array.

**Parameters:**

Name | Type | Default | Description |
------ | ------ | ------ | ------ |
`utxoids` | Array‹string› |  undefined | An optional array of UTXOIDs, returns all [UTXO](_apis_avm_utxos_.utxo.md)s if not provided  |

**Returns:** *Array‹string›*

An array of [UTXO](_apis_avm_utxos_.utxo.md)s as AVA serialized strings.

___

###  getAllUTXOs

▸ **getAllUTXOs**(`utxoids`: Array‹string›): *Array‹[UTXO](_apis_avm_utxos_.utxo.md)›*

*Defined in [apis/avm/utxos.ts:295](https://github.com/ava-labs/slopes/blob/48cc94f/src/apis/avm/utxos.ts#L295)*

Gets all the [UTXO](_apis_avm_utxos_.utxo.md)s, optionally that match with UTXOIDs in an array

**Parameters:**

Name | Type | Default | Description |
------ | ------ | ------ | ------ |
`utxoids` | Array‹string› |  undefined | An optional array of UTXOIDs, returns all [UTXO](_apis_avm_utxos_.utxo.md)s if not provided  |

**Returns:** *Array‹[UTXO](_apis_avm_utxos_.utxo.md)›*

An array of [UTXO](_apis_avm_utxos_.utxo.md)s.

___

###  getAssetIDs

▸ **getAssetIDs**(`addresses`: Array‹Buffer›): *Array‹Buffer›*

*Defined in [apis/avm/utxos.ts:401](https://github.com/ava-labs/slopes/blob/48cc94f/src/apis/avm/utxos.ts#L401)*

Gets all the Asset IDs, optionally that match with Asset IDs in an array

**Parameters:**

Name | Type | Default |
------ | ------ | ------ |
`addresses` | Array‹Buffer› |  undefined |

**Returns:** *Array‹Buffer›*

An array of [Buffer](https://github.com/feross/buffer) representing the Asset IDs.

___

###  getBalance

▸ **getBalance**(`addresses`: Array‹Buffer›, `assetID`: Buffer | string, `asOf`: BN): *BN*

*Defined in [apis/avm/utxos.ts:376](https://github.com/ava-labs/slopes/blob/48cc94f/src/apis/avm/utxos.ts#L376)*

Returns the balance of a set of addresses in the UTXOSet.

**Parameters:**

Name | Type | Default | Description |
------ | ------ | ------ | ------ |
`addresses` | Array‹Buffer› | - | An array of addresses |
`assetID` | Buffer &#124; string | - | Either a [Buffer](https://github.com/feross/buffer) or an AVA serialized representation of an AssetID |
`asOf` | BN |  undefined | The timestamp to verify the transaction against as a [BN](https://github.com/indutny/bn.js/)  |

**Returns:** *BN*

Returns the total balance as a [BN](https://github.com/indutny/bn.js/).

___

###  getUTXO

▸ **getUTXO**(`utxoid`: string): *[UTXO](_apis_avm_utxos_.utxo.md)*

*Defined in [apis/avm/utxos.ts:284](https://github.com/ava-labs/slopes/blob/48cc94f/src/apis/avm/utxos.ts#L284)*

Gets a [UTXO](_apis_avm_utxos_.utxo.md) from the [UTXOSet](_apis_avm_utxos_.utxoset.md) by its UTXOID.

**Parameters:**

Name | Type | Description |
------ | ------ | ------ |
`utxoid` | string | String representing the UTXOID  |

**Returns:** *[UTXO](_apis_avm_utxos_.utxo.md)*

A [UTXO](_apis_avm_utxos_.utxo.md) if it exists in the set.

___

###  getUTXOIDs

▸ **getUTXOIDs**(`addresses`: Array‹Buffer›, `spendable`: boolean): *Array‹string›*

*Defined in [apis/avm/utxos.ts:341](https://github.com/ava-labs/slopes/blob/48cc94f/src/apis/avm/utxos.ts#L341)*

Given an address or array of addresses, returns all the UTXOIDs for those addresses

**Parameters:**

Name | Type | Default | Description |
------ | ------ | ------ | ------ |
`addresses` | Array‹Buffer› |  undefined | - |
`spendable` | boolean | true | If true, only retrieves UTXOIDs whose locktime has passed  |

**Returns:** *Array‹string›*

An array of addresses.

___

###  includes

▸ **includes**(`utxo`: [UTXO](_apis_avm_utxos_.utxo.md) | string): *boolean*

*Defined in [apis/avm/utxos.ts:161](https://github.com/ava-labs/slopes/blob/48cc94f/src/apis/avm/utxos.ts#L161)*

Returns true if the [UTXO](_apis_avm_utxos_.utxo.md) is in the UTXOSet.

**Parameters:**

Name | Type | Description |
------ | ------ | ------ |
`utxo` | [UTXO](_apis_avm_utxos_.utxo.md) &#124; string | Either a [UTXO](_apis_avm_utxos_.utxo.md) an AVA serialized string representing a UTXO  |

**Returns:** *boolean*

___

###  intersection

▸ **intersection**(`utxoset`: [UTXOSet](_apis_avm_utxos_.utxoset.md)): *[UTXOSet](_apis_avm_utxos_.utxoset.md)*

*Defined in [apis/avm/utxos.ts:641](https://github.com/ava-labs/slopes/blob/48cc94f/src/apis/avm/utxos.ts#L641)*

Set intersetion between this set and a parameter.

**Parameters:**

Name | Type | Description |
------ | ------ | ------ |
`utxoset` | [UTXOSet](_apis_avm_utxos_.utxoset.md) | The set to intersect  |

**Returns:** *[UTXOSet](_apis_avm_utxos_.utxoset.md)*

A new UTXOSet containing the intersection

___

###  makeBaseTx

▸ **makeBaseTx**(`networkid`: number, `blockchainid`: Buffer, `amount`: BN, `toAddresses`: Array‹Buffer›, `fromAddresses`: Array‹Buffer›, `changeAddresses`: Array‹Buffer›, `assetID`: Buffer, `asOf`: BN, `locktime`: BN, `threshold`: number, `outputID`: number): *[UnsignedTx](_apis_avm_tx_.unsignedtx.md)*

*Defined in [apis/avm/utxos.ts:438](https://github.com/ava-labs/slopes/blob/48cc94f/src/apis/avm/utxos.ts#L438)*

Creates an [UnsignedTx](_apis_avm_tx_.unsignedtx.md) wrapping a [BaseTx](_apis_avm_tx_.basetx.md). For more granular control, you may create your own
[UnsignedTx](_apis_avm_tx_.unsignedtx.md) wrapping a [BaseTx](_apis_avm_tx_.basetx.md) manually (with their corresponding [TransferableInput](_apis_avm_inputs_.transferableinput.md)s and [TransferableOutput](_apis_avm_outputs_.transferableoutput.md)s).

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
`asOf` | BN |  UnixNow() | Optional. The timestamp to verify the transaction against as a [BN](https://github.com/indutny/bn.js/) |
`locktime` | BN |  new BN(0) | Optional. The locktime field created in the resulting outputs |
`threshold` | number | 1 | Optional. The number of signatures required to spend the funds in the resultant UTXO |
`outputID` | number |  AVMConstants.SECPOUTPUTID | Optional. The outputID used for this transaction, must implement AmountOutput, default AVMConstants.SECPOUTPUTID  |

**Returns:** *[UnsignedTx](_apis_avm_tx_.unsignedtx.md)*

An unsigned transaction created from the passed in parameters.

___

###  makeCreateAssetTx

▸ **makeCreateAssetTx**(`networkid`: number, `blockchainid`: Buffer, `avaAssetID`: Buffer, `fee`: BN, `feeSenderAddresses`: Array‹Buffer›, `initialState`: [InitialStates](_apis_avm_types_.initialstates.md), `name`: string, `symbol`: string, `denomination`: number): *[UnsignedTx](_apis_avm_tx_.unsignedtx.md)*

*Defined in [apis/avm/utxos.ts:538](https://github.com/ava-labs/slopes/blob/48cc94f/src/apis/avm/utxos.ts#L538)*

Creates an unsigned transaction. For more granular control, you may create your own
[[TxCreateAsset]] manually (with their corresponding [TransferableInput](_apis_avm_inputs_.transferableinput.md)s, [TransferableOutput](_apis_avm_outputs_.transferableoutput.md)s).

**Parameters:**

Name | Type | Description |
------ | ------ | ------ |
`networkid` | number | The number representing NetworkID of the node |
`blockchainid` | Buffer | The [Buffer](https://github.com/feross/buffer) representing the BlockchainID for the transaction |
`avaAssetID` | Buffer | - |
`fee` | BN | The amount of AVA to be paid for fees, in $nAVA |
`feeSenderAddresses` | Array‹Buffer› | The addresses to send the fees |
`initialState` | [InitialStates](_apis_avm_types_.initialstates.md) | The [InitialStates](_apis_avm_types_.initialstates.md)that represent the intial state of a created asset |
`name` | string | String for the descriptive name of the asset |
`symbol` | string | String for the ticker symbol of the asset |
`denomination` | number | Optional number for the denomination which is 10^D. D must be >= 0 and <= 32. Ex: $1 AVA = 10^9 $nAVA  |

**Returns:** *[UnsignedTx](_apis_avm_tx_.unsignedtx.md)*

An unsigned transaction created from the passed in parameters.

___

###  makeNFTTransferTx

▸ **makeNFTTransferTx**(`networkid`: number, `blockchainid`: Buffer, `feeAssetID`: Buffer, `fee`: BN, `feeSenderAddresses`: Array‹Buffer›, `toAddresses`: Array‹Buffer›, `fromAddresses`: Array‹Buffer›, `utxoids`: Array‹string›, `asOf`: BN, `locktime`: BN, `threshold`: number): *[UnsignedTx](_apis_avm_tx_.unsignedtx.md)*

*Defined in [apis/avm/utxos.ts:571](https://github.com/ava-labs/slopes/blob/48cc94f/src/apis/avm/utxos.ts#L571)*

Creates an unsigned NFT transfer transaction. For more granular control, you may create your own
[NFTTransferOperation](_apis_avm_ops_.nfttransferoperation.md) manually (with their corresponding [TransferableInput](_apis_avm_inputs_.transferableinput.md)s, [TransferableOutput](_apis_avm_outputs_.transferableoutput.md)s, and [[TransferOperation]]s).

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
`asOf` | BN |  UnixNow() | Optional. The timestamp to verify the transaction against as a [BN](https://github.com/indutny/bn.js/) |
`locktime` | BN |  new BN(0) | Optional. The locktime field created in the resulting outputs |
`threshold` | number | 1 | Optional. The number of signatures required to spend the funds in the resultant UTXO |

**Returns:** *[UnsignedTx](_apis_avm_tx_.unsignedtx.md)*

An unsigned transaction created from the passed in parameters.

___

###  merge

▸ **merge**(`utxoset`: [UTXOSet](_apis_avm_utxos_.utxoset.md), `hasUTXOIDs`: Array‹string›): *[UTXOSet](_apis_avm_utxos_.utxoset.md)*

*Defined in [apis/avm/utxos.ts:622](https://github.com/ava-labs/slopes/blob/48cc94f/src/apis/avm/utxos.ts#L622)*

Returns a new set with copy of UTXOs in this and set parameter.

**Parameters:**

Name | Type | Default | Description |
------ | ------ | ------ | ------ |
`utxoset` | [UTXOSet](_apis_avm_utxos_.utxoset.md) | - | The [UTXOSet](_apis_avm_utxos_.utxoset.md) to merge with this one |
`hasUTXOIDs` | Array‹string› |  undefined | Will subselect a set of [UTXO](_apis_avm_utxos_.utxo.md)s which have the UTXOIDs provided in this array, defults to all UTXOs  |

**Returns:** *[UTXOSet](_apis_avm_utxos_.utxoset.md)*

A new UTXOSet that contains all the filtered elements.

___

###  mergeByRule

▸ **mergeByRule**(`utxoset`: [UTXOSet](_apis_avm_utxos_.utxoset.md), `mergeRule`: [MergeRule](../modules/_apis_avm_types_.md#mergerule)): *[UTXOSet](_apis_avm_utxos_.utxoset.md)*

*Defined in [apis/avm/utxos.ts:709](https://github.com/ava-labs/slopes/blob/48cc94f/src/apis/avm/utxos.ts#L709)*

Merges a set by the rule provided.

**Parameters:**

Name | Type | Description |
------ | ------ | ------ |
`utxoset` | [UTXOSet](_apis_avm_utxos_.utxoset.md) | The set to merge by the MergeRule |
`mergeRule` | [MergeRule](../modules/_apis_avm_types_.md#mergerule) | The [MergeRule](../modules/_apis_avm_types_.md#mergerule) to apply  |

**Returns:** *[UTXOSet](_apis_avm_utxos_.utxoset.md)*

A new UTXOSet containing the merged data

___

###  remove

▸ **remove**(`utxo`: [UTXO](_apis_avm_utxos_.utxo.md) | string): *[UTXO](_apis_avm_utxos_.utxo.md)*

*Defined in [apis/avm/utxos.ts:236](https://github.com/ava-labs/slopes/blob/48cc94f/src/apis/avm/utxos.ts#L236)*

Removes a [UTXO](_apis_avm_utxos_.utxo.md) from the [UTXOSet](_apis_avm_utxos_.utxoset.md) if it exists.

**Parameters:**

Name | Type | Description |
------ | ------ | ------ |
`utxo` | [UTXO](_apis_avm_utxos_.utxo.md) &#124; string | Either a [UTXO](_apis_avm_utxos_.utxo.md) an AVA serialized string representing a UTXO  |

**Returns:** *[UTXO](_apis_avm_utxos_.utxo.md)*

A [UTXO](_apis_avm_utxos_.utxo.md) if it was removed and undefined if nothing was removed.

___

###  removeArray

▸ **removeArray**(`utxos`: Array‹string | [UTXO](_apis_avm_utxos_.utxo.md)›): *Array‹[UTXO](_apis_avm_utxos_.utxo.md)›*

*Defined in [apis/avm/utxos.ts:266](https://github.com/ava-labs/slopes/blob/48cc94f/src/apis/avm/utxos.ts#L266)*

Removes an array of [UTXO](_apis_avm_utxos_.utxo.md)s to the [UTXOSet](_apis_avm_utxos_.utxoset.md).

**Parameters:**

Name | Type |
------ | ------ |
`utxos` | Array‹string &#124; [UTXO](_apis_avm_utxos_.utxo.md)› |

**Returns:** *Array‹[UTXO](_apis_avm_utxos_.utxo.md)›*

An array of UTXOs which were removed.

___

###  symDifference

▸ **symDifference**(`utxoset`: [UTXOSet](_apis_avm_utxos_.utxoset.md)): *[UTXOSet](_apis_avm_utxos_.utxoset.md)*

*Defined in [apis/avm/utxos.ts:671](https://github.com/ava-labs/slopes/blob/48cc94f/src/apis/avm/utxos.ts#L671)*

Set symmetrical difference between this set and a parameter.

**Parameters:**

Name | Type | Description |
------ | ------ | ------ |
`utxoset` | [UTXOSet](_apis_avm_utxos_.utxoset.md) | The set to symmetrical difference  |

**Returns:** *[UTXOSet](_apis_avm_utxos_.utxoset.md)*

A new UTXOSet containing the symmetrical difference

___

###  union

▸ **union**(`utxoset`: [UTXOSet](_apis_avm_utxos_.utxoset.md)): *[UTXOSet](_apis_avm_utxos_.utxoset.md)*

*Defined in [apis/avm/utxos.ts:687](https://github.com/ava-labs/slopes/blob/48cc94f/src/apis/avm/utxos.ts#L687)*

Set union between this set and a parameter.

**Parameters:**

Name | Type | Description |
------ | ------ | ------ |
`utxoset` | [UTXOSet](_apis_avm_utxos_.utxoset.md) | The set to union  |

**Returns:** *[UTXOSet](_apis_avm_utxos_.utxoset.md)*

A new UTXOSet containing the union
