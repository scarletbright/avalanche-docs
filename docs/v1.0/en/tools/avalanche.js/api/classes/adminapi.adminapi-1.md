[avalanche](../README.md) › [AdminAPI](../modules/adminapi.md) › [AdminAPI](adminapi.adminapi-1.md)

# Class: AdminAPI

Class for interacting with a node's AdminAPI.

**`remarks`** This extends the [JRPCAPI](utils_types.jrpcapi.md) class. This class should not be directly called. Instead, use the [Avalanche.addAPI](avalanche.avalanche-1.md#addapi) function to register this interface with Avalanche.

## Hierarchy

  ↳ [JRPCAPI](utils_types.jrpcapi.md)

  ↳ **AdminAPI**

## Index

### Constructors

* [constructor](adminapi.adminapi-1.md#constructor)

### Properties

* [baseurl](adminapi.adminapi-1.md#protected-baseurl)
* [core](adminapi.adminapi-1.md#protected-core)
* [db](adminapi.adminapi-1.md#protected-db)
* [jrpcVersion](adminapi.adminapi-1.md#protected-jrpcversion)
* [rpcid](adminapi.adminapi-1.md#protected-rpcid)

### Methods

* [alias](adminapi.adminapi-1.md#alias)
* [aliasChain](adminapi.adminapi-1.md#aliaschain)
* [callMethod](adminapi.adminapi-1.md#callmethod)
* [getBaseURL](adminapi.adminapi-1.md#getbaseurl)
* [getBlockchainID](adminapi.adminapi-1.md#getblockchainid)
* [getDB](adminapi.adminapi-1.md#getdb)
* [getNetworkID](adminapi.adminapi-1.md#getnetworkid)
* [getNetworkName](adminapi.adminapi-1.md#getnetworkname)
* [getNodeID](adminapi.adminapi-1.md#getnodeid)
* [getNodeVersion](adminapi.adminapi-1.md#getnodeversion)
* [getRPCID](adminapi.adminapi-1.md#getrpcid)
* [lockProfile](adminapi.adminapi-1.md#lockprofile)
* [memoryProfile](adminapi.adminapi-1.md#memoryprofile)
* [peers](adminapi.adminapi-1.md#peers)
* [setBaseURL](adminapi.adminapi-1.md#setbaseurl)
* [startCPUProfiler](adminapi.adminapi-1.md#startcpuprofiler)
* [stopCPUProfiler](adminapi.adminapi-1.md#stopcpuprofiler)

## Constructors

###  constructor

\+ **new AdminAPI**(`core`: [AvalancheCore](avalanchecore.avalanchecore-1.md), `baseurl`: string): *[AdminAPI](adminapi.adminapi-1.md)*

*Overrides [JRPCAPI](utils_types.jrpcapi.md).[constructor](utils_types.jrpcapi.md#constructor)*

*Defined in [apis/admin/api.ts:182](https://github.com/ava-labs/avalanche.js/blob/c723742/src/apis/admin/api.ts#L182)*

This class should not be instantiated directly. Instead use the [Avalanche.addAPI](avalanche.avalanche-1.md#addapi) method.

**Parameters:**

Name | Type | Default | Description |
------ | ------ | ------ | ------ |
`core` | [AvalancheCore](avalanchecore.avalanchecore-1.md) | - | A reference to the Avalanche class |
`baseurl` | string | "/ext/admin" | Defaults to the string "/ext/admin" as the path to rpc's baseurl  |

**Returns:** *[AdminAPI](adminapi.adminapi-1.md)*

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

###  alias

▸ **alias**(`endpoint`: string, `alias`: string): *Promise‹boolean›*

*Defined in [apis/admin/api.ts:49](https://github.com/ava-labs/avalanche.js/blob/c723742/src/apis/admin/api.ts#L49)*

Assign an API an alias, a different endpoint for the API. The original endpoint will still work. This change only affects this node; other nodes will not know about this alias.

The API being aliased can now be called at ext/alias

**Parameters:**

Name | Type | Description |
------ | ------ | ------ |
`endpoint` | string | The original endpoint of the API. endpoint should only include the part of the endpoint after /ext/ |
`alias` | string | - |

**Returns:** *Promise‹boolean›*

Returns a Promise<boolean> containing success, true for success, false for failure.

___

###  aliasChain

▸ **aliasChain**(`chain`: string, `alias`: string): *Promise‹boolean›*

*Defined in [apis/admin/api.ts:67](https://github.com/ava-labs/avalanche.js/blob/c723742/src/apis/admin/api.ts#L67)*

Give a blockchain an alias, a different name that can be used any place the blockchain’s ID is used.

**Parameters:**

Name | Type | Description |
------ | ------ | ------ |
`chain` | string | - |
`alias` | string | Can now be used in place of the blockchain’s ID (in API endpoints, for example)  |

**Returns:** *Promise‹boolean›*

Returns a Promise<boolean> containing success, true for success, false for failure.

___

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

*Defined in [apis/admin/api.ts:84](https://github.com/ava-labs/avalanche.js/blob/c723742/src/apis/admin/api.ts#L84)*

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

*Defined in [apis/admin/api.ts:34](https://github.com/ava-labs/avalanche.js/blob/c723742/src/apis/admin/api.ts#L34)*

Fetches the networkID from the node.

**Returns:** *Promise‹number›*

Returns a Promise<number> of the networkID.

___

###  getNetworkName

▸ **getNetworkName**(): *Promise‹string›*

*Defined in [apis/admin/api.ts:109](https://github.com/ava-labs/avalanche.js/blob/c723742/src/apis/admin/api.ts#L109)*

Fetches the network name this node is running on

**Returns:** *Promise‹string›*

Returns a Promise<string> containing the network name.

___

###  getNodeID

▸ **getNodeID**(): *Promise‹string›*

*Defined in [apis/admin/api.ts:22](https://github.com/ava-labs/avalanche.js/blob/c723742/src/apis/admin/api.ts#L22)*

Fetches the nodeID from the node.

**Returns:** *Promise‹string›*

Returns a Promise<string> of the nodeID.

___

###  getNodeVersion

▸ **getNodeVersion**(): *Promise‹string›*

*Defined in [apis/admin/api.ts:98](https://github.com/ava-labs/avalanche.js/blob/c723742/src/apis/admin/api.ts#L98)*

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

###  lockProfile

▸ **lockProfile**(`filename`: string): *Promise‹boolean›*

*Defined in [apis/admin/api.ts:122](https://github.com/ava-labs/avalanche.js/blob/c723742/src/apis/admin/api.ts#L122)*

Dump the mutex statistics of the node to the specified file.

**Parameters:**

Name | Type | Description |
------ | ------ | ------ |
`filename` | string | Name of the file to write the statistics.  |

**Returns:** *Promise‹boolean›*

Promise for a boolean that is true on success.

___

###  memoryProfile

▸ **memoryProfile**(`filename`: string): *Promise‹boolean›*

*Defined in [apis/admin/api.ts:138](https://github.com/ava-labs/avalanche.js/blob/c723742/src/apis/admin/api.ts#L138)*

Dump the current memory footprint of the node to the specified file.

**Parameters:**

Name | Type | Description |
------ | ------ | ------ |
`filename` | string | Name of the file to write the profile information.  |

**Returns:** *Promise‹boolean›*

Promise for a boolean that is true on success.

___

###  peers

▸ **peers**(): *Promise‹Array‹string››*

*Defined in [apis/admin/api.ts:152](https://github.com/ava-labs/avalanche.js/blob/c723742/src/apis/admin/api.ts#L152)*

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

___

###  startCPUProfiler

▸ **startCPUProfiler**(`filename`: string): *Promise‹boolean›*

*Defined in [apis/admin/api.ts:164](https://github.com/ava-labs/avalanche.js/blob/c723742/src/apis/admin/api.ts#L164)*

Start profiling the cpu utilization of the node. Will dump the profile information into the specified file on stop.

**Parameters:**

Name | Type | Description |
------ | ------ | ------ |
`filename` | string | Name of the file to write the profile information on stop.  |

**Returns:** *Promise‹boolean›*

Promise for a boolean that is true on success.

___

###  stopCPUProfiler

▸ **stopCPUProfiler**(): *Promise‹boolean›*

*Defined in [apis/admin/api.ts:178](https://github.com/ava-labs/avalanche.js/blob/c723742/src/apis/admin/api.ts#L178)*

Stop the CPU profile that was previously started.

**Returns:** *Promise‹boolean›*

Promise for a boolean that is true on success.
