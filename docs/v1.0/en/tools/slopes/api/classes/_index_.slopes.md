[slopes - v1.7.5](../README.md) › ["index"](../modules/_index_.md) › [Slopes](_index_.slopes.md)

# Class: Slopes

Slopes is middleware for interacting with AVA node RPC APIs.

Example usage:
```js
let slopes = new Slopes("127.0.0.1", 9650, "https");
```

## Hierarchy

* [SlopesCore](_slopes_.slopescore.md)

  ↳ **Slopes**

## Index

### Constructors

* [constructor](_index_.slopes.md#constructor)

### Properties

* [apis](_index_.slopes.md#protected-apis)
* [ip](_index_.slopes.md#protected-ip)
* [networkID](_index_.slopes.md#protected-networkid)
* [port](_index_.slopes.md#protected-port)
* [protocol](_index_.slopes.md#protected-protocol)
* [url](_index_.slopes.md#protected-url)

### Methods

* [AVM](_index_.slopes.md#avm)
* [Admin](_index_.slopes.md#admin)
* [Health](_index_.slopes.md#health)
* [NodeKeys](_index_.slopes.md#nodekeys)
* [Platform](_index_.slopes.md#platform)
* [addAPI](_index_.slopes.md#addapi)
* [api](_index_.slopes.md#api)
* [delete](_index_.slopes.md#delete)
* [get](_index_.slopes.md#get)
* [getIP](_index_.slopes.md#getip)
* [getNetworkID](_index_.slopes.md#getnetworkid)
* [getPort](_index_.slopes.md#getport)
* [getProtocol](_index_.slopes.md#getprotocol)
* [getURL](_index_.slopes.md#geturl)
* [patch](_index_.slopes.md#patch)
* [post](_index_.slopes.md#post)
* [put](_index_.slopes.md#put)
* [setAddress](_index_.slopes.md#setaddress)
* [setNetworkID](_index_.slopes.md#setnetworkid)

## Constructors

###  constructor

\+ **new Slopes**(`ip`: string, `port`: number, `protocol`: string, `networkID`: number, `avmChainID`: string, `skipinit`: boolean): *[Slopes](_index_.slopes.md)*

*Overrides [SlopesCore](_slopes_.slopescore.md).[constructor](_slopes_.slopescore.md#constructor)*

*Defined in [index.ts:61](https://github.com/ava-labs/slopes/blob/db73b16/src/index.ts#L61)*

Creates a new AVA instance. Sets the address and port of the main AVA Client.

**Parameters:**

Name | Type | Default | Description |
------ | ------ | ------ | ------ |
`ip` | string | - | The hostname to resolve to reach the AVA Client RPC APIs |
`port` | number | - | The port to resolve to reach the AVA Client RPC APIs |
`protocol` | string | "http" | The protocol string to use before a "://" in a request, ex: "http", "https", "git", "ws", etc ... |
`networkID` | number | 3 | - |
`avmChainID` | string |  undefined | Sets the blockchainID for the AVM. Will try to auto-detect, otherwise default "4R5p2RXDGLqaifZE4hHWH9owe34pfoBULn1DrQTWivjg8o4aH" |
`skipinit` | boolean | false | Skips creating the APIs  |

**Returns:** *[Slopes](_index_.slopes.md)*

## Properties

### `Protected` apis

• **apis**: *object*

*Inherited from [SlopesCore](_slopes_.slopescore.md).[apis](_slopes_.slopescore.md#protected-apis)*

*Defined in [slopes.ts:23](https://github.com/ava-labs/slopes/blob/db73b16/src/slopes.ts#L23)*

#### Type declaration:

* \[ **k**: *string*\]: [APIBase](_utils_types_.apibase.md)

___

### `Protected` ip

• **ip**: *string*

*Inherited from [SlopesCore](_slopes_.slopescore.md).[ip](_slopes_.slopescore.md#protected-ip)*

*Defined in [slopes.ts:20](https://github.com/ava-labs/slopes/blob/db73b16/src/slopes.ts#L20)*

___

### `Protected` networkID

• **networkID**: *number* = 3

*Inherited from [SlopesCore](_slopes_.slopescore.md).[networkID](_slopes_.slopescore.md#protected-networkid)*

*Defined in [slopes.ts:18](https://github.com/ava-labs/slopes/blob/db73b16/src/slopes.ts#L18)*

___

### `Protected` port

• **port**: *number*

*Inherited from [SlopesCore](_slopes_.slopescore.md).[port](_slopes_.slopescore.md#protected-port)*

*Defined in [slopes.ts:21](https://github.com/ava-labs/slopes/blob/db73b16/src/slopes.ts#L21)*

___

### `Protected` protocol

• **protocol**: *string*

*Inherited from [SlopesCore](_slopes_.slopescore.md).[protocol](_slopes_.slopescore.md#protected-protocol)*

*Defined in [slopes.ts:19](https://github.com/ava-labs/slopes/blob/db73b16/src/slopes.ts#L19)*

___

### `Protected` url

• **url**: *string*

*Inherited from [SlopesCore](_slopes_.slopescore.md).[url](_slopes_.slopescore.md#protected-url)*

*Defined in [slopes.ts:22](https://github.com/ava-labs/slopes/blob/db73b16/src/slopes.ts#L22)*

## Methods

###  AVM

▸ **AVM**(): *[AVMAPI](_apis_avm_api_.avmapi.md)‹›*

*Defined in [index.ts:38](https://github.com/ava-labs/slopes/blob/db73b16/src/index.ts#L38)*

Returns a reference to the AVM RPC.

**Returns:** *[AVMAPI](_apis_avm_api_.avmapi.md)‹›*

___

###  Admin

▸ **Admin**(): *[AdminAPI](_apis_admin_api_.adminapi.md)‹›*

*Defined in [index.ts:31](https://github.com/ava-labs/slopes/blob/db73b16/src/index.ts#L31)*

Returns a reference to the Admin RPC.

**Returns:** *[AdminAPI](_apis_admin_api_.adminapi.md)‹›*

___

###  Health

▸ **Health**(): *[HealthAPI](_apis_health_api_.healthapi.md)‹›*

*Defined in [index.ts:59](https://github.com/ava-labs/slopes/blob/db73b16/src/index.ts#L59)*

Returns a reference to the Health RPC for a node.

**Returns:** *[HealthAPI](_apis_health_api_.healthapi.md)‹›*

___

###  NodeKeys

▸ **NodeKeys**(): *[KeystoreAPI](_apis_keystore_api_.keystoreapi.md)‹›*

*Defined in [index.ts:52](https://github.com/ava-labs/slopes/blob/db73b16/src/index.ts#L52)*

Returns a reference to the Keystore RPC for a node. We label it "NodeKeys" to reduce confusion about what it's accessing.

**Returns:** *[KeystoreAPI](_apis_keystore_api_.keystoreapi.md)‹›*

___

###  Platform

▸ **Platform**(): *[PlatformAPI](_apis_platform_api_.platformapi.md)‹›*

*Defined in [index.ts:45](https://github.com/ava-labs/slopes/blob/db73b16/src/index.ts#L45)*

Returns a reference to the Platform RPC.

**Returns:** *[PlatformAPI](_apis_platform_api_.platformapi.md)‹›*

___

###  addAPI

▸ **addAPI**<**GA**>(`apiName`: string, `constructorFN`: object, `baseurl`: string, ...`args`: Array‹any›): *void*

*Inherited from [SlopesCore](_slopes_.slopescore.md)*

*Defined in [slopes.ts:100](https://github.com/ava-labs/slopes/blob/db73b16/src/slopes.ts#L100)*

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

*Inherited from [SlopesCore](_slopes_.slopescore.md)*

*Defined in [slopes.ts:113](https://github.com/ava-labs/slopes/blob/db73b16/src/slopes.ts#L113)*

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

*Inherited from [SlopesCore](_slopes_.slopescore.md)*

*Defined in [slopes.ts:174](https://github.com/ava-labs/slopes/blob/db73b16/src/slopes.ts#L174)*

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

*Inherited from [SlopesCore](_slopes_.slopescore.md)*

*Defined in [slopes.ts:159](https://github.com/ava-labs/slopes/blob/db73b16/src/slopes.ts#L159)*

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

*Inherited from [SlopesCore](_slopes_.slopescore.md)*

*Defined in [slopes.ts:49](https://github.com/ava-labs/slopes/blob/db73b16/src/slopes.ts#L49)*

Returns the IP for the AVA node.

**Returns:** *string*

___

###  getNetworkID

▸ **getNetworkID**(): *number*

*Inherited from [SlopesCore](_slopes_.slopescore.md)*

*Defined in [slopes.ts:70](https://github.com/ava-labs/slopes/blob/db73b16/src/slopes.ts#L70)*

Returns the networkID;

**Returns:** *number*

___

###  getPort

▸ **getPort**(): *number*

*Inherited from [SlopesCore](_slopes_.slopescore.md)*

*Defined in [slopes.ts:56](https://github.com/ava-labs/slopes/blob/db73b16/src/slopes.ts#L56)*

Returns the port for the AVA node.

**Returns:** *number*

___

###  getProtocol

▸ **getProtocol**(): *string*

*Inherited from [SlopesCore](_slopes_.slopescore.md)*

*Defined in [slopes.ts:42](https://github.com/ava-labs/slopes/blob/db73b16/src/slopes.ts#L42)*

Returns the protocol such as "http", "https", "git", "ws", etc.

**Returns:** *string*

___

###  getURL

▸ **getURL**(): *string*

*Inherited from [SlopesCore](_slopes_.slopescore.md)*

*Defined in [slopes.ts:63](https://github.com/ava-labs/slopes/blob/db73b16/src/slopes.ts#L63)*

Returns the URL of the AVA node (ip + port);

**Returns:** *string*

___

###  patch

▸ **patch**(`baseurl`: string, `getdata`: object, `postdata`: string | object | ArrayBuffer | ArrayBufferView, `headers`: object, `axiosConfig`: AxiosRequestConfig): *Promise‹[RequestResponseData](_utils_types_.requestresponsedata.md)›*

*Inherited from [SlopesCore](_slopes_.slopescore.md)*

*Defined in [slopes.ts:222](https://github.com/ava-labs/slopes/blob/db73b16/src/slopes.ts#L222)*

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

*Inherited from [SlopesCore](_slopes_.slopescore.md)*

*Defined in [slopes.ts:190](https://github.com/ava-labs/slopes/blob/db73b16/src/slopes.ts#L190)*

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

*Inherited from [SlopesCore](_slopes_.slopescore.md)*

*Defined in [slopes.ts:206](https://github.com/ava-labs/slopes/blob/db73b16/src/slopes.ts#L206)*

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

*Inherited from [SlopesCore](_slopes_.slopescore.md)*

*Defined in [slopes.ts:32](https://github.com/ava-labs/slopes/blob/db73b16/src/slopes.ts#L32)*

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

*Inherited from [SlopesCore](_slopes_.slopescore.md)*

*Defined in [slopes.ts:77](https://github.com/ava-labs/slopes/blob/db73b16/src/slopes.ts#L77)*

Sets the networkID

**Parameters:**

Name | Type |
------ | ------ |
`netid` | number |

**Returns:** *void*
