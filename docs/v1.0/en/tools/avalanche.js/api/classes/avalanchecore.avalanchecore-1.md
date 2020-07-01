[avalanche](../README.md) › [AvalancheCore](../modules/avalanchecore.md) › [AvalancheCore](avalanchecore.avalanchecore-1.md)

# Class: AvalancheCore

AvalancheCore is middleware for interacting with AVA node RPC APIs.

Example usage:
```js
let avalanche = new AvalancheCore("127.0.0.1", 9650, "https");
```

## Hierarchy

* **AvalancheCore**

  ↳ [Avalanche](avalanche.avalanche-1.md)

## Index

### Constructors

* [constructor](avalanchecore.avalanchecore-1.md#constructor)

### Properties

* [apis](avalanchecore.avalanchecore-1.md#protected-apis)
* [ip](avalanchecore.avalanchecore-1.md#protected-ip)
* [networkID](avalanchecore.avalanchecore-1.md#protected-networkid)
* [port](avalanchecore.avalanchecore-1.md#protected-port)
* [protocol](avalanchecore.avalanchecore-1.md#protected-protocol)
* [url](avalanchecore.avalanchecore-1.md#protected-url)

### Methods

* [addAPI](avalanchecore.avalanchecore-1.md#addapi)
* [api](avalanchecore.avalanchecore-1.md#api)
* [delete](avalanchecore.avalanchecore-1.md#delete)
* [get](avalanchecore.avalanchecore-1.md#get)
* [getIP](avalanchecore.avalanchecore-1.md#getip)
* [getNetworkID](avalanchecore.avalanchecore-1.md#getnetworkid)
* [getPort](avalanchecore.avalanchecore-1.md#getport)
* [getProtocol](avalanchecore.avalanchecore-1.md#getprotocol)
* [getURL](avalanchecore.avalanchecore-1.md#geturl)
* [patch](avalanchecore.avalanchecore-1.md#patch)
* [post](avalanchecore.avalanchecore-1.md#post)
* [put](avalanchecore.avalanchecore-1.md#put)
* [setAddress](avalanchecore.avalanchecore-1.md#setaddress)
* [setNetworkID](avalanchecore.avalanchecore-1.md#setnetworkid)

## Constructors

###  constructor

\+ **new AvalancheCore**(`ip`: string, `port`: number, `protocol`: string): *[AvalancheCore](avalanchecore.avalanchecore-1.md)*

*Defined in [avalanche.ts:225](https://github.com/ava-labs/avalanche.js/blob/3888064/src/avalanche.ts#L225)*

Creates a new Avalanche instance. Sets the address and port of the main AVA Client.

**Parameters:**

Name | Type | Default | Description |
------ | ------ | ------ | ------ |
`ip` | string | - | The hostname to resolve to reach the AVA Client APIs |
`port` | number | - | The port to resolve to reach the AVA Client APIs |
`protocol` | string | "http" | The protocol string to use before a "://" in a request, ex: "http", "https", "git", "ws", etc ...  |

**Returns:** *[AvalancheCore](avalanchecore.avalanchecore-1.md)*

## Properties

### `Protected` apis

• **apis**: *object*

*Defined in [avalanche.ts:24](https://github.com/ava-labs/avalanche.js/blob/3888064/src/avalanche.ts#L24)*

#### Type declaration:

* \[ **k**: *string*\]: [APIBase](utils_types.apibase.md)

___

### `Protected` ip

• **ip**: *string*

*Defined in [avalanche.ts:21](https://github.com/ava-labs/avalanche.js/blob/3888064/src/avalanche.ts#L21)*

___

### `Protected` networkID

• **networkID**: *number* = 3

*Defined in [avalanche.ts:19](https://github.com/ava-labs/avalanche.js/blob/3888064/src/avalanche.ts#L19)*

___

### `Protected` port

• **port**: *number*

*Defined in [avalanche.ts:22](https://github.com/ava-labs/avalanche.js/blob/3888064/src/avalanche.ts#L22)*

___

### `Protected` protocol

• **protocol**: *string*

*Defined in [avalanche.ts:20](https://github.com/ava-labs/avalanche.js/blob/3888064/src/avalanche.ts#L20)*

___

### `Protected` url

• **url**: *string*

*Defined in [avalanche.ts:23](https://github.com/ava-labs/avalanche.js/blob/3888064/src/avalanche.ts#L23)*

## Methods

###  addAPI

▸ **addAPI**‹**GA**›(`apiName`: string, `constructorFN`: object, `baseurl`: string, ...`args`: Array‹any›): *void*

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

A promise for [RequestResponseData](utils_types.requestresponsedata.md)

___

###  get

▸ **get**(`baseurl`: string, `getdata`: object, `headers`: object, `axiosConfig`: AxiosRequestConfig): *Promise‹[RequestResponseData](utils_types.requestresponsedata.md)›*

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

A promise for [RequestResponseData](utils_types.requestresponsedata.md)

___

###  getIP

▸ **getIP**(): *string*

*Defined in [avalanche.ts:50](https://github.com/ava-labs/avalanche.js/blob/3888064/src/avalanche.ts#L50)*

Returns the IP for the AVA node.

**Returns:** *string*

___

###  getNetworkID

▸ **getNetworkID**(): *number*

*Defined in [avalanche.ts:71](https://github.com/ava-labs/avalanche.js/blob/3888064/src/avalanche.ts#L71)*

Returns the networkID;

**Returns:** *number*

___

###  getPort

▸ **getPort**(): *number*

*Defined in [avalanche.ts:57](https://github.com/ava-labs/avalanche.js/blob/3888064/src/avalanche.ts#L57)*

Returns the port for the AVA node.

**Returns:** *number*

___

###  getProtocol

▸ **getProtocol**(): *string*

*Defined in [avalanche.ts:43](https://github.com/ava-labs/avalanche.js/blob/3888064/src/avalanche.ts#L43)*

Returns the protocol such as "http", "https", "git", "ws", etc.

**Returns:** *string*

___

###  getURL

▸ **getURL**(): *string*

*Defined in [avalanche.ts:64](https://github.com/ava-labs/avalanche.js/blob/3888064/src/avalanche.ts#L64)*

Returns the URL of the AVA node (ip + port);

**Returns:** *string*

___

###  patch

▸ **patch**(`baseurl`: string, `getdata`: object, `postdata`: string | object | ArrayBuffer | ArrayBufferView, `headers`: object, `axiosConfig`: AxiosRequestConfig): *Promise‹[RequestResponseData](utils_types.requestresponsedata.md)›*

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

A promise for [RequestResponseData](utils_types.requestresponsedata.md)

___

###  post

▸ **post**(`baseurl`: string, `getdata`: object, `postdata`: string | object | ArrayBuffer | ArrayBufferView, `headers`: object, `axiosConfig`: AxiosRequestConfig): *Promise‹[RequestResponseData](utils_types.requestresponsedata.md)›*

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

A promise for [RequestResponseData](utils_types.requestresponsedata.md)

___

###  put

▸ **put**(`baseurl`: string, `getdata`: object, `postdata`: string | object | ArrayBuffer | ArrayBufferView, `headers`: object, `axiosConfig`: AxiosRequestConfig): *Promise‹[RequestResponseData](utils_types.requestresponsedata.md)›*

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

A promise for [RequestResponseData](utils_types.requestresponsedata.md)

___

###  setAddress

▸ **setAddress**(`ip`: string, `port`: number, `protocol`: string): *void*

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

*Defined in [avalanche.ts:78](https://github.com/ava-labs/avalanche.js/blob/3888064/src/avalanche.ts#L78)*

Sets the networkID

**Parameters:**

Name | Type |
------ | ------ |
`netid` | number |

**Returns:** *void*
