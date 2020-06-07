[slopes - v1.7.4](../README.md) › ["utils/bintools"](../modules/_utils_bintools_.md) › [BinTools](_utils_bintools_.bintools.md)

# Class: BinTools

A class containing tools useful in interacting with binary data cross-platform using nodejs & javascript.

This class should never be instantiated directly. Instead, invoke the "BinTools.getInstance()" static
function to grab the singleton instance of the tools.

Everything in this library uses the [feross's Buffer class](https://github.com/feross/buffer).

```js
const bintools = BinTools.getInstance();
let b58str = bintools.bufferToB58(Buffer.from("Wubalubadubdub!"));
```

## Hierarchy

* **BinTools**

## Index

### Constructors

* [constructor](_utils_bintools_.bintools.md#private-constructor)

### Properties

* [b58](_utils_bintools_.bintools.md#private-b58)
* [instance](_utils_bintools_.bintools.md#static-private-instance)

### Methods

* [addChecksum](_utils_bintools_.bintools.md#addchecksum)
* [addressToString](_utils_bintools_.bintools.md#addresstostring)
* [avaDeserialize](_utils_bintools_.bintools.md#avadeserialize)
* [avaSerialize](_utils_bintools_.bintools.md#avaserialize)
* [b58ToBuffer](_utils_bintools_.bintools.md#b58tobuffer)
* [bufferToB58](_utils_bintools_.bintools.md#buffertob58)
* [bufferToString](_utils_bintools_.bintools.md#buffertostring)
* [copyFrom](_utils_bintools_.bintools.md#copyfrom)
* [fromArrayBufferToBuffer](_utils_bintools_.bintools.md#fromarraybuffertobuffer)
* [fromBNToBuffer](_utils_bintools_.bintools.md#frombntobuffer)
* [fromBufferToArrayBuffer](_utils_bintools_.bintools.md#frombuffertoarraybuffer)
* [fromBufferToBN](_utils_bintools_.bintools.md#frombuffertobn)
* [parseAddress](_utils_bintools_.bintools.md#parseaddress)
* [stringToAddress](_utils_bintools_.bintools.md#stringtoaddress)
* [stringToBuffer](_utils_bintools_.bintools.md#stringtobuffer)
* [validateChecksum](_utils_bintools_.bintools.md#validatechecksum)
* [getInstance](_utils_bintools_.bintools.md#static-getinstance)

## Constructors

### `Private` constructor

\+ **new BinTools**(): *[BinTools](_utils_bintools_.bintools.md)*

*Defined in [utils/bintools.ts:22](https://github.com/ava-labs/slopes/blob/998aaee/src/utils/bintools.ts#L22)*

**Returns:** *[BinTools](_utils_bintools_.bintools.md)*

## Properties

### `Private` b58

• **b58**: *[Base58](_utils_bintools_.base58.md)*

*Defined in [utils/bintools.ts:26](https://github.com/ava-labs/slopes/blob/998aaee/src/utils/bintools.ts#L26)*

___

### `Static` `Private` instance

▪ **instance**: *[BinTools](_utils_bintools_.bintools.md)*

*Defined in [utils/bintools.ts:22](https://github.com/ava-labs/slopes/blob/998aaee/src/utils/bintools.ts#L22)*

## Methods

###  addChecksum

▸ **addChecksum**(`buff`: Buffer): *Buffer*

*Defined in [utils/bintools.ts:151](https://github.com/ava-labs/slopes/blob/998aaee/src/utils/bintools.ts#L151)*

Takes a [Buffer](https://github.com/feross/buffer) and adds a checksum, returning a [Buffer](https://github.com/feross/buffer) with the 4-byte checksum appended.

**Parameters:**

Name | Type | Description |
------ | ------ | ------ |
`buff` | Buffer | The [Buffer](https://github.com/feross/buffer) to append a checksum  |

**Returns:** *Buffer*

___

###  addressToString

▸ **addressToString**(`chainid`: string, `bytes`: Buffer): *string*

*Defined in [utils/bintools.ts:194](https://github.com/ava-labs/slopes/blob/998aaee/src/utils/bintools.ts#L194)*

**Parameters:**

Name | Type |
------ | ------ |
`chainid` | string |
`bytes` | Buffer |

**Returns:** *string*

___

###  avaDeserialize

▸ **avaDeserialize**(`bytes`: Buffer | string): *Buffer*

*Defined in [utils/bintools.ts:184](https://github.com/ava-labs/slopes/blob/998aaee/src/utils/bintools.ts#L184)*

Takes an AVA serialized [Buffer](https://github.com/feross/buffer) or base-58 string and returns a [Buffer](https://github.com/feross/buffer) of the original data. Throws on error.

**Parameters:**

Name | Type | Description |
------ | ------ | ------ |
`bytes` | Buffer &#124; string | An AVA serialized [Buffer](https://github.com/feross/buffer) or base-58 string  |

**Returns:** *Buffer*

___

###  avaSerialize

▸ **avaSerialize**(`bytes`: Buffer): *string*

*Defined in [utils/bintools.ts:174](https://github.com/ava-labs/slopes/blob/998aaee/src/utils/bintools.ts#L174)*

Takes a [Buffer](https://github.com/feross/buffer) and returns a base-58 string with checksum as per the AVA standard.

**Parameters:**

Name | Type | Description |
------ | ------ | ------ |
`bytes` | Buffer | A [Buffer](https://github.com/feross/buffer) to serialize  |

**Returns:** *string*

A serialized base-58 strig of the Buffer.

___

###  b58ToBuffer

▸ **b58ToBuffer**(`b58str`: string): *Buffer*

*Defined in [utils/bintools.ts:89](https://github.com/ava-labs/slopes/blob/998aaee/src/utils/bintools.ts#L89)*

Takes a base-58 string and returns a [Buffer](https://github.com/feross/buffer).

**Parameters:**

Name | Type | Description |
------ | ------ | ------ |
`b58str` | string | The base-58 string to convert to a [Buffer](https://github.com/feross/buffer)  |

**Returns:** *Buffer*

___

###  bufferToB58

▸ **bufferToB58**(`buff`: Buffer): *string*

*Defined in [utils/bintools.ts:80](https://github.com/ava-labs/slopes/blob/998aaee/src/utils/bintools.ts#L80)*

Takes a [Buffer](https://github.com/feross/buffer) and returns a base-58 string of the [Buffer](https://github.com/feross/buffer).

**Parameters:**

Name | Type | Description |
------ | ------ | ------ |
`buff` | Buffer | The [Buffer](https://github.com/feross/buffer) to convert to base-58  |

**Returns:** *string*

___

###  bufferToString

▸ **bufferToString**(`buff`: Buffer): *string*

*Defined in [utils/bintools.ts:44](https://github.com/ava-labs/slopes/blob/998aaee/src/utils/bintools.ts#L44)*

Produces a string from a [Buffer](https://github.com/feross/buffer) representing a string.

**Parameters:**

Name | Type | Description |
------ | ------ | ------ |
`buff` | Buffer | The [Buffer](https://github.com/feross/buffer) to convert to a string  |

**Returns:** *string*

___

###  copyFrom

▸ **copyFrom**(`buff`: Buffer, `start`: number, `end`: number): *Buffer*

*Defined in [utils/bintools.ts:67](https://github.com/ava-labs/slopes/blob/998aaee/src/utils/bintools.ts#L67)*

Makes a copy (no reference) of a [Buffer](https://github.com/feross/buffer) over provided indecies.

**Parameters:**

Name | Type | Default | Description |
------ | ------ | ------ | ------ |
`buff` | Buffer | - | The [Buffer](https://github.com/feross/buffer) to copy |
`start` | number | 0 | The index to start the copy |
`end` | number |  undefined | The index to end the copy  |

**Returns:** *Buffer*

___

###  fromArrayBufferToBuffer

▸ **fromArrayBufferToBuffer**(`ab`: ArrayBuffer): *Buffer*

*Defined in [utils/bintools.ts:112](https://github.com/ava-labs/slopes/blob/998aaee/src/utils/bintools.ts#L112)*

Takes an ArrayBuffer and converts it to a [Buffer](https://github.com/feross/buffer).

**Parameters:**

Name | Type | Description |
------ | ------ | ------ |
`ab` | ArrayBuffer | The ArrayBuffer to convert to a [Buffer](https://github.com/feross/buffer)  |

**Returns:** *Buffer*

___

###  fromBNToBuffer

▸ **fromBNToBuffer**(`bn`: BN, `length?`: number): *Buffer*

*Defined in [utils/bintools.ts:135](https://github.com/ava-labs/slopes/blob/998aaee/src/utils/bintools.ts#L135)*

Takes a [BN](https://github.com/indutny/bn.js/) and converts it to a [Buffer](https://github.com/feross/buffer).

**Parameters:**

Name | Type | Description |
------ | ------ | ------ |
`bn` | BN | The [BN](https://github.com/indutny/bn.js/) to convert to a [Buffer](https://github.com/feross/buffer) |
`length?` | number | The zero-padded length of the [Buffer](https://github.com/feross/buffer)  |

**Returns:** *Buffer*

___

###  fromBufferToArrayBuffer

▸ **fromBufferToArrayBuffer**(`buff`: Buffer): *ArrayBuffer*

*Defined in [utils/bintools.ts:98](https://github.com/ava-labs/slopes/blob/998aaee/src/utils/bintools.ts#L98)*

Takes a [Buffer](https://github.com/feross/buffer) and returns an ArrayBuffer.

**Parameters:**

Name | Type | Description |
------ | ------ | ------ |
`buff` | Buffer | The [Buffer](https://github.com/feross/buffer) to convert to an ArrayBuffer  |

**Returns:** *ArrayBuffer*

___

###  fromBufferToBN

▸ **fromBufferToBN**(`buff`: Buffer): *BN*

*Defined in [utils/bintools.ts:125](https://github.com/ava-labs/slopes/blob/998aaee/src/utils/bintools.ts#L125)*

Takes a [Buffer](https://github.com/feross/buffer) and converts it to a [BN](https://github.com/indutny/bn.js/).

**Parameters:**

Name | Type | Description |
------ | ------ | ------ |
`buff` | Buffer | The [Buffer](https://github.com/feross/buffer) to convert to a [BN](https://github.com/indutny/bn.js/)  |

**Returns:** *BN*

___

###  parseAddress

▸ **parseAddress**(`addr`: string, `blockchainID`: string, `alias`: string, `addrlen`: number): *Buffer*

*Defined in [utils/bintools.ts:208](https://github.com/ava-labs/slopes/blob/998aaee/src/utils/bintools.ts#L208)*

Takes an address and returns its [Buffer](https://github.com/feross/buffer) representation if valid.

**Parameters:**

Name | Type | Default |
------ | ------ | ------ |
`addr` | string | - |
`blockchainID` | string | - |
`alias` | string |  undefined |
`addrlen` | number | 20 |

**Returns:** *Buffer*

A [Buffer](https://github.com/feross/buffer) for the address if valid, undefined if not valid.

___

###  stringToAddress

▸ **stringToAddress**(`address`: string): *Buffer*

*Defined in [utils/bintools.ts:198](https://github.com/ava-labs/slopes/blob/998aaee/src/utils/bintools.ts#L198)*

**Parameters:**

Name | Type |
------ | ------ |
`address` | string |

**Returns:** *Buffer*

___

###  stringToBuffer

▸ **stringToBuffer**(`str`: string): *Buffer*

*Defined in [utils/bintools.ts:53](https://github.com/ava-labs/slopes/blob/998aaee/src/utils/bintools.ts#L53)*

Produces a [Buffer](https://github.com/feross/buffer) from a string.

**Parameters:**

Name | Type | Description |
------ | ------ | ------ |
`str` | string | The string to convert to a [Buffer](https://github.com/feross/buffer)  |

**Returns:** *Buffer*

___

###  validateChecksum

▸ **validateChecksum**(`buff`: Buffer): *boolean*

*Defined in [utils/bintools.ts:161](https://github.com/ava-labs/slopes/blob/998aaee/src/utils/bintools.ts#L161)*

Takes a [Buffer](https://github.com/feross/buffer) with an appended 4-byte checksum and returns true if the checksum is valid, otherwise false.

**Parameters:**

Name | Type |
------ | ------ |
`buff` | Buffer |

**Returns:** *boolean*

___

### `Static` getInstance

▸ **getInstance**(): *[BinTools](_utils_bintools_.bintools.md)*

*Defined in [utils/bintools.ts:32](https://github.com/ava-labs/slopes/blob/998aaee/src/utils/bintools.ts#L32)*

Retrieves the BinTools singleton.

**Returns:** *[BinTools](_utils_bintools_.bintools.md)*
