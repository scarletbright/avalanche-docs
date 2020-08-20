[avalanche](../README.md) › [Common-Payload](../modules/common_payload.md) › [XCHAINADDRPayload](common_payload.xchainaddrpayload.md)

# Class: XCHAINADDRPayload

Class for payloads representing X-Chin addresses.

## Hierarchy

  ↳ [ChainAddressPayload](common_payload.chainaddresspayload.md)

  ↳ **XCHAINADDRPayload**

## Index

### Constructors

* [constructor](common_payload.xchainaddrpayload.md#constructor)

### Properties

* [chainid](common_payload.xchainaddrpayload.md#protected-chainid)
* [payload](common_payload.xchainaddrpayload.md#protected-payload)
* [typeid](common_payload.xchainaddrpayload.md#protected-typeid)

### Methods

* [fromBuffer](common_payload.xchainaddrpayload.md#frombuffer)
* [getContent](common_payload.xchainaddrpayload.md#getcontent)
* [getPayload](common_payload.xchainaddrpayload.md#getpayload)
* [returnChainID](common_payload.xchainaddrpayload.md#returnchainid)
* [returnType](common_payload.xchainaddrpayload.md#returntype)
* [toBuffer](common_payload.xchainaddrpayload.md#tobuffer)
* [typeID](common_payload.xchainaddrpayload.md#typeid)
* [typeName](common_payload.xchainaddrpayload.md#typename)

## Constructors

###  constructor

\+ **new XCHAINADDRPayload**(`payload`: any): *[XCHAINADDRPayload](common_payload.xchainaddrpayload.md)*

*Inherited from [ChainAddressPayload](common_payload.chainaddresspayload.md).[constructor](common_payload.chainaddresspayload.md#constructor)*

*Overrides [PayloadBase](common_payload.payloadbase.md).[constructor](common_payload.payloadbase.md#constructor)*

Defined in src/utils/payload.ts:411

**Parameters:**

Name | Type | Default | Description |
------ | ------ | ------ | ------ |
`payload` | any | undefined | Buffer or address string  |

**Returns:** *[XCHAINADDRPayload](common_payload.xchainaddrpayload.md)*

## Properties

### `Protected` chainid

• **chainid**: *string* = "X"

*Overrides [ChainAddressPayload](common_payload.chainaddresspayload.md).[chainid](common_payload.chainaddresspayload.md#protected-chainid)*

Defined in src/utils/payload.ts:430

___

### `Protected` payload

• **payload**: *Buffer* = Buffer.alloc(0)

*Inherited from [PayloadBase](common_payload.payloadbase.md).[payload](common_payload.payloadbase.md#protected-payload)*

Defined in src/utils/payload.ts:166

___

### `Protected` typeid

• **typeid**: *number* = 6

*Overrides [ChainAddressPayload](common_payload.chainaddresspayload.md).[typeid](common_payload.chainaddresspayload.md#protected-typeid)*

Defined in src/utils/payload.ts:429

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
