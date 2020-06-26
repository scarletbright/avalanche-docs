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

*Defined in [apis/avm/credentials.ts:71](https://github.com/ava-labs/avalanche.js/blob/3888064/src/apis/avm/credentials.ts#L71)*

**Parameters:**

Name | Type | Default |
------ | ------ | ------ |
`sigarray` | Array‹[Signature](avmapi_types.signature.md)› | undefined |

**Returns:** *[Credential](avmapi_credentials.credential.md)*

## Properties

### `Protected` sigArray

• **sigArray**: *Array‹[Signature](avmapi_types.signature.md)›* = []

*Defined in [apis/avm/credentials.ts:36](https://github.com/ava-labs/avalanche.js/blob/3888064/src/apis/avm/credentials.ts#L36)*

## Methods

###  addSignature

▸ **addSignature**(`sig`: [Signature](avmapi_types.signature.md)): *number*

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

*Defined in [apis/avm/credentials.ts:48](https://github.com/ava-labs/avalanche.js/blob/3888064/src/apis/avm/credentials.ts#L48)*

**Parameters:**

Name | Type | Default |
------ | ------ | ------ |
`bytes` | any | - |
`offset` | number | 0 |

**Returns:** *number*

___

### `Abstract` getCredentialID

▸ **getCredentialID**(): *number*

*Defined in [apis/avm/credentials.ts:38](https://github.com/ava-labs/avalanche.js/blob/3888064/src/apis/avm/credentials.ts#L38)*

**Returns:** *number*

___

###  toBuffer

▸ **toBuffer**(): *Buffer*

*Defined in [apis/avm/credentials.ts:60](https://github.com/ava-labs/avalanche.js/blob/3888064/src/apis/avm/credentials.ts#L60)*

**Returns:** *Buffer*
