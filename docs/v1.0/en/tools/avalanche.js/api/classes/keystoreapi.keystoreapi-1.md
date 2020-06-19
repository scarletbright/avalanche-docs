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

*Defined in [apis/keystore/api.ts:102](https://github.com/ava-labs/avalanche.js/blob/4d26b45/src/apis/keystore/api.ts#L102)*

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

*Defined in [utils/types.ts:34](https://github.com/ava-labs/avalanche.js/blob/4d26b45/src/utils/types.ts#L34)*

___

### `Protected` core

• **core**: *[AvalancheCore](avalanchecore.avalanchecore-1.md)*

*Inherited from [APIBase](utils_types.apibase.md).[core](utils_types.apibase.md#protected-core)*

*Defined in [utils/types.ts:33](https://github.com/ava-labs/avalanche.js/blob/4d26b45/src/utils/types.ts#L33)*

___

### `Protected` db

• **db**: *StoreAPI*

*Inherited from [APIBase](utils_types.apibase.md).[db](utils_types.apibase.md#protected-db)*

*Defined in [utils/types.ts:35](https://github.com/ava-labs/avalanche.js/blob/4d26b45/src/utils/types.ts#L35)*

___

### `Protected` jrpcVersion

• **jrpcVersion**: *string* = "2.0"

*Inherited from [JRPCAPI](utils_types.jrpcapi.md).[jrpcVersion](utils_types.jrpcapi.md#protected-jrpcversion)*

*Defined in [utils/types.ts:81](https://github.com/ava-labs/avalanche.js/blob/4d26b45/src/utils/types.ts#L81)*

___

### `Protected` rpcid

• **rpcid**: *number* = 1

*Inherited from [JRPCAPI](utils_types.jrpcapi.md).[rpcid](utils_types.jrpcapi.md#protected-rpcid)*

*Defined in [utils/types.ts:82](https://github.com/ava-labs/avalanche.js/blob/4d26b45/src/utils/types.ts#L82)*

## Methods

###  callMethod

▸ **callMethod**(`method`: string, `params?`: Array‹object› | object, `baseurl?`: string): *Promise‹[RequestResponseData](utils_types.requestresponsedata.md)›*

*Inherited from [JRPCAPI](utils_types.jrpcapi.md).[callMethod](utils_types.jrpcapi.md#callmethod)*

*Defined in [utils/types.ts:83](https://github.com/ava-labs/avalanche.js/blob/4d26b45/src/utils/types.ts#L83)*

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

*Defined in [apis/keystore/api.ts:27](https://github.com/ava-labs/avalanche.js/blob/4d26b45/src/apis/keystore/api.ts#L27)*

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

*Defined in [apis/keystore/api.ts:94](https://github.com/ava-labs/avalanche.js/blob/4d26b45/src/apis/keystore/api.ts#L94)*

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

*Defined in [apis/keystore/api.ts:45](https://github.com/ava-labs/avalanche.js/blob/4d26b45/src/apis/keystore/api.ts#L45)*

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

*Defined in [utils/types.ts:58](https://github.com/ava-labs/avalanche.js/blob/4d26b45/src/utils/types.ts#L58)*

Returns the baseurl's path.

**Returns:** *string*

___

###  getDB

▸ **getDB**(): *StoreAPI*

*Inherited from [APIBase](utils_types.apibase.md).[getDB](utils_types.apibase.md#getdb)*

*Defined in [utils/types.ts:65](https://github.com/ava-labs/avalanche.js/blob/4d26b45/src/utils/types.ts#L65)*

Returns the baseurl's database.

**Returns:** *StoreAPI*

___

###  getRPCID

▸ **getRPCID**(): *number*

*Inherited from [JRPCAPI](utils_types.jrpcapi.md).[getRPCID](utils_types.jrpcapi.md#getrpcid)*

*Defined in [utils/types.ts:125](https://github.com/ava-labs/avalanche.js/blob/4d26b45/src/utils/types.ts#L125)*

Returns the rpcid, a strictly-increasing number, starting from 1, indicating the next request ID that will be sent.

**Returns:** *number*

___

###  importUser

▸ **importUser**(`username`: string, `user`: string, `password`: string): *Promise‹boolean›*

*Defined in [apis/keystore/api.ts:64](https://github.com/ava-labs/avalanche.js/blob/4d26b45/src/apis/keystore/api.ts#L64)*

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

*Defined in [apis/keystore/api.ts:80](https://github.com/ava-labs/avalanche.js/blob/4d26b45/src/apis/keystore/api.ts#L80)*

Lists the names of all users on the node.

**Returns:** *Promise‹Array‹string››*

Promise of an array with all user names.

___

###  setBaseURL

▸ **setBaseURL**(`baseurl`: string): *void*

*Inherited from [APIBase](utils_types.apibase.md).[setBaseURL](utils_types.apibase.md#setbaseurl)*

*Defined in [utils/types.ts:42](https://github.com/ava-labs/avalanche.js/blob/4d26b45/src/utils/types.ts#L42)*

Sets the path of the APIs baseurl.

**Parameters:**

Name | Type | Description |
------ | ------ | ------ |
`baseurl` | string | Path of the APIs baseurl - ex: "/ext/bc/avm"  |

**Returns:** *void*
