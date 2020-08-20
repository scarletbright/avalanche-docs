[avalanche](../README.md) › [Common-Constants](common_constants.md)

# Module: Common-Constants

## Index

### Classes

* [Defaults](../classes/common_constants.defaults.md)

### Type aliases

* [MergeRule](common_constants.md#mergerule)

### Variables

* [CChainAlias](common_constants.md#const-cchainalias)
* [CChainVMName](common_constants.md#const-cchainvmname)
* [DefaultNetworkID](common_constants.md#const-defaultnetworkid)
* [DefaultSubnetID](common_constants.md#const-defaultsubnetid)
* [FallbackHRP](common_constants.md#const-fallbackhrp)
* [PChainAlias](common_constants.md#const-pchainalias)
* [PChainVMName](common_constants.md#const-pchainvmname)
* [PlatformChainID](common_constants.md#const-platformchainid)
* [PrimaryAssetAlias](common_constants.md#const-primaryassetalias)
* [XChainAlias](common_constants.md#const-xchainalias)
* [XChainVMName](common_constants.md#const-xchainvmname)

### Object literals

* [HRPToNetworkID](common_constants.md#const-hrptonetworkid)
* [NetworkIDToHRP](common_constants.md#const-networkidtohrp)
* [n12345C](common_constants.md#const-n12345c)
* [n12345P](common_constants.md#const-n12345p)
* [n12345X](common_constants.md#const-n12345x)
* [n1C](common_constants.md#const-n1c)
* [n1P](common_constants.md#const-n1p)
* [n1X](common_constants.md#const-n1x)
* [n2C](common_constants.md#const-n2c)
* [n2P](common_constants.md#const-n2p)
* [n2X](common_constants.md#const-n2x)
* [n3C](common_constants.md#const-n3c)
* [n3P](common_constants.md#const-n3p)
* [n3X](common_constants.md#const-n3x)
* [n4C](common_constants.md#const-n4c)
* [n4P](common_constants.md#const-n4p)
* [n4X](common_constants.md#const-n4x)

## Type aliases

###  MergeRule

Ƭ **MergeRule**: *"intersection" | "differenceSelf" | "differenceNew" | "symDifference" | "union" | "unionMinusNew" | "unionMinusSelf" | "ERROR"*

Defined in src/utils/constants.ts:188

Rules used when merging sets

## Variables

### `Const` CChainAlias

• **CChainAlias**: *string* = "C"

Defined in src/utils/constants.ts:31

___

### `Const` CChainVMName

• **CChainVMName**: *string* = "evm"

Defined in src/utils/constants.ts:34

___

### `Const` DefaultNetworkID

• **DefaultNetworkID**: *number* = 3

Defined in src/utils/constants.ts:26

___

### `Const` DefaultSubnetID

• **DefaultSubnetID**: *string* = "11111111111111111111111111111111LpoYY"

Defined in src/utils/constants.ts:29

___

### `Const` FallbackHRP

• **FallbackHRP**: *string* = "custom"

Defined in src/utils/constants.ts:24

___

### `Const` PChainAlias

• **PChainAlias**: *string* = "P"

Defined in src/utils/constants.ts:32

___

### `Const` PChainVMName

• **PChainVMName**: *string* = "platformvm"

Defined in src/utils/constants.ts:35

___

### `Const` PlatformChainID

• **PlatformChainID**: *string* = "11111111111111111111111111111111LpoYY"

Defined in src/utils/constants.ts:28

___

### `Const` PrimaryAssetAlias

• **PrimaryAssetAlias**: *string* = "AVAX"

Defined in src/utils/constants.ts:6

___

### `Const` XChainAlias

• **XChainAlias**: *string* = "X"

Defined in src/utils/constants.ts:30

___

### `Const` XChainVMName

• **XChainVMName**: *string* = "avm"

Defined in src/utils/constants.ts:33

## Object literals

### `Const` HRPToNetworkID

### ▪ **HRPToNetworkID**: *object*

Defined in src/utils/constants.ts:16

###  avax

• **avax**: *number* = 1

Defined in src/utils/constants.ts:17

###  cascade

• **cascade**: *number* = 2

Defined in src/utils/constants.ts:18

###  denali

• **denali**: *number* = 3

Defined in src/utils/constants.ts:19

###  everest

• **everest**: *number* = 4

Defined in src/utils/constants.ts:20

###  local

• **local**: *number* = 12345

Defined in src/utils/constants.ts:21

___

### `Const` NetworkIDToHRP

### ▪ **NetworkIDToHRP**: *object*

Defined in src/utils/constants.ts:8

###  1

• **1**: *string* = "avax"

Defined in src/utils/constants.ts:9

###  12345

• **12345**: *string* = "local"

Defined in src/utils/constants.ts:13

###  2

• **2**: *string* = "cascade"

Defined in src/utils/constants.ts:10

###  3

• **3**: *string* = "denali"

Defined in src/utils/constants.ts:11

###  4

• **4**: *string* = "everest"

Defined in src/utils/constants.ts:12

___

### `Const` n12345C

### ▪ **n12345C**: *object*

Defined in src/utils/constants.ts:132

___

### `Const` n12345P

### ▪ **n12345P**: *object*

Defined in src/utils/constants.ts:130

___

### `Const` n12345X

### ▪ **n12345X**: *object*

Defined in src/utils/constants.ts:128

___

### `Const` n1C

### ▪ **n1C**: *object*

Defined in src/utils/constants.ts:53

###  alias

• **alias**: *string* = CChainAlias

Defined in src/utils/constants.ts:55

###  blockchainID

• **blockchainID**: *string* = "2mUYSXfLrDtigwbzj1LxKVsHwELghc5sisoXrzJwLqAAQHF4i"

Defined in src/utils/constants.ts:54

###  fee

• **fee**: *number* = 0

Defined in src/utils/constants.ts:57

###  vm

• **vm**: *string* = CChainVMName

Defined in src/utils/constants.ts:56

___

### `Const` n1P

### ▪ **n1P**: *object*

Defined in src/utils/constants.ts:46

###  alias

• **alias**: *string* = PChainAlias

Defined in src/utils/constants.ts:48

###  blockchainID

• **blockchainID**: *string* = PlatformChainID

Defined in src/utils/constants.ts:47

###  fee

• **fee**: *number* = 0

Defined in src/utils/constants.ts:50

###  vm

• **vm**: *string* = PChainVMName

Defined in src/utils/constants.ts:49

___

### `Const` n1X

### ▪ **n1X**: *object*

Defined in src/utils/constants.ts:39

###  alias

• **alias**: *string* = XChainAlias

Defined in src/utils/constants.ts:41

###  blockchainID

• **blockchainID**: *string* = "4ktRjsAKxgMr2aEzv9SWmrU7Xk5FniHUrVCX4P1TZSfTLZWFM"

Defined in src/utils/constants.ts:40

###  fee

• **fee**: *number* = 0

Defined in src/utils/constants.ts:43

###  vm

• **vm**: *string* = XChainVMName

Defined in src/utils/constants.ts:42

___

### `Const` n2C

### ▪ **n2C**: *object*

Defined in src/utils/constants.ts:76

###  alias

• **alias**: *string* = CChainAlias

Defined in src/utils/constants.ts:78

###  blockchainID

• **blockchainID**: *string* = "2mUYSXfLrDtigwbzj1LxKVsHwELghc5sisoXrzJwLqAAQHF4i"

Defined in src/utils/constants.ts:77

###  fee

• **fee**: *number* = 0

Defined in src/utils/constants.ts:80

###  vm

• **vm**: *string* = CChainVMName

Defined in src/utils/constants.ts:79

___

### `Const` n2P

### ▪ **n2P**: *object*

Defined in src/utils/constants.ts:69

###  alias

• **alias**: *string* = PChainAlias

Defined in src/utils/constants.ts:71

###  blockchainID

• **blockchainID**: *string* = PlatformChainID

Defined in src/utils/constants.ts:70

###  fee

• **fee**: *number* = 0

Defined in src/utils/constants.ts:73

###  vm

• **vm**: *string* = PChainVMName

Defined in src/utils/constants.ts:72

___

### `Const` n2X

### ▪ **n2X**: *object*

Defined in src/utils/constants.ts:62

###  alias

• **alias**: *string* = XChainAlias

Defined in src/utils/constants.ts:64

###  blockchainID

• **blockchainID**: *string* = "4ktRjsAKxgMr2aEzv9SWmrU7Xk5FniHUrVCX4P1TZSfTLZWFM"

Defined in src/utils/constants.ts:63

###  fee

• **fee**: *number* = 0

Defined in src/utils/constants.ts:66

###  vm

• **vm**: *string* = XChainVMName

Defined in src/utils/constants.ts:65

___

### `Const` n3C

### ▪ **n3C**: *object*

Defined in src/utils/constants.ts:97

###  alias

• **alias**: *string* = CChainAlias

Defined in src/utils/constants.ts:99

###  blockchainID

• **blockchainID**: *string* = "zJytnh96Pc8rM337bBrtMvJDbEdDNjcXG3WkTNCiLp18ergm9"

Defined in src/utils/constants.ts:98

###  fee

• **fee**: *number* = 0

Defined in src/utils/constants.ts:101

###  vm

• **vm**: *string* = CChainVMName

Defined in src/utils/constants.ts:100

___

### `Const` n3P

### ▪ **n3P**: *object*

Defined in src/utils/constants.ts:90

###  alias

• **alias**: *string* = PChainAlias

Defined in src/utils/constants.ts:92

###  blockchainID

• **blockchainID**: *string* = ""

Defined in src/utils/constants.ts:91

###  fee

• **fee**: *number* = 0

Defined in src/utils/constants.ts:94

###  vm

• **vm**: *string* = PChainVMName

Defined in src/utils/constants.ts:93

___

### `Const` n3X

### ▪ **n3X**: *object*

Defined in src/utils/constants.ts:83

###  alias

• **alias**: *string* = XChainAlias

Defined in src/utils/constants.ts:85

###  blockchainID

• **blockchainID**: *string* = "rrEWX7gc7D9mwcdrdBxBTdqh1a7WDVsMuadhTZgyXfFcRz45L"

Defined in src/utils/constants.ts:84

###  fee

• **fee**: *number* = 0

Defined in src/utils/constants.ts:87

###  vm

• **vm**: *string* = XChainVMName

Defined in src/utils/constants.ts:86

___

### `Const` n4C

### ▪ **n4C**: *object*

Defined in src/utils/constants.ts:119

###  alias

• **alias**: *string* = CChainAlias

Defined in src/utils/constants.ts:121

###  blockchainID

• **blockchainID**: *string* = "zJytnh96Pc8rM337bBrtMvJDbEdDNjcXG3WkTNCiLp18ergm9"

Defined in src/utils/constants.ts:120

###  fee

• **fee**: *number* = 0

Defined in src/utils/constants.ts:123

###  vm

• **vm**: *string* = CChainVMName

Defined in src/utils/constants.ts:122

___

### `Const` n4P

### ▪ **n4P**: *object*

Defined in src/utils/constants.ts:112

###  alias

• **alias**: *string* = PChainAlias

Defined in src/utils/constants.ts:114

###  blockchainID

• **blockchainID**: *string* = PlatformChainID

Defined in src/utils/constants.ts:113

###  fee

• **fee**: *number* = 0

Defined in src/utils/constants.ts:116

###  vm

• **vm**: *string* = PChainVMName

Defined in src/utils/constants.ts:115

___

### `Const` n4X

### ▪ **n4X**: *object*

Defined in src/utils/constants.ts:105

###  alias

• **alias**: *string* = XChainAlias

Defined in src/utils/constants.ts:107

###  blockchainID

• **blockchainID**: *string* = "rrEWX7gc7D9mwcdrdBxBTdqh1a7WDVsMuadhTZgyXfFcRz45L"

Defined in src/utils/constants.ts:106

###  fee

• **fee**: *number* = 0

Defined in src/utils/constants.ts:109

###  vm

• **vm**: *string* = XChainVMName

Defined in src/utils/constants.ts:108
