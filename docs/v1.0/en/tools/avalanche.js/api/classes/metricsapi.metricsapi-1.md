[avalanche](../README.md) › [MetricsAPI](../modules/metricsapi.md) › [MetricsAPI](metricsapi.metricsapi-1.md)

# Class: MetricsAPI

Class for interacting with a node API that is using the node's MetricsApi.

**`remarks`** This extends the [RESTAPI](utils_types.restapi.md) class. This class should not be directly called. Instead, use the [Avalanche.addAPI](avalanche.avalanche-1.md#addapi) function to register this interface with Avalanche.

## Hierarchy

  ↳ [RESTAPI](utils_types.restapi.md)

  ↳ **MetricsAPI**

## Index

### Constructors

* [constructor](metricsapi.metricsapi-1.md#constructor)

### Properties

* [acceptType](metricsapi.metricsapi-1.md#protected-accepttype)
* [baseurl](metricsapi.metricsapi-1.md#protected-baseurl)
* [contentType](metricsapi.metricsapi-1.md#protected-contenttype)
* [core](metricsapi.metricsapi-1.md#protected-core)
* [db](metricsapi.metricsapi-1.md#protected-db)

### Methods

* [delete](metricsapi.metricsapi-1.md#delete)
* [get](metricsapi.metricsapi-1.md#get)
* [getAcceptType](metricsapi.metricsapi-1.md#getaccepttype)
* [getBaseURL](metricsapi.metricsapi-1.md#getbaseurl)
* [getContentType](metricsapi.metricsapi-1.md#getcontenttype)
* [getDB](metricsapi.metricsapi-1.md#getdb)
* [getMetrics](metricsapi.metricsapi-1.md#getmetrics)
* [patch](metricsapi.metricsapi-1.md#patch)
* [post](metricsapi.metricsapi-1.md#post)
* [put](metricsapi.metricsapi-1.md#put)
* [setBaseURL](metricsapi.metricsapi-1.md#setbaseurl)

## Constructors

###  constructor

\+ **new MetricsAPI**(`core`: [AvalancheCore](avalanchecore.avalanchecore-1.md), `baseurl`: string): *[MetricsAPI](metricsapi.metricsapi-1.md)*

*Overrides [RESTAPI](utils_types.restapi.md).[constructor](utils_types.restapi.md#constructor)*

*Defined in [apis/metrics/api.ts:24](https://github.com/ava-labs/avalanche.js/blob/c723742/src/apis/metrics/api.ts#L24)*

This class should not be instantiated directly. Instead use the [Avalanche.addAPI](avalanche.avalanche-1.md#addapi) method.

**Parameters:**

Name | Type | Default | Description |
------ | ------ | ------ | ------ |
`core` | [AvalancheCore](avalanchecore.avalanchecore-1.md) | - | A reference to the Avalanche class |
`baseurl` | string | "/ext/metrics" | Defaults to the string "/ext/metrics" as the path to blockchain's baseurl  |

**Returns:** *[MetricsAPI](metricsapi.metricsapi-1.md)*

## Properties

### `Protected` acceptType

• **acceptType**: *string*

*Inherited from [RESTAPI](utils_types.restapi.md).[acceptType](utils_types.restapi.md#protected-accepttype)*

*Defined in [utils/types.ts:82](https://github.com/ava-labs/avalanche.js/blob/c723742/src/utils/types.ts#L82)*

___

### `Protected` baseurl

• **baseurl**: *string*

*Inherited from [APIBase](utils_types.apibase.md).[baseurl](utils_types.apibase.md#protected-baseurl)*

*Defined in [utils/types.ts:34](https://github.com/ava-labs/avalanche.js/blob/c723742/src/utils/types.ts#L34)*

___

### `Protected` contentType

• **contentType**: *string*

*Inherited from [RESTAPI](utils_types.restapi.md).[contentType](utils_types.restapi.md#protected-contenttype)*

*Defined in [utils/types.ts:81](https://github.com/ava-labs/avalanche.js/blob/c723742/src/utils/types.ts#L81)*

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

## Methods

###  delete

▸ **delete**(`method`: string, `params?`: Array‹object› | object, `baseurl?`: string, `contentType?`: string, `acceptType?`: string): *Promise‹[RequestResponseData](utils_types.requestresponsedata.md)›*

*Inherited from [RESTAPI](utils_types.restapi.md).[delete](utils_types.restapi.md#delete)*

*Defined in [utils/types.ts:179](https://github.com/ava-labs/avalanche.js/blob/c723742/src/utils/types.ts#L179)*

**Parameters:**

Name | Type |
------ | ------ |
`method` | string |
`params?` | Array‹object› &#124; object |
`baseurl?` | string |
`contentType?` | string |
`acceptType?` | string |

**Returns:** *Promise‹[RequestResponseData](utils_types.requestresponsedata.md)›*

___

###  get

▸ **get**(`baseurl?`: string, `contentType?`: string, `acceptType?`: string): *Promise‹[RequestResponseData](utils_types.requestresponsedata.md)›*

*Inherited from [RESTAPI](utils_types.restapi.md).[get](utils_types.restapi.md#get)*

*Defined in [utils/types.ts:84](https://github.com/ava-labs/avalanche.js/blob/c723742/src/utils/types.ts#L84)*

**Parameters:**

Name | Type |
------ | ------ |
`baseurl?` | string |
`contentType?` | string |
`acceptType?` | string |

**Returns:** *Promise‹[RequestResponseData](utils_types.requestresponsedata.md)›*

___

###  getAcceptType

▸ **getAcceptType**(): *string*

*Inherited from [RESTAPI](utils_types.restapi.md).[getAcceptType](utils_types.restapi.md#getaccepttype)*

*Defined in [utils/types.ts:257](https://github.com/ava-labs/avalanche.js/blob/c723742/src/utils/types.ts#L257)*

Returns what type of representation is desired at the client side

**Returns:** *string*

___

###  getBaseURL

▸ **getBaseURL**(): *string*

*Inherited from [APIBase](utils_types.apibase.md).[getBaseURL](utils_types.apibase.md#getbaseurl)*

*Defined in [utils/types.ts:58](https://github.com/ava-labs/avalanche.js/blob/c723742/src/utils/types.ts#L58)*

Returns the baseurl's path.

**Returns:** *string*

___

###  getContentType

▸ **getContentType**(): *string*

*Inherited from [RESTAPI](utils_types.restapi.md).[getContentType](utils_types.restapi.md#getcontenttype)*

*Defined in [utils/types.ts:250](https://github.com/ava-labs/avalanche.js/blob/c723742/src/utils/types.ts#L250)*

Returns the type of the entity attached to the incoming request

**Returns:** *string*

___

###  getDB

▸ **getDB**(): *StoreAPI*

*Inherited from [APIBase](utils_types.apibase.md).[getDB](utils_types.apibase.md#getdb)*

*Defined in [utils/types.ts:65](https://github.com/ava-labs/avalanche.js/blob/c723742/src/utils/types.ts#L65)*

Returns the baseurl's database.

**Returns:** *StoreAPI*

___

###  getMetrics

▸ **getMetrics**(): *Promise‹string›*

*Defined in [apis/metrics/api.ts:20](https://github.com/ava-labs/avalanche.js/blob/c723742/src/apis/metrics/api.ts#L20)*

**Returns:** *Promise‹string›*

Promise for an object containing the metrics response

___

###  patch

▸ **patch**(`method`: string, `params?`: Array‹object› | object, `baseurl?`: string, `contentType?`: string, `acceptType?`: string): *Promise‹[RequestResponseData](utils_types.requestresponsedata.md)›*

*Inherited from [RESTAPI](utils_types.restapi.md).[patch](utils_types.restapi.md#patch)*

*Defined in [utils/types.ts:213](https://github.com/ava-labs/avalanche.js/blob/c723742/src/utils/types.ts#L213)*

**Parameters:**

Name | Type |
------ | ------ |
`method` | string |
`params?` | Array‹object› &#124; object |
`baseurl?` | string |
`contentType?` | string |
`acceptType?` | string |

**Returns:** *Promise‹[RequestResponseData](utils_types.requestresponsedata.md)›*

___

###  post

▸ **post**(`method`: string, `params?`: Array‹object› | object, `baseurl?`: string, `contentType?`: string, `acceptType?`: string): *Promise‹[RequestResponseData](utils_types.requestresponsedata.md)›*

*Inherited from [RESTAPI](utils_types.restapi.md).[post](utils_types.restapi.md#post)*

*Defined in [utils/types.ts:111](https://github.com/ava-labs/avalanche.js/blob/c723742/src/utils/types.ts#L111)*

**Parameters:**

Name | Type |
------ | ------ |
`method` | string |
`params?` | Array‹object› &#124; object |
`baseurl?` | string |
`contentType?` | string |
`acceptType?` | string |

**Returns:** *Promise‹[RequestResponseData](utils_types.requestresponsedata.md)›*

___

###  put

▸ **put**(`method`: string, `params?`: Array‹object› | object, `baseurl?`: string, `contentType?`: string, `acceptType?`: string): *Promise‹[RequestResponseData](utils_types.requestresponsedata.md)›*

*Inherited from [RESTAPI](utils_types.restapi.md).[put](utils_types.restapi.md#put)*

*Defined in [utils/types.ts:145](https://github.com/ava-labs/avalanche.js/blob/c723742/src/utils/types.ts#L145)*

**Parameters:**

Name | Type |
------ | ------ |
`method` | string |
`params?` | Array‹object› &#124; object |
`baseurl?` | string |
`contentType?` | string |
`acceptType?` | string |

**Returns:** *Promise‹[RequestResponseData](utils_types.requestresponsedata.md)›*

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
