[avalanche](../README.md) › [PlatformAPI](../modules/platformapi.md) › [PlatformAPI](platformapi.platformapi-1.md)

# Class: PlatformAPI

Class for interacting with a node's PlatformAPI

**`remarks`** This extends the [JRPCAPI](utils_types.jrpcapi.md) class. This class should not be directly called. Instead, use the [Avalanche.addAPI](avalanche.avalanche-1.md#addapi) function to register this interface with Avalanche.

## Hierarchy

  ↳ [JRPCAPI](utils_types.jrpcapi.md)

  ↳ **PlatformAPI**

## Index

### Constructors

* [constructor](platformapi.platformapi-1.md#constructor)

### Properties

* [baseurl](platformapi.platformapi-1.md#protected-baseurl)
* [core](platformapi.platformapi-1.md#protected-core)
* [db](platformapi.platformapi-1.md#protected-db)
* [jrpcVersion](platformapi.platformapi-1.md#protected-jrpcversion)
* [rpcid](platformapi.platformapi-1.md#protected-rpcid)

### Methods

* [addDefaultSubnetDelegator](platformapi.platformapi-1.md#adddefaultsubnetdelegator)
* [addDefaultSubnetValidator](platformapi.platformapi-1.md#adddefaultsubnetvalidator)
* [addNonDefaultSubnetValidator](platformapi.platformapi-1.md#addnondefaultsubnetvalidator)
* [callMethod](platformapi.platformapi-1.md#callmethod)
* [createAccount](platformapi.platformapi-1.md#createaccount)
* [createBlockchain](platformapi.platformapi-1.md#createblockchain)
* [createSubnet](platformapi.platformapi-1.md#createsubnet)
* [exportAVA](platformapi.platformapi-1.md#exportava)
* [exportKey](platformapi.platformapi-1.md#exportkey)
* [getAccount](platformapi.platformapi-1.md#getaccount)
* [getBaseURL](platformapi.platformapi-1.md#getbaseurl)
* [getBlockchainStatus](platformapi.platformapi-1.md#getblockchainstatus)
* [getBlockchains](platformapi.platformapi-1.md#getblockchains)
* [getCurrentValidators](platformapi.platformapi-1.md#getcurrentvalidators)
* [getDB](platformapi.platformapi-1.md#getdb)
* [getPendingValidators](platformapi.platformapi-1.md#getpendingvalidators)
* [getRPCID](platformapi.platformapi-1.md#getrpcid)
* [getSubnets](platformapi.platformapi-1.md#getsubnets)
* [importAVA](platformapi.platformapi-1.md#importava)
* [importKey](platformapi.platformapi-1.md#importkey)
* [issueTx](platformapi.platformapi-1.md#issuetx)
* [listAccounts](platformapi.platformapi-1.md#listaccounts)
* [sampleValidators](platformapi.platformapi-1.md#samplevalidators)
* [setBaseURL](platformapi.platformapi-1.md#setbaseurl)
* [sign](platformapi.platformapi-1.md#sign)
* [validatedBy](platformapi.platformapi-1.md#validatedby)
* [validates](platformapi.platformapi-1.md#validates)

## Constructors

###  constructor

\+ **new PlatformAPI**(`core`: [AvalancheCore](avalanchecore.avalanchecore-1.md), `baseurl`: string): *[PlatformAPI](platformapi.platformapi-1.md)*

*Overrides [JRPCAPI](utils_types.jrpcapi.md).[constructor](utils_types.jrpcapi.md#constructor)*

*Defined in [apis/platform/api.ts:479](https://github.com/ava-labs/avalanche.js/blob/4d26b45/src/apis/platform/api.ts#L479)*

This class should not be instantiated directly. Instead use the [Avalanche.addAPI](avalanche.avalanche-1.md#addapi) method.

**Parameters:**

Name | Type | Default | Description |
------ | ------ | ------ | ------ |
`core` | [AvalancheCore](avalanchecore.avalanchecore-1.md) | - | A reference to the Avalanche class |
`baseurl` | string | "/ext/P" | Defaults to the string "/ext/P" as the path to blockchain's baseurl  |

**Returns:** *[PlatformAPI](platformapi.platformapi-1.md)*

## Properties

### `Protected` baseurl

• **baseurl**: *string*

*Inherited from [APIBase](utils_types.apibase.md).[baseurl](utils_types.apibase.md#protected-baseurl)*

*Defined in [utils/types.ts:34](https://github.com/ava-labs/avalanche.js/blob/4d26b45/src/utils/types.ts#L34)*

___

### `Protected` core

• **core**: *[AvalancheCore](avalanchecore.avalanchecore-1.md)*

*Inherited from [APIBase](utils_types.apibase.md).[core](utils_types.apibase.md#protected-core)*

*Defined in [utils/types.ts:33](https://github.com/ava-labs/avalanche.js/blob/4d26b45/src/utils/types.ts#L33)*

___

### `Protected` db

• **db**: *StoreAPI*

*Inherited from [APIBase](utils_types.apibase.md).[db](utils_types.apibase.md#protected-db)*

*Defined in [utils/types.ts:35](https://github.com/ava-labs/avalanche.js/blob/4d26b45/src/utils/types.ts#L35)*

___

### `Protected` jrpcVersion

• **jrpcVersion**: *string* = "2.0"

*Inherited from [JRPCAPI](utils_types.jrpcapi.md).[jrpcVersion](utils_types.jrpcapi.md#protected-jrpcversion)*

*Defined in [utils/types.ts:81](https://github.com/ava-labs/avalanche.js/blob/4d26b45/src/utils/types.ts#L81)*

___

### `Protected` rpcid

• **rpcid**: *number* = 1

*Inherited from [JRPCAPI](utils_types.jrpcapi.md).[rpcid](utils_types.jrpcapi.md#protected-rpcid)*

*Defined in [utils/types.ts:82](https://github.com/ava-labs/avalanche.js/blob/4d26b45/src/utils/types.ts#L82)*

## Methods

###  addDefaultSubnetDelegator

▸ **addDefaultSubnetDelegator**(`id`: string, `startTime`: Date, `endTime`: Date, `stakeAmount`: BN, `payerNonce`: number, `destination`: string): *Promise‹string›*

*Defined in [apis/platform/api.ts:264](https://github.com/ava-labs/avalanche.js/blob/4d26b45/src/apis/platform/api.ts#L264)*

Add a delegator to the Default Subnet.

**Parameters:**

Name | Type | Description |
------ | ------ | ------ |
`id` | string | The node ID of the delegatee |
`startTime` | Date | Javascript Date object for when the delegator starts delegating |
`endTime` | Date | Javascript Date object for when the delegator starts delegating |
`stakeAmount` | BN | The amount of nAVA the delegator is staking as a [BN](https://github.com/indutny/bn.js/) |
`payerNonce` | number | The next unused nonce of the account that will provide the staked AVA and pay the transaction fee |
`destination` | string | The address of the account the staked AVA and validation reward (if applicable) are sent to at endTime  |

**Returns:** *Promise‹string›*

Promise for an array of validator's stakingIDs.

___

###  addDefaultSubnetValidator

▸ **addDefaultSubnetValidator**(`id`: string, `startTime`: Date, `endTime`: Date, `stakeAmount`: BN, `payerNonce`: number, `destination`: string, `delegationFeeRate`: BN): *Promise‹string›*

*Defined in [apis/platform/api.ts:204](https://github.com/ava-labs/avalanche.js/blob/4d26b45/src/apis/platform/api.ts#L204)*

Add a validator to the Default Subnet.

**Parameters:**

Name | Type | Default | Description |
------ | ------ | ------ | ------ |
`id` | string | - | The node ID of the validator |
`startTime` | Date | - | Javascript Date object for the start time to validate |
`endTime` | Date | - | Javascript Date object for the end time to validate |
`stakeAmount` | BN | - | The amount of nAVA the validator is staking as a [BN](https://github.com/indutny/bn.js/) |
`payerNonce` | number | - | The next unused nonce of the account that is providing the staked AVA and paying the transaction fee |
`destination` | string | - | The P-Chain address of the account that the staked AVA will be returned to, as well as a validation reward if the validator is sufficiently responsive and correct while it validated |
`delegationFeeRate` | BN | undefined | Optional. The percent fee this validator charges when others delegate stake to them, multiplied by 10,000 as a [BN](https://github.com/indutny/bn.js/). For example, suppose a validator has delegationFeeRate 300,000 and someone delegates to that validator. When the delegation period is over, if the delegator is entitled to a reward, 30% of the reward (300,000 / 10,000) goes to the validator and 70% goes to the delegator |

**Returns:** *Promise‹string›*

Promise for a base58 string of the unsigned transaction.

___

###  addNonDefaultSubnetValidator

▸ **addNonDefaultSubnetValidator**(`id`: string, `subnetID`: Buffer | string, `startTime`: Date, `endTime`: Date, `weight`: number, `payerNonce`: number): *Promise‹string›*

*Defined in [apis/platform/api.ts:233](https://github.com/ava-labs/avalanche.js/blob/4d26b45/src/apis/platform/api.ts#L233)*

Add a validator to a Subnet other than the Default Subnet. The validator must validate the Default Subnet for the entire duration they validate this Subnet.

**Parameters:**

Name | Type | Description |
------ | ------ | ------ |
`id` | string | The node ID of the validator |
`subnetID` | Buffer &#124; string | Either a [Buffer](https://github.com/feross/buffer) or an AVA serialized string for the SubnetID or its alias. |
`startTime` | Date | Javascript Date object for the start time to validate |
`endTime` | Date | Javascript Date object for the end time to validate |
`weight` | number | The validator’s weight used for sampling |
`payerNonce` | number | The next unused nonce of the account that is providing the staked AVA and paying the transaction fee  |

**Returns:** *Promise‹string›*

Promise for the unsigned transaction. It must be signed (using sign) by the proper number of the Subnet’s control keys and by the key of the account paying the transaction fee before it can be issued.

___

###  callMethod

▸ **callMethod**(`method`: string, `params?`: Array‹object› | object, `baseurl?`: string): *Promise‹[RequestResponseData](utils_types.requestresponsedata.md)›*

*Inherited from [JRPCAPI](utils_types.jrpcapi.md).[callMethod](utils_types.jrpcapi.md#callmethod)*

*Defined in [utils/types.ts:83](https://github.com/ava-labs/avalanche.js/blob/4d26b45/src/utils/types.ts#L83)*

**Parameters:**

Name | Type |
------ | ------ |
`method` | string |
`params?` | Array‹object› &#124; object |
`baseurl?` | string |

**Returns:** *Promise‹[RequestResponseData](utils_types.requestresponsedata.md)›*

___

###  createAccount

▸ **createAccount**(`username`: string, `password`: string, `privateKey`: Buffer | string): *Promise‹string›*

*Defined in [apis/platform/api.ts:78](https://github.com/ava-labs/avalanche.js/blob/4d26b45/src/apis/platform/api.ts#L78)*

The P-Chain uses an account model. This method creates a P-Chain account on an existing user in the Keystore.

**Parameters:**

Name | Type | Default | Description |
------ | ------ | ------ | ------ |
`username` | string | - | The username of the Keystore user that controls the new account |
`password` | string | - | The password of the Keystore user that controls the new account |
`privateKey` | Buffer &#124; string | undefined | The private key that controls the account. If omitted, a new private key is generated  |

**Returns:** *Promise‹string›*

Promise for a string of the newly created account address.

___

###  createBlockchain

▸ **createBlockchain**(`vmID`: string, `name`: string, `payerNonce`: number, `genesis`: string, `subnetID`: Buffer | string): *Promise‹string›*

*Defined in [apis/platform/api.ts:36](https://github.com/ava-labs/avalanche.js/blob/4d26b45/src/apis/platform/api.ts#L36)*

Creates a new blockchain.

**Parameters:**

Name | Type | Default | Description |
------ | ------ | ------ | ------ |
`vmID` | string | - | The ID of the Virtual Machine the blockchain runs. Can also be an alias of the Virtual Machine. |
`name` | string | - | A human-readable name for the new blockchain |
`payerNonce` | number | - | The next unused nonce of the account paying the transaction fee |
`genesis` | string | - | The base 58 (with checksum) representation of the genesis state of the new blockchain. Virtual Machines should have a static API method named buildGenesis that can be used to generate genesisData. |
`subnetID` | Buffer &#124; string | undefined | Optional. Either a [Buffer](https://github.com/feross/buffer) or an AVA serialized string for the SubnetID or its alias.  |

**Returns:** *Promise‹string›*

Promise for the unsigned transaction to create this blockchain. Must be signed by a sufficient number of the Subnet’s control keys and by the account paying the transaction fee.

___

###  createSubnet

▸ **createSubnet**(`controlKeys`: Array‹string›, `threshold`: number, `payerNonce`: number): *Promise‹string›*

*Defined in [apis/platform/api.ts:287](https://github.com/ava-labs/avalanche.js/blob/4d26b45/src/apis/platform/api.ts#L287)*

Create an unsigned transaction to create a new Subnet. The unsigned transaction must be signed with the key of the account paying the transaction fee. The Subnet’s ID is the ID of the transaction that creates it (ie the response from issueTx when issuing the signed transaction).

**Parameters:**

Name | Type | Description |
------ | ------ | ------ |
`controlKeys` | Array‹string› | Array of platform addresses as strings |
`threshold` | number | To add a validator to this Subnet, a transaction must have threshold signatures, where each signature is from a key whose address is an element of `controlKeys` |
`payerNonce` | number | The next unused nonce of the account providing the transaction fee  |

**Returns:** *Promise‹string›*

Promise for a string with the unsigned transaction encoded as base58.

___

###  exportAVA

▸ **exportAVA**(`amount`: BN, `to`: string, `payerNonce`: number): *Promise‹string›*

*Defined in [apis/platform/api.ts:356](https://github.com/ava-labs/avalanche.js/blob/4d26b45/src/apis/platform/api.ts#L356)*

Send AVA from an account on the P-Chain to an address on the X-Chain. This transaction must be signed with the key of the account that the AVA is sent from and which pays the transaction fee. After issuing this transaction, you must call the X-Chain’s importAVA method to complete the transfer.

**Parameters:**

Name | Type | Description |
------ | ------ | ------ |
`amount` | BN | Amount of AVA to export as a [BN](https://github.com/indutny/bn.js/) |
`to` | string | The address on the X-Chain to send the AVA to. Do not include X- in the address |
`payerNonce` | number | The next unused nonce of the account paying the tx fee and providing the sent AVA  |

**Returns:** *Promise‹string›*

Promise for an unsigned transaction to be signed by the account the the AVA is sent from and pays the transaction fee.

___

###  exportKey

▸ **exportKey**(`username`: string, `password`: string, `address`: string): *Promise‹string›*

*Defined in [apis/platform/api.ts:450](https://github.com/ava-labs/avalanche.js/blob/4d26b45/src/apis/platform/api.ts#L450)*

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

###  getAccount

▸ **getAccount**(`address`: string): *Promise‹object›*

*Defined in [apis/platform/api.ts:100](https://github.com/ava-labs/avalanche.js/blob/4d26b45/src/apis/platform/api.ts#L100)*

The P-Chain uses an account model. An account is identified by an address. This method returns the account with the given address.

**Parameters:**

Name | Type | Description |
------ | ------ | ------ |
`address` | string | The address of the account  |

**Returns:** *Promise‹object›*

Promise for an object containing the address, the nonce, and the balance.

___

###  getBaseURL

▸ **getBaseURL**(): *string*

*Inherited from [APIBase](utils_types.apibase.md).[getBaseURL](utils_types.apibase.md#getbaseurl)*

*Defined in [utils/types.ts:58](https://github.com/ava-labs/avalanche.js/blob/4d26b45/src/utils/types.ts#L58)*

Returns the baseurl's path.

**Returns:** *string*

___

###  getBlockchainStatus

▸ **getBlockchainStatus**(`blockchainID`: string): *Promise‹string›*

*Defined in [apis/platform/api.ts:60](https://github.com/ava-labs/avalanche.js/blob/4d26b45/src/apis/platform/api.ts#L60)*

Creates a new blockchain.

**Parameters:**

Name | Type | Description |
------ | ------ | ------ |
`blockchainID` | string | The blockchainID requesting a status update  |

**Returns:** *Promise‹string›*

Promise for a string of one of: "Validating", "Created", "Preferred", "Unknown".

___

###  getBlockchains

▸ **getBlockchains**(): *Promise‹Array‹object››*

*Defined in [apis/platform/api.ts:340](https://github.com/ava-labs/avalanche.js/blob/4d26b45/src/apis/platform/api.ts#L340)*

Get all the blockchains that exist (excluding the P-Chain).

**Returns:** *Promise‹Array‹object››*

Promise for an array of objects containing fields "id", "subnetID", and "vmID".

___

###  getCurrentValidators

▸ **getCurrentValidators**(`subnetID`: Buffer | string): *Promise‹Array‹object››*

*Defined in [apis/platform/api.ts:135](https://github.com/ava-labs/avalanche.js/blob/4d26b45/src/apis/platform/api.ts#L135)*

Lists the set of current validators.

**Parameters:**

Name | Type | Default | Description |
------ | ------ | ------ | ------ |
`subnetID` | Buffer &#124; string | undefined | Optional. Either a [Buffer](https://github.com/feross/buffer) or an AVA serialized string for the SubnetID or its alias.  |

**Returns:** *Promise‹Array‹object››*

Promise for an array of validators that are currently staking, see: [platform.getCurrentValidators documentation](https://docs.ava.network/v1.0/en/api/platform/#platformgetcurrentvalidators).

___

###  getDB

▸ **getDB**(): *StoreAPI*

*Inherited from [APIBase](utils_types.apibase.md).[getDB](utils_types.apibase.md#getdb)*

*Defined in [utils/types.ts:65](https://github.com/ava-labs/avalanche.js/blob/4d26b45/src/utils/types.ts#L65)*

Returns the baseurl's database.

**Returns:** *StoreAPI*

___

###  getPendingValidators

▸ **getPendingValidators**(`subnetID`: Buffer | string): *Promise‹Array‹object››*

*Defined in [apis/platform/api.ts:155](https://github.com/ava-labs/avalanche.js/blob/4d26b45/src/apis/platform/api.ts#L155)*

Lists the set of pending validators.

**Parameters:**

Name | Type | Default | Description |
------ | ------ | ------ | ------ |
`subnetID` | Buffer &#124; string | undefined | Optional. Either a [Buffer](https://github.com/feross/buffer) or an AVA serialized string for the SubnetID or its alias.  |

**Returns:** *Promise‹Array‹object››*

Promise for an array of validators that are pending staking, see: [platform.getPendingValidators documentation](https://docs.ava.network/v1.0/en/api/platform/#platformgetpendingvalidators).

___

###  getRPCID

▸ **getRPCID**(): *number*

*Inherited from [JRPCAPI](utils_types.jrpcapi.md).[getRPCID](utils_types.jrpcapi.md#getrpcid)*

*Defined in [utils/types.ts:125](https://github.com/ava-labs/avalanche.js/blob/4d26b45/src/utils/types.ts#L125)*

Returns the rpcid, a strictly-increasing number, starting from 1, indicating the next request ID that will be sent.

**Returns:** *number*

___

###  getSubnets

▸ **getSubnets**(): *Promise‹Array‹object››*

*Defined in [apis/platform/api.ts:434](https://github.com/ava-labs/avalanche.js/blob/4d26b45/src/apis/platform/api.ts#L434)*

Get all the subnets that exist.

**Returns:** *Promise‹Array‹object››*

Promise for an array of objects containing fields "id", "controlKeys", and "threshold".

___

###  importAVA

▸ **importAVA**(`username`: string, `password`: string, `to`: string, `payerNonce`: number): *Promise‹string›*

*Defined in [apis/platform/api.ts:377](https://github.com/ava-labs/avalanche.js/blob/4d26b45/src/apis/platform/api.ts#L377)*

Send AVA from an account on the P-Chain to an address on the X-Chain. This transaction must be signed with the key of the account that the AVA is sent from and which pays the transaction fee. After issuing this transaction, you must call the X-Chain’s importAVA method to complete the transfer.

**Parameters:**

Name | Type | Description |
------ | ------ | ------ |
`username` | string | The Keystore user that controls the account specified in `to` |
`password` | string | The password of the Keystore user |
`to` | string | The ID of the account the AVA is sent to. This must be the same as the to argument in the corresponding call to the X-Chain’s exportAVA |
`payerNonce` | number | The next unused nonce of the account specified in `to`  |

**Returns:** *Promise‹string›*

Promise for a string for the transaction, which should be sent to the network by calling issueTx.

___

###  importKey

▸ **importKey**(`username`: string, `password`: string, `privateKey`: string): *Promise‹string›*

*Defined in [apis/platform/api.ts:470](https://github.com/ava-labs/avalanche.js/blob/4d26b45/src/apis/platform/api.ts#L470)*

Give a user control over an address by providing the private key that controls the address.

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

▸ **issueTx**(`tx`: string): *Promise‹string›*

*Defined in [apis/platform/api.ts:420](https://github.com/ava-labs/avalanche.js/blob/4d26b45/src/apis/platform/api.ts#L420)*

Issue a transaction to the Platform Chain.

**Parameters:**

Name | Type | Description |
------ | ------ | ------ |
`tx` | string | The base 58 (with checksum) representation of a transaction  |

**Returns:** *Promise‹string›*

Promise for an string of the transaction after being signed.

___

###  listAccounts

▸ **listAccounts**(`username`: string, `password`: string): *Promise‹Array‹object››*

*Defined in [apis/platform/api.ts:117](https://github.com/ava-labs/avalanche.js/blob/4d26b45/src/apis/platform/api.ts#L117)*

List the accounts controlled by the user in the Keystore.

**Parameters:**

Name | Type | Description |
------ | ------ | ------ |
`username` | string | The username of the Keystore user |
`password` | string | The password of the Keystore user  |

**Returns:** *Promise‹Array‹object››*

Promise for an array of accounts.

___

###  sampleValidators

▸ **sampleValidators**(`sampleSize`: number, `subnetID`: Buffer | string): *Promise‹Array‹string››*

*Defined in [apis/platform/api.ts:176](https://github.com/ava-labs/avalanche.js/blob/4d26b45/src/apis/platform/api.ts#L176)*

Samples `Size` validators from the current validator set.

**Parameters:**

Name | Type | Default | Description |
------ | ------ | ------ | ------ |
`sampleSize` | number | - | Of the total universe of validators, select this many at random |
`subnetID` | Buffer &#124; string | undefined | Optional. Either a [Buffer](https://github.com/feross/buffer) or an AVA serialized string for the SubnetID or its alias.  |

**Returns:** *Promise‹Array‹string››*

Promise for an array of validator's stakingIDs.

___

###  setBaseURL

▸ **setBaseURL**(`baseurl`: string): *void*

*Inherited from [APIBase](utils_types.apibase.md).[setBaseURL](utils_types.apibase.md#setbaseurl)*

*Defined in [utils/types.ts:42](https://github.com/ava-labs/avalanche.js/blob/4d26b45/src/utils/types.ts#L42)*

Sets the path of the APIs baseurl.

**Parameters:**

Name | Type | Description |
------ | ------ | ------ |
`baseurl` | string | Path of the APIs baseurl - ex: "/ext/bc/avm"  |

**Returns:** *void*

___

###  sign

▸ **sign**(`username`: string, `password`: string, `tx`: string, `signer`: string): *Promise‹string›*

*Defined in [apis/platform/api.ts:401](https://github.com/ava-labs/avalanche.js/blob/4d26b45/src/apis/platform/api.ts#L401)*

Sign an unsigned or partially signed transaction.

Transactions to add non-default Subnets require signatures from control keys and from the account paying the transaction fee. If `signer` is a control key and the transaction needs more signatures from control keys, `sign` will provide a control signature. Otherwise, `signer` will sign to pay the transaction fee.

**Parameters:**

Name | Type | Description |
------ | ------ | ------ |
`username` | string | The Keystore user that controls the key signing `tx` |
`password` | string | The password of the Keystore user |
`tx` | string | The unsigned/partially signed transaction |
`signer` | string | The address of the key signing `tx`  |

**Returns:** *Promise‹string›*

Promise for an string of the transaction after being signed.

___

###  validatedBy

▸ **validatedBy**(`blockchainID`: string): *Promise‹string›*

*Defined in [apis/platform/api.ts:305](https://github.com/ava-labs/avalanche.js/blob/4d26b45/src/apis/platform/api.ts#L305)*

Get the Subnet that validates a given blockchain.

**Parameters:**

Name | Type | Description |
------ | ------ | ------ |
`blockchainID` | string | Either a [Buffer](https://github.com/feross/buffer) or an AVA serialized string for the blockchainID or its alias.  |

**Returns:** *Promise‹string›*

Promise for a string of the subnetID that validates the blockchain.

___

###  validates

▸ **validates**(`subnetID`: Buffer | string): *Promise‹Array‹string››*

*Defined in [apis/platform/api.ts:321](https://github.com/ava-labs/avalanche.js/blob/4d26b45/src/apis/platform/api.ts#L321)*

Get the IDs of the blockchains a Subnet validates.

**Parameters:**

Name | Type | Description |
------ | ------ | ------ |
`subnetID` | Buffer &#124; string | Either a [Buffer](https://github.com/feross/buffer) or an AVA serialized string for the SubnetID or its alias.  |

**Returns:** *Promise‹Array‹string››*

Promise for an array of blockchainIDs the subnet validates.
