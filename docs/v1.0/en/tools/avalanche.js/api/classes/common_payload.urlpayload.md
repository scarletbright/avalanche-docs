[avalanche](../README.md) › [Common-Payload](../modules/common_payload.md) › [URLPayload](common_payload.urlpayload.md)

# Class: URLPayload

Class for payloads representing URL strings.

## Hierarchy

  ↳ [UTF8Payload](common_payload.utf8payload.md)

  ↳ **URLPayload**

## Index

### Constructors

* [constructor](common_payload.urlpayload.md#constructor)

### Properties

* [payload](common_payload.urlpayload.md#protected-payload)
* [typeid](common_payload.urlpayload.md#protected-typeid)

### Methods

* [fromBuffer](common_payload.urlpayload.md#frombuffer)
* [getContent](common_payload.urlpayload.md#getcontent)
* [getPayload](common_payload.urlpayload.md#getpayload)
* [returnType](common_payload.urlpayload.md#returntype)
* [toBuffer](common_payload.urlpayload.md#tobuffer)
* [typeID](common_payload.urlpayload.md#typeid)
* [typeName](common_payload.urlpayload.md#typename)

## Constructors

###  constructor

\+ **new URLPayload**(`payload`: any): *[URLPayload](common_payload.urlpayload.md)*

*Inherited from [UTF8Payload](common_payload.utf8payload.md).[constructor](common_payload.utf8payload.md#constructor)*

*Overrides [PayloadBase](common_payload.payloadbase.md).[constructor](common_payload.payloadbase.md#constructor)*

Defined in src/utils/payload.ts:270

**Parameters:**

Name | Type | Default | Description |
------ | ------ | ------ | ------ |
`payload` | any | undefined | Buffer utf8 string  |

**Returns:** *[URLPayload](common_payload.urlpayload.md)*

## Properties

### `Protected` payload

• **payload**: *Buffer* = Buffer.alloc(0)

*Inherited from [PayloadBase](common_payload.payloadbase.md).[payload](common_payload.payloadbase.md#protected-payload)*

Defined in src/utils/payload.ts:166

___

### `Protected` typeid

• **typeid**: *number* = 27

*Overrides [UTF8Payload](common_payload.utf8payload.md).[typeid](common_payload.utf8payload.md#protected-typeid)*

Defined in src/utils/payload.ts:628

## Methods

###  fromBuffer

▸ **fromBuffer**(`bytes`: Buffer, `offset`: number): *number*

*Inherited from [PayloadBase](common_payload.payloadbase.md).[fromBuffer](common_payload.payloadbase.md#frombuffer)*

Defined in src/utils/payload.ts:204

Decodes the payload as a [Buffer](https://github.com/feross/buffer) including 4 bytes for the length and TypeID.

**Parameters:**

Name | Type | Default |
------ | ------ | ------ |
`bytes` | Buffer | - |
`offset` | number | 0 |

**Returns:** *number*

___

###  getContent

▸ **getContent**(): *Buffer*

*Inherited from [PayloadBase](common_payload.payloadbase.md).[getContent](common_payload.payloadbase.md#getcontent)*

Defined in src/utils/payload.ts:186

Returns the payload content (minus typeID).

**Returns:** *Buffer*

___

###  getPayload

▸ **getPayload**(): *Buffer*

*Inherited from [PayloadBase](common_payload.payloadbase.md).[getPayload](common_payload.payloadbase.md#getpayload)*

Defined in src/utils/payload.ts:194

Returns the payload (with typeID).

**Returns:** *Buffer*

___

###  returnType

▸ **returnType**(): *string*

*Inherited from [UTF8Payload](common_payload.utf8payload.md).[returnType](common_payload.utf8payload.md#returntype)*

*Overrides [PayloadBase](common_payload.payloadbase.md).[returnType](common_payload.payloadbase.md#abstract-returntype)*

Defined in src/utils/payload.ts:268

Returns a string for the payload.

**Returns:** *string*

___

###  toBuffer

▸ **toBuffer**(): *Buffer*

*Inherited from [PayloadBase](common_payload.payloadbase.md).[toBuffer](common_payload.payloadbase.md#tobuffer)*

Defined in src/utils/payload.ts:217

Encodes the payload as a [Buffer](https://github.com/feross/buffer) including 4 bytes for the length and TypeID.

**Returns:** *Buffer*

___

###  typeID

▸ **typeID**(): *number*

*Inherited from [PayloadBase](common_payload.payloadbase.md).[typeID](common_payload.payloadbase.md#typeid)*

Defined in src/utils/payload.ts:172

Returns the TypeID for the payload.

**Returns:** *number*

___

###  typeName

▸ **typeName**(): *string*

*Inherited from [PayloadBase](common_payload.payloadbase.md).[typeName](common_payload.payloadbase.md#typename)*

Defined in src/utils/payload.ts:179

Returns the string name for the payload's type.

**Returns:** *string*
