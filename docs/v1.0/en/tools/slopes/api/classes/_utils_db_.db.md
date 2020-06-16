[slopes - v1.7.5](../README.md) › ["utils/db"](../modules/_utils_db_.md) › [DB](_utils_db_.db.md)

# Class: DB

A class for interacting with the [ store2 module](https://github.com/nbubna/store)

This class should never be instantiated directly. Instead, invoke the "DB.getInstance()" static
function to grab the singleton instance of the database.

```js
const db = DB.getInstance();
const blockchaindb = db.getNamespace("mychain");
```

## Hierarchy

* **DB**

## Index

### Constructors

* [constructor](_utils_db_.db.md#private-constructor)

### Properties

* [instance](_utils_db_.db.md#static-private-instance)
* [store](_utils_db_.db.md#static-private-store)

### Methods

* [getInstance](_utils_db_.db.md#static-getinstance)
* [getNamespace](_utils_db_.db.md#static-getnamespace)

## Constructors

### `Private` constructor

\+ **new DB**(): *[DB](_utils_db_.db.md)*

*Defined in [utils/db.ts:20](https://github.com/ava-labs/slopes/blob/be20cee/src/utils/db.ts#L20)*

**Returns:** *[DB](_utils_db_.db.md)*

## Properties

### `Static` `Private` instance

▪ **instance**: *[DB](_utils_db_.db.md)*

*Defined in [utils/db.ts:19](https://github.com/ava-labs/slopes/blob/be20cee/src/utils/db.ts#L19)*

___

### `Static` `Private` store

▪ **store**: *store* =  store

*Defined in [utils/db.ts:20](https://github.com/ava-labs/slopes/blob/be20cee/src/utils/db.ts#L20)*

## Methods

### `Static` getInstance

▸ **getInstance**(): *[DB](_utils_db_.db.md)*

*Defined in [utils/db.ts:26](https://github.com/ava-labs/slopes/blob/be20cee/src/utils/db.ts#L26)*

Retrieves the database singleton.

**Returns:** *[DB](_utils_db_.db.md)*

___

### `Static` getNamespace

▸ **getNamespace**(`ns`: string): *StoreAPI*

*Defined in [utils/db.ts:38](https://github.com/ava-labs/slopes/blob/be20cee/src/utils/db.ts#L38)*

Gets a namespace from the database singleton.

**Parameters:**

Name | Type | Description |
------ | ------ | ------ |
`ns` | string | Namespace to retrieve.  |

**Returns:** *StoreAPI*
