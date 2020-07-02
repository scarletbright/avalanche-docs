[avalanche](../README.md) › [AVMAPI-Credentials](avmapi_credentials.md)

# Module: AVMAPI-Credentials

## Index

### Classes

* [Credential](../classes/avmapi_credentials.credential.md)
* [NFTCredential](../classes/avmapi_credentials.nftcredential.md)
* [SecpCredential](../classes/avmapi_credentials.secpcredential.md)

### Functions

* [SelectCredentialClass](avmapi_credentials.md#const-selectcredentialclass)

## Functions

### `Const` SelectCredentialClass

▸ **SelectCredentialClass**(`credid`: number, ...`args`: Array‹any›): *[Credential](../classes/avmapi_credentials.credential.md)*

*Defined in [apis/avm/credentials.ts:23](https://github.com/ava-labs/avalanche.js/blob/c723742/src/apis/avm/credentials.ts#L23)*

Takes a buffer representing the credential and returns the proper [Credential](../classes/avmapi_credentials.credential.md) instance.

**Parameters:**

Name | Type | Description |
------ | ------ | ------ |
`credid` | number | A number representing the credential ID parsed prior to the bytes passed in  |
`...args` | Array‹any› | - |

**Returns:** *[Credential](../classes/avmapi_credentials.credential.md)*

An instance of an [Credential](../classes/avmapi_credentials.credential.md)-extended class.
