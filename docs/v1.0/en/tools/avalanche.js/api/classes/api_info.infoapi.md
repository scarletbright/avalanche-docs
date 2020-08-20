[avalanche](../README.md) › [API-Info](../modules/api_info.md) › [InfoAPI](api_info.infoapi.md)

# Class: InfoAPI

Class for interacting with a node's InfoAPI.

**`remarks`** This extends the [JRPCAPI](common_jrpcapi.jrpcapi.md) class. This class should not be directly called. Instead, use the [Avalanche.addAPI](avalanche.avalanche-1.md#addapi) function to register this interface with Avalanche.

## Hierarchy

  ↳ [JRPCAPI](common_jrpcapi.jrpcapi.md)

  ↳ **InfoAPI**

## Index

### Constructors

* [constructor](api_info.infoapi.md#constructor)

### Properties

* [baseurl](api_info.infoapi.md#protected-baseurl)
* [core](api_info.infoapi.md#protected-core)
* [db](api_info.infoapi.md#protected-db)
* [jrpcVersion](api_info.infoapi.md#protected-jrpcversion)
* [rpcid](api_info.infoapi.md#protected-rpcid)

### Methods

* [callMethod](api_info.infoapi.md#callmethod)
* [getBaseURL](api_info.infoapi.md#getbaseurl)
* [getBlockchainID](api_info.infoapi.md#getblockchainid)
* [getDB](api_info.infoapi.md#getdb)
* [getNetworkID](api_info.infoapi.md#getnetworkid)
* [getNetworkName](api_info.infoapi.md#getnetworkname)
* [getNodeID](api_info.infoapi.md#getnodeid)
* [getNodeVersion](api_info.infoapi.md#getnodeversion)
* [getRPCID](api_info.infoapi.md#getrpcid)
* [peers](api_info.infoapi.md#peers)
* [setBaseURL](api_info.infoapi.md#setbaseurl)

## Constructors

###  constructor

\+ **new InfoAPI**(`core`: [AvalancheCore](avalanchecore.avalanchecore-1.md), `baseurl`: string): *[InfoAPI](api_info.infoapi.md)*

*Overrides [JRPCAPI](common_jrpcapi.jrpcapi.md).[constructor](common_jrpcapi.jrpcapi.md#constructor)*

Defined in src/apis/info/api.ts:76

**Parameters:**

Name | Type | Default |
------ | ------ | ------ |
`core` | [AvalancheCore](avalanchecore.avalanchecore-1.md) | - |
`baseurl` | string | "/ext/info" |

**Returns:** *[InfoAPI](api_info.infoapi.md)*

## Properties

### `Protected` baseurl

• **baseurl**: *string*

*Inherited from [APIBase](common_apibase.apibase.md).[baseurl](common_apibase.apibase.md#protected-baseurl)*

Defined in src/common/apibase.ts:38

___

### `Protected` core

• **core**: *[AvalancheCore](avalanchecore.avalanchecore-1.md)*

*Inherited from [APIBase](common_apibase.apibase.md).[core](common_apibase.apibase.md#protected-core)*

Defined in src/common/apibase.ts:36

___

### `Protected` db

• **db**: *StoreAPI*

*Inherited from [APIBase](common_apibase.apibase.md).[db](common_apibase.apibase.md#protected-db)*

Defined in src/common/apibase.ts:40

___

### `Protected` jrpcVersion

• **jrpcVersion**: *string* = "2.0"

*Inherited from [JRPCAPI](common_jrpcapi.jrpcapi.md).[jrpcVersion](common_jrpcapi.jrpcapi.md#protected-jrpcversion)*

Defined in src/common/jrpcapi.ts:17

___

### `Protected` rpcid

• **rpcid**: *number* = 1

*Inherited from [JRPCAPI](common_jrpcapi.jrpcapi.md).[rpcid](common_jrpcapi.jrpcapi.md#protected-rpcid)*

Defined in src/common/jrpcapi.ts:19

## Methods

###  callMethod

▸ **callMethod**(`method`: string, `params?`: Array‹object› | object, `baseurl?`: string): *Promise‹[RequestResponseData](common_apibase.requestresponsedata.md)›*

*Inherited from [JRPCAPI](common_jrpcapi.jrpcapi.md).[callMethod](common_jrpcapi.jrpcapi.md#callmethod)*

Defined in src/common/jrpcapi.ts:21

**Parameters:**

Name | Type |
------ | ------ |
`method` | string |
`params?` | Array‹object› &#124; object |
`baseurl?` | string |

**Returns:** *Promise‹[RequestResponseData](common_apibase.requestresponsedata.md)›*

___

###  getBaseURL

▸ **getBaseURL**(): *string*

*Inherited from [APIBase](common_apibase.apibase.md).[getBaseURL](common_apibase.apibase.md#getbaseurl)*

Defined in src/common/apibase.ts:63

Returns the baseurl's path.

**Returns:** *string*

___

###  getBlockchainID

▸ **getBlockchainID**(`alias`: string): *Promise‹string›*

Defined in src/apis/info/api.ts:24

Fetches the blockchainID from the node for a given alias.

**Parameters:**

Name | Type | Description |
------ | ------ | ------ |
`alias` | string | The blockchain alias to get the blockchainID  |

**Returns:** *Promise‹string›*

Returns a Promise<string> containing the base 58 string representation of the blockchainID.

___

###  getDB

▸ **getDB**(): *StoreAPI*

*Inherited from [APIBase](common_apibase.apibase.md).[getDB](common_apibase.apibase.md#getdb)*

Defined in src/common/apibase.ts:68

Returns the baseurl's database.

**Returns:** *StoreAPI*

___

###  getNetworkID

▸ **getNetworkID**(): *Promise‹number›*

Defined in src/apis/info/api.ts:37

Fetches the networkID from the node.

**Returns:** *Promise‹number›*

Returns a Promise<number> of the networkID.

___

###  getNetworkName

▸ **getNetworkName**(): *Promise‹string›*

Defined in src/apis/info/api.ts:48

Fetches the network name this node is running on

**Returns:** *Promise‹string›*

Returns a Promise<string> containing the network name.

___

###  getNodeID

▸ **getNodeID**(): *Promise‹string›*

Defined in src/apis/info/api.ts:56

Fetches the nodeID from the node.

**Returns:** *Promise‹string›*

Returns a Promise<string> of the nodeID.

___

###  getNodeVersion

▸ **getNodeVersion**(): *Promise‹string›*

Defined in src/apis/info/api.ts:67

Fetches the version of Gecko this node is running

**Returns:** *Promise‹string›*

Returns a Promise<string> containing the version of Gecko.

___

###  getRPCID

▸ **getRPCID**(): *number*

*Inherited from [JRPCAPI](common_jrpcapi.jrpcapi.md).[getRPCID](common_jrpcapi.jrpcapi.md#getrpcid)*

Defined in src/common/jrpcapi.ts:66

Returns the rpcid, a strictly-increasing number, starting from 1, indicating the next
request ID that will be sent.

**Returns:** *number*

___

###  peers

▸ **peers**(): *Promise‹Array‹string››*

Defined in src/apis/info/api.ts:75

Returns the peers connected to the node.

**Returns:** *Promise‹Array‹string››*

Promise for the list of connected peers in <ip>:<port> format.

___

###  setBaseURL

▸ **setBaseURL**(`baseurl`: string): *void*

*Inherited from [APIBase](common_apibase.apibase.md).[setBaseURL](common_apibase.apibase.md#setbaseurl)*

Defined in src/common/apibase.ts:47

Sets the path of the APIs baseurl.

**Parameters:**

Name | Type | Description |
------ | ------ | ------ |
`baseurl` | string | Path of the APIs baseurl - ex: "/ext/bc/avm"  |

**Returns:** *void*
