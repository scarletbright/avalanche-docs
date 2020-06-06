[slopes - v1.7.2](../README.md) › ["apis/platform/api"](../modules/_apis_platform_api_.md) › [PlatformAPI](_apis_platform_api_.platformapi.md)

# Class: PlatformAPI

Class for interacting with a node's PlatformAPI

**`remarks`** This extends the [JRPCAPI](_utils_types_.jrpcapi.md) class. This class should not be directly called. Instead, use the [Slopes.addAPI](_index_.slopes.md#addapi) function to register this interface with Slopes.

## Hierarchy

  ↳ [JRPCAPI](_utils_types_.jrpcapi.md)

  ↳ **PlatformAPI**

## Index

### Constructors

* [constructor](_apis_platform_api_.platformapi.md#constructor)

### Properties

* [baseurl](_apis_platform_api_.platformapi.md#protected-baseurl)
* [core](_apis_platform_api_.platformapi.md#protected-core)
* [db](_apis_platform_api_.platformapi.md#protected-db)
* [jrpcVersion](_apis_platform_api_.platformapi.md#protected-jrpcversion)
* [rpcid](_apis_platform_api_.platformapi.md#protected-rpcid)

### Methods

* [addDefaultSubnetDelegator](_apis_platform_api_.platformapi.md#adddefaultsubnetdelegator)
* [addDefaultSubnetValidator](_apis_platform_api_.platformapi.md#adddefaultsubnetvalidator)
* [addNonDefaultSubnetValidator](_apis_platform_api_.platformapi.md#addnondefaultsubnetvalidator)
* [callMethod](_apis_platform_api_.platformapi.md#callmethod)
* [createAccount](_apis_platform_api_.platformapi.md#createaccount)
* [createBlockchain](_apis_platform_api_.platformapi.md#createblockchain)
* [createSubnet](_apis_platform_api_.platformapi.md#createsubnet)
* [exportAVA](_apis_platform_api_.platformapi.md#exportava)
* [getAccount](_apis_platform_api_.platformapi.md#getaccount)
* [getBaseURL](_apis_platform_api_.platformapi.md#getbaseurl)
* [getBlockchainStatus](_apis_platform_api_.platformapi.md#getblockchainstatus)
* [getBlockchains](_apis_platform_api_.platformapi.md#getblockchains)
* [getCurrentValidators](_apis_platform_api_.platformapi.md#getcurrentvalidators)
* [getDB](_apis_platform_api_.platformapi.md#getdb)
* [getPendingValidators](_apis_platform_api_.platformapi.md#getpendingvalidators)
* [getRPCID](_apis_platform_api_.platformapi.md#getrpcid)
* [getSubnets](_apis_platform_api_.platformapi.md#getsubnets)
* [importAVA](_apis_platform_api_.platformapi.md#importava)
* [issueTx](_apis_platform_api_.platformapi.md#issuetx)
* [listAccounts](_apis_platform_api_.platformapi.md#listaccounts)
* [sampleValidators](_apis_platform_api_.platformapi.md#samplevalidators)
* [setBaseURL](_apis_platform_api_.platformapi.md#setbaseurl)
* [sign](_apis_platform_api_.platformapi.md#sign)
* [validatedBy](_apis_platform_api_.platformapi.md#validatedby)
* [validates](_apis_platform_api_.platformapi.md#validates)

## Constructors

###  constructor

\+ **new PlatformAPI**(`core`: [SlopesCore](_slopes_.slopescore.md), `baseurl`: string): *[PlatformAPI](_apis_platform_api_.platformapi.md)*

*Overrides [JRPCAPI](_utils_types_.jrpcapi.md).[constructor](_utils_types_.jrpcapi.md#constructor)*

*Defined in [apis/platform/api.ts:438](https://github.com/ava-labs/slopes/blob/65cee65/src/apis/platform/api.ts#L438)*

This class should not be instantiated directly. Instead use the [Slopes.addAPI](_index_.slopes.md#addapi) method.

**Parameters:**

Name | Type | Default | Description |
------ | ------ | ------ | ------ |
`core` | [SlopesCore](_slopes_.slopescore.md) | - | A reference to the Slopes class |
`baseurl` | string | "/ext/P" | Defaults to the string "/ext/P" as the path to blockchain's baseurl  |

**Returns:** *[PlatformAPI](_apis_platform_api_.platformapi.md)*

## Properties

### `Protected` baseurl

• **baseurl**: *string*

*Inherited from [APIBase](_utils_types_.apibase.md).[baseurl](_utils_types_.apibase.md#protected-baseurl)*

*Defined in [utils/types.ts:33](https://github.com/ava-labs/slopes/blob/65cee65/src/utils/types.ts#L33)*

___

### `Protected` core

• **core**: *[SlopesCore](_slopes_.slopescore.md)*

*Inherited from [APIBase](_utils_types_.apibase.md).[core](_utils_types_.apibase.md#protected-core)*

*Defined in [utils/types.ts:32](https://github.com/ava-labs/slopes/blob/65cee65/src/utils/types.ts#L32)*

___

### `Protected` db

• **db**: *StoreAPI*

*Inherited from [APIBase](_utils_types_.apibase.md).[db](_utils_types_.apibase.md#protected-db)*

*Defined in [utils/types.ts:34](https://github.com/ava-labs/slopes/blob/65cee65/src/utils/types.ts#L34)*

___

### `Protected` jrpcVersion

• **jrpcVersion**: *string* = "2.0"

*Inherited from [JRPCAPI](_utils_types_.jrpcapi.md).[jrpcVersion](_utils_types_.jrpcapi.md#protected-jrpcversion)*

*Defined in [utils/types.ts:80](https://github.com/ava-labs/slopes/blob/65cee65/src/utils/types.ts#L80)*

___

### `Protected` rpcid

• **rpcid**: *number* = 1

*Inherited from [JRPCAPI](_utils_types_.jrpcapi.md).[rpcid](_utils_types_.jrpcapi.md#protected-rpcid)*

*Defined in [utils/types.ts:81](https://github.com/ava-labs/slopes/blob/65cee65/src/utils/types.ts#L81)*

## Methods

###  addDefaultSubnetDelegator

▸ **addDefaultSubnetDelegator**(`id`: string, `startTime`: Date, `endTime`: Date, `stakeAmount`: BN, `payerNonce`: number, `destination`: string): *Promise‹string›*

*Defined in [apis/platform/api.ts:263](https://github.com/ava-labs/slopes/blob/65cee65/src/apis/platform/api.ts#L263)*

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

*Defined in [apis/platform/api.ts:203](https://github.com/ava-labs/slopes/blob/65cee65/src/apis/platform/api.ts#L203)*

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
`delegationFeeRate` | BN |  undefined | Optional. The percent fee this validator charges when others delegate stake to them, multiplied by 10,000 as a [BN](https://github.com/indutny/bn.js/). For example, suppose a validator has delegationFeeRate 300,000 and someone delegates to that validator. When the delegation period is over, if the delegator is entitled to a reward, 30% of the reward (300,000 / 10,000) goes to the validator and 70% goes to the delegator |

**Returns:** *Promise‹string›*

Promise for a base58 string of the unsigned transaction.

___

###  addNonDefaultSubnetValidator

▸ **addNonDefaultSubnetValidator**(`id`: string, `subnetID`: Buffer | string, `startTime`: Date, `endTime`: Date, `weight`: number, `payerNonce`: number): *Promise‹string›*

*Defined in [apis/platform/api.ts:232](https://github.com/ava-labs/slopes/blob/65cee65/src/apis/platform/api.ts#L232)*

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

▸ **callMethod**(`method`: string, `params?`: Array‹object› | object, `baseurl?`: string): *Promise‹[RequestResponseData](_utils_types_.requestresponsedata.md)›*

*Inherited from [JRPCAPI](_utils_types_.jrpcapi.md)*

*Defined in [utils/types.ts:82](https://github.com/ava-labs/slopes/blob/65cee65/src/utils/types.ts#L82)*

**Parameters:**

Name | Type |
------ | ------ |
`method` | string |
`params?` | Array‹object› &#124; object |
`baseurl?` | string |

**Returns:** *Promise‹[RequestResponseData](_utils_types_.requestresponsedata.md)›*

___

###  createAccount

▸ **createAccount**(`username`: string, `password`: string, `privateKey`: Buffer | string): *Promise‹string›*

*Defined in [apis/platform/api.ts:77](https://github.com/ava-labs/slopes/blob/65cee65/src/apis/platform/api.ts#L77)*

The P-Chain uses an account model. This method creates a P-Chain account on an existing user in the Keystore.

**Parameters:**

Name | Type | Default | Description |
------ | ------ | ------ | ------ |
`username` | string | - | The username of the Keystore user that controls the new account |
`password` | string | - | The password of the Keystore user that controls the new account |
`privateKey` | Buffer &#124; string |  undefined | The private key that controls the account. If omitted, a new private key is generated  |

**Returns:** *Promise‹string›*

Promise for a string of the newly created account address.

___

###  createBlockchain

▸ **createBlockchain**(`vmID`: string, `name`: string, `payerNonce`: number, `genesis`: string, `subnetID`: Buffer | string): *Promise‹string›*

*Defined in [apis/platform/api.ts:35](https://github.com/ava-labs/slopes/blob/65cee65/src/apis/platform/api.ts#L35)*

Creates a new blockchain.

**Parameters:**

Name | Type | Default | Description |
------ | ------ | ------ | ------ |
`vmID` | string | - | The ID of the Virtual Machine the blockchain runs. Can also be an alias of the Virtual Machine. |
`name` | string | - | A human-readable name for the new blockchain |
`payerNonce` | number | - | The next unused nonce of the account paying the transaction fee |
`genesis` | string | - | The base 58 (with checksum) representation of the genesis state of the new blockchain. Virtual Machines should have a static API method named buildGenesis that can be used to generate genesisData. |
`subnetID` | Buffer &#124; string |  undefined | Optional. Either a [Buffer](https://github.com/feross/buffer) or an AVA serialized string for the SubnetID or its alias.  |

**Returns:** *Promise‹string›*

Promise for the unsigned transaction to create this blockchain. Must be signed by a sufficient number of the Subnet’s control keys and by the account paying the transaction fee.

___

###  createSubnet

▸ **createSubnet**(`controlKeys`: Array‹string›, `threshold`: number, `payerNonce`: number): *Promise‹string›*

*Defined in [apis/platform/api.ts:286](https://github.com/ava-labs/slopes/blob/65cee65/src/apis/platform/api.ts#L286)*

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

*Defined in [apis/platform/api.ts:355](https://github.com/ava-labs/slopes/blob/65cee65/src/apis/platform/api.ts#L355)*

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

###  getAccount

▸ **getAccount**(`address`: string): *Promise‹object›*

*Defined in [apis/platform/api.ts:99](https://github.com/ava-labs/slopes/blob/65cee65/src/apis/platform/api.ts#L99)*

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

*Inherited from [APIBase](_utils_types_.apibase.md)*

*Defined in [utils/types.ts:57](https://github.com/ava-labs/slopes/blob/65cee65/src/utils/types.ts#L57)*

Returns the baseurl's path.

**Returns:** *string*

___

###  getBlockchainStatus

▸ **getBlockchainStatus**(`blockchainID`: string): *Promise‹string›*

*Defined in [apis/platform/api.ts:59](https://github.com/ava-labs/slopes/blob/65cee65/src/apis/platform/api.ts#L59)*

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

*Defined in [apis/platform/api.ts:339](https://github.com/ava-labs/slopes/blob/65cee65/src/apis/platform/api.ts#L339)*

Get all the blockchains that exist (excluding the P-Chain).

**Returns:** *Promise‹Array‹object››*

Promise for an array of objects containing fields "id", "subnetID", and "vmID".

___

###  getCurrentValidators

▸ **getCurrentValidators**(`subnetID`: Buffer | string): *Promise‹Array‹object››*

*Defined in [apis/platform/api.ts:134](https://github.com/ava-labs/slopes/blob/65cee65/src/apis/platform/api.ts#L134)*

Lists the set of current validators.

**Parameters:**

Name | Type | Default | Description |
------ | ------ | ------ | ------ |
`subnetID` | Buffer &#124; string |  undefined | Optional. Either a [Buffer](https://github.com/feross/buffer) or an AVA serialized string for the SubnetID or its alias.  |

**Returns:** *Promise‹Array‹object››*

Promise for an array of validators that are currently staking, see: [platform.getCurrentValidators documentation](https://docs.ava.network/v1.0/en/api/platform/#platformgetcurrentvalidators).

___

###  getDB

▸ **getDB**(): *StoreAPI*

*Inherited from [APIBase](_utils_types_.apibase.md)*

*Defined in [utils/types.ts:64](https://github.com/ava-labs/slopes/blob/65cee65/src/utils/types.ts#L64)*

Returns the baseurl's database.

**Returns:** *StoreAPI*

___

###  getPendingValidators

▸ **getPendingValidators**(`subnetID`: Buffer | string): *Promise‹Array‹object››*

*Defined in [apis/platform/api.ts:154](https://github.com/ava-labs/slopes/blob/65cee65/src/apis/platform/api.ts#L154)*

Lists the set of pending validators.

**Parameters:**

Name | Type | Default | Description |
------ | ------ | ------ | ------ |
`subnetID` | Buffer &#124; string |  undefined | Optional. Either a [Buffer](https://github.com/feross/buffer) or an AVA serialized string for the SubnetID or its alias.  |

**Returns:** *Promise‹Array‹object››*

Promise for an array of validators that are pending staking, see: [platform.getPendingValidators documentation](https://docs.ava.network/v1.0/en/api/platform/#platformgetpendingvalidators).

___

###  getRPCID

▸ **getRPCID**(): *number*

*Inherited from [JRPCAPI](_utils_types_.jrpcapi.md)*

*Defined in [utils/types.ts:124](https://github.com/ava-labs/slopes/blob/65cee65/src/utils/types.ts#L124)*

Returns the rpcid, a strictly-increasing number, starting from 1, indicating the next request ID that will be sent.

**Returns:** *number*

___

###  getSubnets

▸ **getSubnets**(): *Promise‹Array‹object››*

*Defined in [apis/platform/api.ts:433](https://github.com/ava-labs/slopes/blob/65cee65/src/apis/platform/api.ts#L433)*

Get all the subnets that exist.

**Returns:** *Promise‹Array‹object››*

Promise for an array of objects containing fields "id", "controlKeys", and "threshold".

___

###  importAVA

▸ **importAVA**(`username`: string, `password`: string, `to`: string, `payerNonce`: number): *Promise‹string›*

*Defined in [apis/platform/api.ts:376](https://github.com/ava-labs/slopes/blob/65cee65/src/apis/platform/api.ts#L376)*

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

###  issueTx

▸ **issueTx**(`tx`: string): *Promise‹string›*

*Defined in [apis/platform/api.ts:419](https://github.com/ava-labs/slopes/blob/65cee65/src/apis/platform/api.ts#L419)*

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

*Defined in [apis/platform/api.ts:116](https://github.com/ava-labs/slopes/blob/65cee65/src/apis/platform/api.ts#L116)*

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

*Defined in [apis/platform/api.ts:175](https://github.com/ava-labs/slopes/blob/65cee65/src/apis/platform/api.ts#L175)*

Samples `Size` validators from the current validator set.

**Parameters:**

Name | Type | Default | Description |
------ | ------ | ------ | ------ |
`sampleSize` | number | - | Of the total universe of validators, select this many at random |
`subnetID` | Buffer &#124; string |  undefined | Optional. Either a [Buffer](https://github.com/feross/buffer) or an AVA serialized string for the SubnetID or its alias.  |

**Returns:** *Promise‹Array‹string››*

Promise for an array of validator's stakingIDs.

___

###  setBaseURL

▸ **setBaseURL**(`baseurl`: string): *void*

*Inherited from [APIBase](_utils_types_.apibase.md)*

*Defined in [utils/types.ts:41](https://github.com/ava-labs/slopes/blob/65cee65/src/utils/types.ts#L41)*

Sets the path of the APIs baseurl.

**Parameters:**

Name | Type | Description |
------ | ------ | ------ |
`baseurl` | string | Path of the APIs baseurl - ex: "/ext/bc/avm"  |

**Returns:** *void*

___

###  sign

▸ **sign**(`username`: string, `password`: string, `tx`: string, `signer`: string): *Promise‹string›*

*Defined in [apis/platform/api.ts:400](https://github.com/ava-labs/slopes/blob/65cee65/src/apis/platform/api.ts#L400)*

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

*Defined in [apis/platform/api.ts:304](https://github.com/ava-labs/slopes/blob/65cee65/src/apis/platform/api.ts#L304)*

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

*Defined in [apis/platform/api.ts:320](https://github.com/ava-labs/slopes/blob/65cee65/src/apis/platform/api.ts#L320)*

Get the IDs of the blockchains a Subnet validates.

**Parameters:**

Name | Type | Description |
------ | ------ | ------ |
`subnetID` | Buffer &#124; string | Either a [Buffer](https://github.com/feross/buffer) or an AVA serialized string for the SubnetID or its alias.  |

**Returns:** *Promise‹Array‹string››*

Promise for an array of blockchainIDs the subnet validates.
