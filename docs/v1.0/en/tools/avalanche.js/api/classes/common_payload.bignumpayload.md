[avalanche](../README.md) › [Common-Payload](../modules/common_payload.md) › [BIGNUMPayload](common_payload.bignumpayload.md)

# Class: BIGNUMPayload

Class for payloads representing Big Numbers.

**`param`** Accepts a Buffer, BN, or base64 string

## Hierarchy

* [PayloadBase](common_payload.payloadbase.md)

  ↳ **BIGNUMPayload**

## Index

### Constructors

* [constructor](common_payload.bignumpayload.md#constructor)

### Properties

* [payload](common_payload.bignumpayload.md#protected-payload)
* [typeid](common_payload.bignumpayload.md#protected-typeid)

### Methods

* [fromBuffer](common_payload.bignumpayload.md#frombuffer)
* [getContent](common_payload.bignumpayload.md#getcontent)
* [getPayload](common_payload.bignumpayload.md#getpayload)
* [returnType](common_payload.bignumpayload.md#returntype)
* [toBuffer](common_payload.bignumpayload.md#tobuffer)
* [typeID](common_payload.bignumpayload.md#typeid)
* [typeName](common_payload.bignumpayload.md#typename)

## Constructors

###  constructor

\+ **new BIGNUMPayload**(`payload`: any): *[BIGNUMPayload](common_payload.bignumpayload.md)*

*Overrides [PayloadBase](common_payload.payloadbase.md).[constructor](common_payload.payloadbase.md#constructor)*

Defined in src/utils/payload.ts:375

**Parameters:**

Name | Type | Default | Description |
------ | ------ | ------ | ------ |
`payload` | any | undefined | Buffer, BN, or base64 string  |

**Returns:** *[BIGNUMPayload](common_payload.bignumpayload.md)*

## Properties

### `Protected` payload

• **payload**: *Buffer* = Buffer.alloc(0)

*Inherited from [PayloadBase](common_payload.payloadbase.md).[payload](common_payload.payloadbase.md#protected-payload)*

Defined in src/utils/payload.ts:166

___

### `Protected` typeid

• **typeid**: *number* = 5

*Overrides [PayloadBase](common_payload.payloadbase.md).[typeid](common_payload.payloadbase.md#protected-typeid)*

Defined in src/utils/payload.ts:368

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

▸ **returnType**(): *BN*

*Overrides [PayloadBase](common_payload.payloadbase.md).[returnType](common_payload.payloadbase.md#abstract-returntype)*

Defined in src/utils/payload.ts:373

Returns a [BN](https://github.com/indutny/bn.js/) for the payload.

**Returns:** *BN*

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
