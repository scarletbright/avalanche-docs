[avalanche](../README.md) › [Common-Payload](../modules/common_payload.md) › [IPFSPayload](common_payload.ipfspayload.md)

# Class: IPFSPayload

Class for payloads representing IPFS addresses.

## Hierarchy

  ↳ [B58STRPayload](common_payload.b58strpayload.md)

  ↳ **IPFSPayload**

## Index

### Constructors

* [constructor](common_payload.ipfspayload.md#constructor)

### Properties

* [payload](common_payload.ipfspayload.md#protected-payload)
* [typeid](common_payload.ipfspayload.md#protected-typeid)

### Methods

* [fromBuffer](common_payload.ipfspayload.md#frombuffer)
* [getContent](common_payload.ipfspayload.md#getcontent)
* [getPayload](common_payload.ipfspayload.md#getpayload)
* [returnType](common_payload.ipfspayload.md#returntype)
* [toBuffer](common_payload.ipfspayload.md#tobuffer)
* [typeID](common_payload.ipfspayload.md#typeid)
* [typeName](common_payload.ipfspayload.md#typename)

## Constructors

###  constructor

\+ **new IPFSPayload**(`payload`: any): *[IPFSPayload](common_payload.ipfspayload.md)*

*Inherited from [B58STRPayload](common_payload.b58strpayload.md).[constructor](common_payload.b58strpayload.md#constructor)*

*Overrides [PayloadBase](common_payload.payloadbase.md).[constructor](common_payload.payloadbase.md#constructor)*

Defined in src/utils/payload.ts:323

**Parameters:**

Name | Type | Default | Description |
------ | ------ | ------ | ------ |
`payload` | any | undefined | Buffer or cb58 encoded string  |

**Returns:** *[IPFSPayload](common_payload.ipfspayload.md)*

## Properties

### `Protected` payload

• **payload**: *Buffer* = Buffer.alloc(0)

*Inherited from [PayloadBase](common_payload.payloadbase.md).[payload](common_payload.payloadbase.md#protected-payload)*

Defined in src/utils/payload.ts:166

___

### `Protected` typeid

• **typeid**: *number* = 28

*Overrides [B58STRPayload](common_payload.b58strpayload.md).[typeid](common_payload.b58strpayload.md#protected-typeid)*

Defined in src/utils/payload.ts:635

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
