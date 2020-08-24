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
* [fromBuffer](api_avm_credentials.nftcredential.md#frombuffer)
* [getCredentialID](api_avm_credentials.nftcredential.md#getcredentialid)
* [toBuffer](api_avm_credentials.nftcredential.md#tobuffer)

## Constructors

###  constructor

\+ **new NFTCredential**(`sigarray`: Array‹[Signature](common_signature.signature.md)›): *[NFTCredential](api_avm_credentials.nftcredential.md)*

*Inherited from [Credential](common_signature.credential.md).[constructor](common_signature.credential.md#constructor)*

Defined in src/common/credentials.ts:93

**Parameters:**

Name | Type | Default |
------ | ------ | ------ |
`sigarray` | Array‹[Signature](common_signature.signature.md)› | undefined |

**Returns:** *[NFTCredential](api_avm_credentials.nftcredential.md)*

## Properties

### `Protected` sigArray

• **sigArray**: *Array‹[Signature](common_signature.signature.md)›* = []

*Inherited from [Credential](common_signature.credential.md).[sigArray](common_signature.credential.md#protected-sigarray)*

Defined in src/common/credentials.ts:58

## Methods

###  addSignature

▸ **addSignature**(`sig`: [Signature](common_signature.signature.md)): *number*

*Inherited from [Credential](common_signature.credential.md).[addSignature](common_signature.credential.md#addsignature)*

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

*Inherited from [Credential](common_signature.credential.md).[fromBuffer](common_signature.credential.md#frombuffer)*

Defined in src/common/credentials.ts:70

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

Defined in src/apis/avm/credentials.ts:42

**Returns:** *number*

___

###  toBuffer

▸ **toBuffer**(): *Buffer*

*Inherited from [Credential](common_signature.credential.md).[toBuffer](common_signature.credential.md#tobuffer)*

Defined in src/common/credentials.ts:82

**Returns:** *Buffer*
