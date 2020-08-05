[avalanche](../README.md) › [AVMAPI-Credentials](../modules/avmapi_credentials.md) › [NFTCredential](avmapi_credentials.nftcredential.md)

# Class: NFTCredential

## Hierarchy

* [Credential](avmapi_credentials.credential.md)

  ↳ **NFTCredential**

## Index

### Constructors

* [constructor](avmapi_credentials.nftcredential.md#constructor)

### Properties

* [sigArray](avmapi_credentials.nftcredential.md#protected-sigarray)

### Methods

* [addSignature](avmapi_credentials.nftcredential.md#addsignature)
* [fromBuffer](avmapi_credentials.nftcredential.md#frombuffer)
* [getCredentialID](avmapi_credentials.nftcredential.md#getcredentialid)
* [toBuffer](avmapi_credentials.nftcredential.md#tobuffer)

## Constructors

###  constructor

\+ **new NFTCredential**(`sigarray`: Array‹[Signature](avmapi_types.signature.md)›): *[NFTCredential](avmapi_credentials.nftcredential.md)*

*Inherited from [Credential](avmapi_credentials.credential.md).[constructor](avmapi_credentials.credential.md#constructor)*

*Defined in [src/apis/avm/credentials.ts:70](https://github.com/ava-labs/avalanche.js/blob/eabcc2f/src/apis/avm/credentials.ts#L70)*

**Parameters:**

Name | Type | Default |
------ | ------ | ------ |
`sigarray` | Array‹[Signature](avmapi_types.signature.md)› | undefined |

**Returns:** *[NFTCredential](avmapi_credentials.nftcredential.md)*

## Properties

### `Protected` sigArray

• **sigArray**: *Array‹[Signature](avmapi_types.signature.md)›* = []

*Inherited from [Credential](avmapi_credentials.credential.md).[sigArray](avmapi_credentials.credential.md#protected-sigarray)*

*Defined in [src/apis/avm/credentials.ts:35](https://github.com/ava-labs/avalanche.js/blob/eabcc2f/src/apis/avm/credentials.ts#L35)*

## Methods

###  addSignature

▸ **addSignature**(`sig`: [Signature](avmapi_types.signature.md)): *number*

*Inherited from [Credential](avmapi_credentials.credential.md).[addSignature](avmapi_credentials.credential.md#addsignature)*

*Defined in [src/apis/avm/credentials.ts:42](https://github.com/ava-labs/avalanche.js/blob/eabcc2f/src/apis/avm/credentials.ts#L42)*

Adds a signature to the credentials and returns the index off the added signature.

**Parameters:**

Name | Type |
------ | ------ |
`sig` | [Signature](avmapi_types.signature.md) |

**Returns:** *number*

___

###  fromBuffer

▸ **fromBuffer**(`bytes`: any, `offset`: number): *number*

*Inherited from [Credential](avmapi_credentials.credential.md).[fromBuffer](avmapi_credentials.credential.md#frombuffer)*

*Defined in [src/apis/avm/credentials.ts:47](https://github.com/ava-labs/avalanche.js/blob/eabcc2f/src/apis/avm/credentials.ts#L47)*

**Parameters:**

Name | Type | Default |
------ | ------ | ------ |
`bytes` | any | - |
`offset` | number | 0 |

**Returns:** *number*

___

###  getCredentialID

▸ **getCredentialID**(): *number*

*Overrides [Credential](avmapi_credentials.credential.md).[getCredentialID](avmapi_credentials.credential.md#abstract-getcredentialid)*

*Defined in [src/apis/avm/credentials.ts:87](https://github.com/ava-labs/avalanche.js/blob/eabcc2f/src/apis/avm/credentials.ts#L87)*

**Returns:** *number*

___

###  toBuffer

▸ **toBuffer**(): *Buffer*

*Inherited from [Credential](avmapi_credentials.credential.md).[toBuffer](avmapi_credentials.credential.md#tobuffer)*

*Defined in [src/apis/avm/credentials.ts:59](https://github.com/ava-labs/avalanche.js/blob/eabcc2f/src/apis/avm/credentials.ts#L59)*

**Returns:** *Buffer*
