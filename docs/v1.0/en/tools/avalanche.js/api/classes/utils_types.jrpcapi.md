[avalanche](../README.md) › [Utils-Types](../modules/utils_types.md) › [JRPCAPI](utils_types.jrpcapi.md)

# Class: JRPCAPI

## Hierarchy

* [APIBase](utils_types.apibase.md)

  ↳ **JRPCAPI**

  ↳ [AdminAPI](adminapi.adminapi-1.md)

  ↳ [AVMAPI](avmapi.avmapi-1.md)

  ↳ [HealthAPI](healthapi.healthapi-1.md)

  ↳ [InfoAPI](infoapi.infoapi-1.md)

  ↳ [KeystoreAPI](keystoreapi.keystoreapi-1.md)

  ↳ [PlatformAPI](platformapi.platformapi-1.md)

## Index

### Constructors

* [constructor](utils_types.jrpcapi.md#constructor)

### Properties

* [baseurl](utils_types.jrpcapi.md#protected-baseurl)
* [core](utils_types.jrpcapi.md#protected-core)
* [db](utils_types.jrpcapi.md#protected-db)
* [jrpcVersion](utils_types.jrpcapi.md#protected-jrpcversion)
* [rpcid](utils_types.jrpcapi.md#protected-rpcid)

### Methods

* [callMethod](utils_types.jrpcapi.md#callmethod)
* [getBaseURL](utils_types.jrpcapi.md#getbaseurl)
* [getDB](utils_types.jrpcapi.md#getdb)
* [getRPCID](utils_types.jrpcapi.md#getrpcid)
* [setBaseURL](utils_types.jrpcapi.md#setbaseurl)

## Constructors

###  constructor

\+ **new JRPCAPI**(`core`: [AvalancheCore](avalanchecore.avalanchecore-1.md), `baseurl`: string, `jrpcVersion`: string): *[JRPCAPI](utils_types.jrpcapi.md)*

*Overrides [APIBase](utils_types.apibase.md).[constructor](utils_types.apibase.md#constructor)*

*Defined in [src/utils/types.ts:340](https://github.com/ava-labs/avalanche.js/blob/eabcc2f/src/utils/types.ts#L340)*

**Parameters:**

Name | Type | Default | Description |
------ | ------ | ------ | ------ |
`core` | [AvalancheCore](avalanchecore.avalanchecore-1.md) | - | Reference to the Avalanche instance using this endpoint |
`baseurl` | string | - | Path of the APIs baseurl - ex: "/ext/bc/avm" |
`jrpcVersion` | string | "2.0" | The jrpc version to use, default "2.0".  |

**Returns:** *[JRPCAPI](utils_types.jrpcapi.md)*

## Properties

### `Protected` baseurl

• **baseurl**: *string*

*Inherited from [APIBase](utils_types.apibase.md).[baseurl](utils_types.apibase.md#protected-baseurl)*

*Defined in [src/utils/types.ts:39](https://github.com/ava-labs/avalanche.js/blob/eabcc2f/src/utils/types.ts#L39)*

___

### `Protected` core

• **core**: *[AvalancheCore](avalanchecore.avalanchecore-1.md)*

*Inherited from [APIBase](utils_types.apibase.md).[core](utils_types.apibase.md#protected-core)*

*Defined in [src/utils/types.ts:37](https://github.com/ava-labs/avalanche.js/blob/eabcc2f/src/utils/types.ts#L37)*

___

### `Protected` db

• **db**: *StoreAPI*

*Inherited from [APIBase](utils_types.apibase.md).[db](utils_types.apibase.md#protected-db)*

*Defined in [src/utils/types.ts:41](https://github.com/ava-labs/avalanche.js/blob/eabcc2f/src/utils/types.ts#L41)*

___

### `Protected` jrpcVersion

• **jrpcVersion**: *string* = "2.0"

*Defined in [src/utils/types.ts:291](https://github.com/ava-labs/avalanche.js/blob/eabcc2f/src/utils/types.ts#L291)*

___

### `Protected` rpcid

• **rpcid**: *number* = 1

*Defined in [src/utils/types.ts:293](https://github.com/ava-labs/avalanche.js/blob/eabcc2f/src/utils/types.ts#L293)*

## Methods

###  callMethod

▸ **callMethod**(`method`: string, `params?`: Array‹object› | object, `baseurl?`: string): *Promise‹[RequestResponseData](utils_types.requestresponsedata.md)›*

*Defined in [src/utils/types.ts:295](https://github.com/ava-labs/avalanche.js/blob/eabcc2f/src/utils/types.ts#L295)*

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

*Defined in [src/utils/types.ts:64](https://github.com/ava-labs/avalanche.js/blob/eabcc2f/src/utils/types.ts#L64)*

Returns the baseurl's path.

**Returns:** *string*

___

###  getDB

▸ **getDB**(): *StoreAPI*

*Inherited from [APIBase](utils_types.apibase.md).[getDB](utils_types.apibase.md#getdb)*

*Defined in [src/utils/types.ts:69](https://github.com/ava-labs/avalanche.js/blob/eabcc2f/src/utils/types.ts#L69)*

Returns the baseurl's database.

**Returns:** *StoreAPI*

___

###  getRPCID

▸ **getRPCID**(): *number*

*Defined in [src/utils/types.ts:340](https://github.com/ava-labs/avalanche.js/blob/eabcc2f/src/utils/types.ts#L340)*

Returns the rpcid, a strictly-increasing number, starting from 1, indicating the next
request ID that will be sent.

**Returns:** *number*

___

###  setBaseURL

▸ **setBaseURL**(`baseurl`: string): *void*

*Inherited from [APIBase](utils_types.apibase.md).[setBaseURL](utils_types.apibase.md#setbaseurl)*

*Defined in [src/utils/types.ts:48](https://github.com/ava-labs/avalanche.js/blob/eabcc2f/src/utils/types.ts#L48)*

Sets the path of the APIs baseurl.

**Parameters:**

Name | Type | Description |
------ | ------ | ------ |
`baseurl` | string | Path of the APIs baseurl - ex: "/ext/bc/avm"  |

**Returns:** *void*
