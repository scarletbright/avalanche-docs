[avalanche](../README.md) › [Utils-BinTools](../modules/utils_bintools.md) › [BinTools](utils_bintools.bintools.md)

# Class: BinTools

A class containing tools useful in interacting with binary data cross-platform using
nodejs & javascript.

This class should never be instantiated directly. Instead,
invoke the "BinTools.getInstance()" static * function to grab the singleton
instance of the tools.

Everything in this library uses
the [feross's Buffer class](https://github.com/feross/buffer).

```js
const bintools = BinTools.getInstance();
let b58str = bintools.bufferToB58(Buffer.from("Wubalubadubdub!"));
```

## Hierarchy

* **BinTools**

## Index

### Constructors

* [constructor](utils_bintools.bintools.md#private-constructor)

### Properties

* [b58](utils_bintools.bintools.md#private-b58)
* [instance](utils_bintools.bintools.md#static-private-instance)

### Methods

* [addChecksum](utils_bintools.bintools.md#addchecksum)
* [addressToString](utils_bintools.bintools.md#addresstostring)
* [avaDeserialize](utils_bintools.bintools.md#avadeserialize)
* [avaSerialize](utils_bintools.bintools.md#avaserialize)
* [b58ToBuffer](utils_bintools.bintools.md#b58tobuffer)
* [bufferToB58](utils_bintools.bintools.md#buffertob58)
* [bufferToString](utils_bintools.bintools.md#buffertostring)
* [copyFrom](utils_bintools.bintools.md#copyfrom)
* [fromArrayBufferToBuffer](utils_bintools.bintools.md#fromarraybuffertobuffer)
* [fromBNToBuffer](utils_bintools.bintools.md#frombntobuffer)
* [fromBufferToArrayBuffer](utils_bintools.bintools.md#frombuffertoarraybuffer)
* [fromBufferToBN](utils_bintools.bintools.md#frombuffertobn)
* [parseAddress](utils_bintools.bintools.md#parseaddress)
* [stringToAddress](utils_bintools.bintools.md#stringtoaddress)
* [stringToBuffer](utils_bintools.bintools.md#stringtobuffer)
* [validateChecksum](utils_bintools.bintools.md#validatechecksum)
* [getInstance](utils_bintools.bintools.md#static-getinstance)

## Constructors

### `Private` constructor

\+ **new BinTools**(): *[BinTools](utils_bintools.bintools.md)*

*Defined in [src/utils/bintools.ts:145](https://github.com/ava-labs/avalanche.js/blob/eabcc2f/src/utils/bintools.ts#L145)*

**Returns:** *[BinTools](utils_bintools.bintools.md)*

## Properties

### `Private` b58

• **b58**: *[Base58](utils_bintools.base58.md)*

*Defined in [src/utils/bintools.ts:151](https://github.com/ava-labs/avalanche.js/blob/eabcc2f/src/utils/bintools.ts#L151)*

___

### `Static` `Private` instance

▪ **instance**: *[BinTools](utils_bintools.bintools.md)*

*Defined in [src/utils/bintools.ts:145](https://github.com/ava-labs/avalanche.js/blob/eabcc2f/src/utils/bintools.ts#L145)*

## Methods

###  addChecksum

▸ **addChecksum**(`buff`: Buffer): *Buffer*

*Defined in [src/utils/bintools.ts:277](https://github.com/ava-labs/avalanche.js/blob/eabcc2f/src/utils/bintools.ts#L277)*

Takes a [Buffer](https://github.com/feross/buffer) and adds a checksum, returning
a [Buffer](https://github.com/feross/buffer) with the 4-byte checksum appended.

**Parameters:**

Name | Type | Description |
------ | ------ | ------ |
`buff` | Buffer | The [Buffer](https://github.com/feross/buffer) to append a checksum  |

**Returns:** *Buffer*

___

###  addressToString

▸ **addressToString**(`chainid`: string, `bytes`: Buffer): *string*

*Defined in [src/utils/bintools.ts:324](https://github.com/ava-labs/avalanche.js/blob/eabcc2f/src/utils/bintools.ts#L324)*

**Parameters:**

Name | Type |
------ | ------ |
`chainid` | string |
`bytes` | Buffer |

**Returns:** *string*

___

###  avaDeserialize

▸ **avaDeserialize**(`bytes`: Buffer | string): *Buffer*

*Defined in [src/utils/bintools.ts:314](https://github.com/ava-labs/avalanche.js/blob/eabcc2f/src/utils/bintools.ts#L314)*

Takes an AVA serialized [Buffer](https://github.com/feross/buffer) or base-58 string
and returns a [Buffer](https://github.com/feross/buffer) of the original data. Throws on error.

**Parameters:**

Name | Type | Description |
------ | ------ | ------ |
`bytes` | Buffer &#124; string | An AVA serialized [Buffer](https://github.com/feross/buffer) or base-58 string  |

**Returns:** *Buffer*

___

###  avaSerialize

▸ **avaSerialize**(`bytes`: Buffer): *string*

*Defined in [src/utils/bintools.ts:303](https://github.com/ava-labs/avalanche.js/blob/eabcc2f/src/utils/bintools.ts#L303)*

Takes a [Buffer](https://github.com/feross/buffer) and returns a base-58 string with
checksum as per the AVA standard.

**Parameters:**

Name | Type | Description |
------ | ------ | ------ |
`bytes` | Buffer | A [Buffer](https://github.com/feross/buffer) to serialize  |

**Returns:** *string*

A serialized base-58 strig of the Buffer.

___

###  b58ToBuffer

▸ **b58ToBuffer**(`b58str`: string): *Buffer*

*Defined in [src/utils/bintools.ts:213](https://github.com/ava-labs/avalanche.js/blob/eabcc2f/src/utils/bintools.ts#L213)*

Takes a base-58 string and returns a [Buffer](https://github.com/feross/buffer).

**Parameters:**

Name | Type | Description |
------ | ------ | ------ |
`b58str` | string | The base-58 string to convert to a [Buffer](https://github.com/feross/buffer)  |

**Returns:** *Buffer*

___

###  bufferToB58

▸ **bufferToB58**(`buff`: Buffer): *string*

*Defined in [src/utils/bintools.ts:205](https://github.com/ava-labs/avalanche.js/blob/eabcc2f/src/utils/bintools.ts#L205)*

Takes a [Buffer](https://github.com/feross/buffer) and returns a base-58 string of
the [Buffer](https://github.com/feross/buffer).

**Parameters:**

Name | Type | Description |
------ | ------ | ------ |
`buff` | Buffer | The [Buffer](https://github.com/feross/buffer) to convert to base-58  |

**Returns:** *string*

___

###  bufferToString

▸ **bufferToString**(`buff`: Buffer): *string*

*Defined in [src/utils/bintools.ts:169](https://github.com/ava-labs/avalanche.js/blob/eabcc2f/src/utils/bintools.ts#L169)*

Produces a string from a [Buffer](https://github.com/feross/buffer)
representing a string.

**Parameters:**

Name | Type | Description |
------ | ------ | ------ |
`buff` | Buffer | The [Buffer](https://github.com/feross/buffer) to convert to a string  |

**Returns:** *string*

___

###  copyFrom

▸ **copyFrom**(`buff`: Buffer, `start`: number, `end`: number): *Buffer*

*Defined in [src/utils/bintools.ts:191](https://github.com/ava-labs/avalanche.js/blob/eabcc2f/src/utils/bintools.ts#L191)*

Makes a copy (no reference) of a [Buffer](https://github.com/feross/buffer)
over provided indecies.

**Parameters:**

Name | Type | Default | Description |
------ | ------ | ------ | ------ |
`buff` | Buffer | - | The [Buffer](https://github.com/feross/buffer) to copy |
`start` | number | 0 | The index to start the copy |
`end` | number | undefined | The index to end the copy  |

**Returns:** *Buffer*

___

###  fromArrayBufferToBuffer

▸ **fromArrayBufferToBuffer**(`ab`: ArrayBuffer): *Buffer*

*Defined in [src/utils/bintools.ts:235](https://github.com/ava-labs/avalanche.js/blob/eabcc2f/src/utils/bintools.ts#L235)*

Takes an ArrayBuffer and converts it to a [Buffer](https://github.com/feross/buffer).

**Parameters:**

Name | Type | Description |
------ | ------ | ------ |
`ab` | ArrayBuffer | The ArrayBuffer to convert to a [Buffer](https://github.com/feross/buffer)  |

**Returns:** *Buffer*

___

###  fromBNToBuffer

▸ **fromBNToBuffer**(`bn`: BN, `length?`: number): *Buffer*

*Defined in [src/utils/bintools.ts:260](https://github.com/ava-labs/avalanche.js/blob/eabcc2f/src/utils/bintools.ts#L260)*

Takes a [BN](https://github.com/indutny/bn.js/) and converts it
to a [Buffer](https://github.com/feross/buffer).

**Parameters:**

Name | Type | Description |
------ | ------ | ------ |
`bn` | BN | The [BN](https://github.com/indutny/bn.js/) to convert to a [Buffer](https://github.com/feross/buffer) |
`length?` | number | The zero-padded length of the [Buffer](https://github.com/feross/buffer)  |

**Returns:** *Buffer*

___

###  fromBufferToArrayBuffer

▸ **fromBufferToArrayBuffer**(`buff`: Buffer): *ArrayBuffer*

*Defined in [src/utils/bintools.ts:221](https://github.com/ava-labs/avalanche.js/blob/eabcc2f/src/utils/bintools.ts#L221)*

Takes a [Buffer](https://github.com/feross/buffer) and returns an ArrayBuffer.

**Parameters:**

Name | Type | Description |
------ | ------ | ------ |
`buff` | Buffer | The [Buffer](https://github.com/feross/buffer) to convert to an ArrayBuffer  |

**Returns:** *ArrayBuffer*

___

###  fromBufferToBN

▸ **fromBufferToBN**(`buff`: Buffer): *BN*

*Defined in [src/utils/bintools.ts:250](https://github.com/ava-labs/avalanche.js/blob/eabcc2f/src/utils/bintools.ts#L250)*

Takes a [Buffer](https://github.com/feross/buffer) and converts it
to a [BN](https://github.com/indutny/bn.js/).

**Parameters:**

Name | Type | Description |
------ | ------ | ------ |
`buff` | Buffer | The [Buffer](https://github.com/feross/buffer) to convert to a [BN](https://github.com/indutny/bn.js/)  |

**Returns:** *BN*

___

###  parseAddress

▸ **parseAddress**(`addr`: string, `blockchainID`: string, `alias`: string, `addrlen`: number): *Buffer*

*Defined in [src/utils/bintools.ts:339](https://github.com/ava-labs/avalanche.js/blob/eabcc2f/src/utils/bintools.ts#L339)*

Takes an address and returns its [Buffer](https://github.com/feross/buffer)
representation if valid.

**Parameters:**

Name | Type | Default |
------ | ------ | ------ |
`addr` | string | - |
`blockchainID` | string | - |
`alias` | string | undefined |
`addrlen` | number | 20 |

**Returns:** *Buffer*

A [Buffer](https://github.com/feross/buffer) for the address if valid,
undefined if not valid.

___

###  stringToAddress

▸ **stringToAddress**(`address`: string): *Buffer*

*Defined in [src/utils/bintools.ts:327](https://github.com/ava-labs/avalanche.js/blob/eabcc2f/src/utils/bintools.ts#L327)*

**Parameters:**

Name | Type |
------ | ------ |
`address` | string |

**Returns:** *Buffer*

___

###  stringToBuffer

▸ **stringToBuffer**(`str`: string): *Buffer*

*Defined in [src/utils/bintools.ts:176](https://github.com/ava-labs/avalanche.js/blob/eabcc2f/src/utils/bintools.ts#L176)*

Produces a [Buffer](https://github.com/feross/buffer) from a string.

**Parameters:**

Name | Type | Description |
------ | ------ | ------ |
`str` | string | The string to convert to a [Buffer](https://github.com/feross/buffer)  |

**Returns:** *Buffer*

___

###  validateChecksum

▸ **validateChecksum**(`buff`: Buffer): *boolean*

*Defined in [src/utils/bintools.ts:288](https://github.com/ava-labs/avalanche.js/blob/eabcc2f/src/utils/bintools.ts#L288)*

Takes a [Buffer](https://github.com/feross/buffer) with an appended 4-byte checksum
and returns true if the checksum is valid, otherwise false.

**Parameters:**

Name | Type |
------ | ------ |
`buff` | Buffer |

**Returns:** *boolean*

___

### `Static` getInstance

▸ **getInstance**(): *[BinTools](utils_bintools.bintools.md)*

*Defined in [src/utils/bintools.ts:156](https://github.com/ava-labs/avalanche.js/blob/eabcc2f/src/utils/bintools.ts#L156)*

Retrieves the BinTools singleton.

**Returns:** *[BinTools](utils_bintools.bintools.md)*
