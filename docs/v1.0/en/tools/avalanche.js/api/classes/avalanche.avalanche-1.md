[avalanche](../README.md) › [Avalanche](../modules/avalanche.md) › [Avalanche](avalanche.avalanche-1.md)

# Class: Avalanche

Avalanche.js is middleware for interacting with Avalanche node RPC APIs.

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
* [hrp](avalanche.avalanche-1.md#protected-hrp)
* [ip](avalanche.avalanche-1.md#protected-ip)
* [networkID](avalanche.avalanche-1.md#protected-networkid)
* [port](avalanche.avalanche-1.md#protected-port)
* [protocol](avalanche.avalanche-1.md#protected-protocol)
* [url](avalanche.avalanche-1.md#protected-url)

### Methods

* [Admin](avalanche.avalanche-1.md#admin)
* [Health](avalanche.avalanche-1.md#health)
* [Info](avalanche.avalanche-1.md#info)
* [Metrics](avalanche.avalanche-1.md#metrics)
* [NodeKeys](avalanche.avalanche-1.md#nodekeys)
* [PChain](avalanche.avalanche-1.md#pchain)
* [XChain](avalanche.avalanche-1.md#xchain)
* [addAPI](avalanche.avalanche-1.md#addapi)
* [api](avalanche.avalanche-1.md#api)
* [delete](avalanche.avalanche-1.md#delete)
* [get](avalanche.avalanche-1.md#get)
* [getHRP](avalanche.avalanche-1.md#gethrp)
* [getIP](avalanche.avalanche-1.md#getip)
* [getNetworkID](avalanche.avalanche-1.md#getnetworkid)
* [getPort](avalanche.avalanche-1.md#getport)
* [getProtocol](avalanche.avalanche-1.md#getprotocol)
* [getURL](avalanche.avalanche-1.md#geturl)
* [patch](avalanche.avalanche-1.md#patch)
* [post](avalanche.avalanche-1.md#post)
* [put](avalanche.avalanche-1.md#put)
* [setAddress](avalanche.avalanche-1.md#setaddress)
* [setHRP](avalanche.avalanche-1.md#sethrp)
* [setNetworkID](avalanche.avalanche-1.md#setnetworkid)

## Constructors

###  constructor

\+ **new Avalanche**(`ip`: string, `port`: number, `protocol`: string, `networkID`: number, `XChainID`: string, `hrp`: string, `skipinit`: boolean): *[Avalanche](avalanche.avalanche-1.md)*

*Overrides [AvalancheCore](avalanchecore.avalanchecore-1.md).[constructor](avalanchecore.avalanchecore-1.md#constructor)*

Defined in src/index.ts:64

Creates a new Avalanche instance. Sets the address and port of the main Avalanche Client.

**Parameters:**

Name | Type | Default | Description |
------ | ------ | ------ | ------ |
`ip` | string | - | The hostname to resolve to reach the Avalanche Client RPC APIs |
`port` | number | - | The port to resolve to reach the Avalanche Client RPC APIs |
`protocol` | string | "http" | The protocol string to use before a "://" in a request, ex: "http", "https", "git", "ws", etc ... |
`networkID` | number | DefaultNetworkID | - |
`XChainID` | string | undefined | - |
`hrp` | string | undefined | - |
`skipinit` | boolean | false | Skips creating the APIs  |

**Returns:** *[Avalanche](avalanche.avalanche-1.md)*

## Properties

### `Protected` apis

• **apis**: *object*

*Inherited from [AvalancheCore](avalanchecore.avalanchecore-1.md).[apis](avalanchecore.avalanchecore-1.md#protected-apis)*

Defined in src/avalanche.ts:31

#### Type declaration:

* \[ **k**: *string*\]: [APIBase](common_apibase.apibase.md)

___

### `Protected` hrp

• **hrp**: *string* = ""

*Inherited from [AvalancheCore](avalanchecore.avalanchecore-1.md).[hrp](avalanchecore.avalanchecore-1.md#protected-hrp)*

Defined in src/avalanche.ts:21

___

### `Protected` ip

• **ip**: *string*

*Inherited from [AvalancheCore](avalanchecore.avalanchecore-1.md).[ip](avalanchecore.avalanchecore-1.md#protected-ip)*

Defined in src/avalanche.ts:25

___

### `Protected` networkID

• **networkID**: *number* = 0

*Inherited from [AvalancheCore](avalanchecore.avalanchecore-1.md).[networkID](avalanchecore.avalanchecore-1.md#protected-networkid)*

Defined in src/avalanche.ts:19

___

### `Protected` port

• **port**: *number*

*Inherited from [AvalancheCore](avalanchecore.avalanchecore-1.md).[port](avalanchecore.avalanchecore-1.md#protected-port)*

Defined in src/avalanche.ts:27

___

### `Protected` protocol

• **protocol**: *string*

*Inherited from [AvalancheCore](avalanchecore.avalanchecore-1.md).[protocol](avalanchecore.avalanchecore-1.md#protected-protocol)*

Defined in src/avalanche.ts:23

___

### `Protected` url

• **url**: *string*

*Inherited from [AvalancheCore](avalanchecore.avalanchecore-1.md).[url](avalanchecore.avalanchecore-1.md#protected-url)*

Defined in src/avalanche.ts:29

## Methods

###  Admin

▸ **Admin**(): *[AdminAPI](api_admin.adminapi.md)‹›*

Defined in src/index.ts:33

Returns a reference to the Admin RPC.

**Returns:** *[AdminAPI](api_admin.adminapi.md)‹›*

___

###  Health

▸ **Health**(): *[HealthAPI](api_health.healthapi.md)‹›*

Defined in src/index.ts:43

Returns a reference to the Health RPC for a node.

**Returns:** *[HealthAPI](api_health.healthapi.md)‹›*

___

###  Info

▸ **Info**(): *[InfoAPI](api_info.infoapi.md)‹›*

Defined in src/index.ts:48

Returns a reference to the Info RPC for a node.

**Returns:** *[InfoAPI](api_info.infoapi.md)‹›*

___

###  Metrics

▸ **Metrics**(): *[MetricsAPI](api_metrics.metricsapi.md)‹›*

Defined in src/index.ts:53

Returns a reference to the Metrics RPC.

**Returns:** *[MetricsAPI](api_metrics.metricsapi.md)‹›*

___

###  NodeKeys

▸ **NodeKeys**(): *[KeystoreAPI](api_keystore.keystoreapi.md)‹›*

Defined in src/index.ts:59

Returns a reference to the Keystore RPC for a node. We label it "NodeKeys" to reduce
confusion about what it's accessing.

**Returns:** *[KeystoreAPI](api_keystore.keystoreapi.md)‹›*

___

###  PChain

▸ **PChain**(): *[PlatformVMAPI](api_platformvm.platformvmapi.md)‹›*

Defined in src/index.ts:64

Returns a reference to the PlatformVM RPC pointed at the P-Chain.

**Returns:** *[PlatformVMAPI](api_platformvm.platformvmapi.md)‹›*

___

###  XChain

▸ **XChain**(): *[AVMAPI](api_avm.avmapi.md)‹›*

Defined in src/index.ts:38

Returns a reference to the AVM RPC pointed at the X-Chain.

**Returns:** *[AVMAPI](api_avm.avmapi.md)‹›*

___

###  addAPI

▸ **addAPI**‹**GA**›(`apiName`: string, `ConstructorFN`: object, `baseurl`: string, ...`args`: Array‹any›): *void*

*Inherited from [AvalancheCore](avalanchecore.avalanchecore-1.md).[addAPI](avalanchecore.avalanchecore-1.md#addapi)*

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

*Inherited from [AvalancheCore](avalanchecore.avalanchecore-1.md).[api](avalanchecore.avalanchecore-1.md#api)*

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

*Inherited from [AvalancheCore](avalanchecore.avalanchecore-1.md).[delete](avalanchecore.avalanchecore-1.md#delete)*

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

*Inherited from [AvalancheCore](avalanchecore.avalanchecore-1.md).[get](avalanchecore.avalanchecore-1.md#get)*

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

*Inherited from [AvalancheCore](avalanchecore.avalanchecore-1.md).[getHRP](avalanchecore.avalanchecore-1.md#gethrp)*

Defined in src/avalanche.ts:86

Returns the Human-Readable-Part of the network associated with this key.

**Returns:** *string*

The [KeyPair](common_keychain.keypair.md)'s Human-Readable-Part of the network's Bech32 addressing scheme

___

###  getIP

▸ **getIP**(): *string*

*Inherited from [AvalancheCore](avalanchecore.avalanchecore-1.md).[getIP](avalanchecore.avalanchecore-1.md#getip)*

Defined in src/avalanche.ts:56

Returns the IP for the Avalanche node.

**Returns:** *string*

___

###  getNetworkID

▸ **getNetworkID**(): *number*

*Inherited from [AvalancheCore](avalanchecore.avalanchecore-1.md).[getNetworkID](avalanchecore.avalanchecore-1.md#getnetworkid)*

Defined in src/avalanche.ts:71

Returns the networkID;

**Returns:** *number*

___

###  getPort

▸ **getPort**(): *number*

*Inherited from [AvalancheCore](avalanchecore.avalanchecore-1.md).[getPort](avalanchecore.avalanchecore-1.md#getport)*

Defined in src/avalanche.ts:61

Returns the port for the Avalanche node.

**Returns:** *number*

___

###  getProtocol

▸ **getProtocol**(): *string*

*Inherited from [AvalancheCore](avalanchecore.avalanchecore-1.md).[getProtocol](avalanchecore.avalanchecore-1.md#getprotocol)*

Defined in src/avalanche.ts:51

Returns the protocol such as "http", "https", "git", "ws", etc.

**Returns:** *string*

___

###  getURL

▸ **getURL**(): *string*

*Inherited from [AvalancheCore](avalanchecore.avalanchecore-1.md).[getURL](avalanchecore.avalanchecore-1.md#geturl)*

Defined in src/avalanche.ts:66

Returns the URL of the Avalanche node (ip + port);

**Returns:** *string*

___

###  patch

▸ **patch**(`baseurl`: string, `getdata`: object, `postdata`: string | object | ArrayBuffer | ArrayBufferView, `headers`: object, `axiosConfig`: AxiosRequestConfig): *Promise‹[RequestResponseData](common_apibase.requestresponsedata.md)›*

*Inherited from [AvalancheCore](avalanchecore.avalanchecore-1.md).[patch](avalanchecore.avalanchecore-1.md#patch)*

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

*Inherited from [AvalancheCore](avalanchecore.avalanchecore-1.md).[post](avalanchecore.avalanchecore-1.md#post)*

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

*Inherited from [AvalancheCore](avalanchecore.avalanchecore-1.md).[put](avalanchecore.avalanchecore-1.md#put)*

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

*Inherited from [AvalancheCore](avalanchecore.avalanchecore-1.md).[setAddress](avalanchecore.avalanchecore-1.md#setaddress)*

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

*Inherited from [AvalancheCore](avalanchecore.avalanchecore-1.md).[setHRP](avalanchecore.avalanchecore-1.md#sethrp)*

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

*Inherited from [AvalancheCore](avalanchecore.avalanchecore-1.md).[setNetworkID](avalanchecore.avalanchecore-1.md#setnetworkid)*

Defined in src/avalanche.ts:76

Sets the networkID

**Parameters:**

Name | Type |
------ | ------ |
`netid` | number |

**Returns:** *void*
