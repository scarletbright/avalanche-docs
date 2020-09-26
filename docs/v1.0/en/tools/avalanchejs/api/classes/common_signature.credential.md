[avalanche](../README.md) › [Common-Signature](../modules/common_signature.md) › [Credential](common_signature.credential.md)

# Class: Credential

## Hierarchy

* **Credential**

  ↳ [SECPCredential](api_avm_credentials.secpcredential.md)

  ↳ [NFTCredential](api_avm_credentials.nftcredential.md)

  ↳ [SECPCredential](api_platformvm_credentials.secpcredential.md)

## Index

### Constructors

* [constructor](common_signature.credential.md#constructor)

### Properties

* [sigArray](common_signature.credential.md#protected-sigarray)

### Methods

* [addSignature](common_signature.credential.md#addsignature)
* [clone](common_signature.credential.md#abstract-clone)
* [create](common_signature.credential.md#abstract-create)
* [fromBuffer](common_signature.credential.md#frombuffer)
* [getCredentialID](common_signature.credential.md#abstract-getcredentialid)
* [select](common_signature.credential.md#abstract-select)
* [toBuffer](common_signature.credential.md#tobuffer)

## Constructors

###  constructor

\+ **new Credential**(`sigarray`: Array‹[Signature](common_signature.signature.md)›): *[Credential](common_signature.credential.md)*

*Defined in [src/common/credentials.ts:121](https://github.com/ava-labs/avalanchejs/blob/a2feb77/src/common/credentials.ts#L121)*

**Parameters:**

Name | Type | Default |
------ | ------ | ------ |
`sigarray` | Array‹[Signature](common_signature.signature.md)› | undefined |

**Returns:** *[Credential](common_signature.credential.md)*

## Properties

### `Protected` sigArray

• **sigArray**: *Array‹[Signature](common_signature.signature.md)›* = []

*Defined in [src/common/credentials.ts:80](https://github.com/ava-labs/avalanchejs/blob/a2feb77/src/common/credentials.ts#L80)*

## Methods

###  addSignature

▸ **addSignature**(`sig`: [Signature](common_signature.signature.md)): *number*

*Defined in [src/common/credentials.ts:87](https://github.com/ava-labs/avalanchejs/blob/a2feb77/src/common/credentials.ts#L87)*

Adds a signature to the credentials and returns the index off the added signature.

**Parameters:**

Name | Type |
------ | ------ |
`sig` | [Signature](common_signature.signature.md) |

**Returns:** *number*

___

### `Abstract` clone

▸ **clone**(): *this*

*Defined in [src/common/credentials.ts:117](https://github.com/ava-labs/avalanchejs/blob/a2feb77/src/common/credentials.ts#L117)*

**Returns:** *this*

___

### `Abstract` create

▸ **create**(...`args`: any[]): *this*

*Defined in [src/common/credentials.ts:119](https://github.com/ava-labs/avalanchejs/blob/a2feb77/src/common/credentials.ts#L119)*

**Parameters:**

Name | Type |
------ | ------ |
`...args` | any[] |

**Returns:** *this*

___

###  fromBuffer

▸ **fromBuffer**(`bytes`: any, `offset`: number): *number*

*Defined in [src/common/credentials.ts:92](https://github.com/ava-labs/avalanchejs/blob/a2feb77/src/common/credentials.ts#L92)*

**Parameters:**

Name | Type | Default |
------ | ------ | ------ |
`bytes` | any | - |
`offset` | number | 0 |

**Returns:** *number*

___

### `Abstract` getCredentialID

▸ **getCredentialID**(): *number*

*Defined in [src/common/credentials.ts:82](https://github.com/ava-labs/avalanchejs/blob/a2feb77/src/common/credentials.ts#L82)*

**Returns:** *number*

___

### `Abstract` select

▸ **select**(`id`: number, ...`args`: any[]): *[Credential](common_signature.credential.md)*

*Defined in [src/common/credentials.ts:121](https://github.com/ava-labs/avalanchejs/blob/a2feb77/src/common/credentials.ts#L121)*

**Parameters:**

Name | Type |
------ | ------ |
`id` | number |
`...args` | any[] |

**Returns:** *[Credential](common_signature.credential.md)*

___

###  toBuffer

▸ **toBuffer**(): *Buffer*

*Defined in [src/common/credentials.ts:104](https://github.com/ava-labs/avalanchejs/blob/a2feb77/src/common/credentials.ts#L104)*

**Returns:** *Buffer*
