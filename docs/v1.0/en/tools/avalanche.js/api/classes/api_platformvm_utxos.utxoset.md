[avalanche](../README.md) › [API-PlatformVM-UTXOs](../modules/api_platformvm_utxos.md) › [UTXOSet](api_platformvm_utxos.utxoset.md)

# Class: UTXOSet

Class representing a set of [UTXO](api_platformvm_utxos.utxo.md)s.

## Hierarchy

* [StandardUTXOSet](common_utxos.standardutxoset.md)‹[UTXO](api_platformvm_utxos.utxo.md)›

  ↳ **UTXOSet**

## Index

### Properties

* [addressUTXOs](api_platformvm_utxos.utxoset.md#protected-addressutxos)
* [utxos](api_platformvm_utxos.utxoset.md#protected-utxos)

### Methods

* [_feeCheck](api_platformvm_utxos.utxoset.md#_feecheck)
* [add](api_platformvm_utxos.utxoset.md#add)
* [addArray](api_platformvm_utxos.utxoset.md#addarray)
* [buildAddDelegatorTx](api_platformvm_utxos.utxoset.md#buildadddelegatortx)
* [buildAddValidatorTx](api_platformvm_utxos.utxoset.md#buildaddvalidatortx)
* [buildBaseTx](api_platformvm_utxos.utxoset.md#buildbasetx)
* [buildCreateSubnetTx](api_platformvm_utxos.utxoset.md#buildcreatesubnettx)
* [buildExportTx](api_platformvm_utxos.utxoset.md#buildexporttx)
* [buildImportTx](api_platformvm_utxos.utxoset.md#buildimporttx)
* [clone](api_platformvm_utxos.utxoset.md#clone)
* [create](api_platformvm_utxos.utxoset.md#create)
* [difference](api_platformvm_utxos.utxoset.md#difference)
* [filter](api_platformvm_utxos.utxoset.md#filter)
* [getAddresses](api_platformvm_utxos.utxoset.md#getaddresses)
* [getAllUTXOStrings](api_platformvm_utxos.utxoset.md#getallutxostrings)
* [getAllUTXOs](api_platformvm_utxos.utxoset.md#getallutxos)
* [getAssetIDs](api_platformvm_utxos.utxoset.md#getassetids)
* [getBalance](api_platformvm_utxos.utxoset.md#getbalance)
* [getMinimumSpendable](api_platformvm_utxos.utxoset.md#getminimumspendable)
* [getUTXO](api_platformvm_utxos.utxoset.md#getutxo)
* [getUTXOIDs](api_platformvm_utxos.utxoset.md#getutxoids)
* [includes](api_platformvm_utxos.utxoset.md#includes)
* [intersection](api_platformvm_utxos.utxoset.md#intersection)
* [merge](api_platformvm_utxos.utxoset.md#merge)
* [mergeByRule](api_platformvm_utxos.utxoset.md#mergebyrule)
* [parseUTXO](api_platformvm_utxos.utxoset.md#parseutxo)
* [remove](api_platformvm_utxos.utxoset.md#remove)
* [removeArray](api_platformvm_utxos.utxoset.md#removearray)
* [symDifference](api_platformvm_utxos.utxoset.md#symdifference)
* [union](api_platformvm_utxos.utxoset.md#union)

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

* \[ **utxoid**: *string*\]: [UTXO](api_platformvm_utxos.utxo.md)

## Methods

###  _feeCheck

▸ **_feeCheck**(`fee`: BN, `feeAssetID`: Buffer): *boolean*

*Defined in [src/apis/platformvm/utxos.ts:124](https://github.com/ava-labs/avalanche.js/blob/a2feb77/src/apis/platformvm/utxos.ts#L124)*

**Parameters:**

Name | Type |
------ | ------ |
`fee` | BN |
`feeAssetID` | Buffer |

**Returns:** *boolean*

___

###  add

▸ **add**(`utxo`: [UTXO](api_platformvm_utxos.utxo.md) | string, `overwrite`: boolean): *[UTXO](api_platformvm_utxos.utxo.md)*

*Inherited from [StandardUTXOSet](common_utxos.standardutxoset.md).[add](common_utxos.standardutxoset.md#add)*

*Defined in [src/common/utxos.ts:181](https://github.com/ava-labs/avalanche.js/blob/a2feb77/src/common/utxos.ts#L181)*

Adds a [StandardUTXO](common_utxos.standardutxo.md) to the StandardUTXOSet.

**Parameters:**

Name | Type | Default | Description |
------ | ------ | ------ | ------ |
`utxo` | [UTXO](api_platformvm_utxos.utxo.md) &#124; string | - | Either a [StandardUTXO](common_utxos.standardutxo.md) an cb58 serialized string representing a StandardUTXO |
`overwrite` | boolean | false | If true, if the UTXOID already exists, overwrite it... default false  |

**Returns:** *[UTXO](api_platformvm_utxos.utxo.md)*

A [StandardUTXO](common_utxos.standardutxo.md) if one was added and undefined if nothing was added.

___

###  addArray

▸ **addArray**(`utxos`: Array‹string | [UTXO](api_platformvm_utxos.utxo.md)›, `overwrite`: boolean): *Array‹[StandardUTXO](common_utxos.standardutxo.md)›*

*Inherited from [StandardUTXOSet](common_utxos.standardutxoset.md).[addArray](common_utxos.standardutxoset.md#addarray)*

*Defined in [src/common/utxos.ts:219](https://github.com/ava-labs/avalanche.js/blob/a2feb77/src/common/utxos.ts#L219)*

Adds an array of [StandardUTXO](common_utxos.standardutxo.md)s to the [StandardUTXOSet](common_utxos.standardutxoset.md).

**Parameters:**

Name | Type | Default | Description |
------ | ------ | ------ | ------ |
`utxos` | Array‹string &#124; [UTXO](api_platformvm_utxos.utxo.md)› | - | - |
`overwrite` | boolean | false | If true, if the UTXOID already exists, overwrite it... default false  |

**Returns:** *Array‹[StandardUTXO](common_utxos.standardutxo.md)›*

An array of StandardUTXOs which were added.

___

###  buildAddDelegatorTx

▸ **buildAddDelegatorTx**(`networkid`: number, `blockchainid`: Buffer, `avaxAssetID`: Buffer, `fromAddresses`: Array‹Buffer›, `changeAddresses`: Array‹Buffer›, `nodeID`: Buffer, `startTime`: BN, `endTime`: BN, `stakeAmount`: BN, `rewardLocktime`: BN, `rewardThreshold`: number, `rewardAddresses`: Array‹Buffer›, `fee`: BN, `feeAssetID`: Buffer, `memo`: Buffer, `asOf`: BN): *[UnsignedTx](api_platformvm_transactions.unsignedtx.md)*

*Defined in [src/apis/platformvm/utxos.ts:566](https://github.com/ava-labs/avalanche.js/blob/a2feb77/src/apis/platformvm/utxos.ts#L566)*

Class representing an unsigned [AddDelegatorTx](api_platformvm_validationtx.adddelegatortx.md) transaction.

**Parameters:**

Name | Type | Default | Description |
------ | ------ | ------ | ------ |
`networkid` | number | DefaultNetworkID | Networkid, [DefaultNetworkID](../modules/utils_constants.md#const-defaultnetworkid) |
`blockchainid` | Buffer | - | Blockchainid, default undefined |
`avaxAssetID` | Buffer | - | [Buffer](https://github.com/feross/buffer) of the asset ID for AVAX |
`fromAddresses` | Array‹Buffer› | - | An array of addresses as [Buffer](https://github.com/feross/buffer) who pays the fees and the stake in AVAX |
`changeAddresses` | Array‹Buffer› | - | An array of addresses as [Buffer](https://github.com/feross/buffer) who gets the change leftover from the staking payment |
`nodeID` | Buffer | - | The node ID of the validator being added. |
`startTime` | BN | - | The Unix time when the validator starts validating the Primary Network. |
`endTime` | BN | - | The Unix time when the validator stops validating the Primary Network (and staked AVAX is returned). |
`stakeAmount` | BN | - | A [BN](https://github.com/indutny/bn.js/) for the amount of stake to be delegated in nAVAX. |
`rewardLocktime` | BN | - | The locktime field created in the resulting reward outputs |
`rewardThreshold` | number | - | The number of signatures required to spend the funds in the resultant reward UTXO |
`rewardAddresses` | Array‹Buffer› | - | The addresses the validator reward goes. |
`fee` | BN | undefined | Optional. The amount of fees to burn in its smallest denomination, represented as [BN](https://github.com/indutny/bn.js/) |
`feeAssetID` | Buffer | undefined | Optional. The assetID of the fees being burned. |
`memo` | Buffer | undefined | Optional contains arbitrary bytes, up to 256 bytes |
`asOf` | BN | UnixNow() | Optional. The timestamp to verify the transaction against as a [BN](https://github.com/indutny/bn.js/)  |

**Returns:** *[UnsignedTx](api_platformvm_transactions.unsignedtx.md)*

An unsigned transaction created from the passed in parameters.

___

###  buildAddValidatorTx

▸ **buildAddValidatorTx**(`networkid`: number, `blockchainid`: Buffer, `avaxAssetID`: Buffer, `fromAddresses`: Array‹Buffer›, `changeAddresses`: Array‹Buffer›, `nodeID`: Buffer, `startTime`: BN, `endTime`: BN, `stakeAmount`: BN, `rewardLocktime`: BN, `rewardThreshold`: number, `rewardAddresses`: Array‹Buffer›, `delegationFee`: number, `fee`: BN, `feeAssetID`: Buffer, `memo`: Buffer, `asOf`: BN): *[UnsignedTx](api_platformvm_transactions.unsignedtx.md)*

*Defined in [src/apis/platformvm/utxos.ts:643](https://github.com/ava-labs/avalanche.js/blob/a2feb77/src/apis/platformvm/utxos.ts#L643)*

Class representing an unsigned [AddValidatorTx](api_platformvm_validationtx.addvalidatortx.md) transaction.

**Parameters:**

Name | Type | Default | Description |
------ | ------ | ------ | ------ |
`networkid` | number | DefaultNetworkID | Networkid, [DefaultNetworkID](../modules/utils_constants.md#const-defaultnetworkid) |
`blockchainid` | Buffer | - | Blockchainid, default undefined |
`avaxAssetID` | Buffer | - | [Buffer](https://github.com/feross/buffer) of the asset ID for AVAX |
`fromAddresses` | Array‹Buffer› | - | An array of addresses as [Buffer](https://github.com/feross/buffer) who pays the fees and the stake in AVAX |
`changeAddresses` | Array‹Buffer› | - | An array of addresses as [Buffer](https://github.com/feross/buffer) who gets the change leftover from the staking payment |
`nodeID` | Buffer | - | The node ID of the validator being added. |
`startTime` | BN | - | The Unix time when the validator starts validating the Primary Network. |
`endTime` | BN | - | The Unix time when the validator stops validating the Primary Network (and staked AVAX is returned). |
`stakeAmount` | BN | - | A [BN](https://github.com/indutny/bn.js/) for the amount of stake to be delegated in nAVAX. |
`rewardLocktime` | BN | - | The locktime field created in the resulting reward outputs |
`rewardThreshold` | number | - | The number of signatures required to spend the funds in the resultant reward UTXO |
`rewardAddresses` | Array‹Buffer› | - | The addresses the validator reward goes. |
`delegationFee` | number | - | A number for the percentage of reward to be given to the validator when someone delegates to them. Must be between 0 and 100. |
`fee` | BN | undefined | Optional. The amount of fees to burn in its smallest denomination, represented as [BN](https://github.com/indutny/bn.js/) |
`feeAssetID` | Buffer | undefined | Optional. The assetID of the fees being burned. |
`memo` | Buffer | undefined | Optional contains arbitrary bytes, up to 256 bytes |
`asOf` | BN | UnixNow() | Optional. The timestamp to verify the transaction against as a [BN](https://github.com/indutny/bn.js/)  |

**Returns:** *[UnsignedTx](api_platformvm_transactions.unsignedtx.md)*

An unsigned transaction created from the passed in parameters.

___

###  buildBaseTx

▸ **buildBaseTx**(`networkid`: number, `blockchainid`: Buffer, `amount`: BN, `assetID`: Buffer, `toAddresses`: Array‹Buffer›, `fromAddresses`: Array‹Buffer›, `changeAddresses`: Array‹Buffer›, `fee`: BN, `feeAssetID`: Buffer, `memo`: Buffer, `asOf`: BN, `locktime`: BN, `threshold`: number): *[UnsignedTx](api_platformvm_transactions.unsignedtx.md)*

*Defined in [src/apis/platformvm/utxos.ts:220](https://github.com/ava-labs/avalanche.js/blob/a2feb77/src/apis/platformvm/utxos.ts#L220)*

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

**Returns:** *[UnsignedTx](api_platformvm_transactions.unsignedtx.md)*

An unsigned transaction created from the passed in parameters.

___

###  buildCreateSubnetTx

▸ **buildCreateSubnetTx**(`networkid`: number, `blockchainid`: Buffer, `fromAddresses`: Array‹Buffer›, `changeAddresses`: Array‹Buffer›, `subnetOwnerAddresses`: Array‹Buffer›, `subnetOwnerThreshold`: number, `fee`: BN, `feeAssetID`: Buffer, `memo`: Buffer, `asOf`: BN): *[UnsignedTx](api_platformvm_transactions.unsignedtx.md)*

*Defined in [src/apis/platformvm/utxos.ts:718](https://github.com/ava-labs/avalanche.js/blob/a2feb77/src/apis/platformvm/utxos.ts#L718)*

Class representing an unsigned [CreateSubnetTx](api_platformvm_createsubnettx.createsubnettx.md) transaction.

**Parameters:**

Name | Type | Default | Description |
------ | ------ | ------ | ------ |
`networkid` | number | DefaultNetworkID | Networkid, [DefaultNetworkID](../modules/utils_constants.md#const-defaultnetworkid) |
`blockchainid` | Buffer | - | Blockchainid, default undefined |
`fromAddresses` | Array‹Buffer› | - | The addresses being used to send the funds from the UTXOs [Buffer](https://github.com/feross/buffer) |
`changeAddresses` | Array‹Buffer› | - | The addresses that can spend the change remaining from the spent UTXOs. |
`subnetOwnerAddresses` | Array‹Buffer› | - | An array of [Buffer](https://github.com/feross/buffer) for the addresses to add to a subnet |
`subnetOwnerThreshold` | number | - | The number of owners's signatures required to add a validator to the network |
`fee` | BN | undefined | Optional. The amount of fees to burn in its smallest denomination, represented as [BN](https://github.com/indutny/bn.js/) |
`feeAssetID` | Buffer | undefined | Optional. The assetID of the fees being burned |
`memo` | Buffer | undefined | Optional contains arbitrary bytes, up to 256 bytes |
`asOf` | BN | UnixNow() | Optional. The timestamp to verify the transaction against as a [BN](https://github.com/indutny/bn.js/)  |

**Returns:** *[UnsignedTx](api_platformvm_transactions.unsignedtx.md)*

An unsigned transaction created from the passed in parameters.

___

###  buildExportTx

▸ **buildExportTx**(`networkid`: number, `blockchainid`: Buffer, `amount`: BN, `avaxAssetID`: Buffer, `toAddresses`: Array‹Buffer›, `fromAddresses`: Array‹Buffer›, `changeAddresses`: Array‹Buffer›, `destinationChain`: Buffer, `fee`: BN, `feeAssetID`: Buffer, `memo`: Buffer, `asOf`: BN, `locktime`: BN, `threshold`: number): *[UnsignedTx](api_platformvm_transactions.unsignedtx.md)*

*Defined in [src/apis/platformvm/utxos.ts:414](https://github.com/ava-labs/avalanche.js/blob/a2feb77/src/apis/platformvm/utxos.ts#L414)*

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
`changeAddresses` | Array‹Buffer› | undefined | An array of addresses as [Buffer](https://github.com/feross/buffer) who gets the change leftover of the AVAX |
`destinationChain` | Buffer | undefined | Optional. A [Buffer](https://github.com/feross/buffer) for the chainid where to send the asset. |
`fee` | BN | undefined | Optional. The amount of fees to burn in its smallest denomination, represented as [BN](https://github.com/indutny/bn.js/) |
`feeAssetID` | Buffer | undefined | Optional. The assetID of the fees being burned. |
`memo` | Buffer | undefined | Optional contains arbitrary bytes, up to 256 bytes |
`asOf` | BN | UnixNow() | Optional. The timestamp to verify the transaction against as a [BN](https://github.com/indutny/bn.js/) |
`locktime` | BN | new BN(0) | Optional. The locktime field created in the resulting outputs |
`threshold` | number | 1 | Optional. The number of signatures required to spend the funds in the resultant UTXO  |

**Returns:** *[UnsignedTx](api_platformvm_transactions.unsignedtx.md)*

An unsigned transaction created from the passed in parameters.

___

###  buildImportTx

▸ **buildImportTx**(`networkid`: number, `blockchainid`: Buffer, `toAddresses`: Array‹Buffer›, `fromAddresses`: Array‹Buffer›, `changeAddresses`: Array‹Buffer›, `atomics`: Array‹[UTXO](api_platformvm_utxos.utxo.md)›, `sourceChain`: Buffer, `fee`: BN, `feeAssetID`: Buffer, `memo`: Buffer, `asOf`: BN, `locktime`: BN, `threshold`: number): *[UnsignedTx](api_platformvm_transactions.unsignedtx.md)*

*Defined in [src/apis/platformvm/utxos.ts:301](https://github.com/ava-labs/avalanche.js/blob/a2feb77/src/apis/platformvm/utxos.ts#L301)*

Creates an unsigned ImportTx transaction.

**Parameters:**

Name | Type | Default | Description |
------ | ------ | ------ | ------ |
`networkid` | number | - | The number representing NetworkID of the node |
`blockchainid` | Buffer | - | The [Buffer](https://github.com/feross/buffer) representing the BlockchainID for the transaction |
`toAddresses` | Array‹Buffer› | - | The addresses to send the funds |
`fromAddresses` | Array‹Buffer› | - | The addresses being used to send the funds from the UTXOs [Buffer](https://github.com/feross/buffer) |
`changeAddresses` | Array‹Buffer› | - | Optional. The addresses that can spend the change remaining from the spent UTXOs. Default: toAddresses |
`atomics` | Array‹[UTXO](api_platformvm_utxos.utxo.md)› | - | - |
`sourceChain` | Buffer | undefined | A [Buffer](https://github.com/feross/buffer) for the chainid where the imports are coming from. |
`fee` | BN | undefined | Optional. The amount of fees to burn in its smallest denomination, represented as [BN](https://github.com/indutny/bn.js/). Fee will come from the inputs first, if they can. |
`feeAssetID` | Buffer | undefined | Optional. The assetID of the fees being burned. |
`memo` | Buffer | undefined | Optional contains arbitrary bytes, up to 256 bytes |
`asOf` | BN | UnixNow() | Optional. The timestamp to verify the transaction against as a [BN](https://github.com/indutny/bn.js/) |
`locktime` | BN | new BN(0) | Optional. The locktime field created in the resulting outputs |
`threshold` | number | 1 | Optional. The number of signatures required to spend the funds in the resultant UTXO |

**Returns:** *[UnsignedTx](api_platformvm_transactions.unsignedtx.md)*

An unsigned transaction created from the passed in parameters.

___

###  clone

▸ **clone**(): *this*

*Overrides [StandardUTXOSet](common_utxos.standardutxoset.md).[clone](common_utxos.standardutxoset.md#abstract-clone)*

*Defined in [src/apis/platformvm/utxos.ts:117](https://github.com/ava-labs/avalanche.js/blob/a2feb77/src/apis/platformvm/utxos.ts#L117)*

**Returns:** *this*

___

###  create

▸ **create**(...`args`: any[]): *this*

*Overrides [StandardUTXOSet](common_utxos.standardutxoset.md).[create](common_utxos.standardutxoset.md#abstract-create)*

*Defined in [src/apis/platformvm/utxos.ts:113](https://github.com/ava-labs/avalanche.js/blob/a2feb77/src/apis/platformvm/utxos.ts#L113)*

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

▸ (`utxo`: [UTXO](api_platformvm_utxos.utxo.md), ...`largs`: any[]): *boolean*

**Parameters:**

Name | Type |
------ | ------ |
`utxo` | [UTXO](api_platformvm_utxos.utxo.md) |
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

▸ **getAllUTXOs**(`utxoids`: Array‹string›): *Array‹[UTXO](api_platformvm_utxos.utxo.md)›*

*Inherited from [StandardUTXOSet](common_utxos.standardutxoset.md).[getAllUTXOs](common_utxos.standardutxoset.md#getallutxos)*

*Defined in [src/common/utxos.ts:299](https://github.com/ava-labs/avalanche.js/blob/a2feb77/src/common/utxos.ts#L299)*

Gets all the [StandardUTXO](common_utxos.standardutxo.md)s, optionally that match with UTXOIDs in an array

**Parameters:**

Name | Type | Default | Description |
------ | ------ | ------ | ------ |
`utxoids` | Array‹string› | undefined | An optional array of UTXOIDs, returns all [StandardUTXO](common_utxos.standardutxo.md)s if not provided  |

**Returns:** *Array‹[UTXO](api_platformvm_utxos.utxo.md)›*

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

▸ **getMinimumSpendable**(`aad`: [AssetAmountDestination](api_platformvm_utxos.assetamountdestination.md), `asOf`: BN, `locktime`: BN, `threshold`: number): *Error*

*Defined in [src/apis/platformvm/utxos.ts:130](https://github.com/ava-labs/avalanche.js/blob/a2feb77/src/apis/platformvm/utxos.ts#L130)*

**Parameters:**

Name | Type | Default |
------ | ------ | ------ |
`aad` | [AssetAmountDestination](api_platformvm_utxos.assetamountdestination.md) | - |
`asOf` | BN | UnixNow() |
`locktime` | BN | new BN(0) |
`threshold` | number | 1 |

**Returns:** *Error*

___

###  getUTXO

▸ **getUTXO**(`utxoid`: string): *[UTXO](api_platformvm_utxos.utxo.md)*

*Inherited from [StandardUTXOSet](common_utxos.standardutxoset.md).[getUTXO](common_utxos.standardutxoset.md#getutxo)*

*Defined in [src/common/utxos.ts:290](https://github.com/ava-labs/avalanche.js/blob/a2feb77/src/common/utxos.ts#L290)*

Gets a [StandardUTXO](common_utxos.standardutxo.md) from the [StandardUTXOSet](common_utxos.standardutxoset.md) by its UTXOID.

**Parameters:**

Name | Type | Description |
------ | ------ | ------ |
`utxoid` | string | String representing the UTXOID  |

**Returns:** *[UTXO](api_platformvm_utxos.utxo.md)*

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

▸ **includes**(`utxo`: [UTXO](api_platformvm_utxos.utxo.md) | string): *boolean*

*Inherited from [StandardUTXOSet](common_utxos.standardutxoset.md).[includes](common_utxos.standardutxoset.md#includes)*

*Defined in [src/common/utxos.ts:156](https://github.com/ava-labs/avalanche.js/blob/a2feb77/src/common/utxos.ts#L156)*

Returns true if the [StandardUTXO](common_utxos.standardutxo.md) is in the StandardUTXOSet.

**Parameters:**

Name | Type | Description |
------ | ------ | ------ |
`utxo` | [UTXO](api_platformvm_utxos.utxo.md) &#124; string | Either a [StandardUTXO](common_utxos.standardutxo.md) a cb58 serialized string representing a StandardUTXO  |

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

▸ **parseUTXO**(`utxo`: [UTXO](api_platformvm_utxos.utxo.md) | string): *[UTXO](api_platformvm_utxos.utxo.md)*

*Overrides [StandardUTXOSet](common_utxos.standardutxoset.md).[parseUTXO](common_utxos.standardutxoset.md#abstract-parseutxo)*

*Defined in [src/apis/platformvm/utxos.ts:99](https://github.com/ava-labs/avalanche.js/blob/a2feb77/src/apis/platformvm/utxos.ts#L99)*

**Parameters:**

Name | Type |
------ | ------ |
`utxo` | [UTXO](api_platformvm_utxos.utxo.md) &#124; string |

**Returns:** *[UTXO](api_platformvm_utxos.utxo.md)*

___

###  remove

▸ **remove**(`utxo`: [UTXO](api_platformvm_utxos.utxo.md) | string): *[UTXO](api_platformvm_utxos.utxo.md)*

*Inherited from [StandardUTXOSet](common_utxos.standardutxoset.md).[remove](common_utxos.standardutxoset.md#remove)*

*Defined in [src/common/utxos.ts:237](https://github.com/ava-labs/avalanche.js/blob/a2feb77/src/common/utxos.ts#L237)*

Removes a [StandardUTXO](common_utxos.standardutxo.md) from the [StandardUTXOSet](common_utxos.standardutxoset.md) if it exists.

**Parameters:**

Name | Type | Description |
------ | ------ | ------ |
`utxo` | [UTXO](api_platformvm_utxos.utxo.md) &#124; string | Either a [StandardUTXO](common_utxos.standardutxo.md) an cb58 serialized string representing a StandardUTXO  |

**Returns:** *[UTXO](api_platformvm_utxos.utxo.md)*

A [StandardUTXO](common_utxos.standardutxo.md) if it was removed and undefined if nothing was removed.

___

###  removeArray

▸ **removeArray**(`utxos`: Array‹string | [UTXO](api_platformvm_utxos.utxo.md)›): *Array‹[UTXO](api_platformvm_utxos.utxo.md)›*

*Inherited from [StandardUTXOSet](common_utxos.standardutxoset.md).[removeArray](common_utxos.standardutxoset.md#removearray)*

*Defined in [src/common/utxos.ts:272](https://github.com/ava-labs/avalanche.js/blob/a2feb77/src/common/utxos.ts#L272)*

Removes an array of [StandardUTXO](common_utxos.standardutxo.md)s to the [StandardUTXOSet](common_utxos.standardutxoset.md).

**Parameters:**

Name | Type |
------ | ------ |
`utxos` | Array‹string &#124; [UTXO](api_platformvm_utxos.utxo.md)› |

**Returns:** *Array‹[UTXO](api_platformvm_utxos.utxo.md)›*

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
