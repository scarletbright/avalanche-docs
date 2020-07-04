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

*Defined in [src/utils/types.ts:269](https://github.com/ava-labs/avalanche.js/blob/eabcc2f/src/utils/types.ts#L269)*

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

*Defined in [src/utils/types.ts:85](https://github.com/ava-labs/avalanche.js/blob/eabcc2f/src/utils/types.ts#L85)*

___

### `Protected` baseurl

• **baseurl**: *string*

*Inherited from [APIBase](utils_types.apibase.md).[baseurl](utils_types.apibase.md#protected-baseurl)*

*Defined in [src/utils/types.ts:39](https://github.com/ava-labs/avalanche.js/blob/eabcc2f/src/utils/types.ts#L39)*

___

### `Protected` contentType

• **contentType**: *string*

*Defined in [src/utils/types.ts:83](https://github.com/ava-labs/avalanche.js/blob/eabcc2f/src/utils/types.ts#L83)*

___

### `Protected` core

• **core**: *[AvalancheCore](avalanchecore.avalanchecore-1.md)*

*Inherited from [APIBase](utils_types.apibase.md).[core](utils_types.apibase.md#protected-core)*

*Defined in [src/utils/types.ts:37](https://github.com/ava-labs/avalanche.js/blob/eabcc2f/src/utils/types.ts#L37)*

___

### `Protected` db

• **db**: *StoreAPI*

*Inherited from [APIBase](utils_types.apibase.md).[db](utils_types.apibase.md#protected-db)*

*Defined in [src/utils/types.ts:41](https://github.com/ava-labs/avalanche.js/blob/eabcc2f/src/utils/types.ts#L41)*

## Methods

###  delete

▸ **delete**(`method`: string, `params?`: Array‹object› | object, `baseurl?`: string, `contentType?`: string, `acceptType?`: string): *Promise‹[RequestResponseData](utils_types.requestresponsedata.md)›*

*Defined in [src/utils/types.ts:188](https://github.com/ava-labs/avalanche.js/blob/eabcc2f/src/utils/types.ts#L188)*

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

*Defined in [src/utils/types.ts:87](https://github.com/ava-labs/avalanche.js/blob/eabcc2f/src/utils/types.ts#L87)*

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

*Defined in [src/utils/types.ts:269](https://github.com/ava-labs/avalanche.js/blob/eabcc2f/src/utils/types.ts#L269)*

Returns what type of representation is desired at the client side

**Returns:** *string*

___

###  getBaseURL

▸ **getBaseURL**(): *string*

*Inherited from [APIBase](utils_types.apibase.md).[getBaseURL](utils_types.apibase.md#getbaseurl)*

*Defined in [src/utils/types.ts:64](https://github.com/ava-labs/avalanche.js/blob/eabcc2f/src/utils/types.ts#L64)*

Returns the baseurl's path.

**Returns:** *string*

___

###  getContentType

▸ **getContentType**(): *string*

*Defined in [src/utils/types.ts:264](https://github.com/ava-labs/avalanche.js/blob/eabcc2f/src/utils/types.ts#L264)*

Returns the type of the entity attached to the incoming request

**Returns:** *string*

___

###  getDB

▸ **getDB**(): *StoreAPI*

*Inherited from [APIBase](utils_types.apibase.md).[getDB](utils_types.apibase.md#getdb)*

*Defined in [src/utils/types.ts:69](https://github.com/ava-labs/avalanche.js/blob/eabcc2f/src/utils/types.ts#L69)*

Returns the baseurl's database.

**Returns:** *StoreAPI*

___

###  patch

▸ **patch**(`method`: string, `params?`: Array‹object› | object, `baseurl?`: string, `contentType?`: string, `acceptType?`: string): *Promise‹[RequestResponseData](utils_types.requestresponsedata.md)›*

*Defined in [src/utils/types.ts:224](https://github.com/ava-labs/avalanche.js/blob/eabcc2f/src/utils/types.ts#L224)*

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

*Defined in [src/utils/types.ts:114](https://github.com/ava-labs/avalanche.js/blob/eabcc2f/src/utils/types.ts#L114)*

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

*Defined in [src/utils/types.ts:151](https://github.com/ava-labs/avalanche.js/blob/eabcc2f/src/utils/types.ts#L151)*

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

*Defined in [src/utils/types.ts:48](https://github.com/ava-labs/avalanche.js/blob/eabcc2f/src/utils/types.ts#L48)*

Sets the path of the APIs baseurl.

**Parameters:**

Name | Type | Description |
------ | ------ | ------ |
`baseurl` | string | Path of the APIs baseurl - ex: "/ext/bc/avm"  |

**Returns:** *void*
