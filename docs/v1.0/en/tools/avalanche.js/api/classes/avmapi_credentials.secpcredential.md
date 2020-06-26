[avalanche](../README.md) › [AVMAPI-Credentials](../modules/avmapi_credentials.md) › [SecpCredential](avmapi_credentials.secpcredential.md)

# Class: SecpCredential

## Hierarchy

* [Credential](avmapi_credentials.credential.md)

  ↳ **SecpCredential**

## Index

### Constructors

* [constructor](avmapi_credentials.secpcredential.md#constructor)

### Properties

* [sigArray](avmapi_credentials.secpcredential.md#protected-sigarray)

### Methods

* [addSignature](avmapi_credentials.secpcredential.md#addsignature)
* [fromBuffer](avmapi_credentials.secpcredential.md#frombuffer)
* [getCredentialID](avmapi_credentials.secpcredential.md#getcredentialid)
* [toBuffer](avmapi_credentials.secpcredential.md#tobuffer)

## Constructors

###  constructor

\+ **new SecpCredential**(`sigarray`: Array‹[Signature](avmapi_types.signature.md)›): *[SecpCredential](avmapi_credentials.secpcredential.md)*

*Inherited from [Credential](avmapi_credentials.credential.md).[constructor](avmapi_credentials.credential.md#constructor)*

*Defined in [apis/avm/credentials.ts:71](https://github.com/ava-labs/avalanche.js/blob/3888064/src/apis/avm/credentials.ts#L71)*

**Parameters:**

Name | Type | Default |
------ | ------ | ------ |
`sigarray` | Array‹[Signature](avmapi_types.signature.md)› | undefined |

**Returns:** *[SecpCredential](avmapi_credentials.secpcredential.md)*

## Properties

### `Protected` sigArray

• **sigArray**: *Array‹[Signature](avmapi_types.signature.md)›* = []

*Inherited from [Credential](avmapi_credentials.credential.md).[sigArray](avmapi_credentials.credential.md#protected-sigarray)*

*Defined in [apis/avm/credentials.ts:36](https://github.com/ava-labs/avalanche.js/blob/3888064/src/apis/avm/credentials.ts#L36)*

## Methods

###  addSignature

▸ **addSignature**(`sig`: [Signature](avmapi_types.signature.md)): *number*

*Inherited from [Credential](avmapi_credentials.credential.md).[addSignature](avmapi_credentials.credential.md#addsignature)*

*Defined in [apis/avm/credentials.ts:43](https://github.com/ava-labs/avalanche.js/blob/3888064/src/apis/avm/credentials.ts#L43)*

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

*Defined in [apis/avm/credentials.ts:48](https://github.com/ava-labs/avalanche.js/blob/3888064/src/apis/avm/credentials.ts#L48)*

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

*Defined in [apis/avm/credentials.ts:83](https://github.com/ava-labs/avalanche.js/blob/3888064/src/apis/avm/credentials.ts#L83)*

**Returns:** *number*

___

###  toBuffer

▸ **toBuffer**(): *Buffer*

*Inherited from [Credential](avmapi_credentials.credential.md).[toBuffer](avmapi_credentials.credential.md#tobuffer)*

*Defined in [apis/avm/credentials.ts:60](https://github.com/ava-labs/avalanche.js/blob/3888064/src/apis/avm/credentials.ts#L60)*

**Returns:** *Buffer*
