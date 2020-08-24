[avalanche](../README.md) › [API-AVM](../modules/api_avm.md) › [AVMAPI](api_avm.avmapi.md)

# Class: AVMAPI

Class for interacting with a node endpoint that is using the AVM.

**`remarks`** This extends the [JRPCAPI](common_jrpcapi.jrpcapi.md) class. This class should not be directly called. Instead, use the [Avalanche.addAPI](avalanche.avalanche-1.md#addapi) function to register this interface with Avalanche.

## Hierarchy

  ↳ [JRPCAPI](common_jrpcapi.jrpcapi.md)

  ↳ **AVMAPI**

## Index

### Constructors

* [constructor](api_avm.avmapi.md#constructor)

### Properties

* [AVAXAssetID](api_avm.avmapi.md#protected-avaxassetid)
* [baseurl](api_avm.avmapi.md#protected-baseurl)
* [blockchainID](api_avm.avmapi.md#protected-blockchainid)
* [core](api_avm.avmapi.md#protected-core)
* [db](api_avm.avmapi.md#protected-db)
* [fee](api_avm.avmapi.md#protected-fee)
* [jrpcVersion](api_avm.avmapi.md#protected-jrpcversion)
* [rpcid](api_avm.avmapi.md#protected-rpcid)

### Methods

* [addressFromBuffer](api_avm.avmapi.md#addressfrombuffer)
* [buildBaseTx](api_avm.avmapi.md#buildbasetx)
* [buildCreateAssetTx](api_avm.avmapi.md#buildcreateassettx)
* [buildCreateNFTAssetTx](api_avm.avmapi.md#buildcreatenftassettx)
* [buildCreateNFTMintTx](api_avm.avmapi.md#buildcreatenftminttx)
* [buildExportTx](api_avm.avmapi.md#buildexporttx)
* [buildGenesis](api_avm.avmapi.md#buildgenesis)
* [buildImportTx](api_avm.avmapi.md#buildimporttx)
* [buildNFTTransferTx](api_avm.avmapi.md#buildnfttransfertx)
* [callMethod](api_avm.avmapi.md#callmethod)
* [checkGooseEgg](api_avm.avmapi.md#checkgooseegg)
* [createAddress](api_avm.avmapi.md#createaddress)
* [createFixedCapAsset](api_avm.avmapi.md#createfixedcapasset)
* [createVariableCapAsset](api_avm.avmapi.md#createvariablecapasset)
* [exportAVAX](api_avm.avmapi.md#exportavax)
* [exportKey](api_avm.avmapi.md#exportkey)
* [getAVAXAssetID](api_avm.avmapi.md#getavaxassetid)
* [getAllBalances](api_avm.avmapi.md#getallbalances)
* [getAssetDescription](api_avm.avmapi.md#getassetdescription)
* [getBalance](api_avm.avmapi.md#getbalance)
* [getBaseURL](api_avm.avmapi.md#getbaseurl)
* [getBlockchainAlias](api_avm.avmapi.md#getblockchainalias)
* [getBlockchainID](api_avm.avmapi.md#getblockchainid)
* [getDB](api_avm.avmapi.md#getdb)
* [getDefaultFee](api_avm.avmapi.md#getdefaultfee)
* [getFee](api_avm.avmapi.md#getfee)
* [getRPCID](api_avm.avmapi.md#getrpcid)
* [getTx](api_avm.avmapi.md#gettx)
* [getTxStatus](api_avm.avmapi.md#gettxstatus)
* [getUTXOs](api_avm.avmapi.md#getutxos)
* [importAVAX](api_avm.avmapi.md#importavax)
* [importKey](api_avm.avmapi.md#importkey)
* [issueTx](api_avm.avmapi.md#issuetx)
* [keyChain](api_avm.avmapi.md#keychain)
* [listAddresses](api_avm.avmapi.md#listaddresses)
* [mint](api_avm.avmapi.md#mint)
* [parseAddress](api_avm.avmapi.md#parseaddress)
* [refreshBlockchainID](api_avm.avmapi.md#refreshblockchainid)
* [send](api_avm.avmapi.md#send)
* [setBaseURL](api_avm.avmapi.md#setbaseurl)
* [setFee](api_avm.avmapi.md#setfee)
* [signTx](api_avm.avmapi.md#signtx)

## Constructors

###  constructor

\+ **new AVMAPI**(`core`: [AvalancheCore](avalanchecore.avalanchecore-1.md), `baseurl`: string, `blockchainID`: string): *[AVMAPI](api_avm.avmapi.md)*

*Overrides [JRPCAPI](common_jrpcapi.jrpcapi.md).[constructor](common_jrpcapi.jrpcapi.md#constructor)*

Defined in src/apis/avm/api.ts:1171

This class should not be instantiated directly. Instead use the [Avalanche.addAPI](avalanche.avalanche-1.md#addapi) method.

**Parameters:**

Name | Type | Default | Description |
------ | ------ | ------ | ------ |
`core` | [AvalancheCore](avalanchecore.avalanchecore-1.md) | - | A reference to the Avalanche class |
`baseurl` | string | "/ext/bc/X" | Defaults to the string "/ext/bc/X" as the path to blockchain's baseurl  |
`blockchainID` | string | "" | - |

**Returns:** *[AVMAPI](api_avm.avmapi.md)*

## Properties

### `Protected` AVAXAssetID

• **AVAXAssetID**: *Buffer* = undefined

Defined in src/apis/avm/api.ts:45

___

### `Protected` baseurl

• **baseurl**: *string*

*Inherited from [APIBase](common_apibase.apibase.md).[baseurl](common_apibase.apibase.md#protected-baseurl)*

Defined in src/common/apibase.ts:38

___

### `Protected` blockchainID

• **blockchainID**: *string* = ""

Defined in src/apis/avm/api.ts:43

___

### `Protected` core

• **core**: *[AvalancheCore](avalanchecore.avalanchecore-1.md)*

*Inherited from [APIBase](common_apibase.apibase.md).[core](common_apibase.apibase.md#protected-core)*

Defined in src/common/apibase.ts:36

___

### `Protected` db

• **db**: *StoreAPI*

*Inherited from [APIBase](common_apibase.apibase.md).[db](common_apibase.apibase.md#protected-db)*

Defined in src/common/apibase.ts:40

___

### `Protected` fee

• **fee**: *BN* = undefined

Defined in src/apis/avm/api.ts:47

___

### `Protected` jrpcVersion

• **jrpcVersion**: *string* = "2.0"

*Inherited from [JRPCAPI](common_jrpcapi.jrpcapi.md).[jrpcVersion](common_jrpcapi.jrpcapi.md#protected-jrpcversion)*

Defined in src/common/jrpcapi.ts:17

___

### `Protected` rpcid

• **rpcid**: *number* = 1

*Inherited from [JRPCAPI](common_jrpcapi.jrpcapi.md).[rpcid](common_jrpcapi.jrpcapi.md#protected-rpcid)*

Defined in src/common/jrpcapi.ts:19

## Methods

###  addressFromBuffer

▸ **addressFromBuffer**(`address`: Buffer): *string*

Defined in src/apis/avm/api.ts:100

**Parameters:**

Name | Type |
------ | ------ |
`address` | Buffer |

**Returns:** *string*

___

###  buildBaseTx

▸ **buildBaseTx**(`utxoset`: [UTXOSet](api_avm_utxos.utxoset.md), `amount`: BN, `assetID`: Buffer | string, `toAddresses`: Array‹string›, `fromAddresses`: Array‹string›, `changeAddresses`: Array‹string›, `memo`: [PayloadBase](common_payload.payloadbase.md) | Buffer, `asOf`: BN, `locktime`: BN, `threshold`: number): *Promise‹[UnsignedTx](api_avm_transactions.unsignedtx.md)›*

Defined in src/apis/avm/api.ts:588

Helper function which creates an unsigned transaction. For more granular control, you may create your own
[UnsignedTx](api_avm_transactions.unsignedtx.md) manually (with their corresponding [TransferableInput](api_avm_inputs.transferableinput.md)s, [TransferableOutput](api_avm_outputs.transferableoutput.md)s, and [[TransferOperation]]s).

**`remarks`** 
This helper exists because the endpoint API should be the primary point of entry for most functionality.

**Parameters:**

Name | Type | Default | Description |
------ | ------ | ------ | ------ |
`utxoset` | [UTXOSet](api_avm_utxos.utxoset.md) | - | A set of UTXOs that the transaction is built on |
`amount` | BN | - | The amount of AssetID to be spent in its smallest denomination, represented as [BN](https://github.com/indutny/bn.js/). |
`assetID` | Buffer &#124; string | undefined | The assetID of the value being sent |
`toAddresses` | Array‹string› | - | The addresses to send the funds |
`fromAddresses` | Array‹string› | - | The addresses being used to send the funds from the UTXOs provided |
`changeAddresses` | Array‹string› | - | The addresses that can spend the change remaining from the spent UTXOs |
`memo` | [PayloadBase](common_payload.payloadbase.md) &#124; Buffer | undefined | Optional contains arbitrary bytes, up to 256 bytes |
`asOf` | BN | UnixNow() | Optional. The timestamp to verify the transaction against as a [BN](https://github.com/indutny/bn.js/) |
`locktime` | BN | new BN(0) | Optional. The locktime field created in the resulting outputs |
`threshold` | number | 1 | Optional. The number of signatures required to spend the funds in the resultant UTXO  |

**Returns:** *Promise‹[UnsignedTx](api_avm_transactions.unsignedtx.md)›*

An unsigned transaction ([UnsignedTx](api_avm_transactions.unsignedtx.md)) which contains a [BaseTx](api_avm_basetx.basetx.md).

___

###  buildCreateAssetTx

▸ **buildCreateAssetTx**(`utxoset`: [UTXOSet](api_avm_utxos.utxoset.md), `fromAddresses`: Array‹string› | Array‹Buffer›, `initialStates`: [InitialStates](api_avm_initialstates.initialstates.md), `name`: string, `symbol`: string, `denomination`: number, `memo`: [PayloadBase](common_payload.payloadbase.md) | Buffer, `asOf`: BN): *Promise‹[UnsignedTx](api_avm_transactions.unsignedtx.md)›*

Defined in src/apis/avm/api.ts:863

Creates an unsigned transaction. For more granular control, you may create your own
[UnsignedTx](api_avm_transactions.unsignedtx.md) manually (with their corresponding [TransferableInput](api_avm_inputs.transferableinput.md)s, [TransferableOutput](api_avm_outputs.transferableoutput.md)s, and [[TransferOperation]]s).

**Parameters:**

Name | Type | Default | Description |
------ | ------ | ------ | ------ |
`utxoset` | [UTXOSet](api_avm_utxos.utxoset.md) | - | A set of UTXOs that the transaction is built on |
`fromAddresses` | Array‹string› &#124; Array‹Buffer› | - | The addresses being used to send the funds from the UTXOs [Buffer](https://github.com/feross/buffer) |
`initialStates` | [InitialStates](api_avm_initialstates.initialstates.md) | - | - |
`name` | string | - | String for the descriptive name of the asset |
`symbol` | string | - | String for the ticker symbol of the asset |
`denomination` | number | - | Optional number for the denomination which is 10^D. D must be >= 0 and <= 32. Ex: $1 AVAX = 10^9 $nAVAX |
`memo` | [PayloadBase](common_payload.payloadbase.md) &#124; Buffer | undefined | Optional contains arbitrary bytes, up to 256 bytes |
`asOf` | BN | UnixNow() | Optional. The timestamp to verify the transaction against as a [BN](https://github.com/indutny/bn.js/)  |

**Returns:** *Promise‹[UnsignedTx](api_avm_transactions.unsignedtx.md)›*

An unsigned transaction ([UnsignedTx](api_avm_transactions.unsignedtx.md)) which contains a [CreateAssetTx](api_avm_createassettx.createassettx.md).

___

###  buildCreateNFTAssetTx

▸ **buildCreateNFTAssetTx**(`utxoset`: [UTXOSet](api_avm_utxos.utxoset.md), `fromAddresses`: Array‹string› | Array‹Buffer›, `minterSets`: [MinterSet](api_avm_minterset.minterset.md)[], `name`: string, `symbol`: string, `memo`: [PayloadBase](common_payload.payloadbase.md) | Buffer, `asOf`: BN, `locktime`: BN): *Promise‹[UnsignedTx](api_avm_transactions.unsignedtx.md)›*

Defined in src/apis/avm/api.ts:948

Creates an unsigned transaction. For more granular control, you may create your own
[UnsignedTx](api_avm_transactions.unsignedtx.md) manually (with their corresponding [TransferableInput](api_avm_inputs.transferableinput.md)s, [TransferableOutput](api_avm_outputs.transferableoutput.md)s, and [[TransferOperation]]s).

**Parameters:**

Name | Type | Default | Description |
------ | ------ | ------ | ------ |
`utxoset` | [UTXOSet](api_avm_utxos.utxoset.md) | - | A set of UTXOs that the transaction is built on |
`fromAddresses` | Array‹string› &#124; Array‹Buffer› | - | The addresses being used to send the funds from the UTXOs [Buffer](https://github.com/feross/buffer) |
`minterSets` | [MinterSet](api_avm_minterset.minterset.md)[] | - | is a list where each element specifies that threshold of the addresses in minters may together mint more of the asset by signing a minting transaction |
`name` | string | - | String for the descriptive name of the asset |
`symbol` | string | - | String for the ticker symbol of the asset |
`memo` | [PayloadBase](common_payload.payloadbase.md) &#124; Buffer | undefined | Optional contains arbitrary bytes, up to 256 bytes |
`asOf` | BN | UnixNow() | Optional. The timestamp to verify the transaction against as a [BN](https://github.com/indutny/bn.js/) |
`locktime` | BN | new BN(0) | Optional. The locktime field created in the resulting mint output  ```js Example minterSets: [      {          "minters":[              "X-avax1ghstjukrtw8935lryqtnh643xe9a94u3tc75c7"          ],          "threshold": 1      },      {          "minters": [              "X-avax1yell3e4nln0m39cfpdhgqprsd87jkh4qnakklx",              "X-avax1k4nr26c80jaquzm9369j5a4shmwcjn0vmemcjz",              "X-avax1ztkzsrjnkn0cek5ryvhqswdtcg23nhge3nnr5e"          ],          "threshold": 2      } ] ```  |

**Returns:** *Promise‹[UnsignedTx](api_avm_transactions.unsignedtx.md)›*

An unsigned transaction ([UnsignedTx](api_avm_transactions.unsignedtx.md)) which contains a [CreateAssetTx](api_avm_createassettx.createassettx.md).

___

###  buildCreateNFTMintTx

▸ **buildCreateNFTMintTx**(`utxoset`: [UTXOSet](api_avm_utxos.utxoset.md), `toAddresses`: Array‹string› | Array‹Buffer›, `fromAddresses`: Array‹string› | Array‹Buffer›, `utxoid`: string | Array‹string›, `groupID`: number, `payload`: [PayloadBase](common_payload.payloadbase.md) | Buffer, `memo`: [PayloadBase](common_payload.payloadbase.md) | Buffer, `asOf`: BN, `locktime`: BN, `threshold`: number): *Promise‹any›*

Defined in src/apis/avm/api.ts:1008

Creates an unsigned transaction. For more granular control, you may create your own
[UnsignedTx](api_avm_transactions.unsignedtx.md) manually (with their corresponding [TransferableInput](api_avm_inputs.transferableinput.md)s, [TransferableOutput](api_avm_outputs.transferableoutput.md)s, and [[TransferOperation]]s).

**Parameters:**

Name | Type | Default | Description |
------ | ------ | ------ | ------ |
`utxoset` | [UTXOSet](api_avm_utxos.utxoset.md) | - | A set of UTXOs that the transaction is built on |
`toAddresses` | Array‹string› &#124; Array‹Buffer› | - | The addresses to send the nft output |
`fromAddresses` | Array‹string› &#124; Array‹Buffer› | - | The addresses being used to send the NFT from the utxoID provided |
`utxoid` | string &#124; Array‹string› | - | A base58 utxoID or an array of base58 utxoIDs for the nft mint output this transaction is sending |
`groupID` | number | 0 | Optional. The group this NFT is issued to. |
`payload` | [PayloadBase](common_payload.payloadbase.md) &#124; Buffer | undefined | Optional. Data for NFT Payload as either a [PayloadBase](common_payload.payloadbase.md) or a [Buffer](https://github.com/feross/buffer) |
`memo` | [PayloadBase](common_payload.payloadbase.md) &#124; Buffer | undefined | Optional contains arbitrary bytes, up to 256 bytes |
`asOf` | BN | UnixNow() | Optional. The timestamp to verify the transaction against as a [BN](https://github.com/indutny/bn.js/) |
`locktime` | BN | new BN(0) | Optional. The locktime field created in the resulting mint output |
`threshold` | number | 1 | Optional. The number of signatures required to spend the funds in the resultant UTXO   |

**Returns:** *Promise‹any›*

An unsigned transaction ([UnsignedTx](api_avm_transactions.unsignedtx.md)) which contains an [OperationTx](api_avm_operationtx.operationtx.md).

___

###  buildExportTx

▸ **buildExportTx**(`utxoset`: [UTXOSet](api_avm_utxos.utxoset.md), `amount`: BN, `toAddresses`: Array‹string›, `fromAddresses`: Array‹string›, `changeAddresses`: Array‹string›, `destinationChain`: Buffer | string, `memo`: [PayloadBase](common_payload.payloadbase.md) | Buffer, `asOf`: BN, `locktime`: BN, `threshold`: number): *Promise‹[UnsignedTx](api_avm_transactions.unsignedtx.md)›*

Defined in src/apis/avm/api.ts:797

Helper function which creates an unsigned Export Tx. For more granular control, you may create your own
[UnsignedTx](api_avm_transactions.unsignedtx.md) manually (with their corresponding [TransferableInput](api_avm_inputs.transferableinput.md)s, [TransferableOutput](api_avm_outputs.transferableoutput.md)s, and [[TransferOperation]]s).

**Parameters:**

Name | Type | Default | Description |
------ | ------ | ------ | ------ |
`utxoset` | [UTXOSet](api_avm_utxos.utxoset.md) | - | A set of UTXOs that the transaction is built on |
`amount` | BN | - | The amount being exported as a [BN](https://github.com/indutny/bn.js/) |
`toAddresses` | Array‹string› | - | The addresses to send the funds |
`fromAddresses` | Array‹string› | - | The addresses being used to send the funds from the UTXOs provided |
`changeAddresses` | Array‹string› | undefined | The addresses that can spend the change remaining from the spent UTXOs |
`destinationChain` | Buffer &#124; string | undefined | The chainid for where the assets will be sent. Default platform chainid. |
`memo` | [PayloadBase](common_payload.payloadbase.md) &#124; Buffer | undefined | Optional contains arbitrary bytes, up to 256 bytes |
`asOf` | BN | UnixNow() | Optional. The timestamp to verify the transaction against as a [BN](https://github.com/indutny/bn.js/) |
`locktime` | BN | new BN(0) | Optional. The locktime field created in the resulting outputs |
`threshold` | number | 1 | Optional. The number of signatures required to spend the funds in the resultant UTXO  |

**Returns:** *Promise‹[UnsignedTx](api_avm_transactions.unsignedtx.md)›*

An unsigned transaction ([UnsignedTx](api_avm_transactions.unsignedtx.md)) which contains an [ExportTx](api_avm_exporttx.exporttx.md).

___

###  buildGenesis

▸ **buildGenesis**(`genesisData`: object): *Promise‹string›*

Defined in src/apis/avm/api.ts:1141

Given a JSON representation of this Virtual Machine’s genesis state, create the byte representation of that state.

**Parameters:**

Name | Type | Description |
------ | ------ | ------ |
`genesisData` | object | The blockchain's genesis data object  |

**Returns:** *Promise‹string›*

Promise of a string of bytes

___

###  buildImportTx

▸ **buildImportTx**(`utxoset`: [UTXOSet](api_avm_utxos.utxoset.md), `ownerAddresses`: Array‹string›, `sourceChain`: Buffer | string, `memo`: [PayloadBase](common_payload.payloadbase.md) | Buffer, `asOf`: BN): *Promise‹[UnsignedTx](api_avm_transactions.unsignedtx.md)›*

Defined in src/apis/avm/api.ts:710

Helper function which creates an unsigned Import Tx. For more granular control, you may create your own
[UnsignedTx](api_avm_transactions.unsignedtx.md) manually (with their corresponding [TransferableInput](api_avm_inputs.transferableinput.md)s, [TransferableOutput](api_avm_outputs.transferableoutput.md)s, and [[TransferOperation]]s).

**`remarks`** 
This helper exists because the endpoint API should be the primary point of entry for most functionality.

**Parameters:**

Name | Type | Default | Description |
------ | ------ | ------ | ------ |
`utxoset` | [UTXOSet](api_avm_utxos.utxoset.md) | - | A set of UTXOs that the transaction is built on |
`ownerAddresses` | Array‹string› | - | The addresses being used to import |
`sourceChain` | Buffer &#124; string | undefined | The chainid for where the import is coming from. Default, platform chainid. |
`memo` | [PayloadBase](common_payload.payloadbase.md) &#124; Buffer | undefined | Optional contains arbitrary bytes, up to 256 bytes |
`asOf` | BN | UnixNow() | Optional. The timestamp to verify the transaction against as a [BN](https://github.com/indutny/bn.js/)  |

**Returns:** *Promise‹[UnsignedTx](api_avm_transactions.unsignedtx.md)›*

An unsigned transaction ([UnsignedTx](api_avm_transactions.unsignedtx.md)) which contains a [ImportTx](api_avm_importtx.importtx.md).

___

###  buildNFTTransferTx

▸ **buildNFTTransferTx**(`utxoset`: [UTXOSet](api_avm_utxos.utxoset.md), `toAddresses`: Array‹string›, `fromAddresses`: Array‹string›, `utxoid`: string | Array‹string›, `memo`: [PayloadBase](common_payload.payloadbase.md) | Buffer, `asOf`: BN, `locktime`: BN, `threshold`: number): *Promise‹[UnsignedTx](api_avm_transactions.unsignedtx.md)›*

Defined in src/apis/avm/api.ts:651

Helper function which creates an unsigned NFT Transfer. For more granular control, you may create your own
[UnsignedTx](api_avm_transactions.unsignedtx.md) manually (with their corresponding [TransferableInput](api_avm_inputs.transferableinput.md)s, [TransferableOutput](api_avm_outputs.transferableoutput.md)s, and [[TransferOperation]]s).

**`remarks`** 
This helper exists because the endpoint API should be the primary point of entry for most functionality.

**Parameters:**

Name | Type | Default | Description |
------ | ------ | ------ | ------ |
`utxoset` | [UTXOSet](api_avm_utxos.utxoset.md) | - | A set of UTXOs that the transaction is built on |
`toAddresses` | Array‹string› | - | The addresses to send the NFT |
`fromAddresses` | Array‹string› | - | The addresses being used to send the NFT from the utxoID provided |
`utxoid` | string &#124; Array‹string› | - | A base58 utxoID or an array of base58 utxoIDs for the nfts this transaction is sending |
`memo` | [PayloadBase](common_payload.payloadbase.md) &#124; Buffer | undefined | Optional contains arbitrary bytes, up to 256 bytes |
`asOf` | BN | UnixNow() | Optional. The timestamp to verify the transaction against as a [BN](https://github.com/indutny/bn.js/) |
`locktime` | BN | new BN(0) | Optional. The locktime field created in the resulting outputs |
`threshold` | number | 1 | Optional. The number of signatures required to spend the funds in the resultant UTXO  |

**Returns:** *Promise‹[UnsignedTx](api_avm_transactions.unsignedtx.md)›*

An unsigned transaction ([UnsignedTx](api_avm_transactions.unsignedtx.md)) which contains a [[NFTTransferTx]].

___

###  callMethod

▸ **callMethod**(`method`: string, `params?`: Array‹object› | object, `baseurl?`: string): *Promise‹[RequestResponseData](common_apibase.requestresponsedata.md)›*

*Inherited from [JRPCAPI](common_jrpcapi.jrpcapi.md).[callMethod](common_jrpcapi.jrpcapi.md#callmethod)*

Defined in src/common/jrpcapi.ts:21

**Parameters:**

Name | Type |
------ | ------ |
`method` | string |
`params?` | Array‹object› &#124; object |
`baseurl?` | string |

**Returns:** *Promise‹[RequestResponseData](common_apibase.requestresponsedata.md)›*

___

###  checkGooseEgg

▸ **checkGooseEgg**(`utx`: [UnsignedTx](api_avm_transactions.unsignedtx.md)): *Promise‹boolean›*

Defined in src/apis/avm/api.ts:184

Helper function which determines if a tx is a goose egg transaction.

**`remarks`** 
A "Goose Egg Transaction" is when the fee far exceeds a reasonable amount

**Parameters:**

Name | Type | Description |
------ | ------ | ------ |
`utx` | [UnsignedTx](api_avm_transactions.unsignedtx.md) | An UnsignedTx  |

**Returns:** *Promise‹boolean›*

boolean true if passes goose egg test and false if fails.

___

###  createAddress

▸ **createAddress**(`username`: string, `password`: string): *Promise‹string›*

Defined in src/apis/avm/api.ts:224

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

▸ **createFixedCapAsset**(`username`: string, `password`: string, `name`: string, `symbol`: string, `denomination`: number, `initialHolders`: Array‹object›): *Promise‹string›*

Defined in src/apis/avm/api.ts:258

Create a new fixed-cap, fungible asset. A quantity of it is created at initialization and there no more is ever created.

**Parameters:**

Name | Type | Description |
------ | ------ | ------ |
`username` | string | The user paying the transaction fee (in $AVAX) for asset creation |
`password` | string | The password for the user paying the transaction fee (in $AVAX) for asset creation |
`name` | string | The human-readable name for the asset |
`symbol` | string | Optional. The shorthand symbol for the asset. Between 0 and 4 characters |
`denomination` | number | Optional. Determines how balances of this asset are displayed by user interfaces. Default is 0 |
`initialHolders` | Array‹object› | An array of objects containing the field "address" and "amount" to establish the genesis values for the new asset  ```js Example initialHolders: [     {         "address": "X-avax1kj06lhgx84h39snsljcey3tpc046ze68mek3g5",         "amount": 10000     },     {         "address": "X-avax1am4w6hfrvmh3akduzkjthrtgtqafalce6an8cr",         "amount": 50000     } ] ```  |

**Returns:** *Promise‹string›*

Returns a Promise<string> containing the base 58 string representation of the ID of the newly created asset.

___

###  createVariableCapAsset

▸ **createVariableCapAsset**(`username`: string, `password`: string, `name`: string, `symbol`: string, `denomination`: number, `minterSets`: Array‹object›): *Promise‹string›*

Defined in src/apis/avm/api.ts:302

Create a new variable-cap, fungible asset. No units of the asset exist at initialization. Minters can mint units of this asset using createMintTx, signMintTx and sendMintTx.

**Parameters:**

Name | Type | Description |
------ | ------ | ------ |
`username` | string | The user paying the transaction fee (in $AVAX) for asset creation |
`password` | string | The password for the user paying the transaction fee (in $AVAX) for asset creation |
`name` | string | The human-readable name for the asset |
`symbol` | string | Optional. The shorthand symbol for the asset -- between 0 and 4 characters |
`denomination` | number | Optional. Determines how balances of this asset are displayed by user interfaces. Default is 0 |
`minterSets` | Array‹object› | is a list where each element specifies that threshold of the addresses in minters may together mint more of the asset by signing a minting transaction  ```js Example minterSets: [      {          "minters":[              "X-avax1am4w6hfrvmh3akduzkjthrtgtqafalce6an8cr"          ],          "threshold": 1      },      {          "minters": [              "X-avax1am4w6hfrvmh3akduzkjthrtgtqafalce6an8cr",              "X-avax1kj06lhgx84h39snsljcey3tpc046ze68mek3g5",              "X-avax1yell3e4nln0m39cfpdhgqprsd87jkh4qnakklx"          ],          "threshold": 2      } ] ```  |

**Returns:** *Promise‹string›*

Returns a Promise<string> containing the base 58 string representation of the ID of the newly created asset.

___

###  exportAVAX

▸ **exportAVAX**(`username`: string, `password`: string, `to`: string, `amount`: BN): *Promise‹string›*

Defined in src/apis/avm/api.ts:400

Send AVAX from the X-Chain to an account on the P-Chain.

After calling this method, you must call the P-Chain’s importAVAX method to complete the transfer.

**Parameters:**

Name | Type | Description |
------ | ------ | ------ |
`username` | string | The Keystore user that controls the P-Chain account specified in `to` |
`password` | string | The password of the Keystore user |
`to` | string | The account on the P-Chain to send the AVAX to. Do not include P- in the address |
`amount` | BN | Amount of AVAX to export as a [BN](https://github.com/indutny/bn.js/)  |

**Returns:** *Promise‹string›*

String representing the transaction id

___

###  exportKey

▸ **exportKey**(`username`: string, `password`: string, `address`: string): *Promise‹string›*

Defined in src/apis/avm/api.ts:357

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

###  getAVAXAssetID

▸ **getAVAXAssetID**(): *Promise‹Buffer›*

Defined in src/apis/avm/api.ts:110

Fetches the AVAX AssetID and returns it in a Promise.

**Returns:** *Promise‹Buffer›*

The the provided string representing the AVAX AssetID

___

###  getAllBalances

▸ **getAllBalances**(`address`: string): *Promise‹Array‹object››*

Defined in src/apis/avm/api.ts:454

Retrieves all assets for an address on a server and their associated balances.

**Parameters:**

Name | Type | Description |
------ | ------ | ------ |
`address` | string | The address to get a list of assets  |

**Returns:** *Promise‹Array‹object››*

Promise of an object mapping assetID strings with [BN](https://github.com/indutny/bn.js/) balance for the address on the blockchain.

___

###  getAssetDescription

▸ **getAssetDescription**(`assetID`: Buffer | string): *Promise‹object›*

Defined in src/apis/avm/api.ts:472

Retrieves an assets name and symbol.

**Parameters:**

Name | Type | Description |
------ | ------ | ------ |
`assetID` | Buffer &#124; string | Either a [Buffer](https://github.com/feross/buffer) or an b58 serialized string for the AssetID or its alias.  |

**Returns:** *Promise‹object›*

Returns a Promise<object> with keys "name" and "symbol".

___

###  getBalance

▸ **getBalance**(`address`: string, `assetID`: string): *Promise‹object›*

Defined in src/apis/avm/api.ts:204

Gets the balance of a particular asset on a blockchain.

**Parameters:**

Name | Type | Description |
------ | ------ | ------ |
`address` | string | The address to pull the asset balance from |
`assetID` | string | The assetID to pull the balance from  |

**Returns:** *Promise‹object›*

Promise with the balance of the assetID as a [BN](https://github.com/indutny/bn.js/) on the provided address for the blockchain.

___

###  getBaseURL

▸ **getBaseURL**(): *string*

*Inherited from [APIBase](common_apibase.apibase.md).[getBaseURL](common_apibase.apibase.md#getbaseurl)*

Defined in src/common/apibase.ts:63

Returns the baseurl's path.

**Returns:** *string*

___

###  getBlockchainAlias

▸ **getBlockchainAlias**(): *string*

Defined in src/apis/avm/api.ts:54

Gets the alias for the blockchainID if it exists, otherwise returns `undefined`.

**Returns:** *string*

The alias for the blockchainID

___

###  getBlockchainID

▸ **getBlockchainID**(): *string*

Defined in src/apis/avm/api.ts:68

Gets the blockchainID and returns it.

**Returns:** *string*

The blockchainID

___

###  getDB

▸ **getDB**(): *StoreAPI*

*Inherited from [APIBase](common_apibase.apibase.md).[getDB](common_apibase.apibase.md#getdb)*

Defined in src/common/apibase.ts:68

Returns the baseurl's database.

**Returns:** *StoreAPI*

___

###  getDefaultFee

▸ **getDefaultFee**(): *BN*

Defined in src/apis/avm/api.ts:128

Gets the default fee for this chain.

**Returns:** *BN*

The default fee as a [BN](https://github.com/indutny/bn.js/)

___

###  getFee

▸ **getFee**(): *BN*

Defined in src/apis/avm/api.ts:137

Gets the fee for this chain.

**Returns:** *BN*

The fee as a [BN](https://github.com/indutny/bn.js/)

___

###  getRPCID

▸ **getRPCID**(): *number*

*Inherited from [JRPCAPI](common_jrpcapi.jrpcapi.md).[getRPCID](common_jrpcapi.jrpcapi.md#getrpcid)*

Defined in src/common/jrpcapi.ts:66

Returns the rpcid, a strictly-increasing number, starting from 1, indicating the next
request ID that will be sent.

**Returns:** *number*

___

###  getTx

▸ **getTx**(`txid`: string): *Promise‹string›*

Defined in src/apis/avm/api.ts:497

Returns the treansaction data of a provided transaction ID by calling the node's `getTx` method.

**Parameters:**

Name | Type | Description |
------ | ------ | ------ |
`txid` | string | The string representation of the transaction ID  |

**Returns:** *Promise‹string›*

Returns a Promise<string> containing the bytes retrieved from the node

___

###  getTxStatus

▸ **getTxStatus**(`txid`: string): *Promise‹string›*

Defined in src/apis/avm/api.ts:511

Returns the status of a provided transaction ID by calling the node's `getTxStatus` method.

**Parameters:**

Name | Type | Description |
------ | ------ | ------ |
`txid` | string | The string representation of the transaction ID  |

**Returns:** *Promise‹string›*

Returns a Promise<string> containing the status retrieved from the node

___

###  getUTXOs

▸ **getUTXOs**(`addresses`: Array‹string› | Array‹Buffer›, `limit`: number, `startIndex`: number, `persistOpts`: [PersistanceOptions](src_utils.persistanceoptions.md)): *Promise‹[UTXOSet](api_avm_utxos.utxoset.md)›*

Defined in src/apis/avm/api.ts:532

Retrieves the UTXOs related to the addresses provided from the node's `getUTXOs` method.

**`remarks`** 
persistOpts is optional and must be of type [PersistanceOptions](src_utils.persistanceoptions.md)

**Parameters:**

Name | Type | Default | Description |
------ | ------ | ------ | ------ |
`addresses` | Array‹string› &#124; Array‹Buffer› | - | An array of addresses as cb58 strings or addresses as [Buffer](https://github.com/feross/buffer)s |
`limit` | number | 0 | Optional. Returns at most [limit] addresses. If [limit] == 0 or > [maxUTXOsToFetch], fetches up to [maxUTXOsToFetch]. |
`startIndex` | number | undefined | Optional. [StartIndex] defines where to start fetching UTXOs (for pagination.) UTXOs fetched are from addresses equal to or greater than [StartIndex.Address] For address [StartIndex.Address], only UTXOs with IDs greater than [StartIndex.Utxo] will be returned. |
`persistOpts` | [PersistanceOptions](src_utils.persistanceoptions.md) | undefined | Options available to persist these UTXOs in local storage  |

**Returns:** *Promise‹[UTXOSet](api_avm_utxos.utxoset.md)›*

___

###  importAVAX

▸ **importAVAX**(`username`: string, `password`: string, `to`: string, `sourceChain`: string): *Promise‹string›*

Defined in src/apis/avm/api.ts:421

Finalize a transfer of AVAX from the P-Chain to the X-Chain.

Before this method is called, you must call the P-Chain’s `exportAVAX` method to initiate the transfer.

**Parameters:**

Name | Type | Description |
------ | ------ | ------ |
`username` | string | The Keystore user that controls the address specified in `to` |
`password` | string | The password of the Keystore user |
`to` | string | The address the AVAX is sent to. This must be the same as the to argument in the corresponding call to the P-Chain’s exportAVAX, except that the prepended X- should be included in this argument |
`sourceChain` | string | Chain the funds are coming from.  |

**Returns:** *Promise‹string›*

String representing the transaction id

___

###  importKey

▸ **importKey**(`username`: string, `password`: string, `privateKey`: string): *Promise‹string›*

Defined in src/apis/avm/api.ts:379

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

▸ **issueTx**(`tx`: string | Buffer | [Tx](api_avm_transactions.tx.md)): *Promise‹string›*

Defined in src/apis/avm/api.ts:1069

Calls the node's issueTx method from the API and returns the resulting transaction ID as a string.

**Parameters:**

Name | Type | Description |
------ | ------ | ------ |
`tx` | string &#124; Buffer &#124; [Tx](api_avm_transactions.tx.md) | A string, [Buffer](https://github.com/feross/buffer), or [Tx](api_avm_transactions.tx.md) representing a transaction  |

**Returns:** *Promise‹string›*

A Promise<string> representing the transaction ID of the posted transaction.

___

###  keyChain

▸ **keyChain**(): *[AVMKeyChain](api_avm_keychain.avmkeychain.md)*

Defined in src/apis/avm/api.ts:158

Gets a reference to the keychain for this class.

**Returns:** *[AVMKeyChain](api_avm_keychain.avmkeychain.md)*

The instance of [AVMKeyChain](api_avm_keychain.avmkeychain.md) for this class

___

###  listAddresses

▸ **listAddresses**(`username`: string, `password`: string): *Promise‹Array‹string››*

Defined in src/apis/avm/api.ts:439

Lists all the addresses under a user.

**Parameters:**

Name | Type | Description |
------ | ------ | ------ |
`username` | string | The user to list addresses |
`password` | string | The password of the user to list the addresses  |

**Returns:** *Promise‹Array‹string››*

Promise of an array of address strings in the format specified by the blockchain.

___

###  mint

▸ **mint**(`username`: string, `password`: string, `amount`: number | BN, `assetID`: Buffer | string, `to`: string, `minters`: Array‹string›): *Promise‹string›*

Defined in src/apis/avm/api.ts:324

Create an unsigned transaction to mint more of an asset.

**Parameters:**

Name | Type | Description |
------ | ------ | ------ |
`username` | string | - |
`password` | string | - |
`amount` | number &#124; BN | The units of the asset to mint |
`assetID` | Buffer &#124; string | The ID of the asset to mint |
`to` | string | The address to assign the units of the minted asset |
`minters` | Array‹string› | Addresses of the minters responsible for signing the transaction  |

**Returns:** *Promise‹string›*

Returns a Promise<string> containing the base 58 string representation of the unsigned transaction.

___

###  parseAddress

▸ **parseAddress**(`addr`: string): *Buffer*

Defined in src/apis/avm/api.ts:94

Takes an address string and returns its [Buffer](https://github.com/feross/buffer) representation if valid.

**Parameters:**

Name | Type |
------ | ------ |
`addr` | string |

**Returns:** *Buffer*

A [Buffer](https://github.com/feross/buffer) for the address if valid, undefined if not valid.

___

###  refreshBlockchainID

▸ **refreshBlockchainID**(`blockchainID`: string): *boolean*

Defined in src/apis/avm/api.ts:77

Refresh blockchainID, and if a blockchainID is passed in, use that.

**Parameters:**

Name | Type | Default |
------ | ------ | ------ |
`blockchainID` | string | undefined |

**Returns:** *boolean*

The blockchainID

___

###  send

▸ **send**(`username`: string, `password`: string, `assetID`: string | Buffer, `amount`: number | BN, `to`: string, `from`: Array‹string› | Array‹Buffer›): *Promise‹string›*

Defined in src/apis/avm/api.ts:1101

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

*Inherited from [APIBase](common_apibase.apibase.md).[setBaseURL](common_apibase.apibase.md#setbaseurl)*

Defined in src/common/apibase.ts:47

Sets the path of the APIs baseurl.

**Parameters:**

Name | Type | Description |
------ | ------ | ------ |
`baseurl` | string | Path of the APIs baseurl - ex: "/ext/bc/avm"  |

**Returns:** *void*

___

###  setFee

▸ **setFee**(`fee`: BN): *void*

Defined in src/apis/avm/api.ts:149

Sets the fee for this chain.

**Parameters:**

Name | Type | Description |
------ | ------ | ------ |
`fee` | BN | The fee amount to set as [BN](https://github.com/indutny/bn.js/)  |

**Returns:** *void*

___

###  signTx

▸ **signTx**(`utx`: [UnsignedTx](api_avm_transactions.unsignedtx.md)): *[Tx](api_avm_transactions.tx.md)*

Defined in src/apis/avm/api.ts:1060

Helper function which takes an unsigned transaction and signs it, returning the resulting [Tx](api_avm_transactions.tx.md).

**Parameters:**

Name | Type | Description |
------ | ------ | ------ |
`utx` | [UnsignedTx](api_avm_transactions.unsignedtx.md) | The unsigned transaction of type [UnsignedTx](api_avm_transactions.unsignedtx.md)  |

**Returns:** *[Tx](api_avm_transactions.tx.md)*

A signed transaction of type [Tx](api_avm_transactions.tx.md)
