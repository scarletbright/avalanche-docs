[avalanche](../README.md) › [Common-Payload](../modules/common_payload.md) › [SECPENCPayload](common_payload.secpencpayload.md)

# Class: SECPENCPayload

Class for payloads representing secp256k1 encrypted messages.
convention: public key (65 bytes) + secp256k1 encrypted message for that public key

## Hierarchy

  ↳ [B58STRPayload](common_payload.b58strpayload.md)

  ↳ **SECPENCPayload**

## Index

### Constructors

* [constructor](common_payload.secpencpayload.md#constructor)

### Properties

* [payload](common_payload.secpencpayload.md#protected-payload)
* [typeid](common_payload.secpencpayload.md#protected-typeid)

### Methods

* [fromBuffer](common_payload.secpencpayload.md#frombuffer)
* [getContent](common_payload.secpencpayload.md#getcontent)
* [getPayload](common_payload.secpencpayload.md#getpayload)
* [returnType](common_payload.secpencpayload.md#returntype)
* [toBuffer](common_payload.secpencpayload.md#tobuffer)
* [typeID](common_payload.secpencpayload.md#typeid)
* [typeName](common_payload.secpencpayload.md#typename)

## Constructors

###  constructor

\+ **new SECPENCPayload**(`payload`: any): *[SECPENCPayload](common_payload.secpencpayload.md)*

*Inherited from [B58STRPayload](common_payload.b58strpayload.md).[constructor](common_payload.b58strpayload.md#constructor)*

*Overrides [PayloadBase](common_payload.payloadbase.md).[constructor](common_payload.payloadbase.md#constructor)*

Defined in src/utils/payload.ts:323

**Parameters:**

Name | Type | Default | Description |
------ | ------ | ------ | ------ |
`payload` | any | undefined | Buffer or cb58 encoded string  |

**Returns:** *[SECPENCPayload](common_payload.secpencpayload.md)*

## Properties

### `Protected` payload

• **payload**: *Buffer* = Buffer.alloc(0)

*Inherited from [PayloadBase](common_payload.payloadbase.md).[payload](common_payload.payloadbase.md#protected-payload)*

Defined in src/utils/payload.ts:166

___

### `Protected` typeid

• **typeid**: *number* = 17

*Overrides [B58STRPayload](common_payload.b58strpayload.md).[typeid](common_payload.b58strpayload.md#protected-typeid)*

Defined in src/utils/payload.ts:542

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

*Inherited from [B58STRPayload](common_payload.b58strpayload.md).[returnType](common_payload.b58strpayload.md#returntype)*

*Overrides [PayloadBase](common_payload.payloadbase.md).[returnType](common_payload.payloadbase.md#abstract-returntype)*

Defined in src/utils/payload.ts:321

Returns a base58 string for the payload.

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
