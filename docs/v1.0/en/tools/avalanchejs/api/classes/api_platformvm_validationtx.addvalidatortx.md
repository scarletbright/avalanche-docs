[avalanche](../README.md) › [API-PlatformVM-ValidationTx](../modules/api_platformvm_validationtx.md) › [AddValidatorTx](api_platformvm_validationtx.addvalidatortx.md)

# Class: AddValidatorTx

## Hierarchy

  ↳ [AddDelegatorTx](api_platformvm_validationtx.adddelegatortx.md)

  ↳ **AddValidatorTx**

## Index

### Constructors

* [constructor](api_platformvm_validationtx.addvalidatortx.md#constructor)

### Properties

* [blockchainid](api_platformvm_validationtx.addvalidatortx.md#protected-blockchainid)
* [delegationFee](api_platformvm_validationtx.addvalidatortx.md#protected-delegationfee)
* [endTime](api_platformvm_validationtx.addvalidatortx.md#protected-endtime)
* [ins](api_platformvm_validationtx.addvalidatortx.md#protected-ins)
* [memo](api_platformvm_validationtx.addvalidatortx.md#protected-memo)
* [networkid](api_platformvm_validationtx.addvalidatortx.md#protected-networkid)
* [nodeID](api_platformvm_validationtx.addvalidatortx.md#protected-nodeid)
* [numins](api_platformvm_validationtx.addvalidatortx.md#protected-numins)
* [numouts](api_platformvm_validationtx.addvalidatortx.md#protected-numouts)
* [outs](api_platformvm_validationtx.addvalidatortx.md#protected-outs)
* [rewardOwners](api_platformvm_validationtx.addvalidatortx.md#protected-rewardowners)
* [stakeOuts](api_platformvm_validationtx.addvalidatortx.md#protected-stakeouts)
* [startTime](api_platformvm_validationtx.addvalidatortx.md#protected-starttime)
* [weight](api_platformvm_validationtx.addvalidatortx.md#protected-weight)
* [delegatorMultiplier](api_platformvm_validationtx.addvalidatortx.md#static-private-delegatormultiplier)

### Methods

* [clone](api_platformvm_validationtx.addvalidatortx.md#clone)
* [create](api_platformvm_validationtx.addvalidatortx.md#create)
* [fromBuffer](api_platformvm_validationtx.addvalidatortx.md#frombuffer)
* [getBlockchainID](api_platformvm_validationtx.addvalidatortx.md#getblockchainid)
* [getDelegationFee](api_platformvm_validationtx.addvalidatortx.md#getdelegationfee)
* [getDelegationFeeBuffer](api_platformvm_validationtx.addvalidatortx.md#getdelegationfeebuffer)
* [getEndTime](api_platformvm_validationtx.addvalidatortx.md#getendtime)
* [getIns](api_platformvm_validationtx.addvalidatortx.md#getins)
* [getMemo](api_platformvm_validationtx.addvalidatortx.md#getmemo)
* [getNetworkID](api_platformvm_validationtx.addvalidatortx.md#getnetworkid)
* [getNodeID](api_platformvm_validationtx.addvalidatortx.md#getnodeid)
* [getNodeIDString](api_platformvm_validationtx.addvalidatortx.md#getnodeidstring)
* [getOuts](api_platformvm_validationtx.addvalidatortx.md#getouts)
* [getRewardOwners](api_platformvm_validationtx.addvalidatortx.md#getrewardowners)
* [getStakeAmount](api_platformvm_validationtx.addvalidatortx.md#getstakeamount)
* [getStakeAmountBuffer](api_platformvm_validationtx.addvalidatortx.md#getstakeamountbuffer)
* [getStakeOuts](api_platformvm_validationtx.addvalidatortx.md#getstakeouts)
* [getStakeOutsTotal](api_platformvm_validationtx.addvalidatortx.md#getstakeoutstotal)
* [getStartTime](api_platformvm_validationtx.addvalidatortx.md#getstarttime)
* [getTotalOuts](api_platformvm_validationtx.addvalidatortx.md#gettotalouts)
* [getTxType](api_platformvm_validationtx.addvalidatortx.md#gettxtype)
* [getWeight](api_platformvm_validationtx.addvalidatortx.md#getweight)
* [getWeightBuffer](api_platformvm_validationtx.addvalidatortx.md#getweightbuffer)
* [select](api_platformvm_validationtx.addvalidatortx.md#select)
* [sign](api_platformvm_validationtx.addvalidatortx.md#sign)
* [toBuffer](api_platformvm_validationtx.addvalidatortx.md#tobuffer)
* [toString](api_platformvm_validationtx.addvalidatortx.md#tostring)

## Constructors

###  constructor

\+ **new AddValidatorTx**(`networkid`: number, `blockchainid`: Buffer, `outs`: Array‹[TransferableOutput](api_platformvm_outputs.transferableoutput.md)›, `ins`: Array‹[TransferableInput](api_platformvm_inputs.transferableinput.md)›, `memo`: Buffer, `nodeID`: Buffer, `startTime`: BN, `endTime`: BN, `stakeAmount`: BN, `stakeOuts`: Array‹[TransferableOutput](api_platformvm_outputs.transferableoutput.md)›, `rewardOwners`: [ParseableOutput](api_platformvm_outputs.parseableoutput.md), `delegationFee`: number): *[AddValidatorTx](api_platformvm_validationtx.addvalidatortx.md)*

*Overrides [AddDelegatorTx](api_platformvm_validationtx.adddelegatortx.md).[constructor](api_platformvm_validationtx.adddelegatortx.md#constructor)*

*Defined in [src/apis/platformvm/validationtx.ts:460](https://github.com/ava-labs/avalanchejs/blob/a2feb77/src/apis/platformvm/validationtx.ts#L460)*

Class representing an unsigned AddValidatorTx transaction.

**Parameters:**

Name | Type | Default | Description |
------ | ------ | ------ | ------ |
`networkid` | number | DefaultNetworkID | Optional. Networkid, [DefaultNetworkID](../modules/utils_constants.md#const-defaultnetworkid) |
`blockchainid` | Buffer | Buffer.alloc(32, 16) | Optional. Blockchainid, default Buffer.alloc(32, 16) |
`outs` | Array‹[TransferableOutput](api_platformvm_outputs.transferableoutput.md)› | undefined | Optional. Array of the [TransferableOutput](api_avm_outputs.transferableoutput.md)s |
`ins` | Array‹[TransferableInput](api_platformvm_inputs.transferableinput.md)› | undefined | Optional. Array of the [TransferableInput](api_avm_inputs.transferableinput.md)s |
`memo` | Buffer | undefined | Optional. [Buffer](https://github.com/feross/buffer) for the memo field |
`nodeID` | Buffer | undefined | Optional. The node ID of the validator being added. |
`startTime` | BN | undefined | Optional. The Unix time when the validator starts validating the Primary Network. |
`endTime` | BN | undefined | Optional. The Unix time when the validator stops validating the Primary Network (and staked AVAX is returned). |
`stakeAmount` | BN | undefined | Optional. The amount of nAVAX the validator is staking. |
`stakeOuts` | Array‹[TransferableOutput](api_platformvm_outputs.transferableoutput.md)› | undefined | Optional. The outputs used in paying the stake. |
`rewardOwners` | [ParseableOutput](api_platformvm_outputs.parseableoutput.md) | undefined | Optional. The [ParseableOutput](api_platformvm_outputs.parseableoutput.md) containing the [SECPOwnerOutput](api_platformvm_outputs.secpowneroutput.md) for the rewards. |
`delegationFee` | number | undefined | Optional. The percent fee this validator charges when others delegate stake to them. Up to 4 decimal places allowed; additional decimal places are ignored. Must be between 0 and 100, inclusive. For example, if delegationFeeRate is 1.2345 and someone delegates to this validator, then when the delegation period is over, 1.2345% of the reward goes to the validator and the rest goes to the delegator.  |

**Returns:** *[AddValidatorTx](api_platformvm_validationtx.addvalidatortx.md)*

## Properties

### `Protected` blockchainid

• **blockchainid**: *Buffer* = Buffer.alloc(32)

*Inherited from [StandardBaseTx](common_transactions.standardbasetx.md).[blockchainid](common_transactions.standardbasetx.md#protected-blockchainid)*

*Defined in [src/common/tx.ts:24](https://github.com/ava-labs/avalanchejs/blob/a2feb77/src/common/tx.ts#L24)*

___

### `Protected` delegationFee

• **delegationFee**: *number* = 0

*Defined in [src/apis/platformvm/validationtx.ts:421](https://github.com/ava-labs/avalanchejs/blob/a2feb77/src/apis/platformvm/validationtx.ts#L421)*

___

### `Protected` endTime

• **endTime**: *Buffer* = Buffer.alloc(8)

*Inherited from [ValidatorTx](api_platformvm_validationtx.validatortx.md).[endTime](api_platformvm_validationtx.validatortx.md#protected-endtime)*

*Defined in [src/apis/platformvm/validationtx.ts:28](https://github.com/ava-labs/avalanchejs/blob/a2feb77/src/apis/platformvm/validationtx.ts#L28)*

___

### `Protected` ins

• **ins**: *Array‹[StandardTransferableInput](common_inputs.standardtransferableinput.md)›*

*Inherited from [StandardBaseTx](common_transactions.standardbasetx.md).[ins](common_transactions.standardbasetx.md#protected-ins)*

*Defined in [src/common/tx.ts:28](https://github.com/ava-labs/avalanchejs/blob/a2feb77/src/common/tx.ts#L28)*

___

### `Protected` memo

• **memo**: *Buffer* = Buffer.alloc(4)

*Inherited from [StandardBaseTx](common_transactions.standardbasetx.md).[memo](common_transactions.standardbasetx.md#protected-memo)*

*Defined in [src/common/tx.ts:29](https://github.com/ava-labs/avalanchejs/blob/a2feb77/src/common/tx.ts#L29)*

___

### `Protected` networkid

• **networkid**: *Buffer* = Buffer.alloc(4)

*Inherited from [StandardBaseTx](common_transactions.standardbasetx.md).[networkid](common_transactions.standardbasetx.md#protected-networkid)*

*Defined in [src/common/tx.ts:23](https://github.com/ava-labs/avalanchejs/blob/a2feb77/src/common/tx.ts#L23)*

___

### `Protected` nodeID

• **nodeID**: *Buffer* = Buffer.alloc(20)

*Inherited from [ValidatorTx](api_platformvm_validationtx.validatortx.md).[nodeID](api_platformvm_validationtx.validatortx.md#protected-nodeid)*

*Defined in [src/apis/platformvm/validationtx.ts:26](https://github.com/ava-labs/avalanchejs/blob/a2feb77/src/apis/platformvm/validationtx.ts#L26)*

___

### `Protected` numins

• **numins**: *Buffer* = Buffer.alloc(4)

*Inherited from [StandardBaseTx](common_transactions.standardbasetx.md).[numins](common_transactions.standardbasetx.md#protected-numins)*

*Defined in [src/common/tx.ts:27](https://github.com/ava-labs/avalanchejs/blob/a2feb77/src/common/tx.ts#L27)*

___

### `Protected` numouts

• **numouts**: *Buffer* = Buffer.alloc(4)

*Inherited from [StandardBaseTx](common_transactions.standardbasetx.md).[numouts](common_transactions.standardbasetx.md#protected-numouts)*

*Defined in [src/common/tx.ts:25](https://github.com/ava-labs/avalanchejs/blob/a2feb77/src/common/tx.ts#L25)*

___

### `Protected` outs

• **outs**: *Array‹[StandardTransferableOutput](common_output.standardtransferableoutput.md)›*

*Inherited from [StandardBaseTx](common_transactions.standardbasetx.md).[outs](common_transactions.standardbasetx.md#protected-outs)*

*Defined in [src/common/tx.ts:26](https://github.com/ava-labs/avalanchejs/blob/a2feb77/src/common/tx.ts#L26)*

___

### `Protected` rewardOwners

• **rewardOwners**: *[ParseableOutput](api_platformvm_outputs.parseableoutput.md)* = undefined

*Inherited from [AddDelegatorTx](api_platformvm_validationtx.adddelegatortx.md).[rewardOwners](api_platformvm_validationtx.adddelegatortx.md#protected-rewardowners)*

*Defined in [src/apis/platformvm/validationtx.ts:282](https://github.com/ava-labs/avalanchejs/blob/a2feb77/src/apis/platformvm/validationtx.ts#L282)*

___

### `Protected` stakeOuts

• **stakeOuts**: *Array‹[TransferableOutput](api_platformvm_outputs.transferableoutput.md)›* = []

*Inherited from [AddDelegatorTx](api_platformvm_validationtx.adddelegatortx.md).[stakeOuts](api_platformvm_validationtx.adddelegatortx.md#protected-stakeouts)*

*Defined in [src/apis/platformvm/validationtx.ts:281](https://github.com/ava-labs/avalanchejs/blob/a2feb77/src/apis/platformvm/validationtx.ts#L281)*

___

### `Protected` startTime

• **startTime**: *Buffer* = Buffer.alloc(8)

*Inherited from [ValidatorTx](api_platformvm_validationtx.validatortx.md).[startTime](api_platformvm_validationtx.validatortx.md#protected-starttime)*

*Defined in [src/apis/platformvm/validationtx.ts:27](https://github.com/ava-labs/avalanchejs/blob/a2feb77/src/apis/platformvm/validationtx.ts#L27)*

___

### `Protected` weight

• **weight**: *Buffer* = Buffer.alloc(8)

*Inherited from [WeightedValidatorTx](api_platformvm_validationtx.weightedvalidatortx.md).[weight](api_platformvm_validationtx.weightedvalidatortx.md#protected-weight)*

*Defined in [src/apis/platformvm/validationtx.ts:102](https://github.com/ava-labs/avalanchejs/blob/a2feb77/src/apis/platformvm/validationtx.ts#L102)*

___

### `Static` `Private` delegatorMultiplier

▪ **delegatorMultiplier**: *number* = 10000

*Defined in [src/apis/platformvm/validationtx.ts:422](https://github.com/ava-labs/avalanchejs/blob/a2feb77/src/apis/platformvm/validationtx.ts#L422)*

## Methods

###  clone

▸ **clone**(): *this*

*Inherited from [AddDelegatorTx](api_platformvm_validationtx.adddelegatortx.md).[clone](api_platformvm_validationtx.adddelegatortx.md#clone)*

*Overrides [BaseTx](api_platformvm_basetx.basetx.md).[clone](api_platformvm_basetx.basetx.md#clone)*

*Defined in [src/apis/platformvm/validationtx.ts:373](https://github.com/ava-labs/avalanchejs/blob/a2feb77/src/apis/platformvm/validationtx.ts#L373)*

**Returns:** *this*

___

###  create

▸ **create**(...`args`: any[]): *this*

*Inherited from [AddDelegatorTx](api_platformvm_validationtx.adddelegatortx.md).[create](api_platformvm_validationtx.adddelegatortx.md#create)*

*Overrides [BaseTx](api_platformvm_basetx.basetx.md).[create](api_platformvm_basetx.basetx.md#create)*

*Defined in [src/apis/platformvm/validationtx.ts:379](https://github.com/ava-labs/avalanchejs/blob/a2feb77/src/apis/platformvm/validationtx.ts#L379)*

**Parameters:**

Name | Type |
------ | ------ |
`...args` | any[] |

**Returns:** *this*

___

###  fromBuffer

▸ **fromBuffer**(`bytes`: Buffer, `offset`: number): *number*

*Overrides [AddDelegatorTx](api_platformvm_validationtx.adddelegatortx.md).[fromBuffer](api_platformvm_validationtx.adddelegatortx.md#frombuffer)*

*Defined in [src/apis/platformvm/validationtx.ts:448](https://github.com/ava-labs/avalanchejs/blob/a2feb77/src/apis/platformvm/validationtx.ts#L448)*

**Parameters:**

Name | Type | Default |
------ | ------ | ------ |
`bytes` | Buffer | - |
`offset` | number | 0 |

**Returns:** *number*

___

###  getBlockchainID

▸ **getBlockchainID**(): *Buffer*

*Inherited from [StandardBaseTx](common_transactions.standardbasetx.md).[getBlockchainID](common_transactions.standardbasetx.md#getblockchainid)*

*Defined in [src/common/tx.ts:44](https://github.com/ava-labs/avalanchejs/blob/a2feb77/src/common/tx.ts#L44)*

Returns the Buffer representation of the BlockchainID

**Returns:** *Buffer*

___

###  getDelegationFee

▸ **getDelegationFee**(): *number*

*Defined in [src/apis/platformvm/validationtx.ts:434](https://github.com/ava-labs/avalanchejs/blob/a2feb77/src/apis/platformvm/validationtx.ts#L434)*

Returns the delegation fee (represents a percentage from 0 to 100);

**Returns:** *number*

___

###  getDelegationFeeBuffer

▸ **getDelegationFeeBuffer**(): *Buffer*

*Defined in [src/apis/platformvm/validationtx.ts:441](https://github.com/ava-labs/avalanchejs/blob/a2feb77/src/apis/platformvm/validationtx.ts#L441)*

Returns the binary representation of the delegation fee as a [Buffer](https://github.com/feross/buffer).

**Returns:** *Buffer*

___

###  getEndTime

▸ **getEndTime**(): *BN‹›*

*Inherited from [ValidatorTx](api_platformvm_validationtx.validatortx.md).[getEndTime](api_platformvm_validationtx.validatortx.md#getendtime)*

*Defined in [src/apis/platformvm/validationtx.ts:53](https://github.com/ava-labs/avalanchejs/blob/a2feb77/src/apis/platformvm/validationtx.ts#L53)*

Returns a [BN](https://github.com/indutny/bn.js/) for the stake amount.

**Returns:** *BN‹›*

___

###  getIns

▸ **getIns**(): *Array‹[StandardTransferableInput](common_inputs.standardtransferableinput.md)›*

*Inherited from [StandardBaseTx](common_transactions.standardbasetx.md).[getIns](common_transactions.standardbasetx.md#getins)*

*Defined in [src/common/tx.ts:49](https://github.com/ava-labs/avalanchejs/blob/a2feb77/src/common/tx.ts#L49)*

Returns the array of [StandardTransferableInput](common_inputs.standardtransferableinput.md)s

**Returns:** *Array‹[StandardTransferableInput](common_inputs.standardtransferableinput.md)›*

___

###  getMemo

▸ **getMemo**(): *Buffer*

*Inherited from [StandardBaseTx](common_transactions.standardbasetx.md).[getMemo](common_transactions.standardbasetx.md#getmemo)*

*Defined in [src/common/tx.ts:64](https://github.com/ava-labs/avalanchejs/blob/a2feb77/src/common/tx.ts#L64)*

Returns the [Buffer](https://github.com/feross/buffer) representation of the memo

**Returns:** *Buffer*

___

###  getNetworkID

▸ **getNetworkID**(): *number*

*Inherited from [StandardBaseTx](common_transactions.standardbasetx.md).[getNetworkID](common_transactions.standardbasetx.md#getnetworkid)*

*Defined in [src/common/tx.ts:39](https://github.com/ava-labs/avalanchejs/blob/a2feb77/src/common/tx.ts#L39)*

Returns the NetworkID as a number

**Returns:** *number*

___

###  getNodeID

▸ **getNodeID**(): *Buffer*

*Inherited from [ValidatorTx](api_platformvm_validationtx.validatortx.md).[getNodeID](api_platformvm_validationtx.validatortx.md#getnodeid)*

*Defined in [src/apis/platformvm/validationtx.ts:33](https://github.com/ava-labs/avalanchejs/blob/a2feb77/src/apis/platformvm/validationtx.ts#L33)*

Returns a [Buffer](https://github.com/feross/buffer) for the stake amount.

**Returns:** *Buffer*

___

###  getNodeIDString

▸ **getNodeIDString**(): *string*

*Inherited from [ValidatorTx](api_platformvm_validationtx.validatortx.md).[getNodeIDString](api_platformvm_validationtx.validatortx.md#getnodeidstring)*

*Defined in [src/apis/platformvm/validationtx.ts:40](https://github.com/ava-labs/avalanchejs/blob/a2feb77/src/apis/platformvm/validationtx.ts#L40)*

Returns a string for the nodeID amount.

**Returns:** *string*

___

###  getOuts

▸ **getOuts**(): *Array‹[StandardTransferableOutput](common_output.standardtransferableoutput.md)›*

*Inherited from [StandardBaseTx](common_transactions.standardbasetx.md).[getOuts](common_transactions.standardbasetx.md#getouts)*

*Defined in [src/common/tx.ts:54](https://github.com/ava-labs/avalanchejs/blob/a2feb77/src/common/tx.ts#L54)*

Returns the array of [StandardTransferableOutput](common_output.standardtransferableoutput.md)s

**Returns:** *Array‹[StandardTransferableOutput](common_output.standardtransferableoutput.md)›*

___

###  getRewardOwners

▸ **getRewardOwners**(): *[ParseableOutput](api_platformvm_outputs.parseableoutput.md)*

*Inherited from [AddDelegatorTx](api_platformvm_validationtx.adddelegatortx.md).[getRewardOwners](api_platformvm_validationtx.adddelegatortx.md#getrewardowners)*

*Defined in [src/apis/platformvm/validationtx.ts:326](https://github.com/ava-labs/avalanchejs/blob/a2feb77/src/apis/platformvm/validationtx.ts#L326)*

Returns a [Buffer](https://github.com/feross/buffer) for the reward address.

**Returns:** *[ParseableOutput](api_platformvm_outputs.parseableoutput.md)*

___

###  getStakeAmount

▸ **getStakeAmount**(): *BN*

*Inherited from [AddDelegatorTx](api_platformvm_validationtx.adddelegatortx.md).[getStakeAmount](api_platformvm_validationtx.adddelegatortx.md#getstakeamount)*

*Defined in [src/apis/platformvm/validationtx.ts:294](https://github.com/ava-labs/avalanchejs/blob/a2feb77/src/apis/platformvm/validationtx.ts#L294)*

Returns a [BN](https://github.com/indutny/bn.js/) for the stake amount.

**Returns:** *BN*

___

###  getStakeAmountBuffer

▸ **getStakeAmountBuffer**(): *Buffer*

*Inherited from [AddDelegatorTx](api_platformvm_validationtx.adddelegatortx.md).[getStakeAmountBuffer](api_platformvm_validationtx.adddelegatortx.md#getstakeamountbuffer)*

*Defined in [src/apis/platformvm/validationtx.ts:301](https://github.com/ava-labs/avalanchejs/blob/a2feb77/src/apis/platformvm/validationtx.ts#L301)*

Returns a [Buffer](https://github.com/feross/buffer) for the stake amount.

**Returns:** *Buffer*

___

###  getStakeOuts

▸ **getStakeOuts**(): *Array‹[TransferableOutput](api_platformvm_outputs.transferableoutput.md)›*

*Inherited from [AddDelegatorTx](api_platformvm_validationtx.adddelegatortx.md).[getStakeOuts](api_platformvm_validationtx.adddelegatortx.md#getstakeouts)*

*Defined in [src/apis/platformvm/validationtx.ts:308](https://github.com/ava-labs/avalanchejs/blob/a2feb77/src/apis/platformvm/validationtx.ts#L308)*

Returns the array of outputs being staked.

**Returns:** *Array‹[TransferableOutput](api_platformvm_outputs.transferableoutput.md)›*

___

###  getStakeOutsTotal

▸ **getStakeOutsTotal**(): *BN*

*Inherited from [AddDelegatorTx](api_platformvm_validationtx.adddelegatortx.md).[getStakeOutsTotal](api_platformvm_validationtx.adddelegatortx.md#getstakeoutstotal)*

*Defined in [src/apis/platformvm/validationtx.ts:315](https://github.com/ava-labs/avalanchejs/blob/a2feb77/src/apis/platformvm/validationtx.ts#L315)*

Should match stakeAmount. Used in sanity checking.

**Returns:** *BN*

___

###  getStartTime

▸ **getStartTime**(): *BN‹›*

*Inherited from [ValidatorTx](api_platformvm_validationtx.validatortx.md).[getStartTime](api_platformvm_validationtx.validatortx.md#getstarttime)*

*Defined in [src/apis/platformvm/validationtx.ts:46](https://github.com/ava-labs/avalanchejs/blob/a2feb77/src/apis/platformvm/validationtx.ts#L46)*

Returns a [BN](https://github.com/indutny/bn.js/) for the stake amount.

**Returns:** *BN‹›*

___

###  getTotalOuts

▸ **getTotalOuts**(): *Array‹[TransferableOutput](api_platformvm_outputs.transferableoutput.md)›*

*Inherited from [AddDelegatorTx](api_platformvm_validationtx.adddelegatortx.md).[getTotalOuts](api_platformvm_validationtx.adddelegatortx.md#gettotalouts)*

*Overrides [BaseTx](api_platformvm_basetx.basetx.md).[getTotalOuts](api_platformvm_basetx.basetx.md#gettotalouts)*

*Defined in [src/apis/platformvm/validationtx.ts:330](https://github.com/ava-labs/avalanchejs/blob/a2feb77/src/apis/platformvm/validationtx.ts#L330)*

**Returns:** *Array‹[TransferableOutput](api_platformvm_outputs.transferableoutput.md)›*

___

###  getTxType

▸ **getTxType**(): *number*

*Overrides [AddDelegatorTx](api_platformvm_validationtx.adddelegatortx.md).[getTxType](api_platformvm_validationtx.adddelegatortx.md#gettxtype)*

*Defined in [src/apis/platformvm/validationtx.ts:427](https://github.com/ava-labs/avalanchejs/blob/a2feb77/src/apis/platformvm/validationtx.ts#L427)*

Returns the id of the [AddDelegatorTx](api_platformvm_validationtx.adddelegatortx.md)

**Returns:** *number*

___

###  getWeight

▸ **getWeight**(): *BN*

*Inherited from [WeightedValidatorTx](api_platformvm_validationtx.weightedvalidatortx.md).[getWeight](api_platformvm_validationtx.weightedvalidatortx.md#getweight)*

*Defined in [src/apis/platformvm/validationtx.ts:107](https://github.com/ava-labs/avalanchejs/blob/a2feb77/src/apis/platformvm/validationtx.ts#L107)*

Returns a [BN](https://github.com/indutny/bn.js/) for the stake amount.

**Returns:** *BN*

___

###  getWeightBuffer

▸ **getWeightBuffer**(): *Buffer*

*Inherited from [WeightedValidatorTx](api_platformvm_validationtx.weightedvalidatortx.md).[getWeightBuffer](api_platformvm_validationtx.weightedvalidatortx.md#getweightbuffer)*

*Defined in [src/apis/platformvm/validationtx.ts:114](https://github.com/ava-labs/avalanchejs/blob/a2feb77/src/apis/platformvm/validationtx.ts#L114)*

Returns a [Buffer](https://github.com/feross/buffer) for the stake amount.

**Returns:** *Buffer*

___

###  select

▸ **select**(`id`: number, ...`args`: any[]): *this*

*Inherited from [BaseTx](api_platformvm_basetx.basetx.md).[select](api_platformvm_basetx.basetx.md#select)*

*Overrides [StandardBaseTx](common_transactions.standardbasetx.md).[select](common_transactions.standardbasetx.md#abstract-select)*

*Defined in [src/apis/platformvm/basetx.ts:112](https://github.com/ava-labs/avalanchejs/blob/a2feb77/src/apis/platformvm/basetx.ts#L112)*

**Parameters:**

Name | Type |
------ | ------ |
`id` | number |
`...args` | any[] |

**Returns:** *this*

___

###  sign

▸ **sign**(`msg`: Buffer, `kc`: [KeyChain](api_platformvm_keychain.keychain.md)): *Array‹[Credential](common_signature.credential.md)›*

*Inherited from [BaseTx](api_platformvm_basetx.basetx.md).[sign](api_platformvm_basetx.basetx.md#sign)*

*Overrides [StandardBaseTx](common_transactions.standardbasetx.md).[sign](common_transactions.standardbasetx.md#abstract-sign)*

*Defined in [src/apis/platformvm/basetx.ts:85](https://github.com/ava-labs/avalanchejs/blob/a2feb77/src/apis/platformvm/basetx.ts#L85)*

Takes the bytes of an [UnsignedTx](api_avm_transactions.unsignedtx.md) and returns an array of [Credential](common_signature.credential.md)s

**Parameters:**

Name | Type | Description |
------ | ------ | ------ |
`msg` | Buffer | A Buffer for the [UnsignedTx](api_avm_transactions.unsignedtx.md) |
`kc` | [KeyChain](api_platformvm_keychain.keychain.md) | An [KeyChain](api_avm_keychain.keychain.md) used in signing  |

**Returns:** *Array‹[Credential](common_signature.credential.md)›*

An array of [Credential](common_signature.credential.md)s

___

###  toBuffer

▸ **toBuffer**(): *Buffer*

*Overrides [AddDelegatorTx](api_platformvm_validationtx.adddelegatortx.md).[toBuffer](api_platformvm_validationtx.adddelegatortx.md#tobuffer)*

*Defined in [src/apis/platformvm/validationtx.ts:456](https://github.com/ava-labs/avalanchejs/blob/a2feb77/src/apis/platformvm/validationtx.ts#L456)*

**Returns:** *Buffer*

___

###  toString

▸ **toString**(): *string*

*Inherited from [StandardBaseTx](common_transactions.standardbasetx.md).[toString](common_transactions.standardbasetx.md#tostring)*

*Defined in [src/common/tx.ts:101](https://github.com/ava-labs/avalanchejs/blob/a2feb77/src/common/tx.ts#L101)*

Returns a base-58 representation of the [StandardBaseTx](common_transactions.standardbasetx.md).

**Returns:** *string*
