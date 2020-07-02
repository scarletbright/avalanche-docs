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

*Defined in [utils/types.ts:322](https://github.com/ava-labs/avalanche.js/blob/c723742/src/utils/types.ts#L322)*

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

*Defined in [utils/types.ts:276](https://github.com/ava-labs/avalanche.js/blob/c723742/src/utils/types.ts#L276)*

___

### `Protected` rpcid

• **rpcid**: *number* = 1

*Defined in [utils/types.ts:277](https://github.com/ava-labs/avalanche.js/blob/c723742/src/utils/types.ts#L277)*

## Methods

###  callMethod

▸ **callMethod**(`method`: string, `params?`: Array‹object› | object, `baseurl?`: string): *Promise‹[RequestResponseData](utils_types.requestresponsedata.md)›*

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

###  getRPCID

▸ **getRPCID**(): *number*

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
