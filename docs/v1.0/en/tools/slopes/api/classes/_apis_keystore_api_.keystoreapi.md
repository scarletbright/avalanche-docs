[slopes - v1.7.2](../README.md) › ["apis/keystore/api"](../modules/_apis_keystore_api_.md) › [KeystoreAPI](_apis_keystore_api_.keystoreapi.md)

# Class: KeystoreAPI

Class for interacting with a node API that is using the node's KeystoreAPI.

**WARNING**: The KeystoreAPI is to be used by the node-owner as the data is stored locally on the node. Do not trust the root user. If you are not the node-owner, do not use this as your wallet.

**`remarks`** This extends the [JRPCAPI](_utils_types_.jrpcapi.md) class. This class should not be directly called. Instead, use the [Slopes.addAPI](_index_.slopes.md#addapi) function to register this interface with Slopes.

## Hierarchy

  ↳ [JRPCAPI](_utils_types_.jrpcapi.md)

  ↳ **KeystoreAPI**

## Index

### Constructors

* [constructor](_apis_keystore_api_.keystoreapi.md#constructor)

### Properties

* [baseurl](_apis_keystore_api_.keystoreapi.md#protected-baseurl)
* [core](_apis_keystore_api_.keystoreapi.md#protected-core)
* [db](_apis_keystore_api_.keystoreapi.md#protected-db)
* [jrpcVersion](_apis_keystore_api_.keystoreapi.md#protected-jrpcversion)
* [rpcid](_apis_keystore_api_.keystoreapi.md#protected-rpcid)

### Methods

* [callMethod](_apis_keystore_api_.keystoreapi.md#callmethod)
* [createUser](_apis_keystore_api_.keystoreapi.md#createuser)
* [deleteUser](_apis_keystore_api_.keystoreapi.md#deleteuser)
* [exportUser](_apis_keystore_api_.keystoreapi.md#exportuser)
* [getBaseURL](_apis_keystore_api_.keystoreapi.md#getbaseurl)
* [getDB](_apis_keystore_api_.keystoreapi.md#getdb)
* [getRPCID](_apis_keystore_api_.keystoreapi.md#getrpcid)
* [importUser](_apis_keystore_api_.keystoreapi.md#importuser)
* [listUsers](_apis_keystore_api_.keystoreapi.md#listusers)
* [setBaseURL](_apis_keystore_api_.keystoreapi.md#setbaseurl)

## Constructors

###  constructor

\+ **new KeystoreAPI**(`core`: [SlopesCore](_slopes_.slopescore.md), `baseurl`: string): *[KeystoreAPI](_apis_keystore_api_.keystoreapi.md)*

*Overrides [JRPCAPI](_utils_types_.jrpcapi.md).[constructor](_utils_types_.jrpcapi.md#constructor)*

*Defined in [apis/keystore/api.ts:101](https://github.com/ava-labs/slopes/blob/65cee65/src/apis/keystore/api.ts#L101)*

This class should not be instantiated directly. Instead use the [Slopes.addAPI](_index_.slopes.md#addapi) method.

**Parameters:**

Name | Type | Default | Description |
------ | ------ | ------ | ------ |
`core` | [SlopesCore](_slopes_.slopescore.md) | - | A reference to the Slopes class |
`baseurl` | string | "/ext/keystore" | Defaults to the string "/ext/keystore" as the path to blockchain's baseurl  |

**Returns:** *[KeystoreAPI](_apis_keystore_api_.keystoreapi.md)*

## Properties

### `Protected` baseurl

• **baseurl**: *string*

*Inherited from [APIBase](_utils_types_.apibase.md).[baseurl](_utils_types_.apibase.md#protected-baseurl)*

*Defined in [utils/types.ts:33](https://github.com/ava-labs/slopes/blob/65cee65/src/utils/types.ts#L33)*

___

### `Protected` core

• **core**: *[SlopesCore](_slopes_.slopescore.md)*

*Inherited from [APIBase](_utils_types_.apibase.md).[core](_utils_types_.apibase.md#protected-core)*

*Defined in [utils/types.ts:32](https://github.com/ava-labs/slopes/blob/65cee65/src/utils/types.ts#L32)*

___

### `Protected` db

• **db**: *StoreAPI*

*Inherited from [APIBase](_utils_types_.apibase.md).[db](_utils_types_.apibase.md#protected-db)*

*Defined in [utils/types.ts:34](https://github.com/ava-labs/slopes/blob/65cee65/src/utils/types.ts#L34)*

___

### `Protected` jrpcVersion

• **jrpcVersion**: *string* = "2.0"

*Inherited from [JRPCAPI](_utils_types_.jrpcapi.md).[jrpcVersion](_utils_types_.jrpcapi.md#protected-jrpcversion)*

*Defined in [utils/types.ts:80](https://github.com/ava-labs/slopes/blob/65cee65/src/utils/types.ts#L80)*

___

### `Protected` rpcid

• **rpcid**: *number* = 1

*Inherited from [JRPCAPI](_utils_types_.jrpcapi.md).[rpcid](_utils_types_.jrpcapi.md#protected-rpcid)*

*Defined in [utils/types.ts:81](https://github.com/ava-labs/slopes/blob/65cee65/src/utils/types.ts#L81)*

## Methods

###  callMethod

▸ **callMethod**(`method`: string, `params?`: Array‹object› | object, `baseurl?`: string): *Promise‹[RequestResponseData](_utils_types_.requestresponsedata.md)›*

*Inherited from [JRPCAPI](_utils_types_.jrpcapi.md)*

*Defined in [utils/types.ts:82](https://github.com/ava-labs/slopes/blob/65cee65/src/utils/types.ts#L82)*

**Parameters:**

Name | Type |
------ | ------ |
`method` | string |
`params?` | Array‹object› &#124; object |
`baseurl?` | string |

**Returns:** *Promise‹[RequestResponseData](_utils_types_.requestresponsedata.md)›*

___

###  createUser

▸ **createUser**(`username`: string, `password`: string): *Promise‹boolean›*

*Defined in [apis/keystore/api.ts:26](https://github.com/ava-labs/slopes/blob/65cee65/src/apis/keystore/api.ts#L26)*

Creates a user in the node's database.

**Parameters:**

Name | Type | Description |
------ | ------ | ------ |
`username` | string | Name of the user to create |
`password` | string | Password for the user  |

**Returns:** *Promise‹boolean›*

Promise for a boolean with true on success

___

###  deleteUser

▸ **deleteUser**(`username`: string, `password`: string): *Promise‹boolean›*

*Defined in [apis/keystore/api.ts:93](https://github.com/ava-labs/slopes/blob/65cee65/src/apis/keystore/api.ts#L93)*

Deletes a user in the node's database.

**Parameters:**

Name | Type | Description |
------ | ------ | ------ |
`username` | string | Name of the user to delete |
`password` | string | Password for the user  |

**Returns:** *Promise‹boolean›*

Promise for a boolean with true on success

___

###  exportUser

▸ **exportUser**(`username`: string, `password`: string): *Promise‹string›*

*Defined in [apis/keystore/api.ts:44](https://github.com/ava-labs/slopes/blob/65cee65/src/apis/keystore/api.ts#L44)*

Exports a user. The user can be imported to another node with keystore.importUser .

**Parameters:**

Name | Type | Description |
------ | ------ | ------ |
`username` | string | The name of the user to export |
`password` | string | The password of the user to export  |

**Returns:** *Promise‹string›*

Promise with a string importable using importUser

___

###  getBaseURL

▸ **getBaseURL**(): *string*

*Inherited from [APIBase](_utils_types_.apibase.md)*

*Defined in [utils/types.ts:57](https://github.com/ava-labs/slopes/blob/65cee65/src/utils/types.ts#L57)*

Returns the baseurl's path.

**Returns:** *string*

___

###  getDB

▸ **getDB**(): *StoreAPI*

*Inherited from [APIBase](_utils_types_.apibase.md)*

*Defined in [utils/types.ts:64](https://github.com/ava-labs/slopes/blob/65cee65/src/utils/types.ts#L64)*

Returns the baseurl's database.

**Returns:** *StoreAPI*

___

###  getRPCID

▸ **getRPCID**(): *number*

*Inherited from [JRPCAPI](_utils_types_.jrpcapi.md)*

*Defined in [utils/types.ts:124](https://github.com/ava-labs/slopes/blob/65cee65/src/utils/types.ts#L124)*

Returns the rpcid, a strictly-increasing number, starting from 1, indicating the next request ID that will be sent.

**Returns:** *number*

___

###  importUser

▸ **importUser**(`username`: string, `user`: string, `password`: string): *Promise‹boolean›*

*Defined in [apis/keystore/api.ts:63](https://github.com/ava-labs/slopes/blob/65cee65/src/apis/keystore/api.ts#L63)*

Imports a user file into the node's user database and assigns it to a username.

**Parameters:**

Name | Type | Description |
------ | ------ | ------ |
`username` | string | The name the user file should be imported into |
`user` | string | AVA serialized string represetning a user's data |
`password` | string | The user's password  |

**Returns:** *Promise‹boolean›*

A promise with a true-value on success.

___

###  listUsers

▸ **listUsers**(): *Promise‹Array‹string››*

*Defined in [apis/keystore/api.ts:79](https://github.com/ava-labs/slopes/blob/65cee65/src/apis/keystore/api.ts#L79)*

Lists the names of all users on the node.

**Returns:** *Promise‹Array‹string››*

Promise of an array with all user names.

___

###  setBaseURL

▸ **setBaseURL**(`baseurl`: string): *void*

*Inherited from [APIBase](_utils_types_.apibase.md)*

*Defined in [utils/types.ts:41](https://github.com/ava-labs/slopes/blob/65cee65/src/utils/types.ts#L41)*

Sets the path of the APIs baseurl.

**Parameters:**

Name | Type | Description |
------ | ------ | ------ |
`baseurl` | string | Path of the APIs baseurl - ex: "/ext/bc/avm"  |

**Returns:** *void*
