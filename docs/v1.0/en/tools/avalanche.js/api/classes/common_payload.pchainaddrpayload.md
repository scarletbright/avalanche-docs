[avalanche](../README.md) › [Common-Payload](../modules/common_payload.md) › [PCHAINADDRPayload](common_payload.pchainaddrpayload.md)

# Class: PCHAINADDRPayload

Class for payloads representing P-Chain addresses.

## Hierarchy

  ↳ [ChainAddressPayload](common_payload.chainaddresspayload.md)

  ↳ **PCHAINADDRPayload**

## Index

### Constructors

* [constructor](common_payload.pchainaddrpayload.md#constructor)

### Properties

* [chainid](common_payload.pchainaddrpayload.md#protected-chainid)
* [payload](common_payload.pchainaddrpayload.md#protected-payload)
* [typeid](common_payload.pchainaddrpayload.md#protected-typeid)

### Methods

* [fromBuffer](common_payload.pchainaddrpayload.md#frombuffer)
* [getContent](common_payload.pchainaddrpayload.md#getcontent)
* [getPayload](common_payload.pchainaddrpayload.md#getpayload)
* [returnChainID](common_payload.pchainaddrpayload.md#returnchainid)
* [returnType](common_payload.pchainaddrpayload.md#returntype)
* [toBuffer](common_payload.pchainaddrpayload.md#tobuffer)
* [typeID](common_payload.pchainaddrpayload.md#typeid)
* [typeName](common_payload.pchainaddrpayload.md#typename)

## Constructors

###  constructor

\+ **new PCHAINADDRPayload**(`payload`: any): *[PCHAINADDRPayload](common_payload.pchainaddrpayload.md)*

*Inherited from [ChainAddressPayload](common_payload.chainaddresspayload.md).[constructor](common_payload.chainaddresspayload.md#constructor)*

*Overrides [PayloadBase](common_payload.payloadbase.md).[constructor](common_payload.payloadbase.md#constructor)*

Defined in src/utils/payload.ts:411

**Parameters:**

Name | Type | Default | Description |
------ | ------ | ------ | ------ |
`payload` | any | undefined | Buffer or address string  |

**Returns:** *[PCHAINADDRPayload](common_payload.pchainaddrpayload.md)*

## Properties

### `Protected` chainid

• **chainid**: *string* = "P"

*Overrides [ChainAddressPayload](common_payload.chainaddresspayload.md).[chainid](common_payload.chainaddresspayload.md#protected-chainid)*

Defined in src/utils/payload.ts:438

___

### `Protected` payload

• **payload**: *Buffer* = Buffer.alloc(0)

*Inherited from [PayloadBase](common_payload.payloadbase.md).[payload](common_payload.payloadbase.md#protected-payload)*

Defined in src/utils/payload.ts:166

___

### `Protected` typeid

• **typeid**: *number* = 7

*Overrides [ChainAddressPayload](common_payload.chainaddresspayload.md).[typeid](common_payload.chainaddresspayload.md#protected-typeid)*

Defined in src/utils/payload.ts:437

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

▸ **returnType**(`hrp`: string): *string*

*Inherited from [ChainAddressPayload](common_payload.chainaddresspayload.md).[returnType](common_payload.chainaddresspayload.md#returntype)*

*Overrides [PayloadBase](common_payload.payloadbase.md).[returnType](common_payload.payloadbase.md#abstract-returntype)*

Defined in src/utils/payload.ts:409

Returns an address string for the payload.

**Parameters:**

Name | Type |
------ | ------ |
`hrp` | string |

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
