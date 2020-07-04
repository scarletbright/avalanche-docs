[avalanche](../README.md) › [Avalanche](../modules/avalanche.md) › [Avalanche](avalanche.avalanche-1.md)

# Class: Avalanche

Avalanche.js is middleware for interacting with AVA node RPC APIs.

Example usage:
```js
let avalanche = new Avalanche("127.0.0.1", 9650, "https");
```

## Hierarchy

* [AvalancheCore](avalanchecore.avalanchecore-1.md)

  ↳ **Avalanche**

## Index

### Constructors

* [constructor](avalanche.avalanche-1.md#constructor)

### Properties

* [apis](avalanche.avalanche-1.md#protected-apis)
* [ip](avalanche.avalanche-1.md#protected-ip)
* [networkID](avalanche.avalanche-1.md#protected-networkid)
* [port](avalanche.avalanche-1.md#protected-port)
* [protocol](avalanche.avalanche-1.md#protected-protocol)
* [url](avalanche.avalanche-1.md#protected-url)

### Methods

* [AVM](avalanche.avalanche-1.md#avm)
* [Admin](avalanche.avalanche-1.md#admin)
* [Health](avalanche.avalanche-1.md#health)
* [Info](avalanche.avalanche-1.md#info)
* [Metrics](avalanche.avalanche-1.md#metrics)
* [NodeKeys](avalanche.avalanche-1.md#nodekeys)
* [Platform](avalanche.avalanche-1.md#platform)
* [addAPI](avalanche.avalanche-1.md#addapi)
* [api](avalanche.avalanche-1.md#api)
* [delete](avalanche.avalanche-1.md#delete)
* [get](avalanche.avalanche-1.md#get)
* [getIP](avalanche.avalanche-1.md#getip)
* [getNetworkID](avalanche.avalanche-1.md#getnetworkid)
* [getPort](avalanche.avalanche-1.md#getport)
* [getProtocol](avalanche.avalanche-1.md#getprotocol)
* [getURL](avalanche.avalanche-1.md#geturl)
* [patch](avalanche.avalanche-1.md#patch)
* [post](avalanche.avalanche-1.md#post)
* [put](avalanche.avalanche-1.md#put)
* [setAddress](avalanche.avalanche-1.md#setaddress)
* [setNetworkID](avalanche.avalanche-1.md#setnetworkid)

## Constructors

###  constructor

\+ **new Avalanche**(`ip`: string, `port`: number, `protocol`: string, `networkID`: number, `avmChainID`: string, `skipinit`: boolean): *[Avalanche](avalanche.avalanche-1.md)*

*Overrides [AvalancheCore](avalanchecore.avalanchecore-1.md).[constructor](avalanchecore.avalanchecore-1.md#constructor)*

*Defined in [src/index.ts:62](https://github.com/ava-labs/avalanche.js/blob/eabcc2f/src/index.ts#L62)*

Creates a new AVA instance. Sets the address and port of the main AVA Client.

**Parameters:**

Name | Type | Default | Description |
------ | ------ | ------ | ------ |
`ip` | string | - | The hostname to resolve to reach the AVA Client RPC APIs |
`port` | number | - | The port to resolve to reach the AVA Client RPC APIs |
`protocol` | string | "http" | The protocol string to use before a "://" in a request, ex: "http", "https", "git", "ws", etc ... |
`networkID` | number | 3 | - |
`avmChainID` | string | undefined | Sets the blockchainID for the AVM. Will try to auto-detect, otherwise default "4R5p2RXDGLqaifZE4hHWH9owe34pfoBULn1DrQTWivjg8o4aH" |
`skipinit` | boolean | false | Skips creating the APIs  |

**Returns:** *[Avalanche](avalanche.avalanche-1.md)*

## Properties

### `Protected` apis

• **apis**: *object*

*Inherited from [AvalancheCore](avalanchecore.avalanchecore-1.md).[apis](avalanchecore.avalanchecore-1.md#protected-apis)*

*Defined in [src/avalanche.ts:28](https://github.com/ava-labs/avalanche.js/blob/eabcc2f/src/avalanche.ts#L28)*

#### Type declaration:

* \[ **k**: *string*\]: [APIBase](utils_types.apibase.md)

___

### `Protected` ip

• **ip**: *string*

*Inherited from [AvalancheCore](avalanchecore.avalanchecore-1.md).[ip](avalanchecore.avalanchecore-1.md#protected-ip)*

*Defined in [src/avalanche.ts:22](https://github.com/ava-labs/avalanche.js/blob/eabcc2f/src/avalanche.ts#L22)*

___

### `Protected` networkID

• **networkID**: *number* = 3

*Inherited from [AvalancheCore](avalanchecore.avalanchecore-1.md).[networkID](avalanchecore.avalanchecore-1.md#protected-networkid)*

*Defined in [src/avalanche.ts:18](https://github.com/ava-labs/avalanche.js/blob/eabcc2f/src/avalanche.ts#L18)*

___

### `Protected` port

• **port**: *number*

*Inherited from [AvalancheCore](avalanchecore.avalanchecore-1.md).[port](avalanchecore.avalanchecore-1.md#protected-port)*

*Defined in [src/avalanche.ts:24](https://github.com/ava-labs/avalanche.js/blob/eabcc2f/src/avalanche.ts#L24)*

___

### `Protected` protocol

• **protocol**: *string*

*Inherited from [AvalancheCore](avalanchecore.avalanchecore-1.md).[protocol](avalanchecore.avalanchecore-1.md#protected-protocol)*

*Defined in [src/avalanche.ts:20](https://github.com/ava-labs/avalanche.js/blob/eabcc2f/src/avalanche.ts#L20)*

___

### `Protected` url

• **url**: *string*

*Inherited from [AvalancheCore](avalanchecore.avalanchecore-1.md).[url](avalanchecore.avalanchecore-1.md#protected-url)*

*Defined in [src/avalanche.ts:26](https://github.com/ava-labs/avalanche.js/blob/eabcc2f/src/avalanche.ts#L26)*

## Methods

###  AVM

▸ **AVM**(): *[AVMAPI](avmapi.avmapi-1.md)‹›*

*Defined in [src/index.ts:36](https://github.com/ava-labs/avalanche.js/blob/eabcc2f/src/index.ts#L36)*

Returns a reference to the AVM RPC.

**Returns:** *[AVMAPI](avmapi.avmapi-1.md)‹›*

___

###  Admin

▸ **Admin**(): *[AdminAPI](adminapi.adminapi-1.md)‹›*

*Defined in [src/index.ts:31](https://github.com/ava-labs/avalanche.js/blob/eabcc2f/src/index.ts#L31)*

Returns a reference to the Admin RPC.

**Returns:** *[AdminAPI](adminapi.adminapi-1.md)‹›*

___

###  Health

▸ **Health**(): *[HealthAPI](healthapi.healthapi-1.md)‹›*

*Defined in [src/index.ts:41](https://github.com/ava-labs/avalanche.js/blob/eabcc2f/src/index.ts#L41)*

Returns a reference to the Health RPC for a node.

**Returns:** *[HealthAPI](healthapi.healthapi-1.md)‹›*

___

###  Info

▸ **Info**(): *[InfoAPI](infoapi.infoapi-1.md)‹›*

*Defined in [src/index.ts:46](https://github.com/ava-labs/avalanche.js/blob/eabcc2f/src/index.ts#L46)*

Returns a reference to the Info RPC for a node.

**Returns:** *[InfoAPI](infoapi.infoapi-1.md)‹›*

___

###  Metrics

▸ **Metrics**(): *[MetricsAPI](metricsapi.metricsapi-1.md)‹›*

*Defined in [src/index.ts:51](https://github.com/ava-labs/avalanche.js/blob/eabcc2f/src/index.ts#L51)*

Returns a reference to the Metrics RPC.

**Returns:** *[MetricsAPI](metricsapi.metricsapi-1.md)‹›*

___

###  NodeKeys

▸ **NodeKeys**(): *[KeystoreAPI](keystoreapi.keystoreapi-1.md)‹›*

*Defined in [src/index.ts:57](https://github.com/ava-labs/avalanche.js/blob/eabcc2f/src/index.ts#L57)*

Returns a reference to the Keystore RPC for a node. We label it "NodeKeys" to reduce
confusion about what it's accessing.

**Returns:** *[KeystoreAPI](keystoreapi.keystoreapi-1.md)‹›*

___

###  Platform

▸ **Platform**(): *[PlatformAPI](platformapi.platformapi-1.md)‹›*

*Defined in [src/index.ts:62](https://github.com/ava-labs/avalanche.js/blob/eabcc2f/src/index.ts#L62)*

Returns a reference to the Platform RPC.

**Returns:** *[PlatformAPI](platformapi.platformapi-1.md)‹›*

___

###  addAPI

▸ **addAPI**‹**GA**›(`apiName`: string, `ConstructorFN`: object, `baseurl`: string, ...`args`: Array‹any›): *void*

*Inherited from [AvalancheCore](avalanchecore.avalanchecore-1.md).[addAPI](avalanchecore.avalanchecore-1.md#addapi)*

*Defined in [src/avalanche.ts:96](https://github.com/ava-labs/avalanche.js/blob/eabcc2f/src/avalanche.ts#L96)*

Adds an API to the middleware. The API resolves to a registered blockchain's RPC.

In TypeScript:
```js
avalanche.addAPI<MyVMClass>("mychain", MyVMClass, "/ext/bc/mychain");
```

In Javascript:
```js
avalanche.addAPI("mychain", MyVMClass, "/ext/bc/mychain");
```

**Type parameters:**

▪ **GA**: *[APIBase](utils_types.apibase.md)*

Class of the API being added

**Parameters:**

Name | Type | Default | Description |
------ | ------ | ------ | ------ |
`apiName` | string | - | A label for referencing the API in the future |
`ConstructorFN` | object | - | - |
`baseurl` | string | undefined | Path to resolve to reach the API   |
`...args` | Array‹any› | - | - |

**Returns:** *void*

___

###  api

▸ **api**‹**GA**›(`apiName`: string): *GA*

*Inherited from [AvalancheCore](avalanchecore.avalanchecore-1.md).[api](avalanchecore.avalanchecore-1.md#api)*

*Defined in [src/avalanche.ts:112](https://github.com/ava-labs/avalanche.js/blob/eabcc2f/src/avalanche.ts#L112)*

Retrieves a reference to an API by its apiName label.

**Type parameters:**

▪ **GA**: *[APIBase](utils_types.apibase.md)*

**Parameters:**

Name | Type | Description |
------ | ------ | ------ |
`apiName` | string | Name of the API to return  |

**Returns:** *GA*

___

###  delete

▸ **delete**(`baseurl`: string, `getdata`: object, `headers`: object, `axiosConfig`: AxiosRequestConfig): *Promise‹[RequestResponseData](utils_types.requestresponsedata.md)›*

*Inherited from [AvalancheCore](avalanchecore.avalanchecore-1.md).[delete](avalanchecore.avalanchecore-1.md#delete)*

*Defined in [src/avalanche.ts:184](https://github.com/ava-labs/avalanche.js/blob/eabcc2f/src/avalanche.ts#L184)*

Makes a DELETE call to an API.

**Parameters:**

Name | Type | Default | Description |
------ | ------ | ------ | ------ |
`baseurl` | string | - | Path to the API |
`getdata` | object | - | Object containing the key value pairs sent in DELETE |
`headers` | object | {} | An array HTTP Request Headers |
`axiosConfig` | AxiosRequestConfig | undefined | Configuration for the axios javascript library that will be the foundation for the rest of the parameters  |

**Returns:** *Promise‹[RequestResponseData](utils_types.requestresponsedata.md)›*

A promise for [RequestResponseData](../modules/avalanche.md#requestresponsedata)

___

###  get

▸ **get**(`baseurl`: string, `getdata`: object, `headers`: object, `axiosConfig`: AxiosRequestConfig): *Promise‹[RequestResponseData](utils_types.requestresponsedata.md)›*

*Inherited from [AvalancheCore](avalanchecore.avalanchecore-1.md).[get](avalanchecore.avalanchecore-1.md#get)*

*Defined in [src/avalanche.ts:161](https://github.com/ava-labs/avalanche.js/blob/eabcc2f/src/avalanche.ts#L161)*

Makes a GET call to an API.

**Parameters:**

Name | Type | Default | Description |
------ | ------ | ------ | ------ |
`baseurl` | string | - | Path to the api |
`getdata` | object | - | Object containing the key value pairs sent in GET |
`headers` | object | {} | An array HTTP Request Headers |
`axiosConfig` | AxiosRequestConfig | undefined | Configuration for the axios javascript library that will be the foundation for the rest of the parameters  |

**Returns:** *Promise‹[RequestResponseData](utils_types.requestresponsedata.md)›*

A promise for [RequestResponseData](../modules/avalanche.md#requestresponsedata)

___

###  getIP

▸ **getIP**(): *string*

*Inherited from [AvalancheCore](avalanchecore.avalanchecore-1.md).[getIP](avalanchecore.avalanchecore-1.md#getip)*

*Defined in [src/avalanche.ts:53](https://github.com/ava-labs/avalanche.js/blob/eabcc2f/src/avalanche.ts#L53)*

Returns the IP for the AVA node.

**Returns:** *string*

___

###  getNetworkID

▸ **getNetworkID**(): *number*

*Inherited from [AvalancheCore](avalanchecore.avalanchecore-1.md).[getNetworkID](avalanchecore.avalanchecore-1.md#getnetworkid)*

*Defined in [src/avalanche.ts:68](https://github.com/ava-labs/avalanche.js/blob/eabcc2f/src/avalanche.ts#L68)*

Returns the networkID;

**Returns:** *number*

___

###  getPort

▸ **getPort**(): *number*

*Inherited from [AvalancheCore](avalanchecore.avalanchecore-1.md).[getPort](avalanchecore.avalanchecore-1.md#getport)*

*Defined in [src/avalanche.ts:58](https://github.com/ava-labs/avalanche.js/blob/eabcc2f/src/avalanche.ts#L58)*

Returns the port for the AVA node.

**Returns:** *number*

___

###  getProtocol

▸ **getProtocol**(): *string*

*Inherited from [AvalancheCore](avalanchecore.avalanchecore-1.md).[getProtocol](avalanchecore.avalanchecore-1.md#getprotocol)*

*Defined in [src/avalanche.ts:48](https://github.com/ava-labs/avalanche.js/blob/eabcc2f/src/avalanche.ts#L48)*

Returns the protocol such as "http", "https", "git", "ws", etc.

**Returns:** *string*

___

###  getURL

▸ **getURL**(): *string*

*Inherited from [AvalancheCore](avalanchecore.avalanchecore-1.md).[getURL](avalanchecore.avalanchecore-1.md#geturl)*

*Defined in [src/avalanche.ts:63](https://github.com/ava-labs/avalanche.js/blob/eabcc2f/src/avalanche.ts#L63)*

Returns the URL of the AVA node (ip + port);

**Returns:** *string*

___

###  patch

▸ **patch**(`baseurl`: string, `getdata`: object, `postdata`: string | object | ArrayBuffer | ArrayBufferView, `headers`: object, `axiosConfig`: AxiosRequestConfig): *Promise‹[RequestResponseData](utils_types.requestresponsedata.md)›*

*Inherited from [AvalancheCore](avalanchecore.avalanchecore-1.md).[patch](avalanchecore.avalanchecore-1.md#patch)*

*Defined in [src/avalanche.ts:258](https://github.com/ava-labs/avalanche.js/blob/eabcc2f/src/avalanche.ts#L258)*

Makes a PATCH call to an API.

**Parameters:**

Name | Type | Default | Description |
------ | ------ | ------ | ------ |
`baseurl` | string | - | Path to the baseurl |
`getdata` | object | - | Object containing the key value pairs sent in PATCH |
`postdata` | string &#124; object &#124; ArrayBuffer &#124; ArrayBufferView | - | Object containing the key value pairs sent in PATCH |
`headers` | object | {} | An array HTTP Request Headers |
`axiosConfig` | AxiosRequestConfig | undefined | Configuration for the axios javascript library that will be the foundation for the rest of the parameters  |

**Returns:** *Promise‹[RequestResponseData](utils_types.requestresponsedata.md)›*

A promise for [RequestResponseData](../modules/avalanche.md#requestresponsedata)

___

###  post

▸ **post**(`baseurl`: string, `getdata`: object, `postdata`: string | object | ArrayBuffer | ArrayBufferView, `headers`: object, `axiosConfig`: AxiosRequestConfig): *Promise‹[RequestResponseData](utils_types.requestresponsedata.md)›*

*Inherited from [AvalancheCore](avalanchecore.avalanchecore-1.md).[post](avalanchecore.avalanchecore-1.md#post)*

*Defined in [src/avalanche.ts:208](https://github.com/ava-labs/avalanche.js/blob/eabcc2f/src/avalanche.ts#L208)*

Makes a POST call to an API.

**Parameters:**

Name | Type | Default | Description |
------ | ------ | ------ | ------ |
`baseurl` | string | - | Path to the API |
`getdata` | object | - | Object containing the key value pairs sent in POST |
`postdata` | string &#124; object &#124; ArrayBuffer &#124; ArrayBufferView | - | Object containing the key value pairs sent in POST |
`headers` | object | {} | An array HTTP Request Headers |
`axiosConfig` | AxiosRequestConfig | undefined | Configuration for the axios javascript library that will be the foundation for the rest of the parameters  |

**Returns:** *Promise‹[RequestResponseData](utils_types.requestresponsedata.md)›*

A promise for [RequestResponseData](../modules/avalanche.md#requestresponsedata)

___

###  put

▸ **put**(`baseurl`: string, `getdata`: object, `postdata`: string | object | ArrayBuffer | ArrayBufferView, `headers`: object, `axiosConfig`: AxiosRequestConfig): *Promise‹[RequestResponseData](utils_types.requestresponsedata.md)›*

*Inherited from [AvalancheCore](avalanchecore.avalanchecore-1.md).[put](avalanchecore.avalanchecore-1.md#put)*

*Defined in [src/avalanche.ts:233](https://github.com/ava-labs/avalanche.js/blob/eabcc2f/src/avalanche.ts#L233)*

Makes a PUT call to an API.

**Parameters:**

Name | Type | Default | Description |
------ | ------ | ------ | ------ |
`baseurl` | string | - | Path to the baseurl |
`getdata` | object | - | Object containing the key value pairs sent in PUT |
`postdata` | string &#124; object &#124; ArrayBuffer &#124; ArrayBufferView | - | Object containing the key value pairs sent in PUT |
`headers` | object | {} | An array HTTP Request Headers |
`axiosConfig` | AxiosRequestConfig | undefined | Configuration for the axios javascript library that will be the foundation for the rest of the parameters  |

**Returns:** *Promise‹[RequestResponseData](utils_types.requestresponsedata.md)›*

A promise for [RequestResponseData](../modules/avalanche.md#requestresponsedata)

___

###  setAddress

▸ **setAddress**(`ip`: string, `port`: number, `protocol`: string): *void*

*Inherited from [AvalancheCore](avalanchecore.avalanchecore-1.md).[setAddress](avalanchecore.avalanchecore-1.md#setaddress)*

*Defined in [src/avalanche.ts:38](https://github.com/ava-labs/avalanche.js/blob/eabcc2f/src/avalanche.ts#L38)*

Sets the address and port of the main AVA Client.

**Parameters:**

Name | Type | Default | Description |
------ | ------ | ------ | ------ |
`ip` | string | - | The hostname to resolve to reach the AVA Client RPC APIs |
`port` | number | - | The port to resolve to reach the AVA Client RPC APIs |
`protocol` | string | "http" | The protocol string to use before a "://" in a request, ex: "http", "https", "git", "ws", etc ...  |

**Returns:** *void*

___

###  setNetworkID

▸ **setNetworkID**(`netid`: number): *void*

*Inherited from [AvalancheCore](avalanchecore.avalanchecore-1.md).[setNetworkID](avalanchecore.avalanchecore-1.md#setnetworkid)*

*Defined in [src/avalanche.ts:73](https://github.com/ava-labs/avalanche.js/blob/eabcc2f/src/avalanche.ts#L73)*

Sets the networkID

**Parameters:**

Name | Type |
------ | ------ |
`netid` | number |

**Returns:** *void*
