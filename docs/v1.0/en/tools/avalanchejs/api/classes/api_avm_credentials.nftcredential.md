[avalanche](../README.md) › [API-AVM-Credentials](../modules/api_avm_credentials.md) › [NFTCredential](api_avm_credentials.nftcredential.md)

# Class: NFTCredential

## Hierarchy

* [Credential](common_signature.credential.md)

  ↳ **NFTCredential**

## Index

### Constructors

* [constructor](api_avm_credentials.nftcredential.md#constructor)

### Properties

* [sigArray](api_avm_credentials.nftcredential.md#protected-sigarray)

### Methods

* [addSignature](api_avm_credentials.nftcredential.md#addsignature)
* [clone](api_avm_credentials.nftcredential.md#clone)
* [create](api_avm_credentials.nftcredential.md#create)
* [fromBuffer](api_avm_credentials.nftcredential.md#frombuffer)
* [getCredentialID](api_avm_credentials.nftcredential.md#getcredentialid)
* [select](api_avm_credentials.nftcredential.md#select)
* [toBuffer](api_avm_credentials.nftcredential.md#tobuffer)

## Constructors

###  constructor

\+ **new NFTCredential**(`sigarray`: Array‹[Signature](common_signature.signature.md)›): *[NFTCredential](api_avm_credentials.nftcredential.md)*

*Inherited from [Credential](common_signature.credential.md).[constructor](common_signature.credential.md#constructor)*

*Defined in [src/common/credentials.ts:121](https://github.com/ava-labs/avalanchejs/blob/a2feb77/src/common/credentials.ts#L121)*

**Parameters:**

Name | Type | Default |
------ | ------ | ------ |
`sigarray` | Array‹[Signature](common_signature.signature.md)› | undefined |

**Returns:** *[NFTCredential](api_avm_credentials.nftcredential.md)*

## Properties

### `Protected` sigArray

• **sigArray**: *Array‹[Signature](common_signature.signature.md)›* = []

*Inherited from [Credential](common_signature.credential.md).[sigArray](common_signature.credential.md#protected-sigarray)*

*Defined in [src/common/credentials.ts:80](https://github.com/ava-labs/avalanchejs/blob/a2feb77/src/common/credentials.ts#L80)*

## Methods

###  addSignature

▸ **addSignature**(`sig`: [Signature](common_signature.signature.md)): *number*

*Inherited from [Credential](common_signature.credential.md).[addSignature](common_signature.credential.md#addsignature)*

*Defined in [src/common/credentials.ts:87](https://github.com/ava-labs/avalanchejs/blob/a2feb77/src/common/credentials.ts#L87)*

Adds a signature to the credentials and returns the index off the added signature.

**Parameters:**

Name | Type |
------ | ------ |
`sig` | [Signature](common_signature.signature.md) |

**Returns:** *number*

___

###  clone

▸ **clone**(): *this*

*Overrides [Credential](common_signature.credential.md).[clone](common_signature.credential.md#abstract-clone)*

*Defined in [src/apis/avm/credentials.ts:62](https://github.com/ava-labs/avalanchejs/blob/a2feb77/src/apis/avm/credentials.ts#L62)*

**Returns:** *this*

___

###  create

▸ **create**(...`args`: any[]): *this*

*Overrides [Credential](common_signature.credential.md).[create](common_signature.credential.md#abstract-create)*

*Defined in [src/apis/avm/credentials.ts:68](https://github.com/ava-labs/avalanchejs/blob/a2feb77/src/apis/avm/credentials.ts#L68)*

**Parameters:**

Name | Type |
------ | ------ |
`...args` | any[] |

**Returns:** *this*

___

###  fromBuffer

▸ **fromBuffer**(`bytes`: any, `offset`: number): *number*

*Inherited from [Credential](common_signature.credential.md).[fromBuffer](common_signature.credential.md#frombuffer)*

*Defined in [src/common/credentials.ts:92](https://github.com/ava-labs/avalanchejs/blob/a2feb77/src/common/credentials.ts#L92)*

**Parameters:**

Name | Type | Default |
------ | ------ | ------ |
`bytes` | any | - |
`offset` | number | 0 |

**Returns:** *number*

___

###  getCredentialID

▸ **getCredentialID**(): *number*

*Overrides [Credential](common_signature.credential.md).[getCredentialID](common_signature.credential.md#abstract-getcredentialid)*

*Defined in [src/apis/avm/credentials.ts:58](https://github.com/ava-labs/avalanchejs/blob/a2feb77/src/apis/avm/credentials.ts#L58)*

**Returns:** *number*

___

###  select

▸ **select**(`id`: number, ...`args`: any[]): *this*

*Overrides [Credential](common_signature.credential.md).[select](common_signature.credential.md#abstract-select)*

*Defined in [src/apis/avm/credentials.ts:72](https://github.com/ava-labs/avalanchejs/blob/a2feb77/src/apis/avm/credentials.ts#L72)*

**Parameters:**

Name | Type |
------ | ------ |
`id` | number |
`...args` | any[] |

**Returns:** *this*

___

###  toBuffer

▸ **toBuffer**(): *Buffer*

*Inherited from [Credential](common_signature.credential.md).[toBuffer](common_signature.credential.md#tobuffer)*

*Defined in [src/common/credentials.ts:104](https://github.com/ava-labs/avalanchejs/blob/a2feb77/src/common/credentials.ts#L104)*

**Returns:** *Buffer*
