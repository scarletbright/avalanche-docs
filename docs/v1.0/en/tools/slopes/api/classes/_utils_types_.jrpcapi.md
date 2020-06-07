[slopes - v1.7.3](../README.md) › ["utils/types"](../modules/_utils_types_.md) › [JRPCAPI](_utils_types_.jrpcapi.md)

# Class: JRPCAPI

## Hierarchy

* [APIBase](_utils_types_.apibase.md)

  ↳ **JRPCAPI**

  ↳ [AdminAPI](_apis_admin_api_.adminapi.md)

  ↳ [AVMAPI](_apis_avm_api_.avmapi.md)

  ↳ [HealthAPI](_apis_health_api_.healthapi.md)

  ↳ [KeystoreAPI](_apis_keystore_api_.keystoreapi.md)

  ↳ [PlatformAPI](_apis_platform_api_.platformapi.md)

## Index

### Constructors

* [constructor](_utils_types_.jrpcapi.md#constructor)

### Properties

* [baseurl](_utils_types_.jrpcapi.md#protected-baseurl)
* [core](_utils_types_.jrpcapi.md#protected-core)
* [db](_utils_types_.jrpcapi.md#protected-db)
* [jrpcVersion](_utils_types_.jrpcapi.md#protected-jrpcversion)
* [rpcid](_utils_types_.jrpcapi.md#protected-rpcid)

### Methods

* [callMethod](_utils_types_.jrpcapi.md#callmethod)
* [getBaseURL](_utils_types_.jrpcapi.md#getbaseurl)
* [getDB](_utils_types_.jrpcapi.md#getdb)
* [getRPCID](_utils_types_.jrpcapi.md#getrpcid)
* [setBaseURL](_utils_types_.jrpcapi.md#setbaseurl)

## Constructors

###  constructor

\+ **new JRPCAPI**(`core`: [SlopesCore](_slopes_.slopescore.md), `baseurl`: string, `jrpcVersion`: string): *[JRPCAPI](_utils_types_.jrpcapi.md)*

*Overrides [APIBase](_utils_types_.apibase.md).[constructor](_utils_types_.apibase.md#constructor)*

*Defined in [utils/types.ts:126](https://github.com/ava-labs/slopes/blob/51a37ef/src/utils/types.ts#L126)*

**Parameters:**

Name | Type | Default | Description |
------ | ------ | ------ | ------ |
`core` | [SlopesCore](_slopes_.slopescore.md) | - | Reference to the Slopes instance using this endpoint |
`baseurl` | string | - | Path of the APIs baseurl - ex: "/ext/bc/avm" |
`jrpcVersion` | string | "2.0" | The jrpc version to use, default "2.0".  |

**Returns:** *[JRPCAPI](_utils_types_.jrpcapi.md)*

## Properties

### `Protected` baseurl

• **baseurl**: *string*

*Inherited from [APIBase](_utils_types_.apibase.md).[baseurl](_utils_types_.apibase.md#protected-baseurl)*

*Defined in [utils/types.ts:33](https://github.com/ava-labs/slopes/blob/51a37ef/src/utils/types.ts#L33)*

___

### `Protected` core

• **core**: *[SlopesCore](_slopes_.slopescore.md)*

*Inherited from [APIBase](_utils_types_.apibase.md).[core](_utils_types_.apibase.md#protected-core)*

*Defined in [utils/types.ts:32](https://github.com/ava-labs/slopes/blob/51a37ef/src/utils/types.ts#L32)*

___

### `Protected` db

• **db**: *StoreAPI*

*Inherited from [APIBase](_utils_types_.apibase.md).[db](_utils_types_.apibase.md#protected-db)*

*Defined in [utils/types.ts:34](https://github.com/ava-labs/slopes/blob/51a37ef/src/utils/types.ts#L34)*

___

### `Protected` jrpcVersion

• **jrpcVersion**: *string* = "2.0"

*Defined in [utils/types.ts:80](https://github.com/ava-labs/slopes/blob/51a37ef/src/utils/types.ts#L80)*

___

### `Protected` rpcid

• **rpcid**: *number* = 1

*Defined in [utils/types.ts:81](https://github.com/ava-labs/slopes/blob/51a37ef/src/utils/types.ts#L81)*

## Methods

###  callMethod

▸ **callMethod**(`method`: string, `params?`: Array‹object› | object, `baseurl?`: string): *Promise‹[RequestResponseData](_utils_types_.requestresponsedata.md)›*

*Defined in [utils/types.ts:82](https://github.com/ava-labs/slopes/blob/51a37ef/src/utils/types.ts#L82)*

**Parameters:**

Name | Type |
------ | ------ |
`method` | string |
`params?` | Array‹object› &#124; object |
`baseurl?` | string |

**Returns:** *Promise‹[RequestResponseData](_utils_types_.requestresponsedata.md)›*

___

###  getBaseURL

▸ **getBaseURL**(): *string*

*Inherited from [APIBase](_utils_types_.apibase.md)*

*Defined in [utils/types.ts:57](https://github.com/ava-labs/slopes/blob/51a37ef/src/utils/types.ts#L57)*

Returns the baseurl's path.

**Returns:** *string*

___

###  getDB

▸ **getDB**(): *StoreAPI*

*Inherited from [APIBase](_utils_types_.apibase.md)*

*Defined in [utils/types.ts:64](https://github.com/ava-labs/slopes/blob/51a37ef/src/utils/types.ts#L64)*

Returns the baseurl's database.

**Returns:** *StoreAPI*

___

###  getRPCID

▸ **getRPCID**(): *number*

*Defined in [utils/types.ts:124](https://github.com/ava-labs/slopes/blob/51a37ef/src/utils/types.ts#L124)*

Returns the rpcid, a strictly-increasing number, starting from 1, indicating the next request ID that will be sent.

**Returns:** *number*

___

###  setBaseURL

▸ **setBaseURL**(`baseurl`: string): *void*

*Inherited from [APIBase](_utils_types_.apibase.md)*

*Defined in [utils/types.ts:41](https://github.com/ava-labs/slopes/blob/51a37ef/src/utils/types.ts#L41)*

Sets the path of the APIs baseurl.

**Parameters:**

Name | Type | Description |
------ | ------ | ------ |
`baseurl` | string | Path of the APIs baseurl - ex: "/ext/bc/avm"  |

**Returns:** *void*
