[avalanche](../README.md) › [Utils-Constants](utils_constants.md)

# Module: Utils-Constants

## Index

### Classes

* [Defaults](../classes/utils_constants.defaults.md)

### Type aliases

* [MergeRule](utils_constants.md#mergerule)

### Variables

* [AVAXGWEI](utils_constants.md#const-avaxgwei)
* [CChainAlias](utils_constants.md#const-cchainalias)
* [CChainVMName](utils_constants.md#const-cchainvmname)
* [CENTIAVAX](utils_constants.md#const-centiavax)
* [DECIAVAX](utils_constants.md#const-deciavax)
* [DefaultNetworkID](utils_constants.md#const-defaultnetworkid)
* [FallbackHRP](utils_constants.md#const-fallbackhrp)
* [FallbackNetworkName](utils_constants.md#const-fallbacknetworkname)
* [GWEI](utils_constants.md#const-gwei)
* [MICROAVAX](utils_constants.md#const-microavax)
* [MILLIAVAX](utils_constants.md#const-milliavax)
* [NANOAVAX](utils_constants.md#const-nanoavax)
* [NodeIDPrefix](utils_constants.md#const-nodeidprefix)
* [ONEAVAX](utils_constants.md#const-oneavax)
* [PChainAlias](utils_constants.md#const-pchainalias)
* [PChainVMName](utils_constants.md#const-pchainvmname)
* [PlatformChainID](utils_constants.md#const-platformchainid)
* [PrimaryAssetAlias](utils_constants.md#const-primaryassetalias)
* [PrimaryNetworkID](utils_constants.md#const-primarynetworkid)
* [PrivateKeyPrefix](utils_constants.md#const-privatekeyprefix)
* [WEI](utils_constants.md#const-wei)
* [XChainAlias](utils_constants.md#const-xchainalias)
* [XChainVMName](utils_constants.md#const-xchainvmname)

### Object literals

* [HRPToNetworkID](utils_constants.md#const-hrptonetworkid)
* [NetworkIDToHRP](utils_constants.md#const-networkidtohrp)
* [NetworkIDToNetworkNames](utils_constants.md#const-networkidtonetworknames)
* [NetworkNameToNetworkID](utils_constants.md#const-networknametonetworkid)
* [n12345C](utils_constants.md#const-n12345c)
* [n12345P](utils_constants.md#const-n12345p)
* [n12345X](utils_constants.md#const-n12345x)
* [n1C](utils_constants.md#const-n1c)
* [n1P](utils_constants.md#const-n1p)
* [n1X](utils_constants.md#const-n1x)
* [n2C](utils_constants.md#const-n2c)
* [n2P](utils_constants.md#const-n2p)
* [n2X](utils_constants.md#const-n2x)
* [n3C](utils_constants.md#const-n3c)
* [n3P](utils_constants.md#const-n3p)
* [n3X](utils_constants.md#const-n3x)
* [n4C](utils_constants.md#const-n4c)
* [n4P](utils_constants.md#const-n4p)
* [n4X](utils_constants.md#const-n4x)

## Type aliases

###  MergeRule

Ƭ **MergeRule**: *"intersection" | "differenceSelf" | "differenceNew" | "symDifference" | "union" | "unionMinusNew" | "unionMinusSelf" | "ERROR"*

*Defined in [src/utils/constants.ts:251](https://github.com/ava-labs/avalanche.js/blob/a2feb77/src/utils/constants.ts#L251)*

Rules used when merging sets

## Variables

### `Const` AVAXGWEI

• **AVAXGWEI**: *BN* = NANOAVAX.clone()

*Defined in [src/utils/constants.ts:78](https://github.com/ava-labs/avalanche.js/blob/a2feb77/src/utils/constants.ts#L78)*

___

### `Const` CChainAlias

• **CChainAlias**: *string* = "C"

*Defined in [src/utils/constants.ts:56](https://github.com/ava-labs/avalanche.js/blob/a2feb77/src/utils/constants.ts#L56)*

___

### `Const` CChainVMName

• **CChainVMName**: *string* = "evm"

*Defined in [src/utils/constants.ts:59](https://github.com/ava-labs/avalanche.js/blob/a2feb77/src/utils/constants.ts#L59)*

___

### `Const` CENTIAVAX

• **CENTIAVAX**: *BN* = ONEAVAX.div(new BN(100))

*Defined in [src/utils/constants.ts:66](https://github.com/ava-labs/avalanche.js/blob/a2feb77/src/utils/constants.ts#L66)*

___

### `Const` DECIAVAX

• **DECIAVAX**: *BN* = ONEAVAX.div(new BN(10))

*Defined in [src/utils/constants.ts:64](https://github.com/ava-labs/avalanche.js/blob/a2feb77/src/utils/constants.ts#L64)*

___

### `Const` DefaultNetworkID

• **DefaultNetworkID**: *number* = 4

*Defined in [src/utils/constants.ts:51](https://github.com/ava-labs/avalanche.js/blob/a2feb77/src/utils/constants.ts#L51)*

___

### `Const` FallbackHRP

• **FallbackHRP**: *string* = "custom"

*Defined in [src/utils/constants.ts:48](https://github.com/ava-labs/avalanche.js/blob/a2feb77/src/utils/constants.ts#L48)*

___

### `Const` FallbackNetworkName

• **FallbackNetworkName**: *string* = "Custom Network"

*Defined in [src/utils/constants.ts:49](https://github.com/ava-labs/avalanche.js/blob/a2feb77/src/utils/constants.ts#L49)*

___

### `Const` GWEI

• **GWEI**: *BN* = WEI.mul(new BN(1000000000))

*Defined in [src/utils/constants.ts:76](https://github.com/ava-labs/avalanche.js/blob/a2feb77/src/utils/constants.ts#L76)*

___

### `Const` MICROAVAX

• **MICROAVAX**: *BN* = ONEAVAX.div(new BN(1000000))

*Defined in [src/utils/constants.ts:70](https://github.com/ava-labs/avalanche.js/blob/a2feb77/src/utils/constants.ts#L70)*

___

### `Const` MILLIAVAX

• **MILLIAVAX**: *BN* = ONEAVAX.div(new BN(1000))

*Defined in [src/utils/constants.ts:68](https://github.com/ava-labs/avalanche.js/blob/a2feb77/src/utils/constants.ts#L68)*

___

### `Const` NANOAVAX

• **NANOAVAX**: *BN* = ONEAVAX.div(new BN(1000000000))

*Defined in [src/utils/constants.ts:72](https://github.com/ava-labs/avalanche.js/blob/a2feb77/src/utils/constants.ts#L72)*

___

### `Const` NodeIDPrefix

• **NodeIDPrefix**: *string* = "NodeID-"

*Defined in [src/utils/constants.ts:10](https://github.com/ava-labs/avalanche.js/blob/a2feb77/src/utils/constants.ts#L10)*

___

### `Const` ONEAVAX

• **ONEAVAX**: *BN* = new BN(1000000000)

*Defined in [src/utils/constants.ts:62](https://github.com/ava-labs/avalanche.js/blob/a2feb77/src/utils/constants.ts#L62)*

___

### `Const` PChainAlias

• **PChainAlias**: *string* = "P"

*Defined in [src/utils/constants.ts:57](https://github.com/ava-labs/avalanche.js/blob/a2feb77/src/utils/constants.ts#L57)*

___

### `Const` PChainVMName

• **PChainVMName**: *string* = "platformvm"

*Defined in [src/utils/constants.ts:60](https://github.com/ava-labs/avalanche.js/blob/a2feb77/src/utils/constants.ts#L60)*

___

### `Const` PlatformChainID

• **PlatformChainID**: *string* = "11111111111111111111111111111111LpoYY"

*Defined in [src/utils/constants.ts:53](https://github.com/ava-labs/avalanche.js/blob/a2feb77/src/utils/constants.ts#L53)*

___

### `Const` PrimaryAssetAlias

• **PrimaryAssetAlias**: *string* = "AVAX"

*Defined in [src/utils/constants.ts:12](https://github.com/ava-labs/avalanche.js/blob/a2feb77/src/utils/constants.ts#L12)*

___

### `Const` PrimaryNetworkID

• **PrimaryNetworkID**: *string* = "11111111111111111111111111111111LpoYY"

*Defined in [src/utils/constants.ts:54](https://github.com/ava-labs/avalanche.js/blob/a2feb77/src/utils/constants.ts#L54)*

___

### `Const` PrivateKeyPrefix

• **PrivateKeyPrefix**: *string* = "PrivateKey-"

*Defined in [src/utils/constants.ts:8](https://github.com/ava-labs/avalanche.js/blob/a2feb77/src/utils/constants.ts#L8)*

___

### `Const` WEI

• **WEI**: *BN* = new BN(1)

*Defined in [src/utils/constants.ts:74](https://github.com/ava-labs/avalanche.js/blob/a2feb77/src/utils/constants.ts#L74)*

___

### `Const` XChainAlias

• **XChainAlias**: *string* = "X"

*Defined in [src/utils/constants.ts:55](https://github.com/ava-labs/avalanche.js/blob/a2feb77/src/utils/constants.ts#L55)*

___

### `Const` XChainVMName

• **XChainVMName**: *string* = "avm"

*Defined in [src/utils/constants.ts:58](https://github.com/ava-labs/avalanche.js/blob/a2feb77/src/utils/constants.ts#L58)*

## Object literals

### `Const` HRPToNetworkID

### ▪ **HRPToNetworkID**: *object*

*Defined in [src/utils/constants.ts:22](https://github.com/ava-labs/avalanche.js/blob/a2feb77/src/utils/constants.ts#L22)*

###  avax

• **avax**: *number* = 1

*Defined in [src/utils/constants.ts:23](https://github.com/ava-labs/avalanche.js/blob/a2feb77/src/utils/constants.ts#L23)*

###  cascade

• **cascade**: *number* = 2

*Defined in [src/utils/constants.ts:24](https://github.com/ava-labs/avalanche.js/blob/a2feb77/src/utils/constants.ts#L24)*

###  denali

• **denali**: *number* = 3

*Defined in [src/utils/constants.ts:25](https://github.com/ava-labs/avalanche.js/blob/a2feb77/src/utils/constants.ts#L25)*

###  everest

• **everest**: *number* = 4

*Defined in [src/utils/constants.ts:26](https://github.com/ava-labs/avalanche.js/blob/a2feb77/src/utils/constants.ts#L26)*

###  local

• **local**: *number* = 12345

*Defined in [src/utils/constants.ts:27](https://github.com/ava-labs/avalanche.js/blob/a2feb77/src/utils/constants.ts#L27)*

___

### `Const` NetworkIDToHRP

### ▪ **NetworkIDToHRP**: *object*

*Defined in [src/utils/constants.ts:14](https://github.com/ava-labs/avalanche.js/blob/a2feb77/src/utils/constants.ts#L14)*

###  1

• **1**: *string* = "avax"

*Defined in [src/utils/constants.ts:15](https://github.com/ava-labs/avalanche.js/blob/a2feb77/src/utils/constants.ts#L15)*

###  12345

• **12345**: *string* = "local"

*Defined in [src/utils/constants.ts:19](https://github.com/ava-labs/avalanche.js/blob/a2feb77/src/utils/constants.ts#L19)*

###  2

• **2**: *string* = "cascade"

*Defined in [src/utils/constants.ts:16](https://github.com/ava-labs/avalanche.js/blob/a2feb77/src/utils/constants.ts#L16)*

###  3

• **3**: *string* = "denali"

*Defined in [src/utils/constants.ts:17](https://github.com/ava-labs/avalanche.js/blob/a2feb77/src/utils/constants.ts#L17)*

###  4

• **4**: *string* = "everest"

*Defined in [src/utils/constants.ts:18](https://github.com/ava-labs/avalanche.js/blob/a2feb77/src/utils/constants.ts#L18)*

___

### `Const` NetworkIDToNetworkNames

### ▪ **NetworkIDToNetworkNames**: *object*

*Defined in [src/utils/constants.ts:30](https://github.com/ava-labs/avalanche.js/blob/a2feb77/src/utils/constants.ts#L30)*

###  1

• **1**: *string[]* = ["Avalanche","Mainnet"]

*Defined in [src/utils/constants.ts:31](https://github.com/ava-labs/avalanche.js/blob/a2feb77/src/utils/constants.ts#L31)*

###  12345

• **12345**: *string[]* = ["Local Network"]

*Defined in [src/utils/constants.ts:35](https://github.com/ava-labs/avalanche.js/blob/a2feb77/src/utils/constants.ts#L35)*

###  2

• **2**: *string[]* = ["Cascade"]

*Defined in [src/utils/constants.ts:32](https://github.com/ava-labs/avalanche.js/blob/a2feb77/src/utils/constants.ts#L32)*

###  3

• **3**: *string[]* = ["Denali"]

*Defined in [src/utils/constants.ts:33](https://github.com/ava-labs/avalanche.js/blob/a2feb77/src/utils/constants.ts#L33)*

###  4

• **4**: *string[]* = ["Everest", "Testnet"]

*Defined in [src/utils/constants.ts:34](https://github.com/ava-labs/avalanche.js/blob/a2feb77/src/utils/constants.ts#L34)*

___

### `Const` NetworkNameToNetworkID

### ▪ **NetworkNameToNetworkID**: *object*

*Defined in [src/utils/constants.ts:38](https://github.com/ava-labs/avalanche.js/blob/a2feb77/src/utils/constants.ts#L38)*

###  Avalanche

• **Avalanche**: *number* = 1

*Defined in [src/utils/constants.ts:39](https://github.com/ava-labs/avalanche.js/blob/a2feb77/src/utils/constants.ts#L39)*

###  Cascade

• **Cascade**: *number* = 2

*Defined in [src/utils/constants.ts:41](https://github.com/ava-labs/avalanche.js/blob/a2feb77/src/utils/constants.ts#L41)*

###  Denali

• **Denali**: *number* = 3

*Defined in [src/utils/constants.ts:42](https://github.com/ava-labs/avalanche.js/blob/a2feb77/src/utils/constants.ts#L42)*

###  Everest

• **Everest**: *number* = 4

*Defined in [src/utils/constants.ts:43](https://github.com/ava-labs/avalanche.js/blob/a2feb77/src/utils/constants.ts#L43)*

###  Local Network

• **Local Network**: *number* = 12345

*Defined in [src/utils/constants.ts:45](https://github.com/ava-labs/avalanche.js/blob/a2feb77/src/utils/constants.ts#L45)*

###  Mainnet

• **Mainnet**: *number* = 1

*Defined in [src/utils/constants.ts:40](https://github.com/ava-labs/avalanche.js/blob/a2feb77/src/utils/constants.ts#L40)*

###  Testnet

• **Testnet**: *number* = 4

*Defined in [src/utils/constants.ts:44](https://github.com/ava-labs/avalanche.js/blob/a2feb77/src/utils/constants.ts#L44)*

___

### `Const` n12345C

### ▪ **n12345C**: *object*

*Defined in [src/utils/constants.ts:195](https://github.com/ava-labs/avalanche.js/blob/a2feb77/src/utils/constants.ts#L195)*

___

### `Const` n12345P

### ▪ **n12345P**: *object*

*Defined in [src/utils/constants.ts:193](https://github.com/ava-labs/avalanche.js/blob/a2feb77/src/utils/constants.ts#L193)*

___

### `Const` n12345X

### ▪ **n12345X**: *object*

*Defined in [src/utils/constants.ts:191](https://github.com/ava-labs/avalanche.js/blob/a2feb77/src/utils/constants.ts#L191)*

___

### `Const` n1C

### ▪ **n1C**: *object*

*Defined in [src/utils/constants.ts:101](https://github.com/ava-labs/avalanche.js/blob/a2feb77/src/utils/constants.ts#L101)*

###  alias

• **alias**: *string* = CChainAlias

*Defined in [src/utils/constants.ts:103](https://github.com/ava-labs/avalanche.js/blob/a2feb77/src/utils/constants.ts#L103)*

###  blockchainID

• **blockchainID**: *string* = "2mUYSXfLrDtigwbzj1LxKVsHwELghc5sisoXrzJwLqAAQHF4i"

*Defined in [src/utils/constants.ts:102](https://github.com/ava-labs/avalanche.js/blob/a2feb77/src/utils/constants.ts#L102)*

###  fee

• **fee**: *BN‹›* = GWEI.mul(new BN(470))

*Defined in [src/utils/constants.ts:105](https://github.com/ava-labs/avalanche.js/blob/a2feb77/src/utils/constants.ts#L105)*

###  vm

• **vm**: *string* = CChainVMName

*Defined in [src/utils/constants.ts:104](https://github.com/ava-labs/avalanche.js/blob/a2feb77/src/utils/constants.ts#L104)*

___

### `Const` n1P

### ▪ **n1P**: *object*

*Defined in [src/utils/constants.ts:89](https://github.com/ava-labs/avalanche.js/blob/a2feb77/src/utils/constants.ts#L89)*

###  alias

• **alias**: *string* = PChainAlias

*Defined in [src/utils/constants.ts:91](https://github.com/ava-labs/avalanche.js/blob/a2feb77/src/utils/constants.ts#L91)*

###  blockchainID

• **blockchainID**: *string* = PlatformChainID

*Defined in [src/utils/constants.ts:90](https://github.com/ava-labs/avalanche.js/blob/a2feb77/src/utils/constants.ts#L90)*

###  fee

• **fee**: *number* = 1000000

*Defined in [src/utils/constants.ts:93](https://github.com/ava-labs/avalanche.js/blob/a2feb77/src/utils/constants.ts#L93)*

###  maxConsumption

• **maxConsumption**: *number* = 0.12

*Defined in [src/utils/constants.ts:95](https://github.com/ava-labs/avalanche.js/blob/a2feb77/src/utils/constants.ts#L95)*

###  maxStakingDuration

• **maxStakingDuration**: *BN‹›* = new BN(31536000)

*Defined in [src/utils/constants.ts:96](https://github.com/ava-labs/avalanche.js/blob/a2feb77/src/utils/constants.ts#L96)*

###  maxSupply

• **maxSupply**: *BN‹›* = new BN(720000000).mul(ONEAVAX)

*Defined in [src/utils/constants.ts:97](https://github.com/ava-labs/avalanche.js/blob/a2feb77/src/utils/constants.ts#L97)*

###  minConsumption

• **minConsumption**: *number* = 0.1

*Defined in [src/utils/constants.ts:94](https://github.com/ava-labs/avalanche.js/blob/a2feb77/src/utils/constants.ts#L94)*

###  minStake

• **minStake**: *BN‹›* = ONEAVAX.mul(new BN(2000))

*Defined in [src/utils/constants.ts:98](https://github.com/ava-labs/avalanche.js/blob/a2feb77/src/utils/constants.ts#L98)*

###  vm

• **vm**: *string* = PChainVMName

*Defined in [src/utils/constants.ts:92](https://github.com/ava-labs/avalanche.js/blob/a2feb77/src/utils/constants.ts#L92)*

___

### `Const` n1X

### ▪ **n1X**: *object*

*Defined in [src/utils/constants.ts:82](https://github.com/ava-labs/avalanche.js/blob/a2feb77/src/utils/constants.ts#L82)*

###  alias

• **alias**: *string* = XChainAlias

*Defined in [src/utils/constants.ts:84](https://github.com/ava-labs/avalanche.js/blob/a2feb77/src/utils/constants.ts#L84)*

###  blockchainID

• **blockchainID**: *string* = "4ktRjsAKxgMr2aEzv9SWmrU7Xk5FniHUrVCX4P1TZSfTLZWFM"

*Defined in [src/utils/constants.ts:83](https://github.com/ava-labs/avalanche.js/blob/a2feb77/src/utils/constants.ts#L83)*

###  fee

• **fee**: *number* = 1000000

*Defined in [src/utils/constants.ts:86](https://github.com/ava-labs/avalanche.js/blob/a2feb77/src/utils/constants.ts#L86)*

###  vm

• **vm**: *string* = XChainVMName

*Defined in [src/utils/constants.ts:85](https://github.com/ava-labs/avalanche.js/blob/a2feb77/src/utils/constants.ts#L85)*

___

### `Const` n2C

### ▪ **n2C**: *object*

*Defined in [src/utils/constants.ts:129](https://github.com/ava-labs/avalanche.js/blob/a2feb77/src/utils/constants.ts#L129)*

###  alias

• **alias**: *string* = CChainAlias

*Defined in [src/utils/constants.ts:131](https://github.com/ava-labs/avalanche.js/blob/a2feb77/src/utils/constants.ts#L131)*

###  blockchainID

• **blockchainID**: *string* = "2mUYSXfLrDtigwbzj1LxKVsHwELghc5sisoXrzJwLqAAQHF4i"

*Defined in [src/utils/constants.ts:130](https://github.com/ava-labs/avalanche.js/blob/a2feb77/src/utils/constants.ts#L130)*

###  fee

• **fee**: *number* = 0

*Defined in [src/utils/constants.ts:133](https://github.com/ava-labs/avalanche.js/blob/a2feb77/src/utils/constants.ts#L133)*

###  vm

• **vm**: *string* = CChainVMName

*Defined in [src/utils/constants.ts:132](https://github.com/ava-labs/avalanche.js/blob/a2feb77/src/utils/constants.ts#L132)*

___

### `Const` n2P

### ▪ **n2P**: *object*

*Defined in [src/utils/constants.ts:117](https://github.com/ava-labs/avalanche.js/blob/a2feb77/src/utils/constants.ts#L117)*

###  alias

• **alias**: *string* = PChainAlias

*Defined in [src/utils/constants.ts:119](https://github.com/ava-labs/avalanche.js/blob/a2feb77/src/utils/constants.ts#L119)*

###  blockchainID

• **blockchainID**: *string* = PlatformChainID

*Defined in [src/utils/constants.ts:118](https://github.com/ava-labs/avalanche.js/blob/a2feb77/src/utils/constants.ts#L118)*

###  fee

• **fee**: *number* = 0

*Defined in [src/utils/constants.ts:121](https://github.com/ava-labs/avalanche.js/blob/a2feb77/src/utils/constants.ts#L121)*

###  maxConsumption

• **maxConsumption**: *number* = 0.12

*Defined in [src/utils/constants.ts:123](https://github.com/ava-labs/avalanche.js/blob/a2feb77/src/utils/constants.ts#L123)*

###  maxStakingDuration

• **maxStakingDuration**: *BN‹›* = new BN(31536000)

*Defined in [src/utils/constants.ts:124](https://github.com/ava-labs/avalanche.js/blob/a2feb77/src/utils/constants.ts#L124)*

###  maxSupply

• **maxSupply**: *BN‹›* = new BN(720000000).mul(ONEAVAX)

*Defined in [src/utils/constants.ts:125](https://github.com/ava-labs/avalanche.js/blob/a2feb77/src/utils/constants.ts#L125)*

###  minConsumption

• **minConsumption**: *number* = 0.1

*Defined in [src/utils/constants.ts:122](https://github.com/ava-labs/avalanche.js/blob/a2feb77/src/utils/constants.ts#L122)*

###  minStake

• **minStake**: *BN‹›* = ONEAVAX.mul(new BN(2000))

*Defined in [src/utils/constants.ts:126](https://github.com/ava-labs/avalanche.js/blob/a2feb77/src/utils/constants.ts#L126)*

###  vm

• **vm**: *string* = PChainVMName

*Defined in [src/utils/constants.ts:120](https://github.com/ava-labs/avalanche.js/blob/a2feb77/src/utils/constants.ts#L120)*

___

### `Const` n2X

### ▪ **n2X**: *object*

*Defined in [src/utils/constants.ts:110](https://github.com/ava-labs/avalanche.js/blob/a2feb77/src/utils/constants.ts#L110)*

###  alias

• **alias**: *string* = XChainAlias

*Defined in [src/utils/constants.ts:112](https://github.com/ava-labs/avalanche.js/blob/a2feb77/src/utils/constants.ts#L112)*

###  blockchainID

• **blockchainID**: *string* = "4ktRjsAKxgMr2aEzv9SWmrU7Xk5FniHUrVCX4P1TZSfTLZWFM"

*Defined in [src/utils/constants.ts:111](https://github.com/ava-labs/avalanche.js/blob/a2feb77/src/utils/constants.ts#L111)*

###  fee

• **fee**: *number* = 0

*Defined in [src/utils/constants.ts:114](https://github.com/ava-labs/avalanche.js/blob/a2feb77/src/utils/constants.ts#L114)*

###  vm

• **vm**: *string* = XChainVMName

*Defined in [src/utils/constants.ts:113](https://github.com/ava-labs/avalanche.js/blob/a2feb77/src/utils/constants.ts#L113)*

___

### `Const` n3C

### ▪ **n3C**: *object*

*Defined in [src/utils/constants.ts:155](https://github.com/ava-labs/avalanche.js/blob/a2feb77/src/utils/constants.ts#L155)*

###  alias

• **alias**: *string* = CChainAlias

*Defined in [src/utils/constants.ts:157](https://github.com/ava-labs/avalanche.js/blob/a2feb77/src/utils/constants.ts#L157)*

###  blockchainID

• **blockchainID**: *string* = "zJytnh96Pc8rM337bBrtMvJDbEdDNjcXG3WkTNCiLp18ergm9"

*Defined in [src/utils/constants.ts:156](https://github.com/ava-labs/avalanche.js/blob/a2feb77/src/utils/constants.ts#L156)*

###  fee

• **fee**: *number* = 0

*Defined in [src/utils/constants.ts:159](https://github.com/ava-labs/avalanche.js/blob/a2feb77/src/utils/constants.ts#L159)*

###  vm

• **vm**: *string* = CChainVMName

*Defined in [src/utils/constants.ts:158](https://github.com/ava-labs/avalanche.js/blob/a2feb77/src/utils/constants.ts#L158)*

___

### `Const` n3P

### ▪ **n3P**: *object*

*Defined in [src/utils/constants.ts:143](https://github.com/ava-labs/avalanche.js/blob/a2feb77/src/utils/constants.ts#L143)*

###  alias

• **alias**: *string* = PChainAlias

*Defined in [src/utils/constants.ts:145](https://github.com/ava-labs/avalanche.js/blob/a2feb77/src/utils/constants.ts#L145)*

###  blockchainID

• **blockchainID**: *string* = ""

*Defined in [src/utils/constants.ts:144](https://github.com/ava-labs/avalanche.js/blob/a2feb77/src/utils/constants.ts#L144)*

###  fee

• **fee**: *number* = 0

*Defined in [src/utils/constants.ts:147](https://github.com/ava-labs/avalanche.js/blob/a2feb77/src/utils/constants.ts#L147)*

###  maxConsumption

• **maxConsumption**: *number* = 0.12

*Defined in [src/utils/constants.ts:149](https://github.com/ava-labs/avalanche.js/blob/a2feb77/src/utils/constants.ts#L149)*

###  maxStakingDuration

• **maxStakingDuration**: *BN‹›* = new BN(31536000)

*Defined in [src/utils/constants.ts:150](https://github.com/ava-labs/avalanche.js/blob/a2feb77/src/utils/constants.ts#L150)*

###  maxSupply

• **maxSupply**: *BN‹›* = new BN(720000000).mul(ONEAVAX)

*Defined in [src/utils/constants.ts:151](https://github.com/ava-labs/avalanche.js/blob/a2feb77/src/utils/constants.ts#L151)*

###  minConsumption

• **minConsumption**: *number* = 0.1

*Defined in [src/utils/constants.ts:148](https://github.com/ava-labs/avalanche.js/blob/a2feb77/src/utils/constants.ts#L148)*

###  minStake

• **minStake**: *BN‹›* = ONEAVAX.mul(new BN(2000))

*Defined in [src/utils/constants.ts:152](https://github.com/ava-labs/avalanche.js/blob/a2feb77/src/utils/constants.ts#L152)*

###  vm

• **vm**: *string* = PChainVMName

*Defined in [src/utils/constants.ts:146](https://github.com/ava-labs/avalanche.js/blob/a2feb77/src/utils/constants.ts#L146)*

___

### `Const` n3X

### ▪ **n3X**: *object*

*Defined in [src/utils/constants.ts:136](https://github.com/ava-labs/avalanche.js/blob/a2feb77/src/utils/constants.ts#L136)*

###  alias

• **alias**: *string* = XChainAlias

*Defined in [src/utils/constants.ts:138](https://github.com/ava-labs/avalanche.js/blob/a2feb77/src/utils/constants.ts#L138)*

###  blockchainID

• **blockchainID**: *string* = "rrEWX7gc7D9mwcdrdBxBTdqh1a7WDVsMuadhTZgyXfFcRz45L"

*Defined in [src/utils/constants.ts:137](https://github.com/ava-labs/avalanche.js/blob/a2feb77/src/utils/constants.ts#L137)*

###  fee

• **fee**: *number* = 0

*Defined in [src/utils/constants.ts:140](https://github.com/ava-labs/avalanche.js/blob/a2feb77/src/utils/constants.ts#L140)*

###  vm

• **vm**: *string* = XChainVMName

*Defined in [src/utils/constants.ts:139](https://github.com/ava-labs/avalanche.js/blob/a2feb77/src/utils/constants.ts#L139)*

___

### `Const` n4C

### ▪ **n4C**: *object*

*Defined in [src/utils/constants.ts:182](https://github.com/ava-labs/avalanche.js/blob/a2feb77/src/utils/constants.ts#L182)*

###  alias

• **alias**: *string* = CChainAlias

*Defined in [src/utils/constants.ts:184](https://github.com/ava-labs/avalanche.js/blob/a2feb77/src/utils/constants.ts#L184)*

###  blockchainID

• **blockchainID**: *string* = "saMG5YgNsFxzjz4NMkEkt3bAH6hVxWdZkWcEnGB3Z15pcAmsK"

*Defined in [src/utils/constants.ts:183](https://github.com/ava-labs/avalanche.js/blob/a2feb77/src/utils/constants.ts#L183)*

###  fee

• **fee**: *BN‹›* = GWEI.mul(new BN(470))

*Defined in [src/utils/constants.ts:186](https://github.com/ava-labs/avalanche.js/blob/a2feb77/src/utils/constants.ts#L186)*

###  vm

• **vm**: *string* = CChainVMName

*Defined in [src/utils/constants.ts:185](https://github.com/ava-labs/avalanche.js/blob/a2feb77/src/utils/constants.ts#L185)*

___

### `Const` n4P

### ▪ **n4P**: *object*

*Defined in [src/utils/constants.ts:170](https://github.com/ava-labs/avalanche.js/blob/a2feb77/src/utils/constants.ts#L170)*

###  alias

• **alias**: *string* = PChainAlias

*Defined in [src/utils/constants.ts:172](https://github.com/ava-labs/avalanche.js/blob/a2feb77/src/utils/constants.ts#L172)*

###  blockchainID

• **blockchainID**: *string* = PlatformChainID

*Defined in [src/utils/constants.ts:171](https://github.com/ava-labs/avalanche.js/blob/a2feb77/src/utils/constants.ts#L171)*

###  fee

• **fee**: *number* = 1000000

*Defined in [src/utils/constants.ts:174](https://github.com/ava-labs/avalanche.js/blob/a2feb77/src/utils/constants.ts#L174)*

###  maxConsumption

• **maxConsumption**: *number* = 0.12

*Defined in [src/utils/constants.ts:176](https://github.com/ava-labs/avalanche.js/blob/a2feb77/src/utils/constants.ts#L176)*

###  maxStakingDuration

• **maxStakingDuration**: *BN‹›* = new BN(31536000)

*Defined in [src/utils/constants.ts:177](https://github.com/ava-labs/avalanche.js/blob/a2feb77/src/utils/constants.ts#L177)*

###  maxSupply

• **maxSupply**: *BN‹›* = new BN(720000000).mul(ONEAVAX)

*Defined in [src/utils/constants.ts:178](https://github.com/ava-labs/avalanche.js/blob/a2feb77/src/utils/constants.ts#L178)*

###  minConsumption

• **minConsumption**: *number* = 0.1

*Defined in [src/utils/constants.ts:175](https://github.com/ava-labs/avalanche.js/blob/a2feb77/src/utils/constants.ts#L175)*

###  minStake

• **minStake**: *BN‹›* = ONEAVAX.mul(new BN(2000))

*Defined in [src/utils/constants.ts:179](https://github.com/ava-labs/avalanche.js/blob/a2feb77/src/utils/constants.ts#L179)*

###  vm

• **vm**: *string* = PChainVMName

*Defined in [src/utils/constants.ts:173](https://github.com/ava-labs/avalanche.js/blob/a2feb77/src/utils/constants.ts#L173)*

___

### `Const` n4X

### ▪ **n4X**: *object*

*Defined in [src/utils/constants.ts:163](https://github.com/ava-labs/avalanche.js/blob/a2feb77/src/utils/constants.ts#L163)*

###  alias

• **alias**: *string* = XChainAlias

*Defined in [src/utils/constants.ts:165](https://github.com/ava-labs/avalanche.js/blob/a2feb77/src/utils/constants.ts#L165)*

###  blockchainID

• **blockchainID**: *string* = "jnUjZSRt16TcRnZzmh5aMhavwVHz3zBrSN8GfFMTQkzUnoBxC"

*Defined in [src/utils/constants.ts:164](https://github.com/ava-labs/avalanche.js/blob/a2feb77/src/utils/constants.ts#L164)*

###  fee

• **fee**: *number* = 1000000

*Defined in [src/utils/constants.ts:167](https://github.com/ava-labs/avalanche.js/blob/a2feb77/src/utils/constants.ts#L167)*

###  vm

• **vm**: *string* = XChainVMName

*Defined in [src/utils/constants.ts:166](https://github.com/ava-labs/avalanche.js/blob/a2feb77/src/utils/constants.ts#L166)*
