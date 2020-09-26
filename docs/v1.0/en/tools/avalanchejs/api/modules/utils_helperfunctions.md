[avalanche](../README.md) › [Utils-HelperFunctions](utils_helperfunctions.md)

# Module: Utils-HelperFunctions

## Index

### Functions

* [NodeIDStringToBuffer](utils_helperfunctions.md#nodeidstringtobuffer)
* [UnixNow](utils_helperfunctions.md#unixnow)
* [bufferToNodeIDString](utils_helperfunctions.md#buffertonodeidstring)
* [bufferToPrivateKeyString](utils_helperfunctions.md#buffertoprivatekeystring)
* [getPreferredHRP](utils_helperfunctions.md#getpreferredhrp)
* [privateKeyStringToBuffer](utils_helperfunctions.md#privatekeystringtobuffer)

## Functions

###  NodeIDStringToBuffer

▸ **NodeIDStringToBuffer**(`pk`: string): *Buffer*

*Defined in [src/utils/helperfunctions.ts:68](https://github.com/ava-labs/avalanchejs/blob/a2feb77/src/utils/helperfunctions.ts#L68)*

Takes a nodeID string and produces a nodeID [Buffer](https://github.com/feross/buffer).

**Parameters:**

Name | Type | Description |
------ | ------ | ------ |
`pk` | string | A string for the nodeID.  |

**Returns:** *Buffer*

___

###  UnixNow

▸ **UnixNow**(): *BN*

*Defined in [src/utils/helperfunctions.ts:28](https://github.com/ava-labs/avalanchejs/blob/a2feb77/src/utils/helperfunctions.ts#L28)*

Function providing the current UNIX time using a [BN](https://github.com/indutny/bn.js/).

**Returns:** *BN*

___

###  bufferToNodeIDString

▸ **bufferToNodeIDString**(`pk`: Buffer): *string*

*Defined in [src/utils/helperfunctions.ts:59](https://github.com/ava-labs/avalanchejs/blob/a2feb77/src/utils/helperfunctions.ts#L59)*

Takes a nodeID buffer and produces a nodeID string with prefix.

**Parameters:**

Name | Type | Description |
------ | ------ | ------ |
`pk` | Buffer | A [Buffer](https://github.com/feross/buffer) for the nodeID.  |

**Returns:** *string*

___

###  bufferToPrivateKeyString

▸ **bufferToPrivateKeyString**(`pk`: Buffer): *string*

*Defined in [src/utils/helperfunctions.ts:37](https://github.com/ava-labs/avalanchejs/blob/a2feb77/src/utils/helperfunctions.ts#L37)*

Takes a private key buffer and produces a private key string with prefix.

**Parameters:**

Name | Type | Description |
------ | ------ | ------ |
`pk` | Buffer | A [Buffer](https://github.com/feross/buffer) for the private key.  |

**Returns:** *string*

___

###  getPreferredHRP

▸ **getPreferredHRP**(`networkID`: number): *any*

*Defined in [src/utils/helperfunctions.ts:16](https://github.com/ava-labs/avalanchejs/blob/a2feb77/src/utils/helperfunctions.ts#L16)*

**Parameters:**

Name | Type | Default |
------ | ------ | ------ |
`networkID` | number | undefined |

**Returns:** *any*

___

###  privateKeyStringToBuffer

▸ **privateKeyStringToBuffer**(`pk`: string): *Buffer*

*Defined in [src/utils/helperfunctions.ts:46](https://github.com/ava-labs/avalanchejs/blob/a2feb77/src/utils/helperfunctions.ts#L46)*

Takes a private key string and produces a private key [Buffer](https://github.com/feross/buffer).

**Parameters:**

Name | Type | Description |
------ | ------ | ------ |
`pk` | string | A string for the private key.  |

**Returns:** *Buffer*
