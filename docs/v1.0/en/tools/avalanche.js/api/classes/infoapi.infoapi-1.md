[avalanche](../README.md) › [InfoAPI](../modules/infoapi.md) › [InfoAPI](infoapi.infoapi-1.md)

# Class: InfoAPI

Class for interacting with a node's InfoAPI.

**`remarks`** This extends the [JRPCAPI](utils_types.jrpcapi.md) class. This class should not be directly called. Instead, use the [Avalanche.addAPI](avalanche.avalanche-1.md#addapi) function to register this interface with Avalanche.

## Hierarchy

  ↳ [JRPCAPI](utils_types.jrpcapi.md)

  ↳ **InfoAPI**

## Index

### Constructors

* [constructor](infoapi.infoapi-1.md#constructor)

### Properties

* [baseurl](infoapi.infoapi-1.md#protected-baseurl)
* [core](infoapi.infoapi-1.md#protected-core)
* [db](infoapi.infoapi-1.md#protected-db)
* [jrpcVersion](infoapi.infoapi-1.md#protected-jrpcversion)
* [rpcid](infoapi.infoapi-1.md#protected-rpcid)

### Methods

* [callMethod](infoapi.infoapi-1.md#callmethod)
* [getBaseURL](infoapi.infoapi-1.md#getbaseurl)
* [getBlockchainID](infoapi.infoapi-1.md#getblockchainid)
* [getDB](infoapi.infoapi-1.md#getdb)
* [getNetworkID](infoapi.infoapi-1.md#getnetworkid)
* [getNetworkName](infoapi.infoapi-1.md#getnetworkname)
* [getNodeID](infoapi.infoapi-1.md#getnodeid)
* [getNodeVersion](infoapi.infoapi-1.md#getnodeversion)
* [getRPCID](infoapi.infoapi-1.md#getrpcid)
* [peers](infoapi.infoapi-1.md#peers)
* [setBaseURL](infoapi.infoapi-1.md#setbaseurl)

## Constructors

###  constructor

\+ **new InfoAPI**(`core`: [AvalancheCore](avalanchecore.avalanchecore-1.md), `baseurl`: string): *[InfoAPI](infoapi.infoapi-1.md)*

*Overrides [JRPCAPI](utils_types.jrpcapi.md).[constructor](utils_types.jrpcapi.md#constructor)*

*Defined in [apis/info/api.ts:88](https://github.com/ava-labs/avalanche.js/blob/c723742/src/apis/info/api.ts#L88)*

**Parameters:**

Name | Type | Default |
------ | ------ | ------ |
`core` | [AvalancheCore](avalanchecore.avalanchecore-1.md) | - |
`baseurl` | string | "/ext/info" |

**Returns:** *[InfoAPI](infoapi.infoapi-1.md)*

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

*Inherited from [JRPCAPI](utils_types.jrpcapi.md).[jrpcVersion](utils_types.jrpcapi.md#protected-jrpcversion)*

*Defined in [utils/types.ts:276](https://github.com/ava-labs/avalanche.js/blob/c723742/src/utils/types.ts#L276)*

___

### `Protected` rpcid

• **rpcid**: *number* = 1

*Inherited from [JRPCAPI](utils_types.jrpcapi.md).[rpcid](utils_types.jrpcapi.md#protected-rpcid)*

*Defined in [utils/types.ts:277](https://github.com/ava-labs/avalanche.js/blob/c723742/src/utils/types.ts#L277)*

## Methods

###  callMethod

▸ **callMethod**(`method`: string, `params?`: Array‹object› | object, `baseurl?`: string): *Promise‹[RequestResponseData](utils_types.requestresponsedata.md)›*

*Inherited from [JRPCAPI](utils_types.jrpcapi.md).[callMethod](utils_types.jrpcapi.md#callmethod)*

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

###  getBlockchainID

▸ **getBlockchainID**(`alias`: string): *Promise‹string›*

*Defined in [apis/info/api.ts:24](https://github.com/ava-labs/avalanche.js/blob/c723742/src/apis/info/api.ts#L24)*

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

*Inherited from [APIBase](utils_types.apibase.md).[getDB](utils_types.apibase.md#getdb)*

*Defined in [utils/types.ts:65](https://github.com/ava-labs/avalanche.js/blob/c723742/src/utils/types.ts#L65)*

Returns the baseurl's database.

**Returns:** *StoreAPI*

___

###  getNetworkID

▸ **getNetworkID**(): *Promise‹number›*

*Defined in [apis/info/api.ts:38](https://github.com/ava-labs/avalanche.js/blob/c723742/src/apis/info/api.ts#L38)*

Fetches the networkID from the node.

**Returns:** *Promise‹number›*

Returns a Promise<number> of the networkID.

___

###  getNetworkName

▸ **getNetworkName**(): *Promise‹string›*

*Defined in [apis/info/api.ts:50](https://github.com/ava-labs/avalanche.js/blob/c723742/src/apis/info/api.ts#L50)*

Fetches the network name this node is running on

**Returns:** *Promise‹string›*

Returns a Promise<string> containing the network name.

___

###  getNodeID

▸ **getNodeID**(): *Promise‹string›*

*Defined in [apis/info/api.ts:61](https://github.com/ava-labs/avalanche.js/blob/c723742/src/apis/info/api.ts#L61)*

Fetches the nodeID from the node.

**Returns:** *Promise‹string›*

Returns a Promise<string> of the nodeID.

___

###  getNodeVersion

▸ **getNodeVersion**(): *Promise‹string›*

*Defined in [apis/info/api.ts:73](https://github.com/ava-labs/avalanche.js/blob/c723742/src/apis/info/api.ts#L73)*

Fetches the version of Gecko this node is running

**Returns:** *Promise‹string›*

Returns a Promise<string> containing the version of Gecko.

___

###  getRPCID

▸ **getRPCID**(): *number*

*Inherited from [JRPCAPI](utils_types.jrpcapi.md).[getRPCID](utils_types.jrpcapi.md#getrpcid)*

*Defined in [utils/types.ts:320](https://github.com/ava-labs/avalanche.js/blob/c723742/src/utils/types.ts#L320)*

Returns the rpcid, a strictly-increasing number, starting from 1, indicating the next request ID that will be sent.

**Returns:** *number*

___

###  peers

▸ **peers**(): *Promise‹Array‹string››*

*Defined in [apis/info/api.ts:84](https://github.com/ava-labs/avalanche.js/blob/c723742/src/apis/info/api.ts#L84)*

Returns the peers connected to the node.

**Returns:** *Promise‹Array‹string››*

Promise for the list of connected peers in <ip>:<port> format.

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
