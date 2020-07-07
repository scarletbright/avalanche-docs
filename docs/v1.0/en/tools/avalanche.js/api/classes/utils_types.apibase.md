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

*Defined in [src/utils/types.ts:69](https://github.com/ava-labs/avalanche.js/blob/eabcc2f/src/utils/types.ts#L69)*

**Parameters:**

Name | Type | Description |
------ | ------ | ------ |
`core` | [AvalancheCore](avalanchecore.avalanchecore-1.md) | Reference to the Avalanche instance using this baseurl |
`baseurl` | string | Path to the baseurl - ex: "/ext/bc/avm"  |

**Returns:** *[APIBase](utils_types.apibase.md)*

## Properties

### `Protected` baseurl

• **baseurl**: *string*

*Defined in [src/utils/types.ts:39](https://github.com/ava-labs/avalanche.js/blob/eabcc2f/src/utils/types.ts#L39)*

___

### `Protected` core

• **core**: *[AvalancheCore](avalanchecore.avalanchecore-1.md)*

*Defined in [src/utils/types.ts:37](https://github.com/ava-labs/avalanche.js/blob/eabcc2f/src/utils/types.ts#L37)*

___

### `Protected` db

• **db**: *StoreAPI*

*Defined in [src/utils/types.ts:41](https://github.com/ava-labs/avalanche.js/blob/eabcc2f/src/utils/types.ts#L41)*

## Methods

###  getBaseURL

▸ **getBaseURL**(): *string*

*Defined in [src/utils/types.ts:64](https://github.com/ava-labs/avalanche.js/blob/eabcc2f/src/utils/types.ts#L64)*

Returns the baseurl's path.

**Returns:** *string*

___

###  getDB

▸ **getDB**(): *StoreAPI*

*Defined in [src/utils/types.ts:69](https://github.com/ava-labs/avalanche.js/blob/eabcc2f/src/utils/types.ts#L69)*

Returns the baseurl's database.

**Returns:** *StoreAPI*

___

###  setBaseURL

▸ **setBaseURL**(`baseurl`: string): *void*

*Defined in [src/utils/types.ts:48](https://github.com/ava-labs/avalanche.js/blob/eabcc2f/src/utils/types.ts#L48)*

Sets the path of the APIs baseurl.

**Parameters:**

Name | Type | Description |
------ | ------ | ------ |
`baseurl` | string | Path of the APIs baseurl - ex: "/ext/bc/avm"  |

**Returns:** *void*
