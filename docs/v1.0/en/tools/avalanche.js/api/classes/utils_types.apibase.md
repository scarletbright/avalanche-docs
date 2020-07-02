[avalanche](../README.md) › [Utils-Types](../modules/utils_types.md) › [APIBase](utils_types.apibase.md)

# Class: APIBase

Abstract class defining a generic endpoint that all endpoints must implement (extend).

## Hierarchy

* **APIBase**

  ↳ [RESTAPI](utils_types.restapi.md)

  ↳ [JRPCAPI](utils_types.jrpcapi.md)

## Index

### Constructors

* [constructor](utils_types.apibase.md#constructor)

### Properties

* [baseurl](utils_types.apibase.md#protected-baseurl)
* [core](utils_types.apibase.md#protected-core)
* [db](utils_types.apibase.md#protected-db)

### Methods

* [getBaseURL](utils_types.apibase.md#getbaseurl)
* [getDB](utils_types.apibase.md#getdb)
* [setBaseURL](utils_types.apibase.md#setbaseurl)

## Constructors

###  constructor

\+ **new APIBase**(`core`: [AvalancheCore](avalanchecore.avalanchecore-1.md), `baseurl`: string): *[APIBase](utils_types.apibase.md)*

*Defined in [utils/types.ts:67](https://github.com/ava-labs/avalanche.js/blob/c723742/src/utils/types.ts#L67)*

**Parameters:**

Name | Type | Description |
------ | ------ | ------ |
`core` | [AvalancheCore](avalanchecore.avalanchecore-1.md) | Reference to the Avalanche instance using this baseurl |
`baseurl` | string | Path to the baseurl - ex: "/ext/bc/avm"  |

**Returns:** *[APIBase](utils_types.apibase.md)*

## Properties

### `Protected` baseurl

• **baseurl**: *string*

*Defined in [utils/types.ts:34](https://github.com/ava-labs/avalanche.js/blob/c723742/src/utils/types.ts#L34)*

___

### `Protected` core

• **core**: *[AvalancheCore](avalanchecore.avalanchecore-1.md)*

*Defined in [utils/types.ts:33](https://github.com/ava-labs/avalanche.js/blob/c723742/src/utils/types.ts#L33)*

___

### `Protected` db

• **db**: *StoreAPI*

*Defined in [utils/types.ts:35](https://github.com/ava-labs/avalanche.js/blob/c723742/src/utils/types.ts#L35)*

## Methods

###  getBaseURL

▸ **getBaseURL**(): *string*

*Defined in [utils/types.ts:58](https://github.com/ava-labs/avalanche.js/blob/c723742/src/utils/types.ts#L58)*

Returns the baseurl's path.

**Returns:** *string*

___

###  getDB

▸ **getDB**(): *StoreAPI*

*Defined in [utils/types.ts:65](https://github.com/ava-labs/avalanche.js/blob/c723742/src/utils/types.ts#L65)*

Returns the baseurl's database.

**Returns:** *StoreAPI*

___

###  setBaseURL

▸ **setBaseURL**(`baseurl`: string): *void*

*Defined in [utils/types.ts:42](https://github.com/ava-labs/avalanche.js/blob/c723742/src/utils/types.ts#L42)*

Sets the path of the APIs baseurl.

**Parameters:**

Name | Type | Description |
------ | ------ | ------ |
`baseurl` | string | Path of the APIs baseurl - ex: "/ext/bc/avm"  |

**Returns:** *void*
