[avalanche](../README.md) › [HealthAPI](../modules/healthapi.md) › [HealthAPI](healthapi.healthapi-1.md)

# Class: HealthAPI

Class for interacting with a node API that is using the node's HealthApi.

**`remarks`** This extends the [JRPCAPI](utils_types.jrpcapi.md) class. This class should not be directly called. Instead, use the [Avalanche.addAPI](avalanche.avalanche-1.md#addapi) function to register this interface with Avalanche.

## Hierarchy

  ↳ [JRPCAPI](utils_types.jrpcapi.md)

  ↳ **HealthAPI**

## Index

### Constructors

* [constructor](healthapi.healthapi-1.md#constructor)

### Properties

* [baseurl](healthapi.healthapi-1.md#protected-baseurl)
* [core](healthapi.healthapi-1.md#protected-core)
* [db](healthapi.healthapi-1.md#protected-db)
* [jrpcVersion](healthapi.healthapi-1.md#protected-jrpcversion)
* [rpcid](healthapi.healthapi-1.md#protected-rpcid)

### Methods

* [callMethod](healthapi.healthapi-1.md#callmethod)
* [getBaseURL](healthapi.healthapi-1.md#getbaseurl)
* [getDB](healthapi.healthapi-1.md#getdb)
* [getLiveness](healthapi.healthapi-1.md#getliveness)
* [getRPCID](healthapi.healthapi-1.md#getrpcid)
* [setBaseURL](healthapi.healthapi-1.md#setbaseurl)

## Constructors

###  constructor

\+ **new HealthAPI**(`core`: [AvalancheCore](avalanchecore.avalanchecore-1.md), `baseurl`: string): *[HealthAPI](healthapi.healthapi-1.md)*

*Overrides [JRPCAPI](utils_types.jrpcapi.md).[constructor](utils_types.jrpcapi.md#constructor)*

*Defined in [apis/health/api.ts:25](https://github.com/ava-labs/avalanche.js/blob/c723742/src/apis/health/api.ts#L25)*

This class should not be instantiated directly. Instead use the [Avalanche.addAPI](avalanche.avalanche-1.md#addapi) method.

**Parameters:**

Name | Type | Default | Description |
------ | ------ | ------ | ------ |
`core` | [AvalancheCore](avalanchecore.avalanchecore-1.md) | - | A reference to the Avalanche class |
`baseurl` | string | "/ext/health" | Defaults to the string "/ext/health" as the path to blockchain's baseurl  |

**Returns:** *[HealthAPI](healthapi.healthapi-1.md)*

## Properties

### `Protected` baseurl

• **baseurl**: *string*

*Inherited from [APIBase](utils_types.apibase.md).[baseurl](utils_types.apibase.md#protected-baseurl)*

*Defined in [utils/types.ts:34](https://github.com/ava-labs/avalanche.js/blob/c723742/src/utils/types.ts#L34)*

___

### `Protected` core

• **core**: *[AvalancheCore](avalanchecore.avalanchecore-1.md)*

*Inherited from [APIBase](utils_types.apibase.md).[core](utils_types.apibase.md#protected-core)*

*Defined in [utils/types.ts:33](https://github.com/ava-labs/avalanche.js/blob/c723742/src/utils/types.ts#L33)*

___

### `Protected` db

• **db**: *StoreAPI*

*Inherited from [APIBase](utils_types.apibase.md).[db](utils_types.apibase.md#protected-db)*

*Defined in [utils/types.ts:35](https://github.com/ava-labs/avalanche.js/blob/c723742/src/utils/types.ts#L35)*

___

### `Protected` jrpcVersion

• **jrpcVersion**: *string* = "2.0"

*Inherited from [JRPCAPI](utils_types.jrpcapi.md).[jrpcVersion](utils_types.jrpcapi.md#protected-jrpcversion)*

*Defined in [utils/types.ts:276](https://github.com/ava-labs/avalanche.js/blob/c723742/src/utils/types.ts#L276)*

___

### `Protected` rpcid

• **rpcid**: *number* = 1

*Inherited from [JRPCAPI](utils_types.jrpcapi.md).[rpcid](utils_types.jrpcapi.md#protected-rpcid)*

*Defined in [utils/types.ts:277](https://github.com/ava-labs/avalanche.js/blob/c723742/src/utils/types.ts#L277)*

## Methods

###  callMethod

▸ **callMethod**(`method`: string, `params?`: Array‹object› | object, `baseurl?`: string): *Promise‹[RequestResponseData](utils_types.requestresponsedata.md)›*

*Inherited from [JRPCAPI](utils_types.jrpcapi.md).[callMethod](utils_types.jrpcapi.md#callmethod)*

*Defined in [utils/types.ts:278](https://github.com/ava-labs/avalanche.js/blob/c723742/src/utils/types.ts#L278)*

**Parameters:**

Name | Type |
------ | ------ |
`method` | string |
`params?` | Array‹object› &#124; object |
`baseurl?` | string |

**Returns:** *Promise‹[RequestResponseData](utils_types.requestresponsedata.md)›*

___

###  getBaseURL

▸ **getBaseURL**(): *string*

*Inherited from [APIBase](utils_types.apibase.md).[getBaseURL](utils_types.apibase.md#getbaseurl)*

*Defined in [utils/types.ts:58](https://github.com/ava-labs/avalanche.js/blob/c723742/src/utils/types.ts#L58)*

Returns the baseurl's path.

**Returns:** *string*

___

###  getDB

▸ **getDB**(): *StoreAPI*

*Inherited from [APIBase](utils_types.apibase.md).[getDB](utils_types.apibase.md#getdb)*

*Defined in [utils/types.ts:65](https://github.com/ava-labs/avalanche.js/blob/c723742/src/utils/types.ts#L65)*

Returns the baseurl's database.

**Returns:** *StoreAPI*

___

###  getLiveness

▸ **getLiveness**(): *Promise‹object›*

*Defined in [apis/health/api.ts:21](https://github.com/ava-labs/avalanche.js/blob/c723742/src/apis/health/api.ts#L21)*

**Returns:** *Promise‹object›*

Promise for an object containing the health check response

___

###  getRPCID

▸ **getRPCID**(): *number*

*Inherited from [JRPCAPI](utils_types.jrpcapi.md).[getRPCID](utils_types.jrpcapi.md#getrpcid)*

*Defined in [utils/types.ts:320](https://github.com/ava-labs/avalanche.js/blob/c723742/src/utils/types.ts#L320)*

Returns the rpcid, a strictly-increasing number, starting from 1, indicating the next request ID that will be sent.

**Returns:** *number*

___

###  setBaseURL

▸ **setBaseURL**(`baseurl`: string): *void*

*Inherited from [APIBase](utils_types.apibase.md).[setBaseURL](utils_types.apibase.md#setbaseurl)*

*Defined in [utils/types.ts:42](https://github.com/ava-labs/avalanche.js/blob/c723742/src/utils/types.ts#L42)*

Sets the path of the APIs baseurl.

**Parameters:**

Name | Type | Description |
------ | ------ | ------ |
`baseurl` | string | Path of the APIs baseurl - ex: "/ext/bc/avm"  |

**Returns:** *void*
