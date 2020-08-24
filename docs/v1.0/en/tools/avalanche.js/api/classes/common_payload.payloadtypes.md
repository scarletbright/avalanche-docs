[avalanche](../README.md) › [Common-Payload](../modules/common_payload.md) › [PayloadTypes](common_payload.payloadtypes.md)

# Class: PayloadTypes

Class for determining payload types and managing the lookup table.

## Hierarchy

* **PayloadTypes**

## Index

### Constructors

* [constructor](common_payload.payloadtypes.md#private-constructor)

### Properties

* [types](common_payload.payloadtypes.md#protected-types)
* [instance](common_payload.payloadtypes.md#static-private-instance)

### Methods

* [getContent](common_payload.payloadtypes.md#getcontent)
* [getPayload](common_payload.payloadtypes.md#getpayload)
* [getTypeID](common_payload.payloadtypes.md#gettypeid)
* [lookupID](common_payload.payloadtypes.md#lookupid)
* [lookupType](common_payload.payloadtypes.md#lookuptype)
* [recast](common_payload.payloadtypes.md#recast)
* [select](common_payload.payloadtypes.md#select)
* [getInstance](common_payload.payloadtypes.md#static-getinstance)

## Constructors

### `Private` constructor

\+ **new PayloadTypes**(): *[PayloadTypes](common_payload.payloadtypes.md)*

Defined in src/utils/payload.ts:151

**Returns:** *[PayloadTypes](common_payload.payloadtypes.md)*

## Properties

### `Protected` types

• **types**: *Array‹string›* = []

Defined in src/utils/payload.ts:21

___

### `Static` `Private` instance

▪ **instance**: *[PayloadTypes](common_payload.payloadtypes.md)*

Defined in src/utils/payload.ts:20

## Methods

###  getContent

▸ **getContent**(`payload`: Buffer): *Buffer*

Defined in src/utils/payload.ts:26

Given an encoded payload buffer returns the payload content (minus typeID).

**Parameters:**

Name | Type |
------ | ------ |
`payload` | Buffer |

**Returns:** *Buffer*

___

###  getPayload

▸ **getPayload**(`payload`: Buffer): *Buffer*

Defined in src/utils/payload.ts:34

Given an encoded payload buffer returns the payload (with typeID).

**Parameters:**

Name | Type |
------ | ------ |
`payload` | Buffer |

**Returns:** *Buffer*

___

###  getTypeID

▸ **getTypeID**(`payload`: Buffer): *number*

Defined in src/utils/payload.ts:42

Given a payload buffer returns the proper TypeID.

**Parameters:**

Name | Type |
------ | ------ |
`payload` | Buffer |

**Returns:** *number*

___

###  lookupID

▸ **lookupID**(`typestr`: string): *number*

Defined in src/utils/payload.ts:53

Given a type string returns the proper TypeID.

**Parameters:**

Name | Type |
------ | ------ |
`typestr` | string |

**Returns:** *number*

___

###  lookupType

▸ **lookupType**(`value`: number): *string*

Defined in src/utils/payload.ts:60

Given a TypeID returns a string describing the payload type.

**Parameters:**

Name | Type |
------ | ------ |
`value` | number |

**Returns:** *string*

___

###  recast

▸ **recast**(`unknowPayload`: [PayloadBase](common_payload.payloadbase.md)): *[PayloadBase](common_payload.payloadbase.md)*

Defined in src/utils/payload.ts:138

Given a [PayloadBase](common_payload.payloadbase.md) which may not be cast properly, returns a properly cast [PayloadBase](common_payload.payloadbase.md).

**Parameters:**

Name | Type |
------ | ------ |
`unknowPayload` | [PayloadBase](common_payload.payloadbase.md) |

**Returns:** *[PayloadBase](common_payload.payloadbase.md)*

___

###  select

▸ **select**(`typeid`: number, ...`args`: Array‹any›): *[PayloadBase](common_payload.payloadbase.md)*

Defined in src/utils/payload.ts:67

Given a TypeID returns the proper [PayloadBase](common_payload.payloadbase.md).

**Parameters:**

Name | Type |
------ | ------ |
`typeid` | number |
`...args` | Array‹any› |

**Returns:** *[PayloadBase](common_payload.payloadbase.md)*

___

### `Static` getInstance

▸ **getInstance**(): *[PayloadTypes](common_payload.payloadtypes.md)*

Defined in src/utils/payload.ts:145

Returns the [PayloadTypes](common_payload.payloadtypes.md) singleton.

**Returns:** *[PayloadTypes](common_payload.payloadtypes.md)*
