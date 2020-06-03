[slopes - v1.7.2](../README.md) › ["apis/avm/credentials"](../modules/_apis_avm_credentials_.md) › [Credential](_apis_avm_credentials_.credential.md)

# Class: Credential

## Hierarchy

* **Credential**

  ↳ [SecpCredential](_apis_avm_credentials_.secpcredential.md)

  ↳ [NFTCredential](_apis_avm_credentials_.nftcredential.md)

## Index

### Constructors

* [constructor](_apis_avm_credentials_.credential.md#constructor)

### Properties

* [sigArray](_apis_avm_credentials_.credential.md#protected-sigarray)

### Methods

* [addSignature](_apis_avm_credentials_.credential.md#addsignature)
* [fromBuffer](_apis_avm_credentials_.credential.md#frombuffer)
* [getCredentialID](_apis_avm_credentials_.credential.md#abstract-getcredentialid)
* [toBuffer](_apis_avm_credentials_.credential.md#tobuffer)

## Constructors

###  constructor

\+ **new Credential**(`sigarray`: Array‹[Signature](_apis_avm_types_.signature.md)›): *[Credential](_apis_avm_credentials_.credential.md)*

*Defined in [apis/avm/credentials.ts:70](https://github.com/ava-labs/slopes/blob/2d2915d/src/apis/avm/credentials.ts#L70)*

**Parameters:**

Name | Type | Default |
------ | ------ | ------ |
`sigarray` | Array‹[Signature](_apis_avm_types_.signature.md)› |  undefined |

**Returns:** *[Credential](_apis_avm_credentials_.credential.md)*

## Properties

### `Protected` sigArray

• **sigArray**: *Array‹[Signature](_apis_avm_types_.signature.md)›* =  []

*Defined in [apis/avm/credentials.ts:35](https://github.com/ava-labs/slopes/blob/2d2915d/src/apis/avm/credentials.ts#L35)*

## Methods

###  addSignature

▸ **addSignature**(`sig`: [Signature](_apis_avm_types_.signature.md)): *number*

*Defined in [apis/avm/credentials.ts:42](https://github.com/ava-labs/slopes/blob/2d2915d/src/apis/avm/credentials.ts#L42)*

Adds a signature to the credentials and returns the index off the added signature.

**Parameters:**

Name | Type |
------ | ------ |
`sig` | [Signature](_apis_avm_types_.signature.md) |

**Returns:** *number*

___

###  fromBuffer

▸ **fromBuffer**(`bytes`: any, `offset`: number): *number*

*Defined in [apis/avm/credentials.ts:47](https://github.com/ava-labs/slopes/blob/2d2915d/src/apis/avm/credentials.ts#L47)*

**Parameters:**

Name | Type | Default |
------ | ------ | ------ |
`bytes` | any | - |
`offset` | number | 0 |

**Returns:** *number*

___

### `Abstract` getCredentialID

▸ **getCredentialID**(): *number*

*Defined in [apis/avm/credentials.ts:37](https://github.com/ava-labs/slopes/blob/2d2915d/src/apis/avm/credentials.ts#L37)*

**Returns:** *number*

___

###  toBuffer

▸ **toBuffer**(): *Buffer*

*Defined in [apis/avm/credentials.ts:59](https://github.com/ava-labs/slopes/blob/2d2915d/src/apis/avm/credentials.ts#L59)*

**Returns:** *Buffer*
