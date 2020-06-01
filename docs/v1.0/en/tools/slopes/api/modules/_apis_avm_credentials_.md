[slopes - v1.7.1](../README.md) › ["apis/avm/credentials"](_apis_avm_credentials_.md)

# External module: "apis/avm/credentials"

## Index

### Classes

* [Credential](../classes/_apis_avm_credentials_.credential.md)
* [NFTCredential](../classes/_apis_avm_credentials_.nftcredential.md)
* [SecpCredential](../classes/_apis_avm_credentials_.secpcredential.md)

### Functions

* [SelectCredentialClass](_apis_avm_credentials_.md#const-selectcredentialclass)

## Functions

### `Const` SelectCredentialClass

▸ **SelectCredentialClass**(`credid`: number, ...`args`: Array‹any›): *[Credential](../classes/_apis_avm_credentials_.credential.md)*

*Defined in [apis/avm/credentials.ts:22](https://github.com/ava-labs/slopes/blob/0d1acbd/src/apis/avm/credentials.ts#L22)*

Takes a buffer representing the credential and returns the proper [Credential](../classes/_apis_avm_credentials_.credential.md) instance.

**Parameters:**

Name | Type | Description |
------ | ------ | ------ |
`credid` | number | A number representing the credential ID parsed prior to the bytes passed in  |
`...args` | Array‹any› | - |

**Returns:** *[Credential](../classes/_apis_avm_credentials_.credential.md)*

An instance of an [Credential](../classes/_apis_avm_credentials_.credential.md)-extended class.
