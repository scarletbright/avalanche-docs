[avalanche](../README.md) › [Utils-Types](../modules/utils_types.md) › [RESTAPI](utils_types.restapi.md)

# Class: RESTAPI

## Hierarchy

* [APIBase](utils_types.apibase.md)

  ↳ **RESTAPI**

  ↳ [MetricsAPI](metricsapi.metricsapi-1.md)

## Index

### Constructors

* [constructor](utils_types.restapi.md#constructor)

### Properties

* [acceptType](utils_types.restapi.md#protected-accepttype)
* [baseurl](utils_types.restapi.md#protected-baseurl)
* [contentType](utils_types.restapi.md#protected-contenttype)
* [core](utils_types.restapi.md#protected-core)
* [db](utils_types.restapi.md#protected-db)

### Methods

* [delete](utils_types.restapi.md#delete)
* [get](utils_types.restapi.md#get)
* [getAcceptType](utils_types.restapi.md#getaccepttype)
* [getBaseURL](utils_types.restapi.md#getbaseurl)
* [getContentType](utils_types.restapi.md#getcontenttype)
* [getDB](utils_types.restapi.md#getdb)
* [patch](utils_types.restapi.md#patch)
* [post](utils_types.restapi.md#post)
* [put](utils_types.restapi.md#put)
* [setBaseURL](utils_types.restapi.md#setbaseurl)

## Constructors

###  constructor

\+ **new RESTAPI**(`core`: [AvalancheCore](avalanchecore.avalanchecore-1.md), `baseurl`: string, `contentType`: string, `acceptType`: string): *[RESTAPI](utils_types.restapi.md)*

*Overrides [APIBase](utils_types.apibase.md).[constructor](utils_types.apibase.md#constructor)*

*Defined in [utils/types.ts:259](https://github.com/ava-labs/avalanche.js/blob/c723742/src/utils/types.ts#L259)*

**Parameters:**

Name | Type | Default | Description |
------ | ------ | ------ | ------ |
`core` | [AvalancheCore](avalanchecore.avalanchecore-1.md) | - | Reference to the Avalanche instance using this endpoint |
`baseurl` | string | - | Path of the APIs baseurl - ex: "/ext/bc/avm" |
`contentType` | string | "application/json;charset=UTF-8" | Optional Determines the type of the entity attached to the incoming request |
`acceptType` | string | undefined | Optional Determines the type of representation which is desired on the client side  |

**Returns:** *[RESTAPI](utils_types.restapi.md)*

## Properties

### `Protected` acceptType

• **acceptType**: *string*

*Defined in [utils/types.ts:82](https://github.com/ava-labs/avalanche.js/blob/c723742/src/utils/types.ts#L82)*

___

### `Protected` baseurl

• **baseurl**: *string*

*Inherited from [APIBase](utils_types.apibase.md).[baseurl](utils_types.apibase.md#protected-baseurl)*

*Defined in [utils/types.ts:34](https://github.com/ava-labs/avalanche.js/blob/c723742/src/utils/types.ts#L34)*

___

### `Protected` contentType

• **contentType**: *string*

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

###  patch

▸ **patch**(`method`: string, `params?`: Array‹object› | object, `baseurl?`: string, `contentType?`: string, `acceptType?`: string): *Promise‹[RequestResponseData](utils_types.requestresponsedata.md)›*

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
