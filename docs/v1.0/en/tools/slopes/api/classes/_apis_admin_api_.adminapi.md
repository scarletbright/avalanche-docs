[slopes - v1.7.3](../README.md) › ["apis/admin/api"](../modules/_apis_admin_api_.md) › [AdminAPI](_apis_admin_api_.adminapi.md)

# Class: AdminAPI

Class for interacting with a node's AdminAPI.

**`remarks`** This extends the [JRPCAPI](_utils_types_.jrpcapi.md) class. This class should not be directly called. Instead, use the [Slopes.addAPI](_index_.slopes.md#addapi) function to register this interface with Slopes.

## Hierarchy

  ↳ [JRPCAPI](_utils_types_.jrpcapi.md)

  ↳ **AdminAPI**

## Index

### Constructors

* [constructor](_apis_admin_api_.adminapi.md#constructor)

### Properties

* [baseurl](_apis_admin_api_.adminapi.md#protected-baseurl)
* [core](_apis_admin_api_.adminapi.md#protected-core)
* [db](_apis_admin_api_.adminapi.md#protected-db)
* [jrpcVersion](_apis_admin_api_.adminapi.md#protected-jrpcversion)
* [rpcid](_apis_admin_api_.adminapi.md#protected-rpcid)

### Methods

* [alias](_apis_admin_api_.adminapi.md#alias)
* [aliasChain](_apis_admin_api_.adminapi.md#aliaschain)
* [callMethod](_apis_admin_api_.adminapi.md#callmethod)
* [getBaseURL](_apis_admin_api_.adminapi.md#getbaseurl)
* [getBlockchainID](_apis_admin_api_.adminapi.md#getblockchainid)
* [getDB](_apis_admin_api_.adminapi.md#getdb)
* [getNetworkID](_apis_admin_api_.adminapi.md#getnetworkid)
* [getNodeID](_apis_admin_api_.adminapi.md#getnodeid)
* [getRPCID](_apis_admin_api_.adminapi.md#getrpcid)
* [lockProfile](_apis_admin_api_.adminapi.md#lockprofile)
* [memoryProfile](_apis_admin_api_.adminapi.md#memoryprofile)
* [peers](_apis_admin_api_.adminapi.md#peers)
* [setBaseURL](_apis_admin_api_.adminapi.md#setbaseurl)
* [startCPUProfiler](_apis_admin_api_.adminapi.md#startcpuprofiler)
* [stopCPUProfiler](_apis_admin_api_.adminapi.md#stopcpuprofiler)

## Constructors

###  constructor

\+ **new AdminAPI**(`core`: [SlopesCore](_slopes_.slopescore.md), `baseurl`: string): *[AdminAPI](_apis_admin_api_.adminapi.md)*

*Overrides [JRPCAPI](_utils_types_.jrpcapi.md).[constructor](_utils_types_.jrpcapi.md#constructor)*

*Defined in [apis/admin/api.ts:159](https://github.com/ava-labs/slopes/blob/48cc94f/src/apis/admin/api.ts#L159)*

This class should not be instantiated directly. Instead use the [Slopes.addAPI](_index_.slopes.md#addapi) method.

**Parameters:**

Name | Type | Default | Description |
------ | ------ | ------ | ------ |
`core` | [SlopesCore](_slopes_.slopescore.md) | - | A reference to the Slopes class |
`baseurl` | string | "/ext/admin" | Defaults to the string "/ext/admin" as the path to rpc's baseurl  |

**Returns:** *[AdminAPI](_apis_admin_api_.adminapi.md)*

## Properties

### `Protected` baseurl

• **baseurl**: *string*

*Inherited from [APIBase](_utils_types_.apibase.md).[baseurl](_utils_types_.apibase.md#protected-baseurl)*

*Defined in [utils/types.ts:33](https://github.com/ava-labs/slopes/blob/48cc94f/src/utils/types.ts#L33)*

___

### `Protected` core

• **core**: *[SlopesCore](_slopes_.slopescore.md)*

*Inherited from [APIBase](_utils_types_.apibase.md).[core](_utils_types_.apibase.md#protected-core)*

*Defined in [utils/types.ts:32](https://github.com/ava-labs/slopes/blob/48cc94f/src/utils/types.ts#L32)*

___

### `Protected` db

• **db**: *StoreAPI*

*Inherited from [APIBase](_utils_types_.apibase.md).[db](_utils_types_.apibase.md#protected-db)*

*Defined in [utils/types.ts:34](https://github.com/ava-labs/slopes/blob/48cc94f/src/utils/types.ts#L34)*

___

### `Protected` jrpcVersion

• **jrpcVersion**: *string* = "2.0"

*Inherited from [JRPCAPI](_utils_types_.jrpcapi.md).[jrpcVersion](_utils_types_.jrpcapi.md#protected-jrpcversion)*

*Defined in [utils/types.ts:80](https://github.com/ava-labs/slopes/blob/48cc94f/src/utils/types.ts#L80)*

___

### `Protected` rpcid

• **rpcid**: *number* = 1

*Inherited from [JRPCAPI](_utils_types_.jrpcapi.md).[rpcid](_utils_types_.jrpcapi.md#protected-rpcid)*

*Defined in [utils/types.ts:81](https://github.com/ava-labs/slopes/blob/48cc94f/src/utils/types.ts#L81)*

## Methods

###  alias

▸ **alias**(`endpoint`: string, `alias`: string): *Promise‹boolean›*

*Defined in [apis/admin/api.ts:48](https://github.com/ava-labs/slopes/blob/48cc94f/src/apis/admin/api.ts#L48)*

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

*Defined in [apis/admin/api.ts:66](https://github.com/ava-labs/slopes/blob/48cc94f/src/apis/admin/api.ts#L66)*

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

▸ **callMethod**(`method`: string, `params?`: Array‹object› | object, `baseurl?`: string): *Promise‹[RequestResponseData](_utils_types_.requestresponsedata.md)›*

*Inherited from [JRPCAPI](_utils_types_.jrpcapi.md)*

*Defined in [utils/types.ts:82](https://github.com/ava-labs/slopes/blob/48cc94f/src/utils/types.ts#L82)*

**Parameters:**

Name | Type |
------ | ------ |
`method` | string |
`params?` | Array‹object› &#124; object |
`baseurl?` | string |

**Returns:** *Promise‹[RequestResponseData](_utils_types_.requestresponsedata.md)›*

___

###  getBaseURL

▸ **getBaseURL**(): *string*

*Inherited from [APIBase](_utils_types_.apibase.md)*

*Defined in [utils/types.ts:57](https://github.com/ava-labs/slopes/blob/48cc94f/src/utils/types.ts#L57)*

Returns the baseurl's path.

**Returns:** *string*

___

###  getBlockchainID

▸ **getBlockchainID**(`alias`: string): *Promise‹string›*

*Defined in [apis/admin/api.ts:83](https://github.com/ava-labs/slopes/blob/48cc94f/src/apis/admin/api.ts#L83)*

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

*Inherited from [APIBase](_utils_types_.apibase.md)*

*Defined in [utils/types.ts:64](https://github.com/ava-labs/slopes/blob/48cc94f/src/utils/types.ts#L64)*

Returns the baseurl's database.

**Returns:** *StoreAPI*

___

###  getNetworkID

▸ **getNetworkID**(): *Promise‹number›*

*Defined in [apis/admin/api.ts:33](https://github.com/ava-labs/slopes/blob/48cc94f/src/apis/admin/api.ts#L33)*

Fetches the networkID from the node.

**Returns:** *Promise‹number›*

Returns a Promise<number> of the networkID.

___

###  getNodeID

▸ **getNodeID**(): *Promise‹string›*

*Defined in [apis/admin/api.ts:21](https://github.com/ava-labs/slopes/blob/48cc94f/src/apis/admin/api.ts#L21)*

Fetches the nodeID from the node.

**Returns:** *Promise‹string›*

Returns a Promise<string> of the nodeID.

___

###  getRPCID

▸ **getRPCID**(): *number*

*Inherited from [JRPCAPI](_utils_types_.jrpcapi.md)*

*Defined in [utils/types.ts:124](https://github.com/ava-labs/slopes/blob/48cc94f/src/utils/types.ts#L124)*

Returns the rpcid, a strictly-increasing number, starting from 1, indicating the next request ID that will be sent.

**Returns:** *number*

___

###  lockProfile

▸ **lockProfile**(`filename`: string): *Promise‹boolean›*

*Defined in [apis/admin/api.ts:99](https://github.com/ava-labs/slopes/blob/48cc94f/src/apis/admin/api.ts#L99)*

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

*Defined in [apis/admin/api.ts:115](https://github.com/ava-labs/slopes/blob/48cc94f/src/apis/admin/api.ts#L115)*

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

*Defined in [apis/admin/api.ts:129](https://github.com/ava-labs/slopes/blob/48cc94f/src/apis/admin/api.ts#L129)*

Returns the peers connected to the node.

**Returns:** *Promise‹Array‹string››*

Promise for the list of connected peers in <ip>:<port> format.

___

###  setBaseURL

▸ **setBaseURL**(`baseurl`: string): *void*

*Inherited from [APIBase](_utils_types_.apibase.md)*

*Defined in [utils/types.ts:41](https://github.com/ava-labs/slopes/blob/48cc94f/src/utils/types.ts#L41)*

Sets the path of the APIs baseurl.

**Parameters:**

Name | Type | Description |
------ | ------ | ------ |
`baseurl` | string | Path of the APIs baseurl - ex: "/ext/bc/avm"  |

**Returns:** *void*

___

###  startCPUProfiler

▸ **startCPUProfiler**(`filename`: string): *Promise‹boolean›*

*Defined in [apis/admin/api.ts:141](https://github.com/ava-labs/slopes/blob/48cc94f/src/apis/admin/api.ts#L141)*

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

*Defined in [apis/admin/api.ts:155](https://github.com/ava-labs/slopes/blob/48cc94f/src/apis/admin/api.ts#L155)*

Stop the CPU profile that was previously started.

**Returns:** *Promise‹boolean›*

Promise for a boolean that is true on success.
