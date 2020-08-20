[avalanche](../README.md) › [Common-Payload](../modules/common_payload.md) › [JPEGPayload](common_payload.jpegpayload.md)

# Class: JPEGPayload

Class for payloads representing JPEG images.

## Hierarchy

  ↳ [BINPayload](common_payload.binpayload.md)

  ↳ **JPEGPayload**

## Index

### Constructors

* [constructor](common_payload.jpegpayload.md#constructor)

### Properties

* [payload](common_payload.jpegpayload.md#protected-payload)
* [typeid](common_payload.jpegpayload.md#protected-typeid)

### Methods

* [fromBuffer](common_payload.jpegpayload.md#frombuffer)
* [getContent](common_payload.jpegpayload.md#getcontent)
* [getPayload](common_payload.jpegpayload.md#getpayload)
* [returnType](common_payload.jpegpayload.md#returntype)
* [toBuffer](common_payload.jpegpayload.md#tobuffer)
* [typeID](common_payload.jpegpayload.md#typeid)
* [typeName](common_payload.jpegpayload.md#typename)

## Constructors

###  constructor

\+ **new JPEGPayload**(`payload`: any): *[JPEGPayload](common_payload.jpegpayload.md)*

*Inherited from [BINPayload](common_payload.binpayload.md).[constructor](common_payload.binpayload.md#constructor)*

*Overrides [PayloadBase](common_payload.payloadbase.md).[constructor](common_payload.payloadbase.md#constructor)*

Defined in src/utils/payload.ts:245

**Parameters:**

Name | Type | Default | Description |
------ | ------ | ------ | ------ |
`payload` | any | undefined | Buffer only  |

**Returns:** *[JPEGPayload](common_payload.jpegpayload.md)*

## Properties

### `Protected` payload

• **payload**: *Buffer* = Buffer.alloc(0)

*Inherited from [PayloadBase](common_payload.payloadbase.md).[payload](common_payload.payloadbase.md#protected-payload)*

Defined in src/utils/payload.ts:166

___

### `Protected` typeid

• **typeid**: *number* = 18

*Overrides [BINPayload](common_payload.binpayload.md).[typeid](common_payload.binpayload.md#protected-typeid)*

Defined in src/utils/payload.ts:549

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

▸ **returnType**(): *Buffer*

*Inherited from [BINPayload](common_payload.binpayload.md).[returnType](common_payload.binpayload.md#returntype)*

*Overrides [PayloadBase](common_payload.payloadbase.md).[returnType](common_payload.payloadbase.md#abstract-returntype)*

Defined in src/utils/payload.ts:243

Returns a [Buffer](https://github.com/feross/buffer) for the payload.

**Returns:** *Buffer*

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
