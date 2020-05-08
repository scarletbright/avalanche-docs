[slopes - v1.4.3](../README.md) › [Globals](../globals.md) › ["apis/platform/api"](../modules/_apis_platform_api_.md) › [PlatformAPI](_apis_platform_api_.platformapi.md)

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

* [addStaker](_apis_platform_api_.platformapi.md#addstaker)
* [callMethod](_apis_platform_api_.platformapi.md#callmethod)
* [createBlockchain](_apis_platform_api_.platformapi.md#createblockchain)
* [getBaseURL](_apis_platform_api_.platformapi.md#getbaseurl)
* [getBlockchainStatus](_apis_platform_api_.platformapi.md#getblockchainstatus)
* [getDB](_apis_platform_api_.platformapi.md#getdb)
* [getRPCID](_apis_platform_api_.platformapi.md#getrpcid)
* [listValidators](_apis_platform_api_.platformapi.md#listvalidators)
* [sampleValidators](_apis_platform_api_.platformapi.md#samplevalidators)
* [setBaseURL](_apis_platform_api_.platformapi.md#setbaseurl)

## Constructors

###  constructor

\+ **new PlatformAPI**(`core`: [SlopesCore](_slopes_.slopescore.md), `baseurl`: string): *[PlatformAPI](_apis_platform_api_.platformapi.md)*

*Overrides [JRPCAPI](_utils_types_.jrpcapi.md).[constructor](_utils_types_.jrpcapi.md#constructor)*

*Defined in [apis/platform/api.ts:95](https://github.com/ava-labs/slopes/blob/709e172/src/apis/platform/api.ts#L95)*

This class should not be instantiated directly. Instead use the [Slopes.addAPI](_index_.slopes.md#addapi) method.

**Parameters:**

Name | Type | Default | Description |
------ | ------ | ------ | ------ |
`core` | [SlopesCore](_slopes_.slopescore.md) | - | A reference to the Slopes class |
`baseurl` | string | "/ext/platform" | Defaults to the string "/ext/platform" as the path to blockchain's baseurl  |

**Returns:** *[PlatformAPI](_apis_platform_api_.platformapi.md)*

## Properties

### `Protected` baseurl

• **baseurl**: *string*

*Inherited from [APIBase](_utils_types_.apibase.md).[baseurl](_utils_types_.apibase.md#protected-baseurl)*

*Defined in [utils/types.ts:33](https://github.com/ava-labs/slopes/blob/709e172/src/utils/types.ts#L33)*

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

###  addStaker

▸ **addStaker**(`tx`: string): *Promise‹boolean›*

*Defined in [apis/platform/api.ts:23](https://github.com/ava-labs/slopes/blob/709e172/src/apis/platform/api.ts#L23)*

Add a staked validator to the validator set.

**Parameters:**

Name | Type | Description |
------ | ------ | ------ |
`tx` | string | The string representation of an AddStakerTx  |

**Returns:** *Promise‹boolean›*

Promise for a boolean value, true on success.

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

###  createBlockchain

▸ **createBlockchain**(`vmID`: string, `name`: string, `method`: string, `genesis`: object): *Promise‹string›*

*Defined in [apis/platform/api.ts:42](https://github.com/ava-labs/slopes/blob/709e172/src/apis/platform/api.ts#L42)*

Creates a new blockchain.

**Parameters:**

Name | Type | Description |
------ | ------ | ------ |
`vmID` | string | The VMID used to build the blockchain |
`name` | string | A human-readable name for the new blockchain |
`method` | string | The VMID's hook method for ingesting genesis data |
`genesis` | object | The object used to build the initial state of the blockchain  |

**Returns:** *Promise‹string›*

Promise for a string for the blockchainID.

___

###  getBaseURL

▸ **getBaseURL**(): *string*

*Inherited from [APIBase](_utils_types_.apibase.md)*

*Defined in [utils/types.ts:57](https://github.com/ava-labs/slopes/blob/709e172/src/utils/types.ts#L57)*

Returns the baseurl's path.

**Returns:** *string*

___

###  getBlockchainStatus

▸ **getBlockchainStatus**(`blockchainID`: string): *Promise‹string›*

*Defined in [apis/platform/api.ts:61](https://github.com/ava-labs/slopes/blob/709e172/src/apis/platform/api.ts#L61)*

Creates a new blockchain.

**Parameters:**

Name | Type | Description |
------ | ------ | ------ |
`blockchainID` | string | The blockchainID requesting a status update  |

**Returns:** *Promise‹string›*

Promise for a string of one of: "Validating", "Created", "Preferred", "Unknown".

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

###  listValidators

▸ **listValidators**(): *Promise‹Array‹string››*

*Defined in [apis/platform/api.ts:75](https://github.com/ava-labs/slopes/blob/709e172/src/apis/platform/api.ts#L75)*

Lists the current set of validators.

**Returns:** *Promise‹Array‹string››*

Promise for an array of validator's stakingIDs.

___

###  sampleValidators

▸ **sampleValidators**(`sampleSize`: number): *Promise‹Array‹string››*

*Defined in [apis/platform/api.ts:88](https://github.com/ava-labs/slopes/blob/709e172/src/apis/platform/api.ts#L88)*

Samples `Size` validators from the current validator set.

**Parameters:**

Name | Type | Description |
------ | ------ | ------ |
`sampleSize` | number | Of the total universe of validators, select this many at random  |

**Returns:** *Promise‹Array‹string››*

Promise for an array of validator's stakingIDs.

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
