[avalanche](../README.md) › [Common-Payload](../modules/common_payload.md) › [PNGPayload](common_payload.pngpayload.md)

# Class: PNGPayload

## Hierarchy

  ↳ [BINPayload](common_payload.binpayload.md)

  ↳ **PNGPayload**

## Index

### Constructors

* [constructor](common_payload.pngpayload.md#constructor)

### Properties

* [payload](common_payload.pngpayload.md#protected-payload)
* [typeid](common_payload.pngpayload.md#protected-typeid)

### Methods

* [fromBuffer](common_payload.pngpayload.md#frombuffer)
* [getContent](common_payload.pngpayload.md#getcontent)
* [getPayload](common_payload.pngpayload.md#getpayload)
* [returnType](common_payload.pngpayload.md#returntype)
* [toBuffer](common_payload.pngpayload.md#tobuffer)
* [typeID](common_payload.pngpayload.md#typeid)
* [typeName](common_payload.pngpayload.md#typename)

## Constructors

###  constructor

\+ **new PNGPayload**(`payload`: any): *[PNGPayload](common_payload.pngpayload.md)*

*Inherited from [BINPayload](common_payload.binpayload.md).[constructor](common_payload.binpayload.md#constructor)*

*Overrides [PayloadBase](common_payload.payloadbase.md).[constructor](common_payload.payloadbase.md#constructor)*

Defined in src/utils/payload.ts:245

**Parameters:**

Name | Type | Default | Description |
------ | ------ | ------ | ------ |
`payload` | any | undefined | Buffer only  |

**Returns:** *[PNGPayload](common_payload.pngpayload.md)*

## Properties

### `Protected` payload

• **payload**: *Buffer* = Buffer.alloc(0)

*Inherited from [PayloadBase](common_payload.payloadbase.md).[payload](common_payload.payloadbase.md#protected-payload)*

Defined in src/utils/payload.ts:166

___

### `Protected` typeid

• **typeid**: *number* = 19

*Overrides [BINPayload](common_payload.binpayload.md).[typeid](common_payload.binpayload.md#protected-typeid)*

Defined in src/utils/payload.ts:553

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
