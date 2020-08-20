[avalanche](../README.md) › [Common-Signature](../modules/common_signature.md) › [Credential](common_signature.credential.md)

# Class: Credential

## Hierarchy

* **Credential**

  ↳ [SecpCredential](api_avm_credentials.secpcredential.md)

  ↳ [NFTCredential](api_avm_credentials.nftcredential.md)

  ↳ [SecpCredential](api_platformvm_credentials.secpcredential.md)

## Index

### Constructors

* [constructor](common_signature.credential.md#constructor)

### Properties

* [sigArray](common_signature.credential.md#protected-sigarray)

### Methods

* [addSignature](common_signature.credential.md#addsignature)
* [fromBuffer](common_signature.credential.md#frombuffer)
* [getCredentialID](common_signature.credential.md#abstract-getcredentialid)
* [toBuffer](common_signature.credential.md#tobuffer)

## Constructors

###  constructor

\+ **new Credential**(`sigarray`: Array‹[Signature](common_signature.signature.md)›): *[Credential](common_signature.credential.md)*

Defined in src/common/credentials.ts:93

**Parameters:**

Name | Type | Default |
------ | ------ | ------ |
`sigarray` | Array‹[Signature](common_signature.signature.md)› | undefined |

**Returns:** *[Credential](common_signature.credential.md)*

## Properties

### `Protected` sigArray

• **sigArray**: *Array‹[Signature](common_signature.signature.md)›* = []

Defined in src/common/credentials.ts:58

## Methods

###  addSignature

▸ **addSignature**(`sig`: [Signature](common_signature.signature.md)): *number*

Defined in src/common/credentials.ts:65

Adds a signature to the credentials and returns the index off the added signature.

**Parameters:**

Name | Type |
------ | ------ |
`sig` | [Signature](common_signature.signature.md) |

**Returns:** *number*

___

###  fromBuffer

▸ **fromBuffer**(`bytes`: any, `offset`: number): *number*

Defined in src/common/credentials.ts:70

**Parameters:**

Name | Type | Default |
------ | ------ | ------ |
`bytes` | any | - |
`offset` | number | 0 |

**Returns:** *number*

___

### `Abstract` getCredentialID

▸ **getCredentialID**(): *number*

Defined in src/common/credentials.ts:60

**Returns:** *number*

___

###  toBuffer

▸ **toBuffer**(): *Buffer*

Defined in src/common/credentials.ts:82

**Returns:** *Buffer*
