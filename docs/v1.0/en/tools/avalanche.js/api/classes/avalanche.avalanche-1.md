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

*Defined in [index.ts:68](https://github.com/ava-labs/avalanche.js/blob/3888064/src/index.ts#L68)*

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

*Defined in [avalanche.ts:24](https://github.com/ava-labs/avalanche.js/blob/3888064/src/avalanche.ts#L24)*

#### Type declaration:

* \[ **k**: *string*\]: [APIBase](utils_types.apibase.md)

___

### `Protected` ip

• **ip**: *string*

*Inherited from [AvalancheCore](avalanchecore.avalanchecore-1.md).[ip](avalanchecore.avalanchecore-1.md#protected-ip)*

*Defined in [avalanche.ts:21](https://github.com/ava-labs/avalanche.js/blob/3888064/src/avalanche.ts#L21)*

___

### `Protected` networkID

• **networkID**: *number* = 3

*Inherited from [AvalancheCore](avalanchecore.avalanchecore-1.md).[networkID](avalanchecore.avalanchecore-1.md#protected-networkid)*

*Defined in [avalanche.ts:19](https://github.com/ava-labs/avalanche.js/blob/3888064/src/avalanche.ts#L19)*

___

### `Protected` port

• **port**: *number*

*Inherited from [AvalancheCore](avalanchecore.avalanchecore-1.md).[port](avalanchecore.avalanchecore-1.md#protected-port)*

*Defined in [avalanche.ts:22](https://github.com/ava-labs/avalanche.js/blob/3888064/src/avalanche.ts#L22)*

___

### `Protected` protocol

• **protocol**: *string*

*Inherited from [AvalancheCore](avalanchecore.avalanchecore-1.md).[protocol](avalanchecore.avalanchecore-1.md#protected-protocol)*

*Defined in [avalanche.ts:20](https://github.com/ava-labs/avalanche.js/blob/3888064/src/avalanche.ts#L20)*

___

### `Protected` url

• **url**: *string*

*Inherited from [AvalancheCore](avalanchecore.avalanchecore-1.md).[url](avalanchecore.avalanchecore-1.md#protected-url)*

*Defined in [avalanche.ts:23](https://github.com/ava-labs/avalanche.js/blob/3888064/src/avalanche.ts#L23)*

## Methods

###  AVM

▸ **AVM**(): *[AVMAPI](avmapi.avmapi-1.md)‹›*

*Defined in [index.ts:38](https://github.com/ava-labs/avalanche.js/blob/3888064/src/index.ts#L38)*

Returns a reference to the AVM RPC.

**Returns:** *[AVMAPI](avmapi.avmapi-1.md)‹›*

___

###  Admin

▸ **Admin**(): *[AdminAPI](adminapi.adminapi-1.md)‹›*

*Defined in [index.ts:31](https://github.com/ava-labs/avalanche.js/blob/3888064/src/index.ts#L31)*

Returns a reference to the Admin RPC.

**Returns:** *[AdminAPI](adminapi.adminapi-1.md)‹›*

___

###  Health

▸ **Health**(): *[HealthAPI](healthapi.healthapi-1.md)‹›*

*Defined in [index.ts:45](https://github.com/ava-labs/avalanche.js/blob/3888064/src/index.ts#L45)*

Returns a reference to the Health RPC for a node.

**Returns:** *[HealthAPI](healthapi.healthapi-1.md)‹›*

___

###  Info

▸ **Info**(): *[InfoAPI](infoapi.infoapi-1.md)‹›*

*Defined in [index.ts:52](https://github.com/ava-labs/avalanche.js/blob/3888064/src/index.ts#L52)*

Returns a reference to the Info RPC for a node.

**Returns:** *[InfoAPI](infoapi.infoapi-1.md)‹›*

___

###  NodeKeys

▸ **NodeKeys**(): *[KeystoreAPI](keystoreapi.keystoreapi-1.md)‹›*

*Defined in [index.ts:59](https://github.com/ava-labs/avalanche.js/blob/3888064/src/index.ts#L59)*

Returns a reference to the Keystore RPC for a node. We label it "NodeKeys" to reduce confusion about what it's accessing.

**Returns:** *[KeystoreAPI](keystoreapi.keystoreapi-1.md)‹›*

___

###  Platform

▸ **Platform**(): *[PlatformAPI](platformapi.platformapi-1.md)‹›*

*Defined in [index.ts:66](https://github.com/ava-labs/avalanche.js/blob/3888064/src/index.ts#L66)*

Returns a reference to the Platform RPC.

**Returns:** *[PlatformAPI](platformapi.platformapi-1.md)‹›*

___

###  addAPI

▸ **addAPI**‹**GA**›(`apiName`: string, `constructorFN`: object, `baseurl`: string, ...`args`: Array‹any›): *void*

*Inherited from [AvalancheCore](avalanchecore.avalanchecore-1.md).[addAPI](avalanchecore.avalanchecore-1.md#addapi)*

*Defined in [avalanche.ts:101](https://github.com/ava-labs/avalanche.js/blob/3888064/src/avalanche.ts#L101)*

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
`constructorFN` | object | - | A reference to the class which instantiates the API |
`baseurl` | string | undefined | Path to resolve to reach the API   |
`...args` | Array‹any› | - | - |

**Returns:** *void*

___

###  api

▸ **api**‹**GA**›(`apiName`: string): *GA*

*Inherited from [AvalancheCore](avalanchecore.avalanchecore-1.md).[api](avalanchecore.avalanchecore-1.md#api)*

*Defined in [avalanche.ts:114](https://github.com/ava-labs/avalanche.js/blob/3888064/src/avalanche.ts#L114)*

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

*Defined in [avalanche.ts:175](https://github.com/ava-labs/avalanche.js/blob/3888064/src/avalanche.ts#L175)*

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

*Defined in [avalanche.ts:160](https://github.com/ava-labs/avalanche.js/blob/3888064/src/avalanche.ts#L160)*

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

*Defined in [avalanche.ts:50](https://github.com/ava-labs/avalanche.js/blob/3888064/src/avalanche.ts#L50)*

Returns the IP for the AVA node.

**Returns:** *string*

___

###  getNetworkID

▸ **getNetworkID**(): *number*

*Inherited from [AvalancheCore](avalanchecore.avalanchecore-1.md).[getNetworkID](avalanchecore.avalanchecore-1.md#getnetworkid)*

*Defined in [avalanche.ts:71](https://github.com/ava-labs/avalanche.js/blob/3888064/src/avalanche.ts#L71)*

Returns the networkID;

**Returns:** *number*

___

###  getPort

▸ **getPort**(): *number*

*Inherited from [AvalancheCore](avalanchecore.avalanchecore-1.md).[getPort](avalanchecore.avalanchecore-1.md#getport)*

*Defined in [avalanche.ts:57](https://github.com/ava-labs/avalanche.js/blob/3888064/src/avalanche.ts#L57)*

Returns the port for the AVA node.

**Returns:** *number*

___

###  getProtocol

▸ **getProtocol**(): *string*

*Inherited from [AvalancheCore](avalanchecore.avalanchecore-1.md).[getProtocol](avalanchecore.avalanchecore-1.md#getprotocol)*

*Defined in [avalanche.ts:43](https://github.com/ava-labs/avalanche.js/blob/3888064/src/avalanche.ts#L43)*

Returns the protocol such as "http", "https", "git", "ws", etc.

**Returns:** *string*

___

###  getURL

▸ **getURL**(): *string*

*Inherited from [AvalancheCore](avalanchecore.avalanchecore-1.md).[getURL](avalanchecore.avalanchecore-1.md#geturl)*

*Defined in [avalanche.ts:64](https://github.com/ava-labs/avalanche.js/blob/3888064/src/avalanche.ts#L64)*

Returns the URL of the AVA node (ip + port);

**Returns:** *string*

___

###  patch

▸ **patch**(`baseurl`: string, `getdata`: object, `postdata`: string | object | ArrayBuffer | ArrayBufferView, `headers`: object, `axiosConfig`: AxiosRequestConfig): *Promise‹[RequestResponseData](utils_types.requestresponsedata.md)›*

*Inherited from [AvalancheCore](avalanchecore.avalanchecore-1.md).[patch](avalanchecore.avalanchecore-1.md#patch)*

*Defined in [avalanche.ts:223](https://github.com/ava-labs/avalanche.js/blob/3888064/src/avalanche.ts#L223)*

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

*Defined in [avalanche.ts:191](https://github.com/ava-labs/avalanche.js/blob/3888064/src/avalanche.ts#L191)*

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

*Defined in [avalanche.ts:207](https://github.com/ava-labs/avalanche.js/blob/3888064/src/avalanche.ts#L207)*

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

*Defined in [avalanche.ts:33](https://github.com/ava-labs/avalanche.js/blob/3888064/src/avalanche.ts#L33)*

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

*Defined in [avalanche.ts:78](https://github.com/ava-labs/avalanche.js/blob/3888064/src/avalanche.ts#L78)*

Sets the networkID

**Parameters:**

Name | Type |
------ | ------ |
`netid` | number |

**Returns:** *void*
