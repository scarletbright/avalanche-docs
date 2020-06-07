[slopes - v1.7.3](../README.md) › ["apis/health/api"](../modules/_apis_health_api_.md) › [HealthAPI](_apis_health_api_.healthapi.md)

# Class: HealthAPI

Class for interacting with a node API that is using the node's HealthApi.

**`remarks`** This extends the [JRPCAPI](_utils_types_.jrpcapi.md) class. This class should not be directly called. Instead, use the [Slopes.addAPI](_index_.slopes.md#addapi) function to register this interface with Slopes.

## Hierarchy

  ↳ [JRPCAPI](_utils_types_.jrpcapi.md)

  ↳ **HealthAPI**

## Index

### Constructors

* [constructor](_apis_health_api_.healthapi.md#constructor)

### Properties

* [baseurl](_apis_health_api_.healthapi.md#protected-baseurl)
* [core](_apis_health_api_.healthapi.md#protected-core)
* [db](_apis_health_api_.healthapi.md#protected-db)
* [jrpcVersion](_apis_health_api_.healthapi.md#protected-jrpcversion)
* [rpcid](_apis_health_api_.healthapi.md#protected-rpcid)

### Methods

* [callMethod](_apis_health_api_.healthapi.md#callmethod)
* [getBaseURL](_apis_health_api_.healthapi.md#getbaseurl)
* [getDB](_apis_health_api_.healthapi.md#getdb)
* [getLiveness](_apis_health_api_.healthapi.md#getliveness)
* [getRPCID](_apis_health_api_.healthapi.md#getrpcid)
* [setBaseURL](_apis_health_api_.healthapi.md#setbaseurl)

## Constructors

###  constructor

\+ **new HealthAPI**(`core`: [SlopesCore](_slopes_.slopescore.md), `baseurl`: string): *[HealthAPI](_apis_health_api_.healthapi.md)*

*Overrides [JRPCAPI](_utils_types_.jrpcapi.md).[constructor](_utils_types_.jrpcapi.md#constructor)*

*Defined in [apis/health/api.ts:24](https://github.com/ava-labs/slopes/blob/51a37ef/src/apis/health/api.ts#L24)*

This class should not be instantiated directly. Instead use the [Slopes.addAPI](_index_.slopes.md#addapi) method.

**Parameters:**

Name | Type | Default | Description |
------ | ------ | ------ | ------ |
`core` | [SlopesCore](_slopes_.slopescore.md) | - | A reference to the Slopes class |
`baseurl` | string | "/ext/health" | Defaults to the string "/ext/health" as the path to blockchain's baseurl  |

**Returns:** *[HealthAPI](_apis_health_api_.healthapi.md)*

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

*Inherited from [JRPCAPI](_utils_types_.jrpcapi.md).[jrpcVersion](_utils_types_.jrpcapi.md#protected-jrpcversion)*

*Defined in [utils/types.ts:80](https://github.com/ava-labs/slopes/blob/51a37ef/src/utils/types.ts#L80)*

___

### `Protected` rpcid

• **rpcid**: *number* = 1

*Inherited from [JRPCAPI](_utils_types_.jrpcapi.md).[rpcid](_utils_types_.jrpcapi.md#protected-rpcid)*

*Defined in [utils/types.ts:81](https://github.com/ava-labs/slopes/blob/51a37ef/src/utils/types.ts#L81)*

## Methods

###  callMethod

▸ **callMethod**(`method`: string, `params?`: Array‹object› | object, `baseurl?`: string): *Promise‹[RequestResponseData](_utils_types_.requestresponsedata.md)›*

*Inherited from [JRPCAPI](_utils_types_.jrpcapi.md)*

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

###  getLiveness

▸ **getLiveness**(): *Promise‹object›*

*Defined in [apis/health/api.ts:20](https://github.com/ava-labs/slopes/blob/51a37ef/src/apis/health/api.ts#L20)*

**Returns:** *Promise‹object›*

Promise for an object containing the health check response

___

###  getRPCID

▸ **getRPCID**(): *number*

*Inherited from [JRPCAPI](_utils_types_.jrpcapi.md)*

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
