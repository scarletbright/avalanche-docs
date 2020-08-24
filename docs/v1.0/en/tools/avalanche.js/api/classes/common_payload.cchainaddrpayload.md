[avalanche](../README.md) › [Common-Payload](../modules/common_payload.md) › [CCHAINADDRPayload](common_payload.cchainaddrpayload.md)

# Class: CCHAINADDRPayload

Class for payloads representing C-Chain addresses.

## Hierarchy

  ↳ [ChainAddressPayload](common_payload.chainaddresspayload.md)

  ↳ **CCHAINADDRPayload**

## Index

### Constructors

* [constructor](common_payload.cchainaddrpayload.md#constructor)

### Properties

* [chainid](common_payload.cchainaddrpayload.md#protected-chainid)
* [payload](common_payload.cchainaddrpayload.md#protected-payload)
* [typeid](common_payload.cchainaddrpayload.md#protected-typeid)

### Methods

* [fromBuffer](common_payload.cchainaddrpayload.md#frombuffer)
* [getContent](common_payload.cchainaddrpayload.md#getcontent)
* [getPayload](common_payload.cchainaddrpayload.md#getpayload)
* [returnChainID](common_payload.cchainaddrpayload.md#returnchainid)
* [returnType](common_payload.cchainaddrpayload.md#returntype)
* [toBuffer](common_payload.cchainaddrpayload.md#tobuffer)
* [typeID](common_payload.cchainaddrpayload.md#typeid)
* [typeName](common_payload.cchainaddrpayload.md#typename)

## Constructors

###  constructor

\+ **new CCHAINADDRPayload**(`payload`: any): *[CCHAINADDRPayload](common_payload.cchainaddrpayload.md)*

*Inherited from [ChainAddressPayload](common_payload.chainaddresspayload.md).[constructor](common_payload.chainaddresspayload.md#constructor)*

*Overrides [PayloadBase](common_payload.payloadbase.md).[constructor](common_payload.payloadbase.md#constructor)*

Defined in src/utils/payload.ts:411

**Parameters:**

Name | Type | Default | Description |
------ | ------ | ------ | ------ |
`payload` | any | undefined | Buffer or address string  |

**Returns:** *[CCHAINADDRPayload](common_payload.cchainaddrpayload.md)*

## Properties

### `Protected` chainid

• **chainid**: *string* = "C"

*Overrides [ChainAddressPayload](common_payload.chainaddresspayload.md).[chainid](common_payload.chainaddresspayload.md#protected-chainid)*

Defined in src/utils/payload.ts:446

___

### `Protected` payload

• **payload**: *Buffer* = Buffer.alloc(0)

*Inherited from [PayloadBase](common_payload.payloadbase.md).[payload](common_payload.payloadbase.md#protected-payload)*

Defined in src/utils/payload.ts:166

___

### `Protected` typeid

• **typeid**: *number* = 8

*Overrides [ChainAddressPayload](common_payload.chainaddresspayload.md).[typeid](common_payload.chainaddresspayload.md#protected-typeid)*

Defined in src/utils/payload.ts:445

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

###  returnChainID

▸ **returnChainID**(): *string*

*Inherited from [ChainAddressPayload](common_payload.chainaddresspayload.md).[returnChainID](common_payload.chainaddresspayload.md#returnchainid)*

Defined in src/utils/payload.ts:402

Returns the chainid.

**Returns:** *string*

___

###  returnType

▸ **returnType**(): *string*

*Overrides [ChainAddressPayload](common_payload.chainaddresspayload.md).[returnType](common_payload.chainaddresspayload.md#returntype)*

Defined in src/utils/payload.ts:451

Returns an address string for the payload.

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
