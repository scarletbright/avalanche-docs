[slopes - v1.7.2](../README.md) › ["utils/types"](../modules/_utils_types_.md) › [APIBase](_utils_types_.apibase.md)

# Class: APIBase

Abstract class defining a generic endpoint that all endpoints must implement (extend).

## Hierarchy

* **APIBase**

  ↳ [JRPCAPI](_utils_types_.jrpcapi.md)

## Index

### Constructors

* [constructor](_utils_types_.apibase.md#constructor)

### Properties

* [baseurl](_utils_types_.apibase.md#protected-baseurl)
* [core](_utils_types_.apibase.md#protected-core)
* [db](_utils_types_.apibase.md#protected-db)

### Methods

* [getBaseURL](_utils_types_.apibase.md#getbaseurl)
* [getDB](_utils_types_.apibase.md#getdb)
* [setBaseURL](_utils_types_.apibase.md#setbaseurl)

## Constructors

###  constructor

\+ **new APIBase**(`core`: [SlopesCore](_slopes_.slopescore.md), `baseurl`: string): *[APIBase](_utils_types_.apibase.md)*

*Defined in [utils/types.ts:66](https://github.com/ava-labs/slopes/blob/ba50532/src/utils/types.ts#L66)*

**Parameters:**

Name | Type | Description |
------ | ------ | ------ |
`core` | [SlopesCore](_slopes_.slopescore.md) | Reference to the Slopes instance using this baseurl |
`baseurl` | string | Path to the baseurl - ex: "/ext/bc/avm"  |

**Returns:** *[APIBase](_utils_types_.apibase.md)*

## Properties

### `Protected` baseurl

• **baseurl**: *string*

*Defined in [utils/types.ts:33](https://github.com/ava-labs/slopes/blob/ba50532/src/utils/types.ts#L33)*

___

### `Protected` core

• **core**: *[SlopesCore](_slopes_.slopescore.md)*

*Defined in [utils/types.ts:32](https://github.com/ava-labs/slopes/blob/ba50532/src/utils/types.ts#L32)*

___

### `Protected` db

• **db**: *StoreAPI*

*Defined in [utils/types.ts:34](https://github.com/ava-labs/slopes/blob/ba50532/src/utils/types.ts#L34)*

## Methods

###  getBaseURL

▸ **getBaseURL**(): *string*

*Defined in [utils/types.ts:57](https://github.com/ava-labs/slopes/blob/ba50532/src/utils/types.ts#L57)*

Returns the baseurl's path.

**Returns:** *string*

___

###  getDB

▸ **getDB**(): *StoreAPI*

*Defined in [utils/types.ts:64](https://github.com/ava-labs/slopes/blob/ba50532/src/utils/types.ts#L64)*

Returns the baseurl's database.

**Returns:** *StoreAPI*

___

###  setBaseURL

▸ **setBaseURL**(`baseurl`: string): *void*

*Defined in [utils/types.ts:41](https://github.com/ava-labs/slopes/blob/ba50532/src/utils/types.ts#L41)*

Sets the path of the APIs baseurl.

**Parameters:**

Name | Type | Description |
------ | ------ | ------ |
`baseurl` | string | Path of the APIs baseurl - ex: "/ext/bc/avm"  |

**Returns:** *void*
