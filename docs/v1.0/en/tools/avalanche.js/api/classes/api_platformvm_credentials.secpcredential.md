[avalanche](../README.md) › [API-PlatformVM-Credentials](../modules/api_platformvm_credentials.md) › [SecpCredential](api_platformvm_credentials.secpcredential.md)

# Class: SecpCredential

## Hierarchy

* [Credential](common_signature.credential.md)

  ↳ **SecpCredential**

## Index

### Constructors

* [constructor](api_platformvm_credentials.secpcredential.md#constructor)

### Properties

* [sigArray](api_platformvm_credentials.secpcredential.md#protected-sigarray)

### Methods

* [addSignature](api_platformvm_credentials.secpcredential.md#addsignature)
* [fromBuffer](api_platformvm_credentials.secpcredential.md#frombuffer)
* [getCredentialID](api_platformvm_credentials.secpcredential.md#getcredentialid)
* [toBuffer](api_platformvm_credentials.secpcredential.md#tobuffer)

## Constructors

###  constructor

\+ **new SecpCredential**(`sigarray`: Array‹[Signature](common_signature.signature.md)›): *[SecpCredential](api_platformvm_credentials.secpcredential.md)*

*Inherited from [Credential](common_signature.credential.md).[constructor](common_signature.credential.md#constructor)*

Defined in src/common/credentials.ts:93

**Parameters:**

Name | Type | Default |
------ | ------ | ------ |
`sigarray` | Array‹[Signature](common_signature.signature.md)› | undefined |

**Returns:** *[SecpCredential](api_platformvm_credentials.secpcredential.md)*

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

Defined in src/apis/platformvm/credentials.ts:33

**Returns:** *number*

___

###  toBuffer

▸ **toBuffer**(): *Buffer*

*Inherited from [Credential](common_signature.credential.md).[toBuffer](common_signature.credential.md#tobuffer)*

Defined in src/common/credentials.ts:82

**Returns:** *Buffer*
