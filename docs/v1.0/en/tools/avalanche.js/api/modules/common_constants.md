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
* [PrimaryNetworkID](common_constants.md#const-primarynetworkid)
* [FallbackHRP](common_constants.md#const-fallbackhrp)
* [FallbackNetworkName](common_constants.md#const-fallbacknetworkname)
* [PChainAlias](common_constants.md#const-pchainalias)
* [PChainVMName](common_constants.md#const-pchainvmname)
* [PlatformChainID](common_constants.md#const-platformchainid)
* [PrimaryAssetAlias](common_constants.md#const-primaryassetalias)
* [XChainAlias](common_constants.md#const-xchainalias)
* [XChainVMName](common_constants.md#const-xchainvmname)

### Object literals

* [HRPToNetworkID](common_constants.md#const-hrptonetworkid)
* [NetworkIDToHRP](common_constants.md#const-networkidtohrp)
* [NetworkIDToNetworkNames](common_constants.md#const-networkidtonetworknames)
* [NetworkNameToNetworkID](common_constants.md#const-networknametonetworkid)
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

Defined in src/utils/constants.ts:207

Rules used when merging sets

## Variables

### `Const` CChainAlias

• **CChainAlias**: *string* = "C"

Defined in src/utils/constants.ts:50

___

### `Const` CChainVMName

• **CChainVMName**: *string* = "evm"

Defined in src/utils/constants.ts:53

___

### `Const` DefaultNetworkID

• **DefaultNetworkID**: *number* = 4

Defined in src/utils/constants.ts:45

___

### `Const` PrimaryNetworkID

• **PrimaryNetworkID**: *string* = "11111111111111111111111111111111LpoYY"

Defined in src/utils/constants.ts:48

___

### `Const` FallbackHRP

• **FallbackHRP**: *string* = "custom"

Defined in src/utils/constants.ts:42

___

### `Const` FallbackNetworkName

• **FallbackNetworkName**: *string* = "Custom Network"

Defined in src/utils/constants.ts:43

___

### `Const` PChainAlias

• **PChainAlias**: *string* = "P"

Defined in src/utils/constants.ts:51

___

### `Const` PChainVMName

• **PChainVMName**: *string* = "platformvm"

Defined in src/utils/constants.ts:54

___

### `Const` PlatformChainID

• **PlatformChainID**: *string* = "11111111111111111111111111111111LpoYY"

Defined in src/utils/constants.ts:47

___

### `Const` PrimaryAssetAlias

• **PrimaryAssetAlias**: *string* = "AVAX"

Defined in src/utils/constants.ts:6

___

### `Const` XChainAlias

• **XChainAlias**: *string* = "X"

Defined in src/utils/constants.ts:49

___

### `Const` XChainVMName

• **XChainVMName**: *string* = "avm"

Defined in src/utils/constants.ts:52

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

### `Const` NetworkIDToNetworkNames

### ▪ **NetworkIDToNetworkNames**: *object*

Defined in src/utils/constants.ts:24

###  1

• **1**: *string[]* = ["Avalanche","Mainnet"]

Defined in src/utils/constants.ts:25

###  12345

• **12345**: *string[]* = ["Local Network"]

Defined in src/utils/constants.ts:29

###  2

• **2**: *string[]* = ["Cascade"]

Defined in src/utils/constants.ts:26

###  3

• **3**: *string[]* = ["Denali"]

Defined in src/utils/constants.ts:27

###  4

• **4**: *string[]* = ["Everest", "Testnet"]

Defined in src/utils/constants.ts:28

___

### `Const` NetworkNameToNetworkID

### ▪ **NetworkNameToNetworkID**: *object*

Defined in src/utils/constants.ts:32

###  Avalanche

• **Avalanche**: *number* = 1

Defined in src/utils/constants.ts:33

###  Cascade

• **Cascade**: *number* = 2

Defined in src/utils/constants.ts:35

###  Denali

• **Denali**: *number* = 3

Defined in src/utils/constants.ts:36

###  Everest

• **Everest**: *number* = 4

Defined in src/utils/constants.ts:37

###  Local Network

• **Local Network**: *number* = 12345

Defined in src/utils/constants.ts:39

###  Mainnet

• **Mainnet**: *number* = 1

Defined in src/utils/constants.ts:34

###  Testnet

• **Testnet**: *number* = 4

Defined in src/utils/constants.ts:38

___

### `Const` n12345C

### ▪ **n12345C**: *object*

Defined in src/utils/constants.ts:151

___

### `Const` n12345P

### ▪ **n12345P**: *object*

Defined in src/utils/constants.ts:149

___

### `Const` n12345X

### ▪ **n12345X**: *object*

Defined in src/utils/constants.ts:147

___

### `Const` n1C

### ▪ **n1C**: *object*

Defined in src/utils/constants.ts:72

###  alias

• **alias**: *string* = CChainAlias

Defined in src/utils/constants.ts:74

###  blockchainID

• **blockchainID**: *string* = "2mUYSXfLrDtigwbzj1LxKVsHwELghc5sisoXrzJwLqAAQHF4i"

Defined in src/utils/constants.ts:73

###  fee

• **fee**: *number* = 0

Defined in src/utils/constants.ts:76

###  vm

• **vm**: *string* = CChainVMName

Defined in src/utils/constants.ts:75

___

### `Const` n1P

### ▪ **n1P**: *object*

Defined in src/utils/constants.ts:65

###  alias

• **alias**: *string* = PChainAlias

Defined in src/utils/constants.ts:67

###  blockchainID

• **blockchainID**: *string* = PlatformChainID

Defined in src/utils/constants.ts:66

###  fee

• **fee**: *number* = 0

Defined in src/utils/constants.ts:69

###  vm

• **vm**: *string* = PChainVMName

Defined in src/utils/constants.ts:68

___

### `Const` n1X

### ▪ **n1X**: *object*

Defined in src/utils/constants.ts:58

###  alias

• **alias**: *string* = XChainAlias

Defined in src/utils/constants.ts:60

###  blockchainID

• **blockchainID**: *string* = "4ktRjsAKxgMr2aEzv9SWmrU7Xk5FniHUrVCX4P1TZSfTLZWFM"

Defined in src/utils/constants.ts:59

###  fee

• **fee**: *number* = 0

Defined in src/utils/constants.ts:62

###  vm

• **vm**: *string* = XChainVMName

Defined in src/utils/constants.ts:61

___

### `Const` n2C

### ▪ **n2C**: *object*

Defined in src/utils/constants.ts:95

###  alias

• **alias**: *string* = CChainAlias

Defined in src/utils/constants.ts:97

###  blockchainID

• **blockchainID**: *string* = "2mUYSXfLrDtigwbzj1LxKVsHwELghc5sisoXrzJwLqAAQHF4i"

Defined in src/utils/constants.ts:96

###  fee

• **fee**: *number* = 0

Defined in src/utils/constants.ts:99

###  vm

• **vm**: *string* = CChainVMName

Defined in src/utils/constants.ts:98

___

### `Const` n2P

### ▪ **n2P**: *object*

Defined in src/utils/constants.ts:88

###  alias

• **alias**: *string* = PChainAlias

Defined in src/utils/constants.ts:90

###  blockchainID

• **blockchainID**: *string* = PlatformChainID

Defined in src/utils/constants.ts:89

###  fee

• **fee**: *number* = 0

Defined in src/utils/constants.ts:92

###  vm

• **vm**: *string* = PChainVMName

Defined in src/utils/constants.ts:91

___

### `Const` n2X

### ▪ **n2X**: *object*

Defined in src/utils/constants.ts:81

###  alias

• **alias**: *string* = XChainAlias

Defined in src/utils/constants.ts:83

###  blockchainID

• **blockchainID**: *string* = "4ktRjsAKxgMr2aEzv9SWmrU7Xk5FniHUrVCX4P1TZSfTLZWFM"

Defined in src/utils/constants.ts:82

###  fee

• **fee**: *number* = 0

Defined in src/utils/constants.ts:85

###  vm

• **vm**: *string* = XChainVMName

Defined in src/utils/constants.ts:84

___

### `Const` n3C

### ▪ **n3C**: *object*

Defined in src/utils/constants.ts:116

###  alias

• **alias**: *string* = CChainAlias

Defined in src/utils/constants.ts:118

###  blockchainID

• **blockchainID**: *string* = "zJytnh96Pc8rM337bBrtMvJDbEdDNjcXG3WkTNCiLp18ergm9"

Defined in src/utils/constants.ts:117

###  fee

• **fee**: *number* = 0

Defined in src/utils/constants.ts:120

###  vm

• **vm**: *string* = CChainVMName

Defined in src/utils/constants.ts:119

___

### `Const` n3P

### ▪ **n3P**: *object*

Defined in src/utils/constants.ts:109

###  alias

• **alias**: *string* = PChainAlias

Defined in src/utils/constants.ts:111

###  blockchainID

• **blockchainID**: *string* = ""

Defined in src/utils/constants.ts:110

###  fee

• **fee**: *number* = 0

Defined in src/utils/constants.ts:113

###  vm

• **vm**: *string* = PChainVMName

Defined in src/utils/constants.ts:112

___

### `Const` n3X

### ▪ **n3X**: *object*

Defined in src/utils/constants.ts:102

###  alias

• **alias**: *string* = XChainAlias

Defined in src/utils/constants.ts:104

###  blockchainID

• **blockchainID**: *string* = "rrEWX7gc7D9mwcdrdBxBTdqh1a7WDVsMuadhTZgyXfFcRz45L"

Defined in src/utils/constants.ts:103

###  fee

• **fee**: *number* = 0

Defined in src/utils/constants.ts:106

###  vm

• **vm**: *string* = XChainVMName

Defined in src/utils/constants.ts:105

___

### `Const` n4C

### ▪ **n4C**: *object*

Defined in src/utils/constants.ts:138

###  alias

• **alias**: *string* = CChainAlias

Defined in src/utils/constants.ts:140

###  blockchainID

• **blockchainID**: *string* = "saMG5YgNsFxzjz4NMkEkt3bAH6hVxWdZkWcEnGB3Z15pcAmsK"

Defined in src/utils/constants.ts:139

###  fee

• **fee**: *number* = 1000000

Defined in src/utils/constants.ts:142

###  vm

• **vm**: *string* = CChainVMName

Defined in src/utils/constants.ts:141

___

### `Const` n4P

### ▪ **n4P**: *object*

Defined in src/utils/constants.ts:131

###  alias

• **alias**: *string* = PChainAlias

Defined in src/utils/constants.ts:133

###  blockchainID

• **blockchainID**: *string* = PlatformChainID

Defined in src/utils/constants.ts:132

###  fee

• **fee**: *number* = 1000000

Defined in src/utils/constants.ts:135

###  vm

• **vm**: *string* = PChainVMName

Defined in src/utils/constants.ts:134

___

### `Const` n4X

### ▪ **n4X**: *object*

Defined in src/utils/constants.ts:124

###  alias

• **alias**: *string* = XChainAlias

Defined in src/utils/constants.ts:126

###  blockchainID

• **blockchainID**: *string* = "jnUjZSRt16TcRnZzmh5aMhavwVHz3zBrSN8GfFMTQkzUnoBxC"

Defined in src/utils/constants.ts:125

###  fee

• **fee**: *number* = 1000000

Defined in src/utils/constants.ts:128

###  vm

• **vm**: *string* = XChainVMName

Defined in src/utils/constants.ts:127
