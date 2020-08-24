[avalanche](../README.md) › [Common-Payload](../modules/common_payload.md) › [cb58EncodedPayload](common_payload.cb58encodedpayload.md)

# Class: cb58EncodedPayload

Class for payloads representing data serialized by bintools.cb58Encode().

## Hierarchy

* [PayloadBase](common_payload.payloadbase.md)

  ↳ **cb58EncodedPayload**

  ↳ [TXIDPayload](common_payload.txidpayload.md)

  ↳ [ASSETIDPayload](common_payload.assetidpayload.md)

  ↳ [UTXOIDPayload](common_payload.utxoidpayload.md)

  ↳ [SUBNETIDPayload](common_payload.subnetidpayload.md)

  ↳ [CHAINIDPayload](common_payload.chainidpayload.md)

  ↳ [NODEIDPayload](common_payload.nodeidpayload.md)

## Index

### Constructors

* [constructor](common_payload.cb58encodedpayload.md#constructor)

### Properties

* [payload](common_payload.cb58encodedpayload.md#protected-payload)
* [typeid](common_payload.cb58encodedpayload.md#protected-typeid)

### Methods

* [fromBuffer](common_payload.cb58encodedpayload.md#frombuffer)
* [getContent](common_payload.cb58encodedpayload.md#getcontent)
* [getPayload](common_payload.cb58encodedpayload.md#getpayload)
* [returnType](common_payload.cb58encodedpayload.md#returntype)
* [toBuffer](common_payload.cb58encodedpayload.md#tobuffer)
* [typeID](common_payload.cb58encodedpayload.md#typeid)
* [typeName](common_payload.cb58encodedpayload.md#typename)

## Constructors

###  constructor

\+ **new cb58EncodedPayload**(`payload`: any): *[cb58EncodedPayload](common_payload.cb58encodedpayload.md)*

*Overrides [PayloadBase](common_payload.payloadbase.md).[constructor](common_payload.payloadbase.md#constructor)*

Defined in src/utils/payload.ts:466

**Parameters:**

Name | Type | Default | Description |
------ | ------ | ------ | ------ |
`payload` | any | undefined | Buffer or cb58 encoded string  |

**Returns:** *[cb58EncodedPayload](common_payload.cb58encodedpayload.md)*

## Properties

### `Protected` payload

• **payload**: *Buffer* = Buffer.alloc(0)

*Inherited from [PayloadBase](common_payload.payloadbase.md).[payload](common_payload.payloadbase.md#protected-payload)*

Defined in src/utils/payload.ts:166

___

### `Protected` typeid

• **typeid**: *number* = undefined

*Inherited from [PayloadBase](common_payload.payloadbase.md).[typeid](common_payload.payloadbase.md#protected-typeid)*

Defined in src/utils/payload.ts:167

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

*Overrides [PayloadBase](common_payload.payloadbase.md).[returnType](common_payload.payloadbase.md#abstract-returntype)*

Defined in src/utils/payload.ts:464

Returns a bintools.cb58Encoded string for the payload.

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
