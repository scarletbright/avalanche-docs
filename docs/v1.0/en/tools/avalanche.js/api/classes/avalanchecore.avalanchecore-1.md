[avalanche](../README.md) › [AvalancheCore](../modules/avalanchecore.md) › [AvalancheCore](avalanchecore.avalanchecore-1.md)

# Class: AvalancheCore

AvalancheCore is middleware for interacting with Avalanche node RPC APIs.

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
* [hrp](avalanchecore.avalanchecore-1.md#protected-hrp)
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
* [getHRP](avalanchecore.avalanchecore-1.md#gethrp)
* [getIP](avalanchecore.avalanchecore-1.md#getip)
* [getNetworkID](avalanchecore.avalanchecore-1.md#getnetworkid)
* [getPort](avalanchecore.avalanchecore-1.md#getport)
* [getProtocol](avalanchecore.avalanchecore-1.md#getprotocol)
* [getURL](avalanchecore.avalanchecore-1.md#geturl)
* [patch](avalanchecore.avalanchecore-1.md#patch)
* [post](avalanchecore.avalanchecore-1.md#post)
* [put](avalanchecore.avalanchecore-1.md#put)
* [setAddress](avalanchecore.avalanchecore-1.md#setaddress)
* [setHRP](avalanchecore.avalanchecore-1.md#sethrp)
* [setNetworkID](avalanchecore.avalanchecore-1.md#setnetworkid)

## Constructors

###  constructor

\+ **new AvalancheCore**(`ip`: string, `port`: number, `protocol`: string): *[AvalancheCore](avalanchecore.avalanchecore-1.md)*

Defined in src/avalanche.ts:288

Creates a new Avalanche instance. Sets the address and port of the main Avalanche Client.

**Parameters:**

Name | Type | Default | Description |
------ | ------ | ------ | ------ |
`ip` | string | - | The hostname to resolve to reach the Avalanche Client APIs |
`port` | number | - | The port to resolve to reach the Avalanche Client APIs |
`protocol` | string | "http" | The protocol string to use before a "://" in a request, ex: "http", "https", "git", "ws", etc ...  |

**Returns:** *[AvalancheCore](avalanchecore.avalanchecore-1.md)*

## Properties

### `Protected` apis

• **apis**: *object*

Defined in src/avalanche.ts:31

#### Type declaration:

* \[ **k**: *string*\]: [APIBase](common_apibase.apibase.md)

___

### `Protected` hrp

• **hrp**: *string* = ""

Defined in src/avalanche.ts:21

___

### `Protected` ip

• **ip**: *string*

Defined in src/avalanche.ts:25

___

### `Protected` networkID

• **networkID**: *number* = 0

Defined in src/avalanche.ts:19

___

### `Protected` port

• **port**: *number*

Defined in src/avalanche.ts:27

___

### `Protected` protocol

• **protocol**: *string*

Defined in src/avalanche.ts:23

___

### `Protected` url

• **url**: *string*

Defined in src/avalanche.ts:29

## Methods

###  addAPI

▸ **addAPI**‹**GA**›(`apiName`: string, `ConstructorFN`: object, `baseurl`: string, ...`args`: Array‹any›): *void*

Defined in src/avalanche.ts:116

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

▪ **GA**: *[APIBase](common_apibase.apibase.md)*

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

Defined in src/avalanche.ts:132

Retrieves a reference to an API by its apiName label.

**Type parameters:**

▪ **GA**: *[APIBase](common_apibase.apibase.md)*

**Parameters:**

Name | Type | Description |
------ | ------ | ------ |
`apiName` | string | Name of the API to return  |

**Returns:** *GA*

___

###  delete

▸ **delete**(`baseurl`: string, `getdata`: object, `headers`: object, `axiosConfig`: AxiosRequestConfig): *Promise‹[RequestResponseData](common_apibase.requestresponsedata.md)›*

Defined in src/avalanche.ts:204

Makes a DELETE call to an API.

**Parameters:**

Name | Type | Default | Description |
------ | ------ | ------ | ------ |
`baseurl` | string | - | Path to the API |
`getdata` | object | - | Object containing the key value pairs sent in DELETE |
`headers` | object | {} | An array HTTP Request Headers |
`axiosConfig` | AxiosRequestConfig | undefined | Configuration for the axios javascript library that will be the foundation for the rest of the parameters  |

**Returns:** *Promise‹[RequestResponseData](common_apibase.requestresponsedata.md)›*

A promise for [RequestResponseData](common_apibase.requestresponsedata.md)

___

###  get

▸ **get**(`baseurl`: string, `getdata`: object, `headers`: object, `axiosConfig`: AxiosRequestConfig): *Promise‹[RequestResponseData](common_apibase.requestresponsedata.md)›*

Defined in src/avalanche.ts:181

Makes a GET call to an API.

**Parameters:**

Name | Type | Default | Description |
------ | ------ | ------ | ------ |
`baseurl` | string | - | Path to the api |
`getdata` | object | - | Object containing the key value pairs sent in GET |
`headers` | object | {} | An array HTTP Request Headers |
`axiosConfig` | AxiosRequestConfig | undefined | Configuration for the axios javascript library that will be the foundation for the rest of the parameters  |

**Returns:** *Promise‹[RequestResponseData](common_apibase.requestresponsedata.md)›*

A promise for [RequestResponseData](common_apibase.requestresponsedata.md)

___

###  getHRP

▸ **getHRP**(): *string*

Defined in src/avalanche.ts:86

Returns the Human-Readable-Part of the network associated with this key.

**Returns:** *string*

The [KeyPair](common_keychain.keypair.md)'s Human-Readable-Part of the network's Bech32 addressing scheme

___

###  getIP

▸ **getIP**(): *string*

Defined in src/avalanche.ts:56

Returns the IP for the Avalanche node.

**Returns:** *string*

___

###  getNetworkID

▸ **getNetworkID**(): *number*

Defined in src/avalanche.ts:71

Returns the networkID;

**Returns:** *number*

___

###  getPort

▸ **getPort**(): *number*

Defined in src/avalanche.ts:61

Returns the port for the Avalanche node.

**Returns:** *number*

___

###  getProtocol

▸ **getProtocol**(): *string*

Defined in src/avalanche.ts:51

Returns the protocol such as "http", "https", "git", "ws", etc.

**Returns:** *string*

___

###  getURL

▸ **getURL**(): *string*

Defined in src/avalanche.ts:66

Returns the URL of the Avalanche node (ip + port);

**Returns:** *string*

___

###  patch

▸ **patch**(`baseurl`: string, `getdata`: object, `postdata`: string | object | ArrayBuffer | ArrayBufferView, `headers`: object, `axiosConfig`: AxiosRequestConfig): *Promise‹[RequestResponseData](common_apibase.requestresponsedata.md)›*

Defined in src/avalanche.ts:278

Makes a PATCH call to an API.

**Parameters:**

Name | Type | Default | Description |
------ | ------ | ------ | ------ |
`baseurl` | string | - | Path to the baseurl |
`getdata` | object | - | Object containing the key value pairs sent in PATCH |
`postdata` | string &#124; object &#124; ArrayBuffer &#124; ArrayBufferView | - | Object containing the key value pairs sent in PATCH |
`headers` | object | {} | An array HTTP Request Headers |
`axiosConfig` | AxiosRequestConfig | undefined | Configuration for the axios javascript library that will be the foundation for the rest of the parameters  |

**Returns:** *Promise‹[RequestResponseData](common_apibase.requestresponsedata.md)›*

A promise for [RequestResponseData](common_apibase.requestresponsedata.md)

___

###  post

▸ **post**(`baseurl`: string, `getdata`: object, `postdata`: string | object | ArrayBuffer | ArrayBufferView, `headers`: object, `axiosConfig`: AxiosRequestConfig): *Promise‹[RequestResponseData](common_apibase.requestresponsedata.md)›*

Defined in src/avalanche.ts:228

Makes a POST call to an API.

**Parameters:**

Name | Type | Default | Description |
------ | ------ | ------ | ------ |
`baseurl` | string | - | Path to the API |
`getdata` | object | - | Object containing the key value pairs sent in POST |
`postdata` | string &#124; object &#124; ArrayBuffer &#124; ArrayBufferView | - | Object containing the key value pairs sent in POST |
`headers` | object | {} | An array HTTP Request Headers |
`axiosConfig` | AxiosRequestConfig | undefined | Configuration for the axios javascript library that will be the foundation for the rest of the parameters  |

**Returns:** *Promise‹[RequestResponseData](common_apibase.requestresponsedata.md)›*

A promise for [RequestResponseData](common_apibase.requestresponsedata.md)

___

###  put

▸ **put**(`baseurl`: string, `getdata`: object, `postdata`: string | object | ArrayBuffer | ArrayBufferView, `headers`: object, `axiosConfig`: AxiosRequestConfig): *Promise‹[RequestResponseData](common_apibase.requestresponsedata.md)›*

Defined in src/avalanche.ts:253

Makes a PUT call to an API.

**Parameters:**

Name | Type | Default | Description |
------ | ------ | ------ | ------ |
`baseurl` | string | - | Path to the baseurl |
`getdata` | object | - | Object containing the key value pairs sent in PUT |
`postdata` | string &#124; object &#124; ArrayBuffer &#124; ArrayBufferView | - | Object containing the key value pairs sent in PUT |
`headers` | object | {} | An array HTTP Request Headers |
`axiosConfig` | AxiosRequestConfig | undefined | Configuration for the axios javascript library that will be the foundation for the rest of the parameters  |

**Returns:** *Promise‹[RequestResponseData](common_apibase.requestresponsedata.md)›*

A promise for [RequestResponseData](common_apibase.requestresponsedata.md)

___

###  setAddress

▸ **setAddress**(`ip`: string, `port`: number, `protocol`: string): *void*

Defined in src/avalanche.ts:41

Sets the address and port of the main Avalanche Client.

**Parameters:**

Name | Type | Default | Description |
------ | ------ | ------ | ------ |
`ip` | string | - | The hostname to resolve to reach the Avalanche Client RPC APIs |
`port` | number | - | The port to resolve to reach the Avalanche Client RPC APIs |
`protocol` | string | "http" | The protocol string to use before a "://" in a request, ex: "http", "https", "git", "ws", etc ...  |

**Returns:** *void*

___

###  setHRP

▸ **setHRP**(`hrp`: string): *void*

Defined in src/avalanche.ts:93

Sets the the Human-Readable-Part of the network associated with this key.

**Parameters:**

Name | Type | Description |
------ | ------ | ------ |
`hrp` | string | String for the Human-Readable-Part of Bech32 addresses  |

**Returns:** *void*

___

###  setNetworkID

▸ **setNetworkID**(`netid`: number): *void*

Defined in src/avalanche.ts:76

Sets the networkID

**Parameters:**

Name | Type |
------ | ------ |
`netid` | number |

**Returns:** *void*
