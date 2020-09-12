[avalanche](../README.md) › [Common-Inputs](../modules/common_inputs.md) › [Input](common_inputs.input.md)

# Class: Input

## Hierarchy

* **Input**

  ↳ [StandardAmountInput](common_inputs.standardamountinput.md)

## Index

### Constructors

* [constructor](common_inputs.input.md#constructor)

### Properties

* [sigCount](common_inputs.input.md#protected-sigcount)
* [sigIdxs](common_inputs.input.md#protected-sigidxs)

### Methods

* [addSignatureIdx](common_inputs.input.md#addsignatureidx)
* [clone](common_inputs.input.md#abstract-clone)
* [create](common_inputs.input.md#abstract-create)
* [fromBuffer](common_inputs.input.md#frombuffer)
* [getCredentialID](common_inputs.input.md#abstract-getcredentialid)
* [getInputID](common_inputs.input.md#abstract-getinputid)
* [getSigIdxs](common_inputs.input.md#getsigidxs)
* [select](common_inputs.input.md#abstract-select)
* [toBuffer](common_inputs.input.md#tobuffer)
* [toString](common_inputs.input.md#tostring)
* [comparator](common_inputs.input.md#static-comparator)

## Constructors

###  constructor

\+ **new Input**(): *[Input](common_inputs.input.md)*

*Defined in [src/common/input.ts:98](https://github.com/ava-labs/avalanchejs/blob/a2feb77/src/common/input.ts#L98)*

**Returns:** *[Input](common_inputs.input.md)*

## Properties

### `Protected` sigCount

• **sigCount**: *Buffer* = Buffer.alloc(4)

*Defined in [src/common/input.ts:17](https://github.com/ava-labs/avalanchejs/blob/a2feb77/src/common/input.ts#L17)*

___

### `Protected` sigIdxs

• **sigIdxs**: *Array‹[SigIdx](common_signature.sigidx.md)›* = []

*Defined in [src/common/input.ts:19](https://github.com/ava-labs/avalanchejs/blob/a2feb77/src/common/input.ts#L19)*

## Methods

###  addSignatureIdx

▸ **addSignatureIdx**(`addressIdx`: number, `address`: Buffer): *void*

*Defined in [src/common/input.ts:36](https://github.com/ava-labs/avalanchejs/blob/a2feb77/src/common/input.ts#L36)*

Creates and adds a [SigIdx](common_signature.sigidx.md) to the [Input](common_inputs.input.md).

**Parameters:**

Name | Type | Description |
------ | ------ | ------ |
`addressIdx` | number | The index of the address to reference in the signatures |
`address` | Buffer | The address of the source of the signature  |

**Returns:** *void*

___

### `Abstract` clone

▸ **clone**(): *this*

*Defined in [src/common/input.ts:94](https://github.com/ava-labs/avalanchejs/blob/a2feb77/src/common/input.ts#L94)*

**Returns:** *this*

___

### `Abstract` create

▸ **create**(...`args`: any[]): *this*

*Defined in [src/common/input.ts:96](https://github.com/ava-labs/avalanchejs/blob/a2feb77/src/common/input.ts#L96)*

**Parameters:**

Name | Type |
------ | ------ |
`...args` | any[] |

**Returns:** *this*

___

###  fromBuffer

▸ **fromBuffer**(`bytes`: Buffer, `offset`: number): *number*

*Defined in [src/common/input.ts:46](https://github.com/ava-labs/avalanchejs/blob/a2feb77/src/common/input.ts#L46)*

**Parameters:**

Name | Type | Default |
------ | ------ | ------ |
`bytes` | Buffer | - |
`offset` | number | 0 |

**Returns:** *number*

___

### `Abstract` getCredentialID

▸ **getCredentialID**(): *number*

*Defined in [src/common/input.ts:28](https://github.com/ava-labs/avalanchejs/blob/a2feb77/src/common/input.ts#L28)*

**Returns:** *number*

___

### `Abstract` getInputID

▸ **getInputID**(): *number*

*Defined in [src/common/input.ts:21](https://github.com/ava-labs/avalanchejs/blob/a2feb77/src/common/input.ts#L21)*

**Returns:** *number*

___

###  getSigIdxs

▸ **getSigIdxs**(): *Array‹[SigIdx](common_signature.sigidx.md)›*

*Defined in [src/common/input.ts:26](https://github.com/ava-labs/avalanchejs/blob/a2feb77/src/common/input.ts#L26)*

Returns the array of [SigIdx](common_signature.sigidx.md) for this [Input](common_inputs.input.md)

**Returns:** *Array‹[SigIdx](common_signature.sigidx.md)›*

___

### `Abstract` select

▸ **select**(`id`: number, ...`args`: any[]): *[Input](common_inputs.input.md)*

*Defined in [src/common/input.ts:98](https://github.com/ava-labs/avalanchejs/blob/a2feb77/src/common/input.ts#L98)*

**Parameters:**

Name | Type |
------ | ------ |
`id` | number |
`...args` | any[] |

**Returns:** *[Input](common_inputs.input.md)*

___

###  toBuffer

▸ **toBuffer**(): *Buffer*

*Defined in [src/common/input.ts:61](https://github.com/ava-labs/avalanchejs/blob/a2feb77/src/common/input.ts#L61)*

**Returns:** *Buffer*

___

###  toString

▸ **toString**(): *string*

*Defined in [src/common/input.ts:76](https://github.com/ava-labs/avalanchejs/blob/a2feb77/src/common/input.ts#L76)*

Returns a base-58 representation of the [Input](common_inputs.input.md).

**Returns:** *string*

___

### `Static` comparator

▸ **comparator**(): *function*

*Defined in [src/common/input.ts:80](https://github.com/ava-labs/avalanchejs/blob/a2feb77/src/common/input.ts#L80)*

**Returns:** *function*

▸ (`a`: [Input](common_inputs.input.md), `b`: [Input](common_inputs.input.md)): *0 | 1 | -1*

**Parameters:**

Name | Type |
------ | ------ |
`a` | [Input](common_inputs.input.md) |
`b` | [Input](common_inputs.input.md) |
