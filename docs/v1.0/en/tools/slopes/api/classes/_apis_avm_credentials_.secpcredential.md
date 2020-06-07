[slopes - v1.7.3](../README.md) › ["apis/avm/credentials"](../modules/_apis_avm_credentials_.md) › [SecpCredential](_apis_avm_credentials_.secpcredential.md)

# Class: SecpCredential

## Hierarchy

* [Credential](_apis_avm_credentials_.credential.md)

  ↳ **SecpCredential**

## Index

### Constructors

* [constructor](_apis_avm_credentials_.secpcredential.md#constructor)

### Properties

* [sigArray](_apis_avm_credentials_.secpcredential.md#protected-sigarray)

### Methods

* [addSignature](_apis_avm_credentials_.secpcredential.md#addsignature)
* [fromBuffer](_apis_avm_credentials_.secpcredential.md#frombuffer)
* [getCredentialID](_apis_avm_credentials_.secpcredential.md#getcredentialid)
* [toBuffer](_apis_avm_credentials_.secpcredential.md#tobuffer)

## Constructors

###  constructor

\+ **new SecpCredential**(`sigarray`: Array‹[Signature](_apis_avm_types_.signature.md)›): *[SecpCredential](_apis_avm_credentials_.secpcredential.md)*

*Inherited from [Credential](_apis_avm_credentials_.credential.md).[constructor](_apis_avm_credentials_.credential.md#constructor)*

*Defined in [apis/avm/credentials.ts:70](https://github.com/ava-labs/slopes/blob/51a37ef/src/apis/avm/credentials.ts#L70)*

**Parameters:**

Name | Type | Default |
------ | ------ | ------ |
`sigarray` | Array‹[Signature](_apis_avm_types_.signature.md)› |  undefined |

**Returns:** *[SecpCredential](_apis_avm_credentials_.secpcredential.md)*

## Properties

### `Protected` sigArray

• **sigArray**: *Array‹[Signature](_apis_avm_types_.signature.md)›* =  []

*Inherited from [Credential](_apis_avm_credentials_.credential.md).[sigArray](_apis_avm_credentials_.credential.md#protected-sigarray)*

*Defined in [apis/avm/credentials.ts:35](https://github.com/ava-labs/slopes/blob/51a37ef/src/apis/avm/credentials.ts#L35)*

## Methods

###  addSignature

▸ **addSignature**(`sig`: [Signature](_apis_avm_types_.signature.md)): *number*

*Inherited from [Credential](_apis_avm_credentials_.credential.md)*

*Defined in [apis/avm/credentials.ts:42](https://github.com/ava-labs/slopes/blob/51a37ef/src/apis/avm/credentials.ts#L42)*

Adds a signature to the credentials and returns the index off the added signature.

**Parameters:**

Name | Type |
------ | ------ |
`sig` | [Signature](_apis_avm_types_.signature.md) |

**Returns:** *number*

___

###  fromBuffer

▸ **fromBuffer**(`bytes`: any, `offset`: number): *number*

*Inherited from [Credential](_apis_avm_credentials_.credential.md).[fromBuffer](_apis_avm_credentials_.credential.md#frombuffer)*

*Defined in [apis/avm/credentials.ts:47](https://github.com/ava-labs/slopes/blob/51a37ef/src/apis/avm/credentials.ts#L47)*

**Parameters:**

Name | Type | Default |
------ | ------ | ------ |
`bytes` | any | - |
`offset` | number | 0 |

**Returns:** *number*

___

###  getCredentialID

▸ **getCredentialID**(): *number*

*Overrides [Credential](_apis_avm_credentials_.credential.md).[getCredentialID](_apis_avm_credentials_.credential.md#abstract-getcredentialid)*

*Defined in [apis/avm/credentials.ts:82](https://github.com/ava-labs/slopes/blob/51a37ef/src/apis/avm/credentials.ts#L82)*

**Returns:** *number*

___

###  toBuffer

▸ **toBuffer**(): *Buffer*

*Inherited from [Credential](_apis_avm_credentials_.credential.md).[toBuffer](_apis_avm_credentials_.credential.md#tobuffer)*

*Defined in [apis/avm/credentials.ts:59](https://github.com/ava-labs/slopes/blob/51a37ef/src/apis/avm/credentials.ts#L59)*

**Returns:** *Buffer*
