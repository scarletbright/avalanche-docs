[avalanche](../README.md) › [KeystoreAPI](../modules/keystoreapi.md) › [KeystoreAPI](keystoreapi.keystoreapi-1.md)

# Class: KeystoreAPI

Class for interacting with a node API that is using the node's KeystoreAPI.

**WARNING**: The KeystoreAPI is to be used by the node-owner as the data is stored locally on the node. Do not trust the root user. If you are not the node-owner, do not use this as your wallet.

**`remarks`** This extends the [JRPCAPI](utils_types.jrpcapi.md) class. This class should not be directly called. Instead, use the [Avalanche.addAPI](avalanche.avalanche-1.md#addapi) function to register this interface with Avalanche.

## Hierarchy

  ↳ [JRPCAPI](utils_types.jrpcapi.md)

  ↳ **KeystoreAPI**

## Index

### Constructors

* [constructor](keystoreapi.keystoreapi-1.md#constructor)

### Properties

* [baseurl](keystoreapi.keystoreapi-1.md#protected-baseurl)
* [core](keystoreapi.keystoreapi-1.md#protected-core)
* [db](keystoreapi.keystoreapi-1.md#protected-db)
* [jrpcVersion](keystoreapi.keystoreapi-1.md#protected-jrpcversion)
* [rpcid](keystoreapi.keystoreapi-1.md#protected-rpcid)

### Methods

* [callMethod](keystoreapi.keystoreapi-1.md#callmethod)
* [createUser](keystoreapi.keystoreapi-1.md#createuser)
* [deleteUser](keystoreapi.keystoreapi-1.md#deleteuser)
* [exportUser](keystoreapi.keystoreapi-1.md#exportuser)
* [getBaseURL](keystoreapi.keystoreapi-1.md#getbaseurl)
* [getDB](keystoreapi.keystoreapi-1.md#getdb)
* [getRPCID](keystoreapi.keystoreapi-1.md#getrpcid)
* [importUser](keystoreapi.keystoreapi-1.md#importuser)
* [listUsers](keystoreapi.keystoreapi-1.md#listusers)
* [setBaseURL](keystoreapi.keystoreapi-1.md#setbaseurl)

## Constructors

###  constructor

\+ **new KeystoreAPI**(`core`: [AvalancheCore](avalanchecore.avalanchecore-1.md), `baseurl`: string): *[KeystoreAPI](keystoreapi.keystoreapi-1.md)*

*Overrides [JRPCAPI](utils_types.jrpcapi.md).[constructor](utils_types.jrpcapi.md#constructor)*

*Defined in [src/apis/keystore/api.ts:94](https://github.com/ava-labs/avalanche.js/blob/eabcc2f/src/apis/keystore/api.ts#L94)*

This class should not be instantiated directly. Instead use the [Avalanche.addAPI](avalanche.avalanche-1.md#addapi) method.

**Parameters:**

Name | Type | Default | Description |
------ | ------ | ------ | ------ |
`core` | [AvalancheCore](avalanchecore.avalanchecore-1.md) | - | A reference to the Avalanche class |
`baseurl` | string | "/ext/keystore" | Defaults to the string "/ext/keystore" as the path to blockchain's baseurl  |

**Returns:** *[KeystoreAPI](keystoreapi.keystoreapi-1.md)*

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

*Inherited from [JRPCAPI](utils_types.jrpcapi.md).[jrpcVersion](utils_types.jrpcapi.md#protected-jrpcversion)*

*Defined in [src/utils/types.ts:291](https://github.com/ava-labs/avalanche.js/blob/eabcc2f/src/utils/types.ts#L291)*

___

### `Protected` rpcid

• **rpcid**: *number* = 1

*Inherited from [JRPCAPI](utils_types.jrpcapi.md).[rpcid](utils_types.jrpcapi.md#protected-rpcid)*

*Defined in [src/utils/types.ts:293](https://github.com/ava-labs/avalanche.js/blob/eabcc2f/src/utils/types.ts#L293)*

## Methods

###  callMethod

▸ **callMethod**(`method`: string, `params?`: Array‹object› | object, `baseurl?`: string): *Promise‹[RequestResponseData](utils_types.requestresponsedata.md)›*

*Inherited from [JRPCAPI](utils_types.jrpcapi.md).[callMethod](utils_types.jrpcapi.md#callmethod)*

*Defined in [src/utils/types.ts:295](https://github.com/ava-labs/avalanche.js/blob/eabcc2f/src/utils/types.ts#L295)*

**Parameters:**

Name | Type |
------ | ------ |
`method` | string |
`params?` | Array‹object› &#124; object |
`baseurl?` | string |

**Returns:** *Promise‹[RequestResponseData](utils_types.requestresponsedata.md)›*

___

###  createUser

▸ **createUser**(`username`: string, `password`: string): *Promise‹boolean›*

*Defined in [src/apis/keystore/api.ts:26](https://github.com/ava-labs/avalanche.js/blob/eabcc2f/src/apis/keystore/api.ts#L26)*

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

*Defined in [src/apis/keystore/api.ts:87](https://github.com/ava-labs/avalanche.js/blob/eabcc2f/src/apis/keystore/api.ts#L87)*

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

*Defined in [src/apis/keystore/api.ts:43](https://github.com/ava-labs/avalanche.js/blob/eabcc2f/src/apis/keystore/api.ts#L43)*

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

*Inherited from [JRPCAPI](utils_types.jrpcapi.md).[getRPCID](utils_types.jrpcapi.md#getrpcid)*

*Defined in [src/utils/types.ts:340](https://github.com/ava-labs/avalanche.js/blob/eabcc2f/src/utils/types.ts#L340)*

Returns the rpcid, a strictly-increasing number, starting from 1, indicating the next
request ID that will be sent.

**Returns:** *number*

___

###  importUser

▸ **importUser**(`username`: string, `user`: string, `password`: string): *Promise‹boolean›*

*Defined in [src/apis/keystore/api.ts:61](https://github.com/ava-labs/avalanche.js/blob/eabcc2f/src/apis/keystore/api.ts#L61)*

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

*Defined in [src/apis/keystore/api.ts:76](https://github.com/ava-labs/avalanche.js/blob/eabcc2f/src/apis/keystore/api.ts#L76)*

Lists the names of all users on the node.

**Returns:** *Promise‹Array‹string››*

Promise of an array with all user names.

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
