[slopes - v1.7.3](../README.md) › ["slopes"](../modules/_slopes_.md) › [SlopesCore](_slopes_.slopescore.md)

# Class: SlopesCore

SlopesCore is middleware for interacting with AVA node RPC APIs.

Example usage:
```js
let slopes = new SlopesCore("127.0.0.1", 9650, "https");
```

## Hierarchy

* **SlopesCore**

  ↳ [Slopes](_index_.slopes.md)

## Index

### Constructors

* [constructor](_slopes_.slopescore.md#constructor)

### Properties

* [apis](_slopes_.slopescore.md#protected-apis)
* [ip](_slopes_.slopescore.md#protected-ip)
* [networkID](_slopes_.slopescore.md#protected-networkid)
* [port](_slopes_.slopescore.md#protected-port)
* [protocol](_slopes_.slopescore.md#protected-protocol)
* [url](_slopes_.slopescore.md#protected-url)

### Methods

* [addAPI](_slopes_.slopescore.md#addapi)
* [api](_slopes_.slopescore.md#api)
* [delete](_slopes_.slopescore.md#delete)
* [get](_slopes_.slopescore.md#get)
* [getIP](_slopes_.slopescore.md#getip)
* [getNetworkID](_slopes_.slopescore.md#getnetworkid)
* [getPort](_slopes_.slopescore.md#getport)
* [getProtocol](_slopes_.slopescore.md#getprotocol)
* [getURL](_slopes_.slopescore.md#geturl)
* [patch](_slopes_.slopescore.md#patch)
* [post](_slopes_.slopescore.md#post)
* [put](_slopes_.slopescore.md#put)
* [setAddress](_slopes_.slopescore.md#setaddress)
* [setNetworkID](_slopes_.slopescore.md#setnetworkid)

## Constructors

###  constructor

\+ **new SlopesCore**(`ip`: string, `port`: number, `protocol`: string): *[SlopesCore](_slopes_.slopescore.md)*

*Defined in [slopes.ts:224](https://github.com/ava-labs/slopes/blob/48cc94f/src/slopes.ts#L224)*

Creates a new Slopes instance. Sets the address and port of the main AVA Client.

**Parameters:**

Name | Type | Default | Description |
------ | ------ | ------ | ------ |
`ip` | string | - | The hostname to resolve to reach the AVA Client APIs |
`port` | number | - | The port to resolve to reach the AVA Client APIs |
`protocol` | string | "http" | The protocol string to use before a "://" in a request, ex: "http", "https", "git", "ws", etc ...  |

**Returns:** *[SlopesCore](_slopes_.slopescore.md)*

## Properties

### `Protected` apis

• **apis**: *object*

*Defined in [slopes.ts:23](https://github.com/ava-labs/slopes/blob/48cc94f/src/slopes.ts#L23)*

#### Type declaration:

* \[ **k**: *string*\]: [APIBase](_utils_types_.apibase.md)

___

### `Protected` ip

• **ip**: *string*

*Defined in [slopes.ts:20](https://github.com/ava-labs/slopes/blob/48cc94f/src/slopes.ts#L20)*

___

### `Protected` networkID

• **networkID**: *number* = 3

*Defined in [slopes.ts:18](https://github.com/ava-labs/slopes/blob/48cc94f/src/slopes.ts#L18)*

___

### `Protected` port

• **port**: *number*

*Defined in [slopes.ts:21](https://github.com/ava-labs/slopes/blob/48cc94f/src/slopes.ts#L21)*

___

### `Protected` protocol

• **protocol**: *string*

*Defined in [slopes.ts:19](https://github.com/ava-labs/slopes/blob/48cc94f/src/slopes.ts#L19)*

___

### `Protected` url

• **url**: *string*

*Defined in [slopes.ts:22](https://github.com/ava-labs/slopes/blob/48cc94f/src/slopes.ts#L22)*

## Methods

###  addAPI

▸ **addAPI**<**GA**>(`apiName`: string, `constructorFN`: object, `baseurl`: string, ...`args`: Array‹any›): *void*

*Defined in [slopes.ts:100](https://github.com/ava-labs/slopes/blob/48cc94f/src/slopes.ts#L100)*

Adds an API to the middleware. The API resolves to a registered blockchain's RPC.

In TypeScript:
```js
slopes.addAPI<MyVMClass>("mychain", MyVMClass, "/ext/bc/mychain");
```

In Javascript:
```js
slopes.addAPI("mychain", MyVMClass, "/ext/bc/mychain");
```

**Type parameters:**

▪ **GA**: *[APIBase](_utils_types_.apibase.md)*

Class of the API being added

**Parameters:**

Name | Type | Default | Description |
------ | ------ | ------ | ------ |
`apiName` | string | - | A label for referencing the API in the future |
`constructorFN` | object | - | A reference to the class which instantiates the API |
`baseurl` | string |  undefined | Path to resolve to reach the API   |
`...args` | Array‹any› | - | - |

**Returns:** *void*

___

###  api

▸ **api**<**GA**>(`apiName`: string): *GA*

*Defined in [slopes.ts:113](https://github.com/ava-labs/slopes/blob/48cc94f/src/slopes.ts#L113)*

Retrieves a reference to an API by its apiName label.

**Type parameters:**

▪ **GA**: *[APIBase](_utils_types_.apibase.md)*

**Parameters:**

Name | Type | Description |
------ | ------ | ------ |
`apiName` | string | Name of the API to return  |

**Returns:** *GA*

___

###  delete

▸ **delete**(`baseurl`: string, `getdata`: object, `headers`: object, `axiosConfig`: AxiosRequestConfig): *Promise‹[RequestResponseData](_utils_types_.requestresponsedata.md)›*

*Defined in [slopes.ts:174](https://github.com/ava-labs/slopes/blob/48cc94f/src/slopes.ts#L174)*

Makes a DELETE call to an API.

**Parameters:**

Name | Type | Default | Description |
------ | ------ | ------ | ------ |
`baseurl` | string | - | Path to the API |
`getdata` | object | - | Object containing the key value pairs sent in DELETE |
`headers` | object |  {} | An array HTTP Request Headers |
`axiosConfig` | AxiosRequestConfig |  undefined | Configuration for the axios javascript library that will be the foundation for the rest of the parameters  |

**Returns:** *Promise‹[RequestResponseData](_utils_types_.requestresponsedata.md)›*

A promise for [RequestResponseData](_utils_types_.requestresponsedata.md)

___

###  get

▸ **get**(`baseurl`: string, `getdata`: object, `headers`: object, `axiosConfig`: AxiosRequestConfig): *Promise‹[RequestResponseData](_utils_types_.requestresponsedata.md)›*

*Defined in [slopes.ts:159](https://github.com/ava-labs/slopes/blob/48cc94f/src/slopes.ts#L159)*

Makes a GET call to an API.

**Parameters:**

Name | Type | Default | Description |
------ | ------ | ------ | ------ |
`baseurl` | string | - | Path to the api |
`getdata` | object | - | Object containing the key value pairs sent in GET |
`headers` | object |  {} | An array HTTP Request Headers |
`axiosConfig` | AxiosRequestConfig |  undefined | Configuration for the axios javascript library that will be the foundation for the rest of the parameters  |

**Returns:** *Promise‹[RequestResponseData](_utils_types_.requestresponsedata.md)›*

A promise for [RequestResponseData](_utils_types_.requestresponsedata.md)

___

###  getIP

▸ **getIP**(): *string*

*Defined in [slopes.ts:49](https://github.com/ava-labs/slopes/blob/48cc94f/src/slopes.ts#L49)*

Returns the IP for the AVA node.

**Returns:** *string*

___

###  getNetworkID

▸ **getNetworkID**(): *number*

*Defined in [slopes.ts:70](https://github.com/ava-labs/slopes/blob/48cc94f/src/slopes.ts#L70)*

Returns the networkID;

**Returns:** *number*

___

###  getPort

▸ **getPort**(): *number*

*Defined in [slopes.ts:56](https://github.com/ava-labs/slopes/blob/48cc94f/src/slopes.ts#L56)*

Returns the port for the AVA node.

**Returns:** *number*

___

###  getProtocol

▸ **getProtocol**(): *string*

*Defined in [slopes.ts:42](https://github.com/ava-labs/slopes/blob/48cc94f/src/slopes.ts#L42)*

Returns the protocol such as "http", "https", "git", "ws", etc.

**Returns:** *string*

___

###  getURL

▸ **getURL**(): *string*

*Defined in [slopes.ts:63](https://github.com/ava-labs/slopes/blob/48cc94f/src/slopes.ts#L63)*

Returns the URL of the AVA node (ip + port);

**Returns:** *string*

___

###  patch

▸ **patch**(`baseurl`: string, `getdata`: object, `postdata`: string | object | ArrayBuffer | ArrayBufferView, `headers`: object, `axiosConfig`: AxiosRequestConfig): *Promise‹[RequestResponseData](_utils_types_.requestresponsedata.md)›*

*Defined in [slopes.ts:222](https://github.com/ava-labs/slopes/blob/48cc94f/src/slopes.ts#L222)*

Makes a PATCH call to an API.

**Parameters:**

Name | Type | Default | Description |
------ | ------ | ------ | ------ |
`baseurl` | string | - | Path to the baseurl |
`getdata` | object | - | Object containing the key value pairs sent in PATCH |
`postdata` | string &#124; object &#124; ArrayBuffer &#124; ArrayBufferView | - | Object containing the key value pairs sent in PATCH |
`headers` | object |  {} | An array HTTP Request Headers |
`axiosConfig` | AxiosRequestConfig |  undefined | Configuration for the axios javascript library that will be the foundation for the rest of the parameters  |

**Returns:** *Promise‹[RequestResponseData](_utils_types_.requestresponsedata.md)›*

A promise for [RequestResponseData](_utils_types_.requestresponsedata.md)

___

###  post

▸ **post**(`baseurl`: string, `getdata`: object, `postdata`: string | object | ArrayBuffer | ArrayBufferView, `headers`: object, `axiosConfig`: AxiosRequestConfig): *Promise‹[RequestResponseData](_utils_types_.requestresponsedata.md)›*

*Defined in [slopes.ts:190](https://github.com/ava-labs/slopes/blob/48cc94f/src/slopes.ts#L190)*

Makes a POST call to an API.

**Parameters:**

Name | Type | Default | Description |
------ | ------ | ------ | ------ |
`baseurl` | string | - | Path to the API |
`getdata` | object | - | Object containing the key value pairs sent in POST |
`postdata` | string &#124; object &#124; ArrayBuffer &#124; ArrayBufferView | - | Object containing the key value pairs sent in POST |
`headers` | object |  {} | An array HTTP Request Headers |
`axiosConfig` | AxiosRequestConfig |  undefined | Configuration for the axios javascript library that will be the foundation for the rest of the parameters  |

**Returns:** *Promise‹[RequestResponseData](_utils_types_.requestresponsedata.md)›*

A promise for [RequestResponseData](_utils_types_.requestresponsedata.md)

___

###  put

▸ **put**(`baseurl`: string, `getdata`: object, `postdata`: string | object | ArrayBuffer | ArrayBufferView, `headers`: object, `axiosConfig`: AxiosRequestConfig): *Promise‹[RequestResponseData](_utils_types_.requestresponsedata.md)›*

*Defined in [slopes.ts:206](https://github.com/ava-labs/slopes/blob/48cc94f/src/slopes.ts#L206)*

Makes a PUT call to an API.

**Parameters:**

Name | Type | Default | Description |
------ | ------ | ------ | ------ |
`baseurl` | string | - | Path to the baseurl |
`getdata` | object | - | Object containing the key value pairs sent in PUT |
`postdata` | string &#124; object &#124; ArrayBuffer &#124; ArrayBufferView | - | Object containing the key value pairs sent in PUT |
`headers` | object |  {} | An array HTTP Request Headers |
`axiosConfig` | AxiosRequestConfig |  undefined | Configuration for the axios javascript library that will be the foundation for the rest of the parameters  |

**Returns:** *Promise‹[RequestResponseData](_utils_types_.requestresponsedata.md)›*

A promise for [RequestResponseData](_utils_types_.requestresponsedata.md)

___

###  setAddress

▸ **setAddress**(`ip`: string, `port`: number, `protocol`: string): *void*

*Defined in [slopes.ts:32](https://github.com/ava-labs/slopes/blob/48cc94f/src/slopes.ts#L32)*

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

*Defined in [slopes.ts:77](https://github.com/ava-labs/slopes/blob/48cc94f/src/slopes.ts#L77)*

Sets the networkID

**Parameters:**

Name | Type |
------ | ------ |
`netid` | number |

**Returns:** *void*
