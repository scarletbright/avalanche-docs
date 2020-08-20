[avalanche](../README.md) › [Common-Payload](../modules/common_payload.md) › [PayloadBase](common_payload.payloadbase.md)

# Class: PayloadBase

Base class for payloads.

## Hierarchy

* **PayloadBase**

  ↳ [BINPayload](common_payload.binpayload.md)

  ↳ [UTF8Payload](common_payload.utf8payload.md)

  ↳ [HEXSTRPayload](common_payload.hexstrpayload.md)

  ↳ [B58STRPayload](common_payload.b58strpayload.md)

  ↳ [B64STRPayload](common_payload.b64strpayload.md)

  ↳ [BIGNUMPayload](common_payload.bignumpayload.md)

  ↳ [ChainAddressPayload](common_payload.chainaddresspayload.md)

  ↳ [cb58EncodedPayload](common_payload.cb58encodedpayload.md)

  ↳ [JSONPayload](common_payload.jsonpayload.md)

## Index

### Constructors

* [constructor](common_payload.payloadbase.md#constructor)

### Properties

* [payload](common_payload.payloadbase.md#protected-payload)
* [typeid](common_payload.payloadbase.md#protected-typeid)

### Methods

* [fromBuffer](common_payload.payloadbase.md#frombuffer)
* [getContent](common_payload.payloadbase.md#getcontent)
* [getPayload](common_payload.payloadbase.md#getpayload)
* [returnType](common_payload.payloadbase.md#abstract-returntype)
* [toBuffer](common_payload.payloadbase.md#tobuffer)
* [typeID](common_payload.payloadbase.md#typeid)
* [typeName](common_payload.payloadbase.md#typename)

## Constructors

###  constructor

\+ **new PayloadBase**(): *[PayloadBase](common_payload.payloadbase.md)*

Defined in src/utils/payload.ts:228

**Returns:** *[PayloadBase](common_payload.payloadbase.md)*

## Properties

### `Protected` payload

• **payload**: *Buffer* = Buffer.alloc(0)

Defined in src/utils/payload.ts:166

___

### `Protected` typeid

• **typeid**: *number* = undefined

Defined in src/utils/payload.ts:167

## Methods

###  fromBuffer

▸ **fromBuffer**(`bytes`: Buffer, `offset`: number): *number*

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

Defined in src/utils/payload.ts:186

Returns the payload content (minus typeID).

**Returns:** *Buffer*

___

###  getPayload

▸ **getPayload**(): *Buffer*

Defined in src/utils/payload.ts:194

Returns the payload (with typeID).

**Returns:** *Buffer*

___

### `Abstract` returnType

▸ **returnType**(...`args`: any): *any*

Defined in src/utils/payload.ts:228

Returns the expected type for the payload.

**Parameters:**

Name | Type |
------ | ------ |
`...args` | any |

**Returns:** *any*

___

###  toBuffer

▸ **toBuffer**(): *Buffer*

Defined in src/utils/payload.ts:217

Encodes the payload as a [Buffer](https://github.com/feross/buffer) including 4 bytes for the length and TypeID.

**Returns:** *Buffer*

___

###  typeID

▸ **typeID**(): *number*

Defined in src/utils/payload.ts:172

Returns the TypeID for the payload.

**Returns:** *number*

___

###  typeName

▸ **typeName**(): *string*

Defined in src/utils/payload.ts:179

Returns the string name for the payload's type.

**Returns:** *string*
