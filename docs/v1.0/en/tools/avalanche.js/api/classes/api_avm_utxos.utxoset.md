[avalanche](../README.md) › [API-AVM-UTXOs](../modules/api_avm_utxos.md) › [UTXOSet](api_avm_utxos.utxoset.md)

# Class: UTXOSet

Class representing a set of [UTXO](api_avm_utxos.utxo.md)s.

## Hierarchy

* [StandardUTXOSet](common_utxos.standardutxoset.md)‹[UTXO](api_avm_utxos.utxo.md)›

  ↳ **UTXOSet**

## Index

### Properties

* [addressUTXOs](api_avm_utxos.utxoset.md#protected-addressutxos)
* [utxos](api_avm_utxos.utxoset.md#protected-utxos)

### Methods

* [_feeCheck](api_avm_utxos.utxoset.md#_feecheck)
* [add](api_avm_utxos.utxoset.md#add)
* [addArray](api_avm_utxos.utxoset.md#addarray)
* [buildBaseTx](api_avm_utxos.utxoset.md#buildbasetx)
* [buildCreateAssetTx](api_avm_utxos.utxoset.md#buildcreateassettx)
* [buildCreateNFTAssetTx](api_avm_utxos.utxoset.md#buildcreatenftassettx)
* [buildCreateNFTMintTx](api_avm_utxos.utxoset.md#buildcreatenftminttx)
* [buildExportTx](api_avm_utxos.utxoset.md#buildexporttx)
* [buildImportTx](api_avm_utxos.utxoset.md#buildimporttx)
* [buildNFTTransferTx](api_avm_utxos.utxoset.md#buildnfttransfertx)
* [buildSECPMintTx](api_avm_utxos.utxoset.md#buildsecpminttx)
* [clone](api_avm_utxos.utxoset.md#clone)
* [create](api_avm_utxos.utxoset.md#create)
* [difference](api_avm_utxos.utxoset.md#difference)
* [filter](api_avm_utxos.utxoset.md#filter)
* [getAddresses](api_avm_utxos.utxoset.md#getaddresses)
* [getAllUTXOStrings](api_avm_utxos.utxoset.md#getallutxostrings)
* [getAllUTXOs](api_avm_utxos.utxoset.md#getallutxos)
* [getAssetIDs](api_avm_utxos.utxoset.md#getassetids)
* [getBalance](api_avm_utxos.utxoset.md#getbalance)
* [getMinimumSpendable](api_avm_utxos.utxoset.md#getminimumspendable)
* [getUTXO](api_avm_utxos.utxoset.md#getutxo)
* [getUTXOIDs](api_avm_utxos.utxoset.md#getutxoids)
* [includes](api_avm_utxos.utxoset.md#includes)
* [intersection](api_avm_utxos.utxoset.md#intersection)
* [merge](api_avm_utxos.utxoset.md#merge)
* [mergeByRule](api_avm_utxos.utxoset.md#mergebyrule)
* [parseUTXO](api_avm_utxos.utxoset.md#parseutxo)
* [remove](api_avm_utxos.utxoset.md#remove)
* [removeArray](api_avm_utxos.utxoset.md#removearray)
* [symDifference](api_avm_utxos.utxoset.md#symdifference)
* [union](api_avm_utxos.utxoset.md#union)

## Properties

### `Protected` addressUTXOs

• **addressUTXOs**: *object*

*Inherited from [StandardUTXOSet](common_utxos.standardutxoset.md).[addressUTXOs](common_utxos.standardutxoset.md#protected-addressutxos)*

*Defined in [src/common/utxos.ts:147](https://github.com/ava-labs/avalanche.js/blob/a2feb77/src/common/utxos.ts#L147)*

#### Type declaration:

* \[ **address**: *string*\]: object

* \[ **utxoid**: *string*\]: BN

___

### `Protected` utxos

• **utxos**: *object*

*Inherited from [StandardUTXOSet](common_utxos.standardutxoset.md).[utxos](common_utxos.standardutxoset.md#protected-utxos)*

*Defined in [src/common/utxos.ts:145](https://github.com/ava-labs/avalanche.js/blob/a2feb77/src/common/utxos.ts#L145)*

#### Type declaration:

* \[ **utxoid**: *string*\]: [UTXO](api_avm_utxos.utxo.md)

## Methods

###  _feeCheck

▸ **_feeCheck**(`fee`: BN, `feeAssetID`: Buffer): *boolean*

*Defined in [src/apis/avm/utxos.ts:127](https://github.com/ava-labs/avalanche.js/blob/a2feb77/src/apis/avm/utxos.ts#L127)*

**Parameters:**

Name | Type |
------ | ------ |
`fee` | BN |
`feeAssetID` | Buffer |

**Returns:** *boolean*

___

###  add

▸ **add**(`utxo`: [UTXO](api_avm_utxos.utxo.md) | string, `overwrite`: boolean): *[UTXO](api_avm_utxos.utxo.md)*

*Inherited from [StandardUTXOSet](common_utxos.standardutxoset.md).[add](common_utxos.standardutxoset.md#add)*

*Defined in [src/common/utxos.ts:181](https://github.com/ava-labs/avalanche.js/blob/a2feb77/src/common/utxos.ts#L181)*

Adds a [StandardUTXO](common_utxos.standardutxo.md) to the StandardUTXOSet.

**Parameters:**

Name | Type | Default | Description |
------ | ------ | ------ | ------ |
`utxo` | [UTXO](api_avm_utxos.utxo.md) &#124; string | - | Either a [StandardUTXO](common_utxos.standardutxo.md) an cb58 serialized string representing a StandardUTXO |
`overwrite` | boolean | false | If true, if the UTXOID already exists, overwrite it... default false  |

**Returns:** *[UTXO](api_avm_utxos.utxo.md)*

A [StandardUTXO](common_utxos.standardutxo.md) if one was added and undefined if nothing was added.

___

###  addArray

▸ **addArray**(`utxos`: Array‹string | [UTXO](api_avm_utxos.utxo.md)›, `overwrite`: boolean): *Array‹[StandardUTXO](common_utxos.standardutxo.md)›*

*Inherited from [StandardUTXOSet](common_utxos.standardutxoset.md).[addArray](common_utxos.standardutxoset.md#addarray)*

*Defined in [src/common/utxos.ts:219](https://github.com/ava-labs/avalanche.js/blob/a2feb77/src/common/utxos.ts#L219)*

Adds an array of [StandardUTXO](common_utxos.standardutxo.md)s to the [StandardUTXOSet](common_utxos.standardutxoset.md).

**Parameters:**

Name | Type | Default | Description |
------ | ------ | ------ | ------ |
`utxos` | Array‹string &#124; [UTXO](api_avm_utxos.utxo.md)› | - | - |
`overwrite` | boolean | false | If true, if the UTXOID already exists, overwrite it... default false  |

**Returns:** *Array‹[StandardUTXO](common_utxos.standardutxo.md)›*

An array of StandardUTXOs which were added.

___

###  buildBaseTx

▸ **buildBaseTx**(`networkid`: number, `blockchainid`: Buffer, `amount`: BN, `assetID`: Buffer, `toAddresses`: Array‹Buffer›, `fromAddresses`: Array‹Buffer›, `changeAddresses`: Array‹Buffer›, `fee`: BN, `feeAssetID`: Buffer, `memo`: Buffer, `asOf`: BN, `locktime`: BN, `threshold`: number): *[UnsignedTx](api_avm_transactions.unsignedtx.md)*

*Defined in [src/apis/avm/utxos.ts:223](https://github.com/ava-labs/avalanche.js/blob/a2feb77/src/apis/avm/utxos.ts#L223)*

Creates an [UnsignedTx](api_avm_transactions.unsignedtx.md) wrapping a [BaseTx](api_avm_basetx.basetx.md). For more granular control, you may create your own
[UnsignedTx](api_avm_transactions.unsignedtx.md) wrapping a [BaseTx](api_avm_basetx.basetx.md) manually (with their corresponding [TransferableInput](api_avm_inputs.transferableinput.md)s and [TransferableOutput](api_avm_outputs.transferableoutput.md)s).

**Parameters:**

Name | Type | Default | Description |
------ | ------ | ------ | ------ |
`networkid` | number | - | The number representing NetworkID of the node |
`blockchainid` | Buffer | - | The [Buffer](https://github.com/feross/buffer) representing the BlockchainID for the transaction |
`amount` | BN | - | The amount of the asset to be spent in its smallest denomination, represented as [BN](https://github.com/indutny/bn.js/). |
`assetID` | Buffer | - | [Buffer](https://github.com/feross/buffer) of the asset ID for the UTXO |
`toAddresses` | Array‹Buffer› | - | The addresses to send the funds |
`fromAddresses` | Array‹Buffer› | - | The addresses being used to send the funds from the UTXOs [Buffer](https://github.com/feross/buffer) |
`changeAddresses` | Array‹Buffer› | undefined | Optional. The addresses that can spend the change remaining from the spent UTXOs. Default: toAddresses |
`fee` | BN | undefined | Optional. The amount of fees to burn in its smallest denomination, represented as [BN](https://github.com/indutny/bn.js/) |
`feeAssetID` | Buffer | undefined | Optional. The assetID of the fees being burned. Default: assetID |
`memo` | Buffer | undefined | Optional. Contains arbitrary data, up to 256 bytes |
`asOf` | BN | UnixNow() | Optional. The timestamp to verify the transaction against as a [BN](https://github.com/indutny/bn.js/) |
`locktime` | BN | new BN(0) | Optional. The locktime field created in the resulting outputs |
`threshold` | number | 1 | Optional. The number of signatures required to spend the funds in the resultant UTXO  |

**Returns:** *[UnsignedTx](api_avm_transactions.unsignedtx.md)*

An unsigned transaction created from the passed in parameters.

___

###  buildCreateAssetTx

▸ **buildCreateAssetTx**(`networkid`: number, `blockchainid`: Buffer, `fromAddresses`: Array‹Buffer›, `changeAddresses`: Array‹Buffer›, `initialState`: [InitialStates](api_avm_initialstates.initialstates.md), `name`: string, `symbol`: string, `denomination`: number, `mintOutputs`: Array‹[SECPMintOutput](api_avm_outputs.secpmintoutput.md)›, `fee`: BN, `feeAssetID`: Buffer, `memo`: Buffer, `asOf`: BN): *[UnsignedTx](api_avm_transactions.unsignedtx.md)*

*Defined in [src/apis/avm/utxos.ts:305](https://github.com/ava-labs/avalanche.js/blob/a2feb77/src/apis/avm/utxos.ts#L305)*

Creates an unsigned Create Asset transaction. For more granular control, you may create your own
[[CreateAssetTX]] manually (with their corresponding [TransferableInput](api_avm_inputs.transferableinput.md)s, [TransferableOutput](api_avm_outputs.transferableoutput.md)s).

**Parameters:**

Name | Type | Default | Description |
------ | ------ | ------ | ------ |
`networkid` | number | - | The number representing NetworkID of the node |
`blockchainid` | Buffer | - | The [Buffer](https://github.com/feross/buffer) representing the BlockchainID for the transaction |
`fromAddresses` | Array‹Buffer› | - | The addresses being used to send the funds from the UTXOs [Buffer](https://github.com/feross/buffer) |
`changeAddresses` | Array‹Buffer› | - | Optional. The addresses that can spend the change remaining from the spent UTXOs |
`initialState` | [InitialStates](api_avm_initialstates.initialstates.md) | - | The [InitialStates](api_avm_initialstates.initialstates.md) that represent the intial state of a created asset |
`name` | string | - | String for the descriptive name of the asset |
`symbol` | string | - | String for the ticker symbol of the asset |
`denomination` | number | - | Optional number for the denomination which is 10^D. D must be >= 0 and <= 32. Ex: $1 AVAX = 10^9 $nAVAX |
`mintOutputs` | Array‹[SECPMintOutput](api_avm_outputs.secpmintoutput.md)› | undefined | Optional. Array of [SECPMintOutput](api_avm_outputs.secpmintoutput.md)s to be included in the transaction. These outputs can be spent to mint more tokens. |
`fee` | BN | undefined | Optional. The amount of fees to burn in its smallest denomination, represented as [BN](https://github.com/indutny/bn.js/) |
`feeAssetID` | Buffer | undefined | Optional. The assetID of the fees being burned. |
`memo` | Buffer | undefined | Optional contains arbitrary bytes, up to 256 bytes |
`asOf` | BN | UnixNow() | Optional. The timestamp to verify the transaction against as a [BN](https://github.com/indutny/bn.js/)  |

**Returns:** *[UnsignedTx](api_avm_transactions.unsignedtx.md)*

An unsigned transaction created from the passed in parameters.

___

###  buildCreateNFTAssetTx

▸ **buildCreateNFTAssetTx**(`networkid`: number, `blockchainid`: Buffer, `fromAddresses`: Array‹Buffer›, `changeAddresses`: Array‹Buffer›, `minterSets`: Array‹[MinterSet](api_avm_minterset.minterset.md)›, `name`: string, `symbol`: string, `fee`: BN, `feeAssetID`: Buffer, `memo`: Buffer, `asOf`: BN, `locktime`: BN): *[UnsignedTx](api_avm_transactions.unsignedtx.md)*

*Defined in [src/apis/avm/utxos.ts:443](https://github.com/ava-labs/avalanche.js/blob/a2feb77/src/apis/avm/utxos.ts#L443)*

Creates an unsigned Create Asset transaction. For more granular control, you may create your own
[[CreateAssetTX]] manually (with their corresponding [TransferableInput](api_avm_inputs.transferableinput.md)s, [TransferableOutput](api_avm_outputs.transferableoutput.md)s).

**Parameters:**

Name | Type | Default | Description |
------ | ------ | ------ | ------ |
`networkid` | number | - | The number representing NetworkID of the node |
`blockchainid` | Buffer | - | The [Buffer](https://github.com/feross/buffer) representing the BlockchainID for the transaction |
`fromAddresses` | Array‹Buffer› | - | The addresses being used to send the funds from the UTXOs [Buffer](https://github.com/feross/buffer) |
`changeAddresses` | Array‹Buffer› | - | Optional. The addresses that can spend the change remaining from the spent UTXOs. |
`minterSets` | Array‹[MinterSet](api_avm_minterset.minterset.md)› | - | The minters and thresholds required to mint this nft asset |
`name` | string | - | String for the descriptive name of the nft asset |
`symbol` | string | - | String for the ticker symbol of the nft asset |
`fee` | BN | undefined | Optional. The amount of fees to burn in its smallest denomination, represented as [BN](https://github.com/indutny/bn.js/) |
`feeAssetID` | Buffer | undefined | Optional. The assetID of the fees being burned. |
`memo` | Buffer | undefined | Optional contains arbitrary bytes, up to 256 bytes |
`asOf` | BN | UnixNow() | Optional. The timestamp to verify the transaction against as a [BN](https://github.com/indutny/bn.js/) |
`locktime` | BN | undefined | Optional. The locktime field created in the resulting mint output  |

**Returns:** *[UnsignedTx](api_avm_transactions.unsignedtx.md)*

An unsigned transaction created from the passed in parameters.

___

###  buildCreateNFTMintTx

▸ **buildCreateNFTMintTx**(`networkid`: number, `blockchainid`: Buffer, `owners`: Array‹[OutputOwners](common_output.outputowners.md)›, `fromAddresses`: Array‹Buffer›, `changeAddresses`: Array‹Buffer›, `utxoids`: Array‹string›, `groupID`: number, `payload`: Buffer, `fee`: BN, `feeAssetID`: Buffer, `memo`: Buffer, `asOf`: BN): *[UnsignedTx](api_avm_transactions.unsignedtx.md)*

*Defined in [src/apis/avm/utxos.ts:507](https://github.com/ava-labs/avalanche.js/blob/a2feb77/src/apis/avm/utxos.ts#L507)*

Creates an unsigned NFT mint transaction. For more granular control, you may create your own
[OperationTx](api_avm_operationtx.operationtx.md) manually (with their corresponding [TransferableInput](api_avm_inputs.transferableinput.md)s, [TransferableOutput](api_avm_outputs.transferableoutput.md)s, and [[TransferOperation]]s).

**Parameters:**

Name | Type | Default | Description |
------ | ------ | ------ | ------ |
`networkid` | number | - | The number representing NetworkID of the node |
`blockchainid` | Buffer | - | The [Buffer](https://github.com/feross/buffer) representing the BlockchainID for the transaction |
`owners` | Array‹[OutputOwners](common_output.outputowners.md)› | - | An array of [OutputOwners](common_output.outputowners.md) who will be given the NFTs. |
`fromAddresses` | Array‹Buffer› | - | The addresses being used to send the funds from the UTXOs |
`changeAddresses` | Array‹Buffer› | - | Optional. The addresses that can spend the change remaining from the spent UTXOs. |
`utxoids` | Array‹string› | - | An array of strings for the NFTs being transferred |
`groupID` | number | 0 | Optional. The group this NFT is issued to. |
`payload` | Buffer | undefined | Optional. Data for NFT Payload. |
`fee` | BN | undefined | Optional. The amount of fees to burn in its smallest denomination, represented as [BN](https://github.com/indutny/bn.js/) |
`feeAssetID` | Buffer | undefined | Optional. The assetID of the fees being burned. |
`memo` | Buffer | undefined | Optional contains arbitrary bytes, up to 256 bytes |
`asOf` | BN | UnixNow() | Optional. The timestamp to verify the transaction against as a [BN](https://github.com/indutny/bn.js/)  |

**Returns:** *[UnsignedTx](api_avm_transactions.unsignedtx.md)*

An unsigned transaction created from the passed in parameters.

___

###  buildExportTx

▸ **buildExportTx**(`networkid`: number, `blockchainid`: Buffer, `amount`: BN, `avaxAssetID`: Buffer, `toAddresses`: Array‹Buffer›, `fromAddresses`: Array‹Buffer›, `changeAddresses`: Array‹Buffer›, `destinationChain`: Buffer, `fee`: BN, `feeAssetID`: Buffer, `memo`: Buffer, `asOf`: BN, `locktime`: BN, `threshold`: number): *[UnsignedTx](api_avm_transactions.unsignedtx.md)*

*Defined in [src/apis/avm/utxos.ts:776](https://github.com/ava-labs/avalanche.js/blob/a2feb77/src/apis/avm/utxos.ts#L776)*

Creates an unsigned ExportTx transaction.

**Parameters:**

Name | Type | Default | Description |
------ | ------ | ------ | ------ |
`networkid` | number | - | The number representing NetworkID of the node |
`blockchainid` | Buffer | - | The [Buffer](https://github.com/feross/buffer) representing the BlockchainID for the transaction |
`amount` | BN | - | The amount being exported as a [BN](https://github.com/indutny/bn.js/) |
`avaxAssetID` | Buffer | - | [Buffer](https://github.com/feross/buffer) of the asset ID for AVAX |
`toAddresses` | Array‹Buffer› | - | An array of addresses as [Buffer](https://github.com/feross/buffer) who recieves the AVAX |
`fromAddresses` | Array‹Buffer› | - | An array of addresses as [Buffer](https://github.com/feross/buffer) who owns the AVAX |
`changeAddresses` | Array‹Buffer› | undefined | Optional. The addresses that can spend the change remaining from the spent UTXOs. |
`destinationChain` | Buffer | undefined | Optional. A [Buffer](https://github.com/feross/buffer) for the chainid where to send the asset. |
`fee` | BN | undefined | Optional. The amount of fees to burn in its smallest denomination, represented as [BN](https://github.com/indutny/bn.js/) |
`feeAssetID` | Buffer | undefined | Optional. The assetID of the fees being burned. |
`memo` | Buffer | undefined | Optional contains arbitrary bytes, up to 256 bytes |
`asOf` | BN | UnixNow() | Optional. The timestamp to verify the transaction against as a [BN](https://github.com/indutny/bn.js/) |
`locktime` | BN | new BN(0) | Optional. The locktime field created in the resulting outputs |
`threshold` | number | 1 | Optional. The number of signatures required to spend the funds in the resultant UTXO |

**Returns:** *[UnsignedTx](api_avm_transactions.unsignedtx.md)*

An unsigned transaction created from the passed in parameters.

___

###  buildImportTx

▸ **buildImportTx**(`networkid`: number, `blockchainid`: Buffer, `toAddresses`: Array‹Buffer›, `fromAddresses`: Array‹Buffer›, `changeAddresses`: Array‹Buffer›, `atomics`: Array‹[UTXO](api_avm_utxos.utxo.md)›, `sourceChain`: Buffer, `fee`: BN, `feeAssetID`: Buffer, `memo`: Buffer, `asOf`: BN, `locktime`: BN, `threshold`: number): *[UnsignedTx](api_avm_transactions.unsignedtx.md)*

*Defined in [src/apis/avm/utxos.ts:663](https://github.com/ava-labs/avalanche.js/blob/a2feb77/src/apis/avm/utxos.ts#L663)*

Creates an unsigned ImportTx transaction.

**Parameters:**

Name | Type | Default | Description |
------ | ------ | ------ | ------ |
`networkid` | number | - | The number representing NetworkID of the node |
`blockchainid` | Buffer | - | The [Buffer](https://github.com/feross/buffer) representing the BlockchainID for the transaction |
`toAddresses` | Array‹Buffer› | - | The addresses to send the funds |
`fromAddresses` | Array‹Buffer› | - | The addresses being used to send the funds from the UTXOs [Buffer](https://github.com/feross/buffer) |
`changeAddresses` | Array‹Buffer› | - | Optional. The addresses that can spend the change remaining from the spent UTXOs. |
`atomics` | Array‹[UTXO](api_avm_utxos.utxo.md)› | - | - |
`sourceChain` | Buffer | undefined | A [Buffer](https://github.com/feross/buffer) for the chainid where the imports are coming from. |
`fee` | BN | undefined | Optional. The amount of fees to burn in its smallest denomination, represented as [BN](https://github.com/indutny/bn.js/). Fee will come from the inputs first, if they can. |
`feeAssetID` | Buffer | undefined | Optional. The assetID of the fees being burned. |
`memo` | Buffer | undefined | Optional contains arbitrary bytes, up to 256 bytes |
`asOf` | BN | UnixNow() | Optional. The timestamp to verify the transaction against as a [BN](https://github.com/indutny/bn.js/) |
`locktime` | BN | new BN(0) | Optional. The locktime field created in the resulting outputs |
`threshold` | number | 1 | Optional. The number of signatures required to spend the funds in the resultant UTXO |

**Returns:** *[UnsignedTx](api_avm_transactions.unsignedtx.md)*

An unsigned transaction created from the passed in parameters.

___

###  buildNFTTransferTx

▸ **buildNFTTransferTx**(`networkid`: number, `blockchainid`: Buffer, `toAddresses`: Array‹Buffer›, `fromAddresses`: Array‹Buffer›, `changeAddresses`: Array‹Buffer›, `utxoids`: Array‹string›, `fee`: BN, `feeAssetID`: Buffer, `memo`: Buffer, `asOf`: BN, `locktime`: BN, `threshold`: number): *[UnsignedTx](api_avm_transactions.unsignedtx.md)*

*Defined in [src/apis/avm/utxos.ts:584](https://github.com/ava-labs/avalanche.js/blob/a2feb77/src/apis/avm/utxos.ts#L584)*

Creates an unsigned NFT transfer transaction. For more granular control, you may create your own
[OperationTx](api_avm_operationtx.operationtx.md) manually (with their corresponding [TransferableInput](api_avm_inputs.transferableinput.md)s, [TransferableOutput](api_avm_outputs.transferableoutput.md)s, and [[TransferOperation]]s).

**Parameters:**

Name | Type | Default | Description |
------ | ------ | ------ | ------ |
`networkid` | number | - | The number representing NetworkID of the node |
`blockchainid` | Buffer | - | The [Buffer](https://github.com/feross/buffer) representing the BlockchainID for the transaction |
`toAddresses` | Array‹Buffer› | - | An array of [Buffer](https://github.com/feross/buffer)s which indicate who recieves the NFT |
`fromAddresses` | Array‹Buffer› | - | An array for [Buffer](https://github.com/feross/buffer) who owns the NFT |
`changeAddresses` | Array‹Buffer› | - | Optional. The addresses that can spend the change remaining from the spent UTXOs. |
`utxoids` | Array‹string› | - | An array of strings for the NFTs being transferred |
`fee` | BN | undefined | Optional. The amount of fees to burn in its smallest denomination, represented as [BN](https://github.com/indutny/bn.js/) |
`feeAssetID` | Buffer | undefined | Optional. The assetID of the fees being burned. |
`memo` | Buffer | undefined | Optional contains arbitrary bytes, up to 256 bytes |
`asOf` | BN | UnixNow() | Optional. The timestamp to verify the transaction against as a [BN](https://github.com/indutny/bn.js/) |
`locktime` | BN | new BN(0) | Optional. The locktime field created in the resulting outputs |
`threshold` | number | 1 | Optional. The number of signatures required to spend the funds in the resultant UTXO  |

**Returns:** *[UnsignedTx](api_avm_transactions.unsignedtx.md)*

An unsigned transaction created from the passed in parameters.

___

###  buildSECPMintTx

▸ **buildSECPMintTx**(`networkid`: number, `blockchainid`: Buffer, `mintOwner`: [SECPMintOutput](api_avm_outputs.secpmintoutput.md), `transferOwners`: Array‹[SECPTransferOutput](api_avm_outputs.secptransferoutput.md)›, `fromAddresses`: Array‹Buffer›, `changeAddresses`: Array‹Buffer›, `mintUTXOID`: string, `fee`: BN, `feeAssetID`: Buffer, `memo`: Buffer, `asOf`: BN): *[UnsignedTx](api_avm_transactions.unsignedtx.md)*

*Defined in [src/apis/avm/utxos.ts:365](https://github.com/ava-labs/avalanche.js/blob/a2feb77/src/apis/avm/utxos.ts#L365)*

Creates an unsigned Secp mint transaction. For more granular control, you may create your own
[OperationTx](api_avm_operationtx.operationtx.md) manually (with their corresponding [TransferableInput](api_avm_inputs.transferableinput.md)s, [TransferableOutput](api_avm_outputs.transferableoutput.md)s, and [[TransferOperation]]s).

**Parameters:**

Name | Type | Default | Description |
------ | ------ | ------ | ------ |
`networkid` | number | - | The number representing NetworkID of the node |
`blockchainid` | Buffer | - | The [Buffer](https://github.com/feross/buffer) representing the BlockchainID for the transaction |
`mintOwner` | [SECPMintOutput](api_avm_outputs.secpmintoutput.md) | - | A [SECPMintOutput](api_avm_outputs.secpmintoutput.md) which specifies the new set of minters |
`transferOwners` | Array‹[SECPTransferOutput](api_avm_outputs.secptransferoutput.md)› | - | An array of [SECPTransferOutput](api_avm_outputs.secptransferoutput.md)s which specifies where the minted tokens will go |
`fromAddresses` | Array‹Buffer› | - | The addresses being used to send the funds from the UTXOs [Buffer](https://github.com/feross/buffer) |
`changeAddresses` | Array‹Buffer› | - | The addresses that can spend the change remaining from the spent UTXOs |
`mintUTXOID` | string | - | The UTXOID for the [[SCPMintOutput]] being spent to produce more tokens |
`fee` | BN | undefined | Optional. The amount of fees to burn in its smallest denomination, represented as [BN](https://github.com/indutny/bn.js/) |
`feeAssetID` | Buffer | undefined | Optional. The assetID of the fees being burned. |
`memo` | Buffer | undefined | Optional contains arbitrary bytes, up to 256 bytes |
`asOf` | BN | UnixNow() | Optional. The timestamp to verify the transaction against as a [BN](https://github.com/indutny/bn.js/)  |

**Returns:** *[UnsignedTx](api_avm_transactions.unsignedtx.md)*

___

###  clone

▸ **clone**(): *this*

*Overrides [StandardUTXOSet](common_utxos.standardutxoset.md).[clone](common_utxos.standardutxoset.md#abstract-clone)*

*Defined in [src/apis/avm/utxos.ts:120](https://github.com/ava-labs/avalanche.js/blob/a2feb77/src/apis/avm/utxos.ts#L120)*

**Returns:** *this*

___

###  create

▸ **create**(...`args`: any[]): *this*

*Overrides [StandardUTXOSet](common_utxos.standardutxoset.md).[create](common_utxos.standardutxoset.md#abstract-create)*

*Defined in [src/apis/avm/utxos.ts:116](https://github.com/ava-labs/avalanche.js/blob/a2feb77/src/apis/avm/utxos.ts#L116)*

**Parameters:**

Name | Type |
------ | ------ |
`...args` | any[] |

**Returns:** *this*

___

###  difference

▸ **difference**(`utxoset`: this): *this*

*Inherited from [StandardUTXOSet](common_utxos.standardutxoset.md).[difference](common_utxos.standardutxoset.md#difference)*

*Defined in [src/common/utxos.ts:482](https://github.com/ava-labs/avalanche.js/blob/a2feb77/src/common/utxos.ts#L482)*

Set difference between this set and a parameter.

**Parameters:**

Name | Type | Description |
------ | ------ | ------ |
`utxoset` | this | The set to difference  |

**Returns:** *this*

A new StandardUTXOSet containing the difference

___

###  filter

▸ **filter**(`args`: any[], `lambda`: function): *this*

*Inherited from [StandardUTXOSet](common_utxos.standardutxoset.md).[filter](common_utxos.standardutxoset.md#filter)*

*Defined in [src/common/utxos.ts:430](https://github.com/ava-labs/avalanche.js/blob/a2feb77/src/common/utxos.ts#L430)*

**Parameters:**

▪ **args**: *any[]*

▪ **lambda**: *function*

▸ (`utxo`: [UTXO](api_avm_utxos.utxo.md), ...`largs`: any[]): *boolean*

**Parameters:**

Name | Type |
------ | ------ |
`utxo` | [UTXO](api_avm_utxos.utxo.md) |
`...largs` | any[] |

**Returns:** *this*

___

###  getAddresses

▸ **getAddresses**(): *Array‹Buffer›*

*Inherited from [StandardUTXOSet](common_utxos.standardutxoset.md).[getAddresses](common_utxos.standardutxoset.md#getaddresses)*

*Defined in [src/common/utxos.ts:369](https://github.com/ava-labs/avalanche.js/blob/a2feb77/src/common/utxos.ts#L369)*

Gets the addresses in the [StandardUTXOSet](common_utxos.standardutxoset.md) and returns an array of [Buffer](https://github.com/feross/buffer).

**Returns:** *Array‹Buffer›*

___

###  getAllUTXOStrings

▸ **getAllUTXOStrings**(`utxoids`: Array‹string›): *Array‹string›*

*Inherited from [StandardUTXOSet](common_utxos.standardutxoset.md).[getAllUTXOStrings](common_utxos.standardutxoset.md#getallutxostrings)*

*Defined in [src/common/utxos.ts:320](https://github.com/ava-labs/avalanche.js/blob/a2feb77/src/common/utxos.ts#L320)*

Gets all the [StandardUTXO](common_utxos.standardutxo.md)s as strings, optionally that match with UTXOIDs in an array.

**Parameters:**

Name | Type | Default | Description |
------ | ------ | ------ | ------ |
`utxoids` | Array‹string› | undefined | An optional array of UTXOIDs, returns all [StandardUTXO](common_utxos.standardutxo.md)s if not provided  |

**Returns:** *Array‹string›*

An array of [StandardUTXO](common_utxos.standardutxo.md)s as cb58 serialized strings.

___

###  getAllUTXOs

▸ **getAllUTXOs**(`utxoids`: Array‹string›): *Array‹[UTXO](api_avm_utxos.utxo.md)›*

*Inherited from [StandardUTXOSet](common_utxos.standardutxoset.md).[getAllUTXOs](common_utxos.standardutxoset.md#getallutxos)*

*Defined in [src/common/utxos.ts:299](https://github.com/ava-labs/avalanche.js/blob/a2feb77/src/common/utxos.ts#L299)*

Gets all the [StandardUTXO](common_utxos.standardutxo.md)s, optionally that match with UTXOIDs in an array

**Parameters:**

Name | Type | Default | Description |
------ | ------ | ------ | ------ |
`utxoids` | Array‹string› | undefined | An optional array of UTXOIDs, returns all [StandardUTXO](common_utxos.standardutxo.md)s if not provided  |

**Returns:** *Array‹[UTXO](api_avm_utxos.utxo.md)›*

An array of [StandardUTXO](common_utxos.standardutxo.md)s.

___

###  getAssetIDs

▸ **getAssetIDs**(`addresses`: Array‹Buffer›): *Array‹Buffer›*

*Inherited from [StandardUTXOSet](common_utxos.standardutxoset.md).[getAssetIDs](common_utxos.standardutxoset.md#getassetids)*

*Defined in [src/common/utxos.ts:408](https://github.com/ava-labs/avalanche.js/blob/a2feb77/src/common/utxos.ts#L408)*

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

*Inherited from [StandardUTXOSet](common_utxos.standardutxoset.md).[getBalance](common_utxos.standardutxoset.md#getbalance)*

*Defined in [src/common/utxos.ts:381](https://github.com/ava-labs/avalanche.js/blob/a2feb77/src/common/utxos.ts#L381)*

Returns the balance of a set of addresses in the StandardUTXOSet.

**Parameters:**

Name | Type | Default | Description |
------ | ------ | ------ | ------ |
`addresses` | Array‹Buffer› | - | An array of addresses |
`assetID` | Buffer &#124; string | - | Either a [Buffer](https://github.com/feross/buffer) or an cb58 serialized representation of an AssetID |
`asOf` | BN | undefined | The timestamp to verify the transaction against as a [BN](https://github.com/indutny/bn.js/)  |

**Returns:** *BN*

Returns the total balance as a [BN](https://github.com/indutny/bn.js/).

___

###  getMinimumSpendable

▸ **getMinimumSpendable**(`aad`: [AssetAmountDestination](api_avm_utxos.assetamountdestination.md), `asOf`: BN, `locktime`: BN, `threshold`: number): *Error*

*Defined in [src/apis/avm/utxos.ts:133](https://github.com/ava-labs/avalanche.js/blob/a2feb77/src/apis/avm/utxos.ts#L133)*

**Parameters:**

Name | Type | Default |
------ | ------ | ------ |
`aad` | [AssetAmountDestination](api_avm_utxos.assetamountdestination.md) | - |
`asOf` | BN | UnixNow() |
`locktime` | BN | new BN(0) |
`threshold` | number | 1 |

**Returns:** *Error*

___

###  getUTXO

▸ **getUTXO**(`utxoid`: string): *[UTXO](api_avm_utxos.utxo.md)*

*Inherited from [StandardUTXOSet](common_utxos.standardutxoset.md).[getUTXO](common_utxos.standardutxoset.md#getutxo)*

*Defined in [src/common/utxos.ts:290](https://github.com/ava-labs/avalanche.js/blob/a2feb77/src/common/utxos.ts#L290)*

Gets a [StandardUTXO](common_utxos.standardutxo.md) from the [StandardUTXOSet](common_utxos.standardutxoset.md) by its UTXOID.

**Parameters:**

Name | Type | Description |
------ | ------ | ------ |
`utxoid` | string | String representing the UTXOID  |

**Returns:** *[UTXO](api_avm_utxos.utxo.md)*

A [StandardUTXO](common_utxos.standardutxo.md) if it exists in the set.

___

###  getUTXOIDs

▸ **getUTXOIDs**(`addresses`: Array‹Buffer›, `spendable`: boolean): *Array‹string›*

*Inherited from [StandardUTXOSet](common_utxos.standardutxoset.md).[getUTXOIDs](common_utxos.standardutxoset.md#getutxoids)*

*Defined in [src/common/utxos.ts:345](https://github.com/ava-labs/avalanche.js/blob/a2feb77/src/common/utxos.ts#L345)*

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

▸ **includes**(`utxo`: [UTXO](api_avm_utxos.utxo.md) | string): *boolean*

*Inherited from [StandardUTXOSet](common_utxos.standardutxoset.md).[includes](common_utxos.standardutxoset.md#includes)*

*Defined in [src/common/utxos.ts:156](https://github.com/ava-labs/avalanche.js/blob/a2feb77/src/common/utxos.ts#L156)*

Returns true if the [StandardUTXO](common_utxos.standardutxo.md) is in the StandardUTXOSet.

**Parameters:**

Name | Type | Description |
------ | ------ | ------ |
`utxo` | [UTXO](api_avm_utxos.utxo.md) &#124; string | Either a [StandardUTXO](common_utxos.standardutxo.md) a cb58 serialized string representing a StandardUTXO  |

**Returns:** *boolean*

___

###  intersection

▸ **intersection**(`utxoset`: this): *this*

*Inherited from [StandardUTXOSet](common_utxos.standardutxoset.md).[intersection](common_utxos.standardutxoset.md#intersection)*

*Defined in [src/common/utxos.ts:468](https://github.com/ava-labs/avalanche.js/blob/a2feb77/src/common/utxos.ts#L468)*

Set intersetion between this set and a parameter.

**Parameters:**

Name | Type | Description |
------ | ------ | ------ |
`utxoset` | this | The set to intersect  |

**Returns:** *this*

A new StandardUTXOSet containing the intersection

___

###  merge

▸ **merge**(`utxoset`: this, `hasUTXOIDs`: Array‹string›): *this*

*Inherited from [StandardUTXOSet](common_utxos.standardutxoset.md).[merge](common_utxos.standardutxoset.md#merge)*

*Defined in [src/common/utxos.ts:449](https://github.com/ava-labs/avalanche.js/blob/a2feb77/src/common/utxos.ts#L449)*

Returns a new set with copy of UTXOs in this and set parameter.

**Parameters:**

Name | Type | Default | Description |
------ | ------ | ------ | ------ |
`utxoset` | this | - | The [StandardUTXOSet](common_utxos.standardutxoset.md) to merge with this one |
`hasUTXOIDs` | Array‹string› | undefined | Will subselect a set of [StandardUTXO](common_utxos.standardutxo.md)s which have the UTXOIDs provided in this array, defults to all UTXOs  |

**Returns:** *this*

A new StandardUTXOSet that contains all the filtered elements.

___

###  mergeByRule

▸ **mergeByRule**(`utxoset`: this, `mergeRule`: [MergeRule](../modules/utils_constants.md#mergerule)): *this*

*Inherited from [StandardUTXOSet](common_utxos.standardutxoset.md).[mergeByRule](common_utxos.standardutxoset.md#mergebyrule)*

*Defined in [src/common/utxos.ts:531](https://github.com/ava-labs/avalanche.js/blob/a2feb77/src/common/utxos.ts#L531)*

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
`utxoset` | this | The set to merge by the MergeRule |
`mergeRule` | [MergeRule](../modules/utils_constants.md#mergerule) | The [MergeRule](../modules/utils_constants.md#mergerule) to apply  |

**Returns:** *this*

A new StandardUTXOSet containing the merged data

___

###  parseUTXO

▸ **parseUTXO**(`utxo`: [UTXO](api_avm_utxos.utxo.md) | string): *[UTXO](api_avm_utxos.utxo.md)*

*Overrides [StandardUTXOSet](common_utxos.standardutxoset.md).[parseUTXO](common_utxos.standardutxoset.md#abstract-parseutxo)*

*Defined in [src/apis/avm/utxos.ts:102](https://github.com/ava-labs/avalanche.js/blob/a2feb77/src/apis/avm/utxos.ts#L102)*

**Parameters:**

Name | Type |
------ | ------ |
`utxo` | [UTXO](api_avm_utxos.utxo.md) &#124; string |

**Returns:** *[UTXO](api_avm_utxos.utxo.md)*

___

###  remove

▸ **remove**(`utxo`: [UTXO](api_avm_utxos.utxo.md) | string): *[UTXO](api_avm_utxos.utxo.md)*

*Inherited from [StandardUTXOSet](common_utxos.standardutxoset.md).[remove](common_utxos.standardutxoset.md#remove)*

*Defined in [src/common/utxos.ts:237](https://github.com/ava-labs/avalanche.js/blob/a2feb77/src/common/utxos.ts#L237)*

Removes a [StandardUTXO](common_utxos.standardutxo.md) from the [StandardUTXOSet](common_utxos.standardutxoset.md) if it exists.

**Parameters:**

Name | Type | Description |
------ | ------ | ------ |
`utxo` | [UTXO](api_avm_utxos.utxo.md) &#124; string | Either a [StandardUTXO](common_utxos.standardutxo.md) an cb58 serialized string representing a StandardUTXO  |

**Returns:** *[UTXO](api_avm_utxos.utxo.md)*

A [StandardUTXO](common_utxos.standardutxo.md) if it was removed and undefined if nothing was removed.

___

###  removeArray

▸ **removeArray**(`utxos`: Array‹string | [UTXO](api_avm_utxos.utxo.md)›): *Array‹[UTXO](api_avm_utxos.utxo.md)›*

*Inherited from [StandardUTXOSet](common_utxos.standardutxoset.md).[removeArray](common_utxos.standardutxoset.md#removearray)*

*Defined in [src/common/utxos.ts:272](https://github.com/ava-labs/avalanche.js/blob/a2feb77/src/common/utxos.ts#L272)*

Removes an array of [StandardUTXO](common_utxos.standardutxo.md)s to the [StandardUTXOSet](common_utxos.standardutxoset.md).

**Parameters:**

Name | Type |
------ | ------ |
`utxos` | Array‹string &#124; [UTXO](api_avm_utxos.utxo.md)› |

**Returns:** *Array‹[UTXO](api_avm_utxos.utxo.md)›*

An array of UTXOs which were removed.

___

###  symDifference

▸ **symDifference**(`utxoset`: this): *this*

*Inherited from [StandardUTXOSet](common_utxos.standardutxoset.md).[symDifference](common_utxos.standardutxoset.md#symdifference)*

*Defined in [src/common/utxos.ts:496](https://github.com/ava-labs/avalanche.js/blob/a2feb77/src/common/utxos.ts#L496)*

Set symmetrical difference between this set and a parameter.

**Parameters:**

Name | Type | Description |
------ | ------ | ------ |
`utxoset` | this | The set to symmetrical difference  |

**Returns:** *this*

A new StandardUTXOSet containing the symmetrical difference

___

###  union

▸ **union**(`utxoset`: this): *this*

*Inherited from [StandardUTXOSet](common_utxos.standardutxoset.md).[union](common_utxos.standardutxoset.md#union)*

*Defined in [src/common/utxos.ts:511](https://github.com/ava-labs/avalanche.js/blob/a2feb77/src/common/utxos.ts#L511)*

Set union between this set and a parameter.

**Parameters:**

Name | Type | Description |
------ | ------ | ------ |
`utxoset` | this | The set to union  |

**Returns:** *this*

A new StandardUTXOSet containing the union
