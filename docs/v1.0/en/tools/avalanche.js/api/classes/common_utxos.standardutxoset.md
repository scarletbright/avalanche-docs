[avalanche](../README.md) › [Common-UTXOs](../modules/common_utxos.md) › [StandardUTXOSet](common_utxos.standardutxoset.md)

# Class: StandardUTXOSet ‹**UTXOClass**›

Class representing a set of [StandardUTXO](common_utxos.standardutxo.md)s.

## Type parameters

▪ **UTXOClass**: *[StandardUTXO](common_utxos.standardutxo.md)*

## Hierarchy

* **StandardUTXOSet**

  ↳ [UTXOSet](api_avm_utxos.utxoset.md)

  ↳ [UTXOSet](api_platformvm_utxos.utxoset.md)

## Index

### Properties

* [addressUTXOs](common_utxos.standardutxoset.md#protected-addressutxos)
* [utxos](common_utxos.standardutxoset.md#protected-utxos)

### Methods

* [add](common_utxos.standardutxoset.md#add)
* [addArray](common_utxos.standardutxoset.md#addarray)
* [clone](common_utxos.standardutxoset.md#abstract-clone)
* [create](common_utxos.standardutxoset.md#abstract-create)
* [difference](common_utxos.standardutxoset.md#difference)
* [filter](common_utxos.standardutxoset.md#filter)
* [getAddresses](common_utxos.standardutxoset.md#getaddresses)
* [getAllUTXOStrings](common_utxos.standardutxoset.md#getallutxostrings)
* [getAllUTXOs](common_utxos.standardutxoset.md#getallutxos)
* [getAssetIDs](common_utxos.standardutxoset.md#getassetids)
* [getBalance](common_utxos.standardutxoset.md#getbalance)
* [getUTXO](common_utxos.standardutxoset.md#getutxo)
* [getUTXOIDs](common_utxos.standardutxoset.md#getutxoids)
* [includes](common_utxos.standardutxoset.md#includes)
* [intersection](common_utxos.standardutxoset.md#intersection)
* [merge](common_utxos.standardutxoset.md#merge)
* [mergeByRule](common_utxos.standardutxoset.md#mergebyrule)
* [parseUTXO](common_utxos.standardutxoset.md#abstract-parseutxo)
* [remove](common_utxos.standardutxoset.md#remove)
* [removeArray](common_utxos.standardutxoset.md#removearray)
* [symDifference](common_utxos.standardutxoset.md#symdifference)
* [union](common_utxos.standardutxoset.md#union)

## Properties

### `Protected` addressUTXOs

• **addressUTXOs**: *object*

*Defined in [src/common/utxos.ts:147](https://github.com/ava-labs/avalanche.js/blob/a2feb77/src/common/utxos.ts#L147)*

#### Type declaration:

* \[ **address**: *string*\]: object

* \[ **utxoid**: *string*\]: BN

___

### `Protected` utxos

• **utxos**: *object*

*Defined in [src/common/utxos.ts:145](https://github.com/ava-labs/avalanche.js/blob/a2feb77/src/common/utxos.ts#L145)*

#### Type declaration:

* \[ **utxoid**: *string*\]: UTXOClass

## Methods

###  add

▸ **add**(`utxo`: UTXOClass | string, `overwrite`: boolean): *UTXOClass*

*Defined in [src/common/utxos.ts:181](https://github.com/ava-labs/avalanche.js/blob/a2feb77/src/common/utxos.ts#L181)*

Adds a [StandardUTXO](common_utxos.standardutxo.md) to the StandardUTXOSet.

**Parameters:**

Name | Type | Default | Description |
------ | ------ | ------ | ------ |
`utxo` | UTXOClass &#124; string | - | Either a [StandardUTXO](common_utxos.standardutxo.md) an cb58 serialized string representing a StandardUTXO |
`overwrite` | boolean | false | If true, if the UTXOID already exists, overwrite it... default false  |

**Returns:** *UTXOClass*

A [StandardUTXO](common_utxos.standardutxo.md) if one was added and undefined if nothing was added.

___

###  addArray

▸ **addArray**(`utxos`: Array‹string | UTXOClass›, `overwrite`: boolean): *Array‹[StandardUTXO](common_utxos.standardutxo.md)›*

*Defined in [src/common/utxos.ts:219](https://github.com/ava-labs/avalanche.js/blob/a2feb77/src/common/utxos.ts#L219)*

Adds an array of [StandardUTXO](common_utxos.standardutxo.md)s to the [StandardUTXOSet](common_utxos.standardutxoset.md).

**Parameters:**

Name | Type | Default | Description |
------ | ------ | ------ | ------ |
`utxos` | Array‹string &#124; UTXOClass› | - | - |
`overwrite` | boolean | false | If true, if the UTXOID already exists, overwrite it... default false  |

**Returns:** *Array‹[StandardUTXO](common_utxos.standardutxo.md)›*

An array of StandardUTXOs which were added.

___

### `Abstract` clone

▸ **clone**(): *this*

*Defined in [src/common/utxos.ts:426](https://github.com/ava-labs/avalanche.js/blob/a2feb77/src/common/utxos.ts#L426)*

**Returns:** *this*

___

### `Abstract` create

▸ **create**(...`args`: any[]): *this*

*Defined in [src/common/utxos.ts:428](https://github.com/ava-labs/avalanche.js/blob/a2feb77/src/common/utxos.ts#L428)*

**Parameters:**

Name | Type |
------ | ------ |
`...args` | any[] |

**Returns:** *this*

___

###  difference

▸ **difference**(`utxoset`: this): *this*

*Defined in [src/common/utxos.ts:482](https://github.com/ava-labs/avalanche.js/blob/a2feb77/src/common/utxos.ts#L482)*

Set difference between this set and a parameter.

**Parameters:**

Name | Type | Description |
------ | ------ | ------ |
`utxoset` | this | The set to difference  |

**Returns:** *this*

A new StandardUTXOSet containing the difference

___

###  filter

▸ **filter**(`args`: any[], `lambda`: function): *this*

*Defined in [src/common/utxos.ts:430](https://github.com/ava-labs/avalanche.js/blob/a2feb77/src/common/utxos.ts#L430)*

**Parameters:**

▪ **args**: *any[]*

▪ **lambda**: *function*

▸ (`utxo`: UTXOClass, ...`largs`: any[]): *boolean*

**Parameters:**

Name | Type |
------ | ------ |
`utxo` | UTXOClass |
`...largs` | any[] |

**Returns:** *this*

___

###  getAddresses

▸ **getAddresses**(): *Array‹Buffer›*

*Defined in [src/common/utxos.ts:369](https://github.com/ava-labs/avalanche.js/blob/a2feb77/src/common/utxos.ts#L369)*

Gets the addresses in the [StandardUTXOSet](common_utxos.standardutxoset.md) and returns an array of [Buffer](https://github.com/feross/buffer).

**Returns:** *Array‹Buffer›*

___

###  getAllUTXOStrings

▸ **getAllUTXOStrings**(`utxoids`: Array‹string›): *Array‹string›*

*Defined in [src/common/utxos.ts:320](https://github.com/ava-labs/avalanche.js/blob/a2feb77/src/common/utxos.ts#L320)*

Gets all the [StandardUTXO](common_utxos.standardutxo.md)s as strings, optionally that match with UTXOIDs in an array.

**Parameters:**

Name | Type | Default | Description |
------ | ------ | ------ | ------ |
`utxoids` | Array‹string› | undefined | An optional array of UTXOIDs, returns all [StandardUTXO](common_utxos.standardutxo.md)s if not provided  |

**Returns:** *Array‹string›*

An array of [StandardUTXO](common_utxos.standardutxo.md)s as cb58 serialized strings.

___

###  getAllUTXOs

▸ **getAllUTXOs**(`utxoids`: Array‹string›): *Array‹UTXOClass›*

*Defined in [src/common/utxos.ts:299](https://github.com/ava-labs/avalanche.js/blob/a2feb77/src/common/utxos.ts#L299)*

Gets all the [StandardUTXO](common_utxos.standardutxo.md)s, optionally that match with UTXOIDs in an array

**Parameters:**

Name | Type | Default | Description |
------ | ------ | ------ | ------ |
`utxoids` | Array‹string› | undefined | An optional array of UTXOIDs, returns all [StandardUTXO](common_utxos.standardutxo.md)s if not provided  |

**Returns:** *Array‹UTXOClass›*

An array of [StandardUTXO](common_utxos.standardutxo.md)s.

___

###  getAssetIDs

▸ **getAssetIDs**(`addresses`: Array‹Buffer›): *Array‹Buffer›*

*Defined in [src/common/utxos.ts:408](https://github.com/ava-labs/avalanche.js/blob/a2feb77/src/common/utxos.ts#L408)*

Gets all the Asset IDs, optionally that match with Asset IDs in an array

**Parameters:**

Name | Type | Default |
------ | ------ | ------ |
`addresses` | Array‹Buffer› | undefined |

**Returns:** *Array‹Buffer›*

An array of [Buffer](https://github.com/feross/buffer) representing the Asset IDs.

___

###  getBalance

▸ **getBalance**(`addresses`: Array‹Buffer›, `assetID`: Buffer | string, `asOf`: BN): *BN*

*Defined in [src/common/utxos.ts:381](https://github.com/ava-labs/avalanche.js/blob/a2feb77/src/common/utxos.ts#L381)*

Returns the balance of a set of addresses in the StandardUTXOSet.

**Parameters:**

Name | Type | Default | Description |
------ | ------ | ------ | ------ |
`addresses` | Array‹Buffer› | - | An array of addresses |
`assetID` | Buffer &#124; string | - | Either a [Buffer](https://github.com/feross/buffer) or an cb58 serialized representation of an AssetID |
`asOf` | BN | undefined | The timestamp to verify the transaction against as a [BN](https://github.com/indutny/bn.js/)  |

**Returns:** *BN*

Returns the total balance as a [BN](https://github.com/indutny/bn.js/).

___

###  getUTXO

▸ **getUTXO**(`utxoid`: string): *UTXOClass*

*Defined in [src/common/utxos.ts:290](https://github.com/ava-labs/avalanche.js/blob/a2feb77/src/common/utxos.ts#L290)*

Gets a [StandardUTXO](common_utxos.standardutxo.md) from the [StandardUTXOSet](common_utxos.standardutxoset.md) by its UTXOID.

**Parameters:**

Name | Type | Description |
------ | ------ | ------ |
`utxoid` | string | String representing the UTXOID  |

**Returns:** *UTXOClass*

A [StandardUTXO](common_utxos.standardutxo.md) if it exists in the set.

___

###  getUTXOIDs

▸ **getUTXOIDs**(`addresses`: Array‹Buffer›, `spendable`: boolean): *Array‹string›*

*Defined in [src/common/utxos.ts:345](https://github.com/ava-labs/avalanche.js/blob/a2feb77/src/common/utxos.ts#L345)*

Given an address or array of addresses, returns all the UTXOIDs for those addresses

**Parameters:**

Name | Type | Default | Description |
------ | ------ | ------ | ------ |
`addresses` | Array‹Buffer› | undefined | - |
`spendable` | boolean | true | If true, only retrieves UTXOIDs whose locktime has passed  |

**Returns:** *Array‹string›*

An array of addresses.

___

###  includes

▸ **includes**(`utxo`: UTXOClass | string): *boolean*

*Defined in [src/common/utxos.ts:156](https://github.com/ava-labs/avalanche.js/blob/a2feb77/src/common/utxos.ts#L156)*

Returns true if the [StandardUTXO](common_utxos.standardutxo.md) is in the StandardUTXOSet.

**Parameters:**

Name | Type | Description |
------ | ------ | ------ |
`utxo` | UTXOClass &#124; string | Either a [StandardUTXO](common_utxos.standardutxo.md) a cb58 serialized string representing a StandardUTXO  |

**Returns:** *boolean*

___

###  intersection

▸ **intersection**(`utxoset`: this): *this*

*Defined in [src/common/utxos.ts:468](https://github.com/ava-labs/avalanche.js/blob/a2feb77/src/common/utxos.ts#L468)*

Set intersetion between this set and a parameter.

**Parameters:**

Name | Type | Description |
------ | ------ | ------ |
`utxoset` | this | The set to intersect  |

**Returns:** *this*

A new StandardUTXOSet containing the intersection

___

###  merge

▸ **merge**(`utxoset`: this, `hasUTXOIDs`: Array‹string›): *this*

*Defined in [src/common/utxos.ts:449](https://github.com/ava-labs/avalanche.js/blob/a2feb77/src/common/utxos.ts#L449)*

Returns a new set with copy of UTXOs in this and set parameter.

**Parameters:**

Name | Type | Default | Description |
------ | ------ | ------ | ------ |
`utxoset` | this | - | The [StandardUTXOSet](common_utxos.standardutxoset.md) to merge with this one |
`hasUTXOIDs` | Array‹string› | undefined | Will subselect a set of [StandardUTXO](common_utxos.standardutxo.md)s which have the UTXOIDs provided in this array, defults to all UTXOs  |

**Returns:** *this*

A new StandardUTXOSet that contains all the filtered elements.

___

###  mergeByRule

▸ **mergeByRule**(`utxoset`: this, `mergeRule`: [MergeRule](../modules/utils_constants.md#mergerule)): *this*

*Defined in [src/common/utxos.ts:531](https://github.com/ava-labs/avalanche.js/blob/a2feb77/src/common/utxos.ts#L531)*

Merges a set by the rule provided.

**`remarks`** 
The merge rules are as follows:
  * "intersection" - the intersection of the set
  * "differenceSelf" - the difference between the existing data and new set
  * "differenceNew" - the difference between the new data and the existing set
  * "symDifference" - the union of the differences between both sets of data
  * "union" - the unique set of all elements contained in both sets
  * "unionMinusNew" - the unique set of all elements contained in both sets, excluding values only found in the new set
  * "unionMinusSelf" - the unique set of all elements contained in both sets, excluding values only found in the existing set

**Parameters:**

Name | Type | Description |
------ | ------ | ------ |
`utxoset` | this | The set to merge by the MergeRule |
`mergeRule` | [MergeRule](../modules/utils_constants.md#mergerule) | The [MergeRule](../modules/utils_constants.md#mergerule) to apply  |

**Returns:** *this*

A new StandardUTXOSet containing the merged data

___

### `Abstract` parseUTXO

▸ **parseUTXO**(`utxo`: UTXOClass | string): *UTXOClass*

*Defined in [src/common/utxos.ts:149](https://github.com/ava-labs/avalanche.js/blob/a2feb77/src/common/utxos.ts#L149)*

**Parameters:**

Name | Type |
------ | ------ |
`utxo` | UTXOClass &#124; string |

**Returns:** *UTXOClass*

___

###  remove

▸ **remove**(`utxo`: UTXOClass | string): *UTXOClass*

*Defined in [src/common/utxos.ts:237](https://github.com/ava-labs/avalanche.js/blob/a2feb77/src/common/utxos.ts#L237)*

Removes a [StandardUTXO](common_utxos.standardutxo.md) from the [StandardUTXOSet](common_utxos.standardutxoset.md) if it exists.

**Parameters:**

Name | Type | Description |
------ | ------ | ------ |
`utxo` | UTXOClass &#124; string | Either a [StandardUTXO](common_utxos.standardutxo.md) an cb58 serialized string representing a StandardUTXO  |

**Returns:** *UTXOClass*

A [StandardUTXO](common_utxos.standardutxo.md) if it was removed and undefined if nothing was removed.

___

###  removeArray

▸ **removeArray**(`utxos`: Array‹string | UTXOClass›): *Array‹UTXOClass›*

*Defined in [src/common/utxos.ts:272](https://github.com/ava-labs/avalanche.js/blob/a2feb77/src/common/utxos.ts#L272)*

Removes an array of [StandardUTXO](common_utxos.standardutxo.md)s to the [StandardUTXOSet](common_utxos.standardutxoset.md).

**Parameters:**

Name | Type |
------ | ------ |
`utxos` | Array‹string &#124; UTXOClass› |

**Returns:** *Array‹UTXOClass›*

An array of UTXOs which were removed.

___

###  symDifference

▸ **symDifference**(`utxoset`: this): *this*

*Defined in [src/common/utxos.ts:496](https://github.com/ava-labs/avalanche.js/blob/a2feb77/src/common/utxos.ts#L496)*

Set symmetrical difference between this set and a parameter.

**Parameters:**

Name | Type | Description |
------ | ------ | ------ |
`utxoset` | this | The set to symmetrical difference  |

**Returns:** *this*

A new StandardUTXOSet containing the symmetrical difference

___

###  union

▸ **union**(`utxoset`: this): *this*

*Defined in [src/common/utxos.ts:511](https://github.com/ava-labs/avalanche.js/blob/a2feb77/src/common/utxos.ts#L511)*

Set union between this set and a parameter.

**Parameters:**

Name | Type | Description |
------ | ------ | ------ |
`utxoset` | this | The set to union  |

**Returns:** *this*

A new StandardUTXOSet containing the union
