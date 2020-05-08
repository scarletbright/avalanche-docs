[slopes - v1.4.3](../README.md) › [Globals](../globals.md) › ["apis/avm/api"](../modules/_apis_avm_api_.md) › [AVMAPI](_apis_avm_api_.avmapi.md)

# Class: AVMAPI

Class for interacting with a node endpoint that is using the AVM.

**`remarks`** This extends the [JRPCAPI](_utils_types_.jrpcapi.md) class. This class should not be directly called. Instead, use the [Slopes.addAPI](_index_.slopes.md#addapi) function to register this interface with Slopes.

## Hierarchy

  ↳ [JRPCAPI](_utils_types_.jrpcapi.md)

  ↳ **AVMAPI**

## Index

### Constructors

* [constructor](_apis_avm_api_.avmapi.md#constructor)

### Properties

* [AVAAssetID](_apis_avm_api_.avmapi.md#protected-avaassetid)
* [baseurl](_apis_avm_api_.avmapi.md#protected-baseurl)
* [blockchainID](_apis_avm_api_.avmapi.md#protected-blockchainid)
* [core](_apis_avm_api_.avmapi.md#protected-core)
* [db](_apis_avm_api_.avmapi.md#protected-db)
* [jrpcVersion](_apis_avm_api_.avmapi.md#protected-jrpcversion)
* [rpcid](_apis_avm_api_.avmapi.md#protected-rpcid)

### Methods

* [addressFromBuffer](_apis_avm_api_.avmapi.md#addressfrombuffer)
* [callMethod](_apis_avm_api_.avmapi.md#callmethod)
* [createAddress](_apis_avm_api_.avmapi.md#createaddress)
* [createFixedCapAsset](_apis_avm_api_.avmapi.md#createfixedcapasset)
* [createMintTx](_apis_avm_api_.avmapi.md#createminttx)
* [createVariableCapAsset](_apis_avm_api_.avmapi.md#createvariablecapasset)
* [exportKey](_apis_avm_api_.avmapi.md#exportkey)
* [getAVAAssetID](_apis_avm_api_.avmapi.md#getavaassetid)
* [getAllBalances](_apis_avm_api_.avmapi.md#getallbalances)
* [getAssetDescription](_apis_avm_api_.avmapi.md#getassetdescription)
* [getBalance](_apis_avm_api_.avmapi.md#getbalance)
* [getBaseURL](_apis_avm_api_.avmapi.md#getbaseurl)
* [getBlockchainAlias](_apis_avm_api_.avmapi.md#getblockchainalias)
* [getBlockchainID](_apis_avm_api_.avmapi.md#getblockchainid)
* [getDB](_apis_avm_api_.avmapi.md#getdb)
* [getRPCID](_apis_avm_api_.avmapi.md#getrpcid)
* [getTxStatus](_apis_avm_api_.avmapi.md#gettxstatus)
* [getUTXOs](_apis_avm_api_.avmapi.md#getutxos)
* [importKey](_apis_avm_api_.avmapi.md#importkey)
* [issueTx](_apis_avm_api_.avmapi.md#issuetx)
* [keyChain](_apis_avm_api_.avmapi.md#keychain)
* [listAddresses](_apis_avm_api_.avmapi.md#listaddresses)
* [makeCreateAssetTx](_apis_avm_api_.avmapi.md#makecreateassettx)
* [makeUnsignedTx](_apis_avm_api_.avmapi.md#makeunsignedtx)
* [parseAddress](_apis_avm_api_.avmapi.md#parseaddress)
* [send](_apis_avm_api_.avmapi.md#send)
* [setBaseURL](_apis_avm_api_.avmapi.md#setbaseurl)
* [signMintTx](_apis_avm_api_.avmapi.md#signminttx)
* [signTx](_apis_avm_api_.avmapi.md#signtx)

## Constructors

###  constructor

\+ **new AVMAPI**(`core`: [SlopesCore](_slopes_.slopescore.md), `baseurl`: string, `blockchainID`: string): *[AVMAPI](_apis_avm_api_.avmapi.md)*

*Overrides [JRPCAPI](_utils_types_.jrpcapi.md).[constructor](_utils_types_.jrpcapi.md#constructor)*

*Defined in [apis/avm/api.ts:696](https://github.com/ava-labs/slopes/blob/709e172/src/apis/avm/api.ts#L696)*

This class should not be instantiated directly. Instead use the [Slopes.addAPI](_index_.slopes.md#addapi) method.

**Parameters:**

Name | Type | Default | Description |
------ | ------ | ------ | ------ |
`core` | [SlopesCore](_slopes_.slopescore.md) | - | A reference to the Slopes class |
`baseurl` | string | "/ext/bc/avm" | Defaults to the string "/ext/bc/avm" as the path to blockchain's baseurl  |
`blockchainID` | string | "" | - |

**Returns:** *[AVMAPI](_apis_avm_api_.avmapi.md)*

## Properties

### `Protected` AVAAssetID

• **AVAAssetID**: *Buffer* =  undefined

*Defined in [apis/avm/api.ts:86](https://github.com/ava-labs/slopes/blob/709e172/src/apis/avm/api.ts#L86)*

___

### `Protected` baseurl

• **baseurl**: *string*

*Inherited from [APIBase](_utils_types_.apibase.md).[baseurl](_utils_types_.apibase.md#protected-baseurl)*

*Defined in [utils/types.ts:33](https://github.com/ava-labs/slopes/blob/709e172/src/utils/types.ts#L33)*

___

### `Protected` blockchainID

• **blockchainID**: *string* = ""

*Defined in [apis/avm/api.ts:85](https://github.com/ava-labs/slopes/blob/709e172/src/apis/avm/api.ts#L85)*

___

### `Protected` core

• **core**: *[SlopesCore](_slopes_.slopescore.md)*

*Inherited from [APIBase](_utils_types_.apibase.md).[core](_utils_types_.apibase.md#protected-core)*

*Defined in [utils/types.ts:32](https://github.com/ava-labs/slopes/blob/709e172/src/utils/types.ts#L32)*

___

### `Protected` db

• **db**: *StoreAPI*

*Inherited from [APIBase](_utils_types_.apibase.md).[db](_utils_types_.apibase.md#protected-db)*

*Defined in [utils/types.ts:34](https://github.com/ava-labs/slopes/blob/709e172/src/utils/types.ts#L34)*

___

### `Protected` jrpcVersion

• **jrpcVersion**: *string* = "2.0"

*Inherited from [JRPCAPI](_utils_types_.jrpcapi.md).[jrpcVersion](_utils_types_.jrpcapi.md#protected-jrpcversion)*

*Defined in [utils/types.ts:80](https://github.com/ava-labs/slopes/blob/709e172/src/utils/types.ts#L80)*

___

### `Protected` rpcid

• **rpcid**: *number* = 1

*Inherited from [JRPCAPI](_utils_types_.jrpcapi.md).[rpcid](_utils_types_.jrpcapi.md#protected-rpcid)*

*Defined in [utils/types.ts:81](https://github.com/ava-labs/slopes/blob/709e172/src/utils/types.ts#L81)*

## Methods

###  addressFromBuffer

▸ **addressFromBuffer**(`address`: Buffer): *string*

*Defined in [apis/avm/api.ts:122](https://github.com/ava-labs/slopes/blob/709e172/src/apis/avm/api.ts#L122)*

**Parameters:**

Name | Type |
------ | ------ |
`address` | Buffer |

**Returns:** *string*

___

###  callMethod

▸ **callMethod**(`method`: string, `params?`: Array‹object› | object, `baseurl?`: string): *Promise‹[RequestResponseData](_utils_types_.requestresponsedata.md)›*

*Inherited from [JRPCAPI](_utils_types_.jrpcapi.md)*

*Defined in [utils/types.ts:82](https://github.com/ava-labs/slopes/blob/709e172/src/utils/types.ts#L82)*

**Parameters:**

Name | Type |
------ | ------ |
`method` | string |
`params?` | Array‹object› &#124; object |
`baseurl?` | string |

**Returns:** *Promise‹[RequestResponseData](_utils_types_.requestresponsedata.md)›*

___

###  createAddress

▸ **createAddress**(`username`: string, `password`: string): *Promise‹string›*

*Defined in [apis/avm/api.ts:194](https://github.com/ava-labs/slopes/blob/709e172/src/apis/avm/api.ts#L194)*

Creates an address (and associated private keys) on a user on a blockchain.

**Parameters:**

Name | Type | Description |
------ | ------ | ------ |
`username` | string | Name of the user to create the address under |
`password` | string | Password to unlock the user and encrypt the private key  |

**Returns:** *Promise‹string›*

Promise for a string representing the address created by the vm.

___

###  createFixedCapAsset

▸ **createFixedCapAsset**(`username`: string, `password`: string, `name`: string, `symbol`: string, `initialHolders`: Array‹object›): *Promise‹string›*

*Defined in [apis/avm/api.ts:229](https://github.com/ava-labs/slopes/blob/709e172/src/apis/avm/api.ts#L229)*

Create a new fixed-cap, fungible asset. A quantity of it is created at initialization and there no more is ever created.

**Parameters:**

Name | Type | Description |
------ | ------ | ------ |
`username` | string | The user paying the transaction fee (in $AVA) for asset creation |
`password` | string | The password for the user paying the transaction fee (in $AVA) for asset creation |
`name` | string | The human-readable name for the asset |
`symbol` | string | Optional. The shorthand symbol for the asset. Between 0 and 4 characters |
`initialHolders` | Array‹object› | An array of objects containing the field "address" and "amount" to establish the genesis values for the new asset  ```js Example initialHolders: [     {         "address": "X-7sik3Pr6r1FeLrvK1oWwECBS8iJ5VPuSh",         "amount": 10000     },     {         "address": "X-7sik3Pr6r1FeLrvK1oWwECBS8iJ5VPuSh",         "amount": 50000     } ] ```  |

**Returns:** *Promise‹string›*

Returns a Promise<string> containing the base 58 string representation of the ID of the newly created asset.

___

###  createMintTx

▸ **createMintTx**(`amount`: number | BN, `assetID`: Buffer | string, `to`: string, `minters`: Array‹string›): *Promise‹string›*

*Defined in [apis/avm/api.ts:296](https://github.com/ava-labs/slopes/blob/709e172/src/apis/avm/api.ts#L296)*

Create an unsigned transaction to mint more of an asset.

**Parameters:**

Name | Type | Description |
------ | ------ | ------ |
`amount` | number &#124; BN | The units of the asset to mint |
`assetID` | Buffer &#124; string | The ID of the asset to mint |
`to` | string | The address to assign the units of the minted asset |
`minters` | Array‹string› | Addresses of the minters responsible for signing the transaction  |

**Returns:** *Promise‹string›*

Returns a Promise<string> containing the base 58 string representation of the unsigned transaction.

___

###  createVariableCapAsset

▸ **createVariableCapAsset**(`username`: string, `password`: string, `name`: string, `symbol`: string, `minterSets`: Array‹object›): *Promise‹string›*

*Defined in [apis/avm/api.ts:273](https://github.com/ava-labs/slopes/blob/709e172/src/apis/avm/api.ts#L273)*

Create a new variable-cap, fungible asset. No units of the asset exist at initialization. Minters can mint units of this asset using createMintTx, signMintTx and sendMintTx.

**Parameters:**

Name | Type | Description |
------ | ------ | ------ |
`username` | string | The user paying the transaction fee (in $AVA) for asset creation |
`password` | string | The password for the user paying the transaction fee (in $AVA) for asset creation |
`name` | string | The human-readable name for the asset |
`symbol` | string | Optional. The shorthand symbol for the asset -- between 0 and 4 characters |
`minterSets` | Array‹object› | is a list where each element specifies that threshold of the addresses in minters may together mint more of the asset by signing a minting transaction  ```js Example minterSets: [      {          "minters":[              "X-4peJsFvhdn7XjhNF4HWAQy6YaJts27s9q"          ],          "threshold": 1      },      {          "minters": [              "X-dcJ6z9duLfyQTgbjq2wBCowkvcPZHVDF",              "X-2fE6iibqfERz5wenXE6qyvinsxDvFhHZk",              "X-7ieAJbfrGQbpNZRAQEpZCC1Gs1z5gz4HU"          ],          "threshold": 2      } ] ```  |

**Returns:** *Promise‹string›*

Returns a Promise<string> containing the base 58 string representation of the ID of the newly created asset.

___

###  exportKey

▸ **exportKey**(`username`: string, `password`: string, `address`: string): *Promise‹string›*

*Defined in [apis/avm/api.ts:355](https://github.com/ava-labs/slopes/blob/709e172/src/apis/avm/api.ts#L355)*

Exports the private key for an address.

**Parameters:**

Name | Type | Description |
------ | ------ | ------ |
`username` | string | The name of the user with the private key |
`password` | string | The password used to decrypt the private key |
`address` | string | The address whose private key should be exported  |

**Returns:** *Promise‹string›*

Promise with the decrypted private key as store in the database

___

###  getAVAAssetID

▸ **getAVAAssetID**(): *Promise‹Buffer›*

*Defined in [apis/avm/api.ts:132](https://github.com/ava-labs/slopes/blob/709e172/src/apis/avm/api.ts#L132)*

Fetches the AVA AssetID and returns it in a Promise.

**Returns:** *Promise‹Buffer›*

The the provided string representing the blockchainID

___

###  getAllBalances

▸ **getAllBalances**(`address`: string): *Promise‹object›*

*Defined in [apis/avm/api.ts:415](https://github.com/ava-labs/slopes/blob/709e172/src/apis/avm/api.ts#L415)*

Retrieves all assets for an address on a server and their associated balances.

**Parameters:**

Name | Type | Description |
------ | ------ | ------ |
`address` | string | The address to get a list of assets  |

**Returns:** *Promise‹object›*

Promise of an object mapping assetID strings with [BN](https://github.com/indutny/bn.js/) balance for the address on the blockchain.

___

###  getAssetDescription

▸ **getAssetDescription**(`assetID`: Buffer | string): *Promise‹object›*

*Defined in [apis/avm/api.ts:440](https://github.com/ava-labs/slopes/blob/709e172/src/apis/avm/api.ts#L440)*

Retrieves an assets name and symbol.

**Parameters:**

Name | Type | Description |
------ | ------ | ------ |
`assetID` | Buffer &#124; string | Either a [Buffer](https://github.com/feross/buffer) or an AVA serialized string for the AssetID or its alias.  |

**Returns:** *Promise‹object›*

Returns a Promise<object> with keys "name" and "symbol".

___

###  getBalance

▸ **getBalance**(`address`: string, `assetID`: string): *Promise‹BN›*

*Defined in [apis/avm/api.ts:171](https://github.com/ava-labs/slopes/blob/709e172/src/apis/avm/api.ts#L171)*

Gets the balance of a particular asset on a blockchain.

**Parameters:**

Name | Type | Description |
------ | ------ | ------ |
`address` | string | The address to pull the asset balance from |
`assetID` | string | The assetID to pull the balance from  |

**Returns:** *Promise‹BN›*

Promise with the balance of the assetID as a [BN](https://github.com/indutny/bn.js/) on the provided address for the blockchain.

___

###  getBaseURL

▸ **getBaseURL**(): *string*

*Inherited from [APIBase](_utils_types_.apibase.md)*

*Defined in [utils/types.ts:57](https://github.com/ava-labs/slopes/blob/709e172/src/utils/types.ts#L57)*

Returns the baseurl's path.

**Returns:** *string*

___

###  getBlockchainAlias

▸ **getBlockchainAlias**(): *string*

*Defined in [apis/avm/api.ts:93](https://github.com/ava-labs/slopes/blob/709e172/src/apis/avm/api.ts#L93)*

Gets the alias for the blockchainID if it exists, otherwise returns `undefined`.

**Returns:** *string*

The alias for the blockchainID

___

###  getBlockchainID

▸ **getBlockchainID**(): *string*

*Defined in [apis/avm/api.ts:107](https://github.com/ava-labs/slopes/blob/709e172/src/apis/avm/api.ts#L107)*

Gets the blockchainID and returns it.

**Returns:** *string*

The blockchainID

___

###  getDB

▸ **getDB**(): *StoreAPI*

*Inherited from [APIBase](_utils_types_.apibase.md)*

*Defined in [utils/types.ts:64](https://github.com/ava-labs/slopes/blob/709e172/src/utils/types.ts#L64)*

Returns the baseurl's database.

**Returns:** *StoreAPI*

___

###  getRPCID

▸ **getRPCID**(): *number*

*Inherited from [JRPCAPI](_utils_types_.jrpcapi.md)*

*Defined in [utils/types.ts:124](https://github.com/ava-labs/slopes/blob/709e172/src/utils/types.ts#L124)*

Returns the rpcid, a strictly-increasing number, starting from 1, indicating the next request ID that will be sent.

**Returns:** *number*

___

###  getTxStatus

▸ **getTxStatus**(`txid`: string): *Promise‹string›*

*Defined in [apis/avm/api.ts:467](https://github.com/ava-labs/slopes/blob/709e172/src/apis/avm/api.ts#L467)*

Returns the status of a provided transaction ID by calling the node's `getTxStatus` method.

**Parameters:**

Name | Type | Description |
------ | ------ | ------ |
`txid` | string | The string representation of the transaction ID  |

**Returns:** *Promise‹string›*

Returns a Promise<string> containing the status retrieved from the node

___

###  getUTXOs

▸ **getUTXOs**(`addresses`: Array‹string› | Array‹Buffer›, `persistOpts`: [PersistanceOptions](_apis_avm_api_.persistanceoptions.md)): *Promise‹[UTXOSet](_apis_avm_utxos_.utxoset.md)›*

*Defined in [apis/avm/api.ts:486](https://github.com/ava-labs/slopes/blob/709e172/src/apis/avm/api.ts#L486)*

Retrieves the UTXOs related to the addresses provided from the node's `getUTXOs` method.

**Parameters:**

Name | Type | Default | Description |
------ | ------ | ------ | ------ |
`addresses` | Array‹string› &#124; Array‹Buffer› | - | An array of addresses as strings or addresses as [Buffer](https://github.com/feross/buffer)s |
`persistOpts` | [PersistanceOptions](_apis_avm_api_.persistanceoptions.md) |  undefined | Options available to persist these UTXOs in local storage  |

**Returns:** *Promise‹[UTXOSet](_apis_avm_utxos_.utxoset.md)›*

___

###  importKey

▸ **importKey**(`username`: string, `password`: string, `privateKey`: string): *Promise‹string›*

*Defined in [apis/avm/api.ts:379](https://github.com/ava-labs/slopes/blob/709e172/src/apis/avm/api.ts#L379)*

Imports a private key into the node's keystore under an user and for a blockchain.

**Parameters:**

Name | Type | Description |
------ | ------ | ------ |
`username` | string | The name of the user to store the private key |
`password` | string | The password that unlocks the user |
`privateKey` | string | A string representing the private key in the vm's format  |

**Returns:** *Promise‹string›*

The address for the imported private key.

___

###  issueTx

▸ **issueTx**(`tx`: string | Buffer | [Tx](_apis_avm_tx_.tx.md)): *Promise‹string›*

*Defined in [apis/avm/api.ts:609](https://github.com/ava-labs/slopes/blob/709e172/src/apis/avm/api.ts#L609)*

Calls the node's issueTx method from the API and returns the resulting transaction ID as a string.

**Parameters:**

Name | Type | Description |
------ | ------ | ------ |
`tx` | string &#124; Buffer &#124; [Tx](_apis_avm_tx_.tx.md) | A string, [Buffer](https://github.com/feross/buffer), or [Tx](_apis_avm_tx_.tx.md) representing a transaction  |

**Returns:** *Promise‹string›*

A Promise<string> representing the transaction ID of the posted transaction.

___

###  keyChain

▸ **keyChain**(): *[AVMKeyChain](_apis_avm_keychain_.avmkeychain.md)*

*Defined in [apis/avm/api.ts:145](https://github.com/ava-labs/slopes/blob/709e172/src/apis/avm/api.ts#L145)*

Gets a reference to the keychain for this class.

**Returns:** *[AVMKeyChain](_apis_avm_keychain_.avmkeychain.md)*

The instance of [AVMKeyChain](_apis_avm_keychain_.avmkeychain.md) for this class

___

###  listAddresses

▸ **listAddresses**(`username`: string, `password`: string): *Promise‹Array‹string››*

*Defined in [apis/avm/api.ts:398](https://github.com/ava-labs/slopes/blob/709e172/src/apis/avm/api.ts#L398)*

Lists all the addresses under a user.

**Parameters:**

Name | Type | Description |
------ | ------ | ------ |
`username` | string | The user to list addresses |
`password` | string | The password of the user to list the addresses  |

**Returns:** *Promise‹Array‹string››*

Promise of an array of address strings in the format specified by the blockchain.

___

###  makeCreateAssetTx

▸ **makeCreateAssetTx**(`utxoset`: [UTXOSet](_apis_avm_utxos_.utxoset.md), `fee`: BN, `creatorAddresses`: Array‹string› | Array‹Buffer›, `initialState`: [InitialStates](_apis_avm_types_.initialstates.md), `name`: string, `symbol`: string, `denomination`: number): *Promise‹[TxCreateAsset](_apis_avm_tx_.txcreateasset.md)›*

*Defined in [apis/avm/api.ts:568](https://github.com/ava-labs/slopes/blob/709e172/src/apis/avm/api.ts#L568)*

Creates an unsigned transaction. For more granular control, you may create your own
[TxCreateAsset](_apis_avm_tx_.txcreateasset.md) manually (with their corresponding [Input](_apis_avm_inputs_.input.md)s, [Output](_apis_avm_outputs_.output.md)s).

**Parameters:**

Name | Type | Description |
------ | ------ | ------ |
`utxoset` | [UTXOSet](_apis_avm_utxos_.utxoset.md) | A set of UTXOs that the transaction is built on |
`fee` | BN | The amount of AVA to be paid for fees, in $nAVA |
`creatorAddresses` | Array‹string› &#124; Array‹Buffer› | The addresses to send the fees |
`initialState` | [InitialStates](_apis_avm_types_.initialstates.md) | The [InitialStates](_apis_avm_types_.initialstates.md) that represent the intial state of a created asset |
`name` | string | String for the descriptive name of the asset |
`symbol` | string | String for the ticker symbol of the asset |
`denomination` | number | Optional number for the denomination which is 10^D. D must be >= 0 and <= 32. Ex: $1 AVA = 10^9 $nAVA  |

**Returns:** *Promise‹[TxCreateAsset](_apis_avm_tx_.txcreateasset.md)›*

An unsigned transaction created from the passed in parameters.

___

###  makeUnsignedTx

▸ **makeUnsignedTx**(`utxoset`: [UTXOSet](_apis_avm_utxos_.utxoset.md), `amount`: BN, `toAddresses`: Array‹string›, `fromAddresses`: Array‹string›, `changeAddresses`: Array‹string›, `assetID`: Buffer | string, `asOf`: BN, `locktime`: BN, `threshold`: number): *Promise‹[TxUnsigned](_apis_avm_tx_.txunsigned.md)›*

*Defined in [apis/avm/api.ts:532](https://github.com/ava-labs/slopes/blob/709e172/src/apis/avm/api.ts#L532)*

Helper function which creates an unsigned transaction. For more granular control, you may create your own
[TxUnsigned](_apis_avm_tx_.txunsigned.md) manually (with their corresponding [Input](_apis_avm_inputs_.input.md)s and [Output](_apis_avm_outputs_.output.md)s.

**Parameters:**

Name | Type | Default | Description |
------ | ------ | ------ | ------ |
`utxoset` | [UTXOSet](_apis_avm_utxos_.utxoset.md) | - | A set of UTXOs that the transaction is built on |
`amount` | BN | - | The amount of AVA to be spent in $nAVA |
`toAddresses` | Array‹string› | - | The addresses to send the funds |
`fromAddresses` | Array‹string› | - | The addresses being used to send the funds from the UTXOs provided |
`changeAddresses` | Array‹string› | - | The addresses that can spend the change remaining from the spent UTXOs |
`assetID` | Buffer &#124; string |  undefined | The assetID of the value being sent |
`asOf` | BN |  UnixNow() | The timestamp to verify the transaction against as a [BN](https://github.com/indutny/bn.js/) |
`locktime` | BN |  new BN(0) | The locktime field created in the resulting outputs |
`threshold` | number | 1 | The number of signatures required to spend the funds in the resultant UTXO  |

**Returns:** *Promise‹[TxUnsigned](_apis_avm_tx_.txunsigned.md)›*

An unsigned transaction created from the passed in parameters.

___

###  parseAddress

▸ **parseAddress**(`addr`: string): *Buffer*

*Defined in [apis/avm/api.ts:116](https://github.com/ava-labs/slopes/blob/709e172/src/apis/avm/api.ts#L116)*

Takes an address string and returns its [Buffer](https://github.com/feross/buffer) representation if valid.

**Parameters:**

Name | Type |
------ | ------ |
`addr` | string |

**Returns:** *Buffer*

A [Buffer](https://github.com/feross/buffer) for the address if valid, undefined if not valid.

___

###  send

▸ **send**(`username`: string, `password`: string, `assetID`: string | Buffer, `amount`: number | BN, `to`: string, `from`: Array‹string› | Array‹Buffer›): *Promise‹string›*

*Defined in [apis/avm/api.ts:641](https://github.com/ava-labs/slopes/blob/709e172/src/apis/avm/api.ts#L641)*

Sends an amount of assetID to the specified address from a list of owned of addresses.

**Parameters:**

Name | Type | Description |
------ | ------ | ------ |
`username` | string | The user that owns the private keys associated with the `from` addresses |
`password` | string | The password unlocking the user |
`assetID` | string &#124; Buffer | The assetID of the asset to send |
`amount` | number &#124; BN | The amount of the asset to be sent |
`to` | string | The address of the recipient |
`from` | Array‹string› &#124; Array‹Buffer› | An array of addresses managed by the node's keystore for this blockchain which will fund this transaction  |

**Returns:** *Promise‹string›*

Promise for the string representing the transaction's ID.

___

###  setBaseURL

▸ **setBaseURL**(`baseurl`: string): *void*

*Inherited from [APIBase](_utils_types_.apibase.md)*

*Defined in [utils/types.ts:41](https://github.com/ava-labs/slopes/blob/709e172/src/utils/types.ts#L41)*

Sets the path of the APIs baseurl.

**Parameters:**

Name | Type | Description |
------ | ------ | ------ |
`baseurl` | string | Path of the APIs baseurl - ex: "/ext/bc/avm"  |

**Returns:** *void*

___

###  signMintTx

▸ **signMintTx**(`username`: string, `password`: string, `tx`: string | Buffer, `minter`: string): *Promise‹string›*

*Defined in [apis/avm/api.ts:330](https://github.com/ava-labs/slopes/blob/709e172/src/apis/avm/api.ts#L330)*

Sign an unsigned or partially signed mint transaction.

**Parameters:**

Name | Type | Description |
------ | ------ | ------ |
`username` | string | The user signing |
`password` | string | The password for the user signing |
`tx` | string &#124; Buffer | The output of createMintTx or signMintTx |
`minter` | string | The minter signing this transaction  |

**Returns:** *Promise‹string›*

Returns a Promise<string> containing the base 58 string representation of the unsigned transaction.

___

###  signTx

▸ **signTx**(`utx`: [TxUnsigned](_apis_avm_tx_.txunsigned.md)): *[Tx](_apis_avm_tx_.tx.md)*

*Defined in [apis/avm/api.ts:598](https://github.com/ava-labs/slopes/blob/709e172/src/apis/avm/api.ts#L598)*

Helper function which takes an unsigned transaction and signs it, returning the resulting [Tx](_apis_avm_tx_.tx.md).

**Parameters:**

Name | Type | Description |
------ | ------ | ------ |
`utx` | [TxUnsigned](_apis_avm_tx_.txunsigned.md) | The unsigned transaction of type [TxUnsigned](_apis_avm_tx_.txunsigned.md)  |

**Returns:** *[Tx](_apis_avm_tx_.tx.md)*

A signed transaction of type [Tx](_apis_avm_tx_.tx.md)
