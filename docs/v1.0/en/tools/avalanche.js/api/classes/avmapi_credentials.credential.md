[avalanche](../README.md) › [AVMAPI-Credentials](../modules/avmapi_credentials.md) › [Credential](avmapi_credentials.credential.md)

# Class: Credential

## Hierarchy

* **Credential**

  ↳ [SecpCredential](avmapi_credentials.secpcredential.md)

  ↳ [NFTCredential](avmapi_credentials.nftcredential.md)

## Index

### Constructors

* [constructor](avmapi_credentials.credential.md#constructor)

### Properties

* [sigArray](avmapi_credentials.credential.md#protected-sigarray)

### Methods

* [addSignature](avmapi_credentials.credential.md#addsignature)
* [fromBuffer](avmapi_credentials.credential.md#frombuffer)
* [getCredentialID](avmapi_credentials.credential.md#abstract-getcredentialid)
* [toBuffer](avmapi_credentials.credential.md#tobuffer)

## Constructors

###  constructor

\+ **new Credential**(`sigarray`: Array‹[Signature](avmapi_types.signature.md)›): *[Credential](avmapi_credentials.credential.md)*

*Defined in [src/apis/avm/credentials.ts:70](https://github.com/ava-labs/avalanche.js/blob/eabcc2f/src/apis/avm/credentials.ts#L70)*

**Parameters:**

Name | Type | Default |
------ | ------ | ------ |
`sigarray` | Array‹[Signature](avmapi_types.signature.md)› | undefined |

**Returns:** *[Credential](avmapi_credentials.credential.md)*

## Properties

### `Protected` sigArray

• **sigArray**: *Array‹[Signature](avmapi_types.signature.md)›* = []

*Defined in [src/apis/avm/credentials.ts:35](https://github.com/ava-labs/avalanche.js/blob/eabcc2f/src/apis/avm/credentials.ts#L35)*

## Methods

###  addSignature

▸ **addSignature**(`sig`: [Signature](avmapi_types.signature.md)): *number*

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

*Defined in [src/apis/avm/credentials.ts:47](https://github.com/ava-labs/avalanche.js/blob/eabcc2f/src/apis/avm/credentials.ts#L47)*

**Parameters:**

Name | Type | Default |
------ | ------ | ------ |
`bytes` | any | - |
`offset` | number | 0 |

**Returns:** *number*

___

### `Abstract` getCredentialID

▸ **getCredentialID**(): *number*

*Defined in [src/apis/avm/credentials.ts:37](https://github.com/ava-labs/avalanche.js/blob/eabcc2f/src/apis/avm/credentials.ts#L37)*

**Returns:** *number*

___

###  toBuffer

▸ **toBuffer**(): *Buffer*

*Defined in [src/apis/avm/credentials.ts:59](https://github.com/ava-labs/avalanche.js/blob/eabcc2f/src/apis/avm/credentials.ts#L59)*

**Returns:** *Buffer*
