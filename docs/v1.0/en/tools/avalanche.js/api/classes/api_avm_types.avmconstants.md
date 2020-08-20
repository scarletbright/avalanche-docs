[avalanche](../README.md) › [API-AVM-Types](../modules/api_avm_types.md) › [AVMConstants](api_avm_types.avmconstants.md)

# Class: AVMConstants

## Hierarchy

* **AVMConstants**

## Index

### Properties

* [ADDRESSLENGTH](api_avm_types.avmconstants.md#static-addresslength)
* [ASSETIDLEN](api_avm_types.avmconstants.md#static-assetidlen)
* [ASSETNAMELEN](api_avm_types.avmconstants.md#static-assetnamelen)
* [BASETX](api_avm_types.avmconstants.md#static-basetx)
* [BLOCKCHAINIDLEN](api_avm_types.avmconstants.md#static-blockchainidlen)
* [CENTIAVAX](api_avm_types.avmconstants.md#static-centiavax)
* [CREATEASSETTX](api_avm_types.avmconstants.md#static-createassettx)
* [DECIAVAX](api_avm_types.avmconstants.md#static-deciavax)
* [EXPORTTX](api_avm_types.avmconstants.md#static-exporttx)
* [IMPORTTX](api_avm_types.avmconstants.md#static-importtx)
* [LATESTCODEC](api_avm_types.avmconstants.md#static-latestcodec)
* [MICROAVAX](api_avm_types.avmconstants.md#static-microavax)
* [MILLIAVAX](api_avm_types.avmconstants.md#static-milliavax)
* [NFTCREDENTIAL](api_avm_types.avmconstants.md#static-nftcredential)
* [NFTFXID](api_avm_types.avmconstants.md#static-nftfxid)
* [NFTMINTOPID](api_avm_types.avmconstants.md#static-nftmintopid)
* [NFTMINTOUTPUTID](api_avm_types.avmconstants.md#static-nftmintoutputid)
* [NFTXFEROP](api_avm_types.avmconstants.md#static-nftxferop)
* [NFTXFEROUTPUTID](api_avm_types.avmconstants.md#static-nftxferoutputid)
* [ONEAVAX](api_avm_types.avmconstants.md#static-oneavax)
* [OPERATIONTX](api_avm_types.avmconstants.md#static-operationtx)
* [SECPCREDENTIAL](api_avm_types.avmconstants.md#static-secpcredential)
* [SECPFXID](api_avm_types.avmconstants.md#static-secpfxid)
* [SECPINPUTID](api_avm_types.avmconstants.md#static-secpinputid)
* [SECPOUTPUTID](api_avm_types.avmconstants.md#static-secpoutputid)
* [SYMBOLMAXLEN](api_avm_types.avmconstants.md#static-symbolmaxlen)

## Properties

### `Static` ADDRESSLENGTH

▪ **ADDRESSLENGTH**: *number* = 20

Defined in src/apis/avm/constants.ts:65

___

### `Static` ASSETIDLEN

▪ **ASSETIDLEN**: *number* = 32

Defined in src/apis/avm/constants.ts:57

___

### `Static` ASSETNAMELEN

▪ **ASSETNAMELEN**: *number* = 128

Defined in src/apis/avm/constants.ts:63

___

### `Static` BASETX

▪ **BASETX**: *number* = 0

Defined in src/apis/avm/constants.ts:43

___

### `Static` BLOCKCHAINIDLEN

▪ **BLOCKCHAINIDLEN**: *number* = 32

Defined in src/apis/avm/constants.ts:59

___

### `Static` CENTIAVAX

▪ **CENTIAVAX**: *BN* = AVMConstants.ONEAVAX.div(new BN(100))

Defined in src/apis/avm/constants.ts:21

___

### `Static` CREATEASSETTX

▪ **CREATEASSETTX**: *number* = 1

Defined in src/apis/avm/constants.ts:45

___

### `Static` DECIAVAX

▪ **DECIAVAX**: *BN* = AVMConstants.ONEAVAX.div(new BN(10))

Defined in src/apis/avm/constants.ts:19

___

### `Static` EXPORTTX

▪ **EXPORTTX**: *number* = 4

Defined in src/apis/avm/constants.ts:51

___

### `Static` IMPORTTX

▪ **IMPORTTX**: *number* = 3

Defined in src/apis/avm/constants.ts:49

___

### `Static` LATESTCODEC

▪ **LATESTCODEC**: *number* = 0

Defined in src/apis/avm/constants.ts:15

___

### `Static` MICROAVAX

▪ **MICROAVAX**: *BN* = AVMConstants.ONEAVAX.div(new BN(1000000))

Defined in src/apis/avm/constants.ts:25

___

### `Static` MILLIAVAX

▪ **MILLIAVAX**: *BN* = AVMConstants.ONEAVAX.div(new BN(1000))

Defined in src/apis/avm/constants.ts:23

___

### `Static` NFTCREDENTIAL

▪ **NFTCREDENTIAL**: *number* = 14

Defined in src/apis/avm/constants.ts:55

___

### `Static` NFTFXID

▪ **NFTFXID**: *number* = 1

Defined in src/apis/avm/constants.ts:29

___

### `Static` NFTMINTOPID

▪ **NFTMINTOPID**: *number* = 12

Defined in src/apis/avm/constants.ts:39

___

### `Static` NFTMINTOUTPUTID

▪ **NFTMINTOUTPUTID**: *number* = 10

Defined in src/apis/avm/constants.ts:35

___

### `Static` NFTXFEROP

▪ **NFTXFEROP**: *number* = 13

Defined in src/apis/avm/constants.ts:41

___

### `Static` NFTXFEROUTPUTID

▪ **NFTXFEROUTPUTID**: *number* = 11

Defined in src/apis/avm/constants.ts:33

___

### `Static` ONEAVAX

▪ **ONEAVAX**: *BN* = new BN(1000000000)

Defined in src/apis/avm/constants.ts:17

___

### `Static` OPERATIONTX

▪ **OPERATIONTX**: *number* = 2

Defined in src/apis/avm/constants.ts:47

___

### `Static` SECPCREDENTIAL

▪ **SECPCREDENTIAL**: *number* = 9

Defined in src/apis/avm/constants.ts:53

___

### `Static` SECPFXID

▪ **SECPFXID**: *number* = 0

Defined in src/apis/avm/constants.ts:27

___

### `Static` SECPINPUTID

▪ **SECPINPUTID**: *number* = 5

Defined in src/apis/avm/constants.ts:37

___

### `Static` SECPOUTPUTID

▪ **SECPOUTPUTID**: *number* = 7

Defined in src/apis/avm/constants.ts:31

___

### `Static` SYMBOLMAXLEN

▪ **SYMBOLMAXLEN**: *number* = 4

Defined in src/apis/avm/constants.ts:61
