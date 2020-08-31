# Platform Transaction Serialization

This file is meant to be the single source of truth for how we serialize transactions in Avalanche's Platform Virtual Machine, aka the `Platform Chain` or `P-Chain`. This document uses the [primitive serialization](./serialization-primitives.md) format for packing and [secp256k1](./cryptographic-primitives.md#cryptography-in-the-avalanche-virtual-machine) for cryptographic user identification.

***

## Codec ID

Some data is prepended with a codec ID (unt16) that denotes how the data should be deserialized.
Right now, the only valid codec ID is 0 (`0x00 0x00`).

## Outputs

Outputs have one possible type: `SECP256K1TransferOutput`.

***

### SECP256K1 Transfer Output

A [secp256k1](./cryptographic-primitives.md#cryptography-in-the-avalanche-virtual-machine) transfer output allows for sending a quantity of an asset to a collection of addresses after a specified unix time.

#### What SECP256K1 Transfer Output Contains

A secp256k1 transfer output contains a `TypeID`, `Amount`, `Locktime`, `Threshold`, and `Addresses`.

- **`TypeID`** is the ID for this output type. It is `0x00000007`.
- **`Amount`** is a long that specifies the quantity of the asset that this output owns. Must be positive.
- **`Locktime`** is a long that contains the unix timestamp that this output can be spent after. The unix timestamp is specific to the second.
- **`Threshold`** is an int that names the number of unique signatures required to spend the output. Must be less than or equal to the length of **`Addresses`**. If **`Addresses`** is empty, must be 0.
- **`Addresses`** is a list of unique addresses that correspond to the private keys that can be used to spend this output. Addresses must be sorted lexicographically.

#### Gantt SECP256K1 Transfer Output Specification

```boo
+-----------+------------+--------------------------------+
| type  ID  : int        |                        4 bytes |
+-----------+------------+--------------------------------+
| amount    : long       |                        8 bytes |
+-----------+------------+--------------------------------+
| locktime  : long       |                        8 bytes |
+-----------+------------+--------------------------------+
| threshold : int        |                        4 bytes |
+-----------+------------+--------------------------------+
| addresses : [][20]byte |  4 + 20 * len(addresses) bytes |
+-----------+------------+--------------------------------+
                         | 28 + 20 * len(addresses) bytes |
                         +--------------------------------+
```

#### Proto SECP256K1 Transfer Output Specification

```protobuf
message SECP256K1TransferOutput {
    uint32 typeID = 1;            // 04 bytes
    uint64 amount = 2;            // 08 bytes
    uint64 locktime = 3;          // 08 bytes
    uint32 threshold = 4;         // 04 bytes
    repeated bytes addresses = 5; // 04 bytes + 20 bytes * len(addresses)
}
```

#### SECP256K1 Transfer Output Example

Let's make a secp256k1 transfer output with:

- **`Amount`**: 12345
- **`Locktime`**: 54321
- **`Threshold`**: 1
- **`Addresses`**:
  - 0xc3344128e060128ede3523a24a461c8943ab0859
  - 0x51025c61fbcfc078f69334f834be6dd26d55a955

```splus
[
    TypeID    <- 0x00000007
    Amount    <- 12345 = 0x0000000000003039
    Locktime  <- 54321 = 0x000000000000d431
    Threshold <- 1     = 0x00000001
    Addresses <- [
        0xc3344128e060128ede3523a24a461c8943ab0859,
        0x51025c61fbcfc078f69334f834be6dd26d55a955,
    ]
]
=
[
    // type ID:
    0x00, 0x00, 0x00, 0x07,
    // amount:
    0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x30, 0x39,
    // locktime:
    0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0xd4, 0x31,
    // threshold:
    0x00, 0x00, 0x00, 0x01,
    // number of addresses:
    0x00, 0x00, 0x00, 0x02,
    // addrs[0]:
    0x51, 0x02, 0x5c, 0x61, 0xfb, 0xcf, 0xc0, 0x78,
    0xf6, 0x93, 0x34, 0xf8, 0x34, 0xbe, 0x6d, 0xd2,
    0x6d, 0x55, 0xa9, 0x55,
    // addrs[1]:
    0xc3, 0x34, 0x41, 0x28, 0xe0, 0x60, 0x12, 0x8e,
    0xde, 0x35, 0x23, 0xa2, 0x4a, 0x46, 0x1c, 0x89,
    0x43, 0xab, 0x08, 0x59,
]
```

***

## Inputs

Inputs have one possible type: `SECP256K1TransferInput`.

***

### SECP256K1 Transfer Input

A [secp256k1](../cryptographic-primitives/#cryptography-in-the-avalanche-virtual-machine) transfer input allows for spending an unspent secp256k1 transfer output.

#### What SECP256K1 Transfer Input Contains

A secp256k1 transfer input contains an `Amount` and `AddressIndices`.

- **`TypeID`** is the ID for this output type. It is `0x00000005`.
- **`Amount`** is a long that specifies the quantity that this input should be consuming from the UTXO. Must be positive. Must be equal to the amount specified in the UTXO.
- **`AddressIndices`** is a list of unique ints that define the private keys are being used to spend the UTXO. Each UTXO has an array of addresses that can spend the UTXO. Each int represents the index in this address array that will sign this transaction. The array must be sorted low to high.

#### Gantt SECP256K1 Transfer Input Specification

```boo
+-------------------------+-------------------------------------+
| type ID         : int   |                             4 bytes |
+-----------------+-------+-------------------------------------+
| amount          : long  |                             8 bytes |
+-----------------+-------+-------------------------------------+
| address_indices : []int |  4 + 4 * len(address_indices) bytes |
+-----------------+-------+-------------------------------------+
                          | 16 + 4 * len(address_indices) bytes |
                          +-------------------------------------+
```

#### Proto SECP256K1 Transfer Input Specification

```protobuf
message SECP256K1TransferInput {
    uint32 typeID = 1;                   // 04 bytes
    uint64 amount = 2;                   // 08 bytes
    repeated uint32 address_indices = 3; // 04 bytes + 4 bytes * len(address_indices)
}
```

#### SECP256K1 Transfer Input Example

Let's make a payment input with:

- **`Amount`**: 123456789
- **`AddressIndices`**: [7,3]

```splus
[
    TypeID         <- 0x00000005
    Amount         <- 123456789 = 0x00000000075bcd15,
    AddressIndices <- [0x00000000]
]
=
[
    // type id:
    0x00, 0x00, 0x00, 0x05,
    // amount:
    0x00, 0x00, 0x00, 0x00, 0x07, 0x5b, 0xcd, 0x15,
    // length:
    0x00, 0x00, 0x00, 0x01,
    // address_indices[0]
    0x00, 0x00, 0x00, 0x07,
]
```

***

## Transferable Input

Transferable inputs describe a specific UTXO with a provided transfer input.

### What Transferable Input Contains

A transferable input contains a `TxID`, `UTXOIndex` `AssetID` and an `Input`.

- **`TxID`** is a 32-byte array that defines which transaction this input is consuming an output from.
- **`UTXOIndex`** is an int that defines which utxo this input is consuming the specified transaction.
- **`AssetID`** is a 32-byte array that defines which asset this input references.
- **`Input`** is a transferable input object.

### Gantt Transferable Input Specification

```boo
+------------+----------+------------------------+
| tx_id      : [32]byte |               32 bytes |
+------------+----------+------------------------+
| utxo_index : int      |               04 bytes |
+------------+----------+------------------------+
| asset_id   : [32]byte |               32 bytes |
+------------+----------+------------------------+
| input      : Input    |      size(input) bytes |
+------------+----------+------------------------+
                        | 68 + size(input) bytes |
                        +------------------------+
```

### Proto Transferable Input Specification

```protobuf
message TransferableInput {
    bytes tx_id = 1;       // 32 bytes
    uint32 utxo_index = 3; // 04 bytes
    bytes asset_id = 3;    // 32 bytes
    Input input = 4;       // size(input)
}
```

### Transferable Input Example

Let's make a transferable input:

- **`TxID`**: `0xf1e1d1c1b1a191817161514131211101f0e0d0c0b0a090807060504030201000`
- **`UTXOIndex`**: `5`
- **`AssetID`**: `0x000102030405060708090a0b0c0d0e0f101112131415161718191a1b1c1d1e1f`
- **`Input`**: "Example SECP256K1 Transfer Input from above"

```splus
[
    TxID      <- 0xf1e1d1c1b1a191817161514131211101f0e0d0c0b0a090807060504030201000
    UTXOIndex <- 5 = 0x00000005
    AssetID   <- 0x000102030405060708090a0b0c0d0e0f101112131415161718191a1b1c1d1e1f
    Input     <- 0x0000000500000000075bcd15000000020000000300000007
]
=
[
    // txID:
    0xf1, 0xe1, 0xd1, 0xc1, 0xb1, 0xa1, 0x91, 0x81,
    0x71, 0x61, 0x51, 0x41, 0x31, 0x21, 0x11, 0x01,
    0xf0, 0xe0, 0xd0, 0xc0, 0xb0, 0xa0, 0x90, 0x80,
    0x70, 0x60, 0x50, 0x40, 0x30, 0x20, 0x10, 0x00,
    // utxoIndex:
    0x00, 0x00, 0x00, 0x05,
    // assetID:
    0x00, 0x01, 0x02, 0x03, 0x04, 0x05, 0x06, 0x07,
    0x08, 0x09, 0x0a, 0x0b, 0x0c, 0x0d, 0x0e, 0x0f,
    0x10, 0x11, 0x12, 0x13, 0x14, 0x15, 0x16, 0x17,
    0x18, 0x19, 0x1a, 0x1b, 0x1c, 0x1d, 0x1e, 0x1f,
    // input:
    0x00, 0x00, 0x00, 0x05, 0x00, 0x00, 0x00, 0x00,
    0x07, 0x5b, 0xcd, 0x15, 0x00, 0x00, 0x00, 0x02,
    0x00, 0x00, 0x00, 0x03, 0x00, 0x00, 0x00, 0x07
]
```

***

## Unsigned Transactions

Unsigned transactions contain the full content of a transaction with only the signatures missing. Unsigned transactions have one possible type: `AddValidatorTx`. They embed `BaseTx`, which contains common fields and operations.

### What Base Tx Contains

A base tx contains a `TypeID`, `NetworkID`, `BlockchainID`, `Outputs`, `Inputs`, and `Memo`.

- **`TypeID`** is the ID for this type. It is `0x0000000a`.
- **`NetworkID`** is an int that defines which network this transaction is meant to be issued to. This value is meant to support transaction routing and is not designed for replay attack prevention.
- **`BlockchainID`** is a 32-byte array that defines which blockchain this transaction was issued to. This is used for replay attack prevention for transactions that could potentially be valid across network or blockchain.
- **`Outputs`** is an array of transferable output objects. Outputs must be sorted lexicographically by their serialized representation. The total quantity of the assets created in these outputs must be less than or equal to the total quantity of each asset consumed in the inputs minus the transaction fee.
- **`Inputs`** is an array of transferable input objects. Inputs must be sorted and unique. Inputs are sorted first lexicographically by their **`TxID`** and then by the **`UTXOIndex`** from low to high. If there are inputs that have the same **`TxID`** and **`UTXOIndex`**, then the transaction is invalid as this would result in a double spend.
- **`Memo`** Memo field contains arbitrary bytes, up to 256 bytes.

### Gantt Base Tx Specification

```boo
+---------------+----------------------+-----------------------------------------+
| type_id       : int                  |                                 4 bytes |
+---------------+----------------------+-----------------------------------------+
| network_id    : int                  |                                 4 bytes |
+---------------+----------------------+-----------------------------------------+
| blockchain_id : [32]byte             |                                32 bytes |
+---------------+----------------------+-----------------------------------------+
| outputs       : []TransferableOutput |                 4 + size(outputs) bytes |
+---------------+----------------------+-----------------------------------------+
| inputs        : []TransferableInput  |                  4 + size(inputs) bytes |
+---------------+----------------------+-----------------------------------------+
| memo          : [256]byte            |                    4 + size(memo) bytes |
+---------------+----------------------+-----------------------------------------+
                          | 52 + size(outputs) + size(inputs) + size(memo) bytes |
                          +------------------------------------------------------+
```

### Proto Base Tx Specification

```protobuf
message BaseTx {
    uint32 type_id = 1;          // 04 bytes
    uint32 network_id = 2;       // 04 bytes
    bytes blockchain_id = 3;     // 32 bytes
    repeated Output outputs = 4; // 04 bytes + size(outs)
    repeated Input inputs = 5;   // 04 bytes + size(ins)
    bytes memo = 6;              // 04 bytes + size(memo)
}
```

### Base Tx Example

Let's make a base tx that uses the inputs and outputs from the previous examples:

- **`TypeID`**: `0`
- **`NetworkID`**: `12345`
- **`BlockchainID`**: `0x000000000000000000000000000000000000000000000000000000000000000`
- **`Outputs`**: `00000007000012309cd7078b000000000000000000000001000000013cb7d3842e8cee6a0ebd09f1fe884f6861e1b29c`
- **`Inputs`**: `136923582736d444a971693dded0aa059053b36a85e98e39447cc92deb9cc4d700000000345aa98e8a990f4101e2268fab4c4e1f731c8dfbcffa3a77978686e6390d624f00000005000012309cd7ddb00000000100000000`

```splus
[
    TypeID       <- 0 = 0x00000000
    NetworkID    <- 12345 = 0x00003039
    BlockchainID <- 0x000000000000000000000000000000000000000000000000000000000000000
    Outputs      <- [
        00000007000012309cd7078b000000000000000000000001000000013cb7d3842e8cee6a0ebd09f1fe884f6861e1b29c
    ]
    Inputs       <- [
        136923582736d444a971693dded0aa059053b36a85e98e39447cc92deb9cc4d700000000345aa98e8a990f4101e2268fab4c4e1f731c8dfbcffa3a77978686e6390d624f00000005000012309cd7ddb00000000100000000
    ]
]
=
[
    // typeID:
    0x00, 0x00, 0x00, 0x0a,
    // networkID:
    0x00, 0x00, 0x30, 0x39,
    // blockchainID:
    0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00,
    0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00,
    0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00,
    0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00,
    // number of outputs:
    0x00, 0x00, 0x00, 0x01,
    // transferable output:
    0x00, 0x00, 0x00, 0x07, 0x00, 0x00, 0x12, 0x30, 0x9c,
    0xd7, 0x07, 0x8b, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00,
    0x00, 0x00, 0x00, 0x00, 0x00, 0x01, 0x00, 0x00, 0x00,
    0x01, 0x3c, 0xb7, 0xd3, 0x84, 0x2e, 0x8c, 0xee, 0x6a,
    0x0e, 0xbd, 0x09, 0xf1, 0xfe, 0x88, 0x4f, 0x68, 0x61,
    0xe1, 0xb2, 0x9c,
    // number of inputs:
    0x00, 0x00, 0x00, 0x01,
    // transferable input:
    0x13, 0x69, 0x23, 0x58, 0x27, 0x36, 0xd4, 0x44, 0xa9,
    0x71, 0x69, 0x3d, 0xde, 0xd0, 0xaa, 0x05, 0x90, 0x53,
    0xb3, 0x6a, 0x85, 0xe9, 0x8e, 0x39, 0x44, 0x7c, 0xc9,
    0x2d, 0xeb, 0x9c, 0xc4, 0xd7, 0x00, 0x00, 0x00, 0x00,
    0x34, 0x5a, 0xa9, 0x8e, 0x8a, 0x99, 0x0f, 0x41, 0x01,
    0xe2, 0x26, 0x8f, 0xab, 0x4c, 0x4e, 0x1f, 0x73, 0x1c,
    0x8d, 0xfb, 0xcf, 0xfa, 0x3a, 0x77, 0x97, 0x86, 0x86,
    0xe6, 0x39, 0x0d, 0x62, 0x4f, 0x00, 0x00, 0x00, 0x05,
    0x00, 0x00, 0x12, 0x30, 0x9c, 0xd7, 0xdd, 0xb0, 0x00,
    0x00, 0x00, 0x01, 0x00, 0x00, 0x00, 0x00,
    // Memo length:
    0x00, 0x00, 0x00, 0x00,
]
```

***

### What Unsigned Add Validator Tx Contains

An unsigned add validator tx contains a `TypeID`, `BaseTx`, `NodeID`, `StartTime`, `EndTime`, `Weight`, `LockedOuts`, `Locktime`, `Threshold`, `RewardAddress` and `Shares`.

- **`TypeID`** is the ID for this type. It is `0x0000000c`.
- **`BaseTx`**
- **`NodeID`** is 20 bytes which is the node ID of the delegatee.
- **`StartTime`** is a long which is the Unix time when the delegator starts delegating.
- **`EndTime`** is a long which is the Unix time when the delegator stops delegating (and staked AVAX is returned).
- **`Weight`** Amount the delegator stakes
- **`LockedOuts`** An array of Transferable Outputs
- **`Locktime`** is a long that contains the unix timestamp that this output can be spent after. The unix timestamp is specific to the second.
- **`Threshold`** is an int that names the number of unique signatures required to spend the output. Must be less than or equal to the length of **`Addresses`**. If **`Addresses`** is empty, must be 0.
- **`RewardAddress`** Address to send reward to, if applicable
- **`Shares`** 10,000 times percentage of reward taken from delegators

### Gantt Unsigned Add Validator Tx Specification

```boo
+---------------+----------------------+-----------------------------------------+
| type_id       : int                  |                                 4 bytes |
+---------------+----------------------+-----------------------------------------+
| base_tx       : BaseTx               |                     size(base_tx) bytes |
+---------------+----------------------+-----------------------------------------+
| node_id       : [20]byte             |                                20 bytes |
+---------------+----------------------+-----------------------------------------+
| start_time    : long                 |                                 8 bytes |
+---------------+----------------------+-----------------------------------------+
| end_time      : long                 |                                 8 bytes |
+---------------+----------------------+-----------------------------------------+
| weight        : long                 |                                 8 bytes |
+---------------+----------------------+-----------------------------------------+
| locked_outs   : []Output             |                 4 + size(outputs) bytes |
+---------------+----------------------+-----------------------------------------+
| locktime      : long                 |                                 8 bytes |
+---------------+----------------------+-----------------------------------------+
| threshold     : int                  |                                 4 bytes |
+---------------+----------------------+-----------------------------------------+
| reward_address: [20]byte             |                                20 bytes |
+---------------+----------------------+-----------------------------------------+
                                      | 84 + size(outputs) + size(base_tx) bytes |
                                      +------------------------------------------+
```

### Proto Unsigned Add Validator Tx Specification

```protobuf
message AddValidatorTx {
    uint32 type_id = 1;              // 04 bytes
    BaseTx base_tx = 2;              // size(base_tx)
    bytes node_id = 3;               // 20 bytes
    uint64 start_time = 4;           // 08 bytes
    uint64 end_time = 5;             // 08 bytes
    uint64 weight = 6;               // 08 bytes
    repeated Output locked_outs = 7; // 4 + size(outputs) bytes
    uint64 lock_time = 8;            // 08 bytes
    uint32 threshold = 9;            // 04 bytes
    bytes reward_address = 10;       // 20 bytes
    uint32 shares = 11;              // 04 bytes
}
```

### Unsigned Add Validator Tx Example

Let's make an unsigned add validator tx that uses the inputs and outputs from the previous examples:

- **`BaseTx`**: `"Example BaseTx as defined above with ID set to 10"`
- **`NodeID`**: `0xe9094f73698002fd52c90819b457b9fbc866ab80`
- **`weight`**: `0x000000000000d431`
- **`StarTime`**: `0x000000005f21f31d`
- **`EndTime`**: `0x000000005f497dc6`
- **`Destination`**: `0x3cb7d3842e8cee6a0ebd09f1fe884f6861e1b29c`

```splus
[
    BaseTx       <- 0x0000000000100000303900000000000000000000000000000000000000000000000000000000000000000000007000012309cd7078b000000000000000000000001000000013cb7d3842e8cee6a0ebd09f1fe884f6861e1b29c136923582736d444a971693dded0aa059053b36a85e98e39447cc92deb9cc4d700000000345aa98e8a990f4101e2268fab4c4e1f731c8dfbcffa3a77978686e6390d624f00000005000012309cd7ddb00000000100000000
    NodeID       <- 0xe9094f73698002fd52c90819b457b9fbc866ab80
    Amount       <- 0x000000000000d431
    StarTime     <- 0x000000005f21f31d
    EndTime      <- 0x000000005f497dc6
    Destination  <- 0x3cb7d3842e8cee6a0ebd09f1fe884f6861e1b29c
]
=
[
    // base tx:
    0x00, 0x00, 0x00, 0x00, 0x00, 0x10, 0x00, 0x00,
    0x30, 0x39, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00,
    0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00,
    0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00,
    0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00,
    0x00, 0x00, 0x00, 0x00, 0x00, 0x01, 0x00, 0x00,
    0x00, 0x07, 0x00, 0x00, 0x12, 0x30, 0x9c, 0xd7,
    0x07, 0x8b, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00,
    0x00, 0x00, 0x00, 0x00, 0x00, 0x01, 0x00, 0x00,
    0x00, 0x01, 0x3c, 0xb7, 0xd3, 0x84, 0x2e, 0x8c,
    0xee, 0x6a, 0x0e, 0xbd, 0x09, 0xf1, 0xfe, 0x88,
    0x4f, 0x68, 0x61, 0xe1, 0xb2, 0x9c, 0x00, 0x00,
    0x00, 0x01, 0x13, 0x69, 0x23, 0x58, 0x27, 0x36,
    0xd4, 0x44, 0xa9, 0x71, 0x69, 0x3d, 0xde, 0xd0,
    0xaa, 0x05, 0x90, 0x53, 0xb3, 0x6a, 0x85, 0xe9,
    0x8e, 0x39, 0x44, 0x7c, 0xc9, 0x2d, 0xeb, 0x9c,
    0xc4, 0xd7, 0x00, 0x00, 0x00, 0x00, 0x34, 0x5a,
    0xa9, 0x8e, 0x8a, 0x99, 0x0f, 0x41, 0x01, 0xe2,
    0x26, 0x8f, 0xab, 0x4c, 0x4e, 0x1f, 0x73, 0x1c,
    0x8d, 0xfb, 0xcf, 0xfa, 0x3a, 0x77, 0x97, 0x86,
    0x86, 0xe6, 0x39, 0x0d, 0x62, 0x4f, 0x00, 0x00,
    0x00, 0x05, 0x00, 0x00, 0x12, 0x30, 0x9c, 0xd7,
    0xdd, 0xb0, 0x00, 0x00, 0x00, 0x01, 0x00, 0x00,
    0x00, 0x00, 0x00, 0x00, 0x00, 0x00,
    // Node ID
    0xe9, 0x09, 0x4f, 0x73, 0x69, 0x80, 0x02, 0xfd, 0x52,
    0xc9, 0x08, 0x19, 0xb4, 0x57, 0xb9, 0xfb, 0xc8, 0x66,
    0xab, 0x80,
    // Amount
    0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0xd4, 0x31,
    // StartTime
    0x00, 0x00, 0x00, 0x00, 0x5f, 0x21, 0xf3, 0x1d,
    // EndTime
    0x00, 0x00, 0x00, 0x00, 0x5f, 0x49, 0x7d, 0xc6,
    // Destination
    0x3c, 0xb7, 0xd3, 0x84, 0x2e, 0x8c, 0xee, 0x6a, 0x0e,
    0xbd, 0x09, 0xf1, 0xfe, 0x88, 0x4f, 0x68, 0x61, 0xe1,
    0xb2, 0x9c,
]
```

***

### What Unsigned Add Subnet Validator Tx Contains

An unsigned add subnet validator tx contains a `TypeID`, `BaseTx`, `NodeID`, `StartTime`, `EndTime`, `Weight`, `Subnet` and `SubnetAuth`.

- **`TypeID`** is the ID for this type. It is `0x0000000c`.
- **`BaseTx`**
- **`NodeID`** is 20 bytes which is the node ID of the delegatee.
- **`StartTime`** is a long which is the Unix time when the delegator starts delegating.
- **`EndTime`** is a long which is the Unix time when the delegator stops delegating (and staked AVAX is returned).
- **`Weight`** Amount the delegator stakes
- **`Subnet`** ID of the subnet the validator will validate
- **`SubnetAuth`** 10,000 times percentage of reward taken from delegators

### Gantt Unsigned Add Subnet Validator Tx Specification

```boo
+---------------+----------------------+-----------------------------------------+
| type_id       : int                  |                                 4 bytes |
+---------------+----------------------+-----------------------------------------+
| base_tx       : BaseTx               |                     size(base_tx) bytes |
+---------------+----------------------+-----------------------------------------+
| node_id       : [20]byte             |                                20 bytes |
+---------------+----------------------+-----------------------------------------+
| start_time    : long                 |                                 8 bytes |
+---------------+----------------------+-----------------------------------------+
| end_time      : long                 |                                 8 bytes |
+---------------+----------------------+-----------------------------------------+
| weight        : long                 |                                 8 bytes |
+---------------+----------------------+-----------------------------------------+
| subnet        : [32]byte             |                                32 bytes |
+---------------+----------------------+-----------------------------------------+
| subnet_auth   : ????????             |                                20 bytes |
+---------------+----------------------+-----------------------------------------+
                                     | 116 + size(outputs) + size(base_tx) bytes |
                                     +-------------------------------------------+
```

### Proto Unsigned Add Subnet Validator Tx Specification

```protobuf
message AddValidatorTx {
    uint32 type_id = 1;              // 04 bytes
    BaseTx base_tx = 2;              // size(base_tx)
    bytes node_id = 3;               // 20 bytes
    uint64 start_time = 4;           // 08 bytes
    uint64 end_time = 5;             // 08 bytes
    uint64 weight = 6;               // 08 bytes
    bytes reward_address = 7;        // 32 bytes
    ?????? subnet_auth = 8;          // ?? bytes
}
```

### Unsigned Add Subnet Validator Tx Example

Let's make an unsigned add validator tx that uses the inputs and outputs from the previous examples:

- **`BaseTx`**: `"Example BaseTx as defined above with ID set to 10"`
- **`NodeID`**: `0xe9094f73698002fd52c90819b457b9fbc866ab80`
- **`weight`**: `0x000000000000d431`
- **`StarTime`**: `0x000000005f21f31d`
- **`EndTime`**: `0x000000005f497dc6`
- **`Destination`**: `0x3cb7d3842e8cee6a0ebd09f1fe884f6861e1b29c`

```splus
[
    BaseTx       <- 0x0000000000100000303900000000000000000000000000000000000000000000000000000000000000000000007000012309cd7078b000000000000000000000001000000013cb7d3842e8cee6a0ebd09f1fe884f6861e1b29c136923582736d444a971693dded0aa059053b36a85e98e39447cc92deb9cc4d700000000345aa98e8a990f4101e2268fab4c4e1f731c8dfbcffa3a77978686e6390d624f00000005000012309cd7ddb00000000100000000
    NodeID       <- 0xe9094f73698002fd52c90819b457b9fbc866ab80
    Amount       <- 0x000000000000d431
    StarTime     <- 0x000000005f21f31d
    EndTime      <- 0x000000005f497dc6
    Destination  <- 0x3cb7d3842e8cee6a0ebd09f1fe884f6861e1b29c
]
=
[
    // base tx:
    0x00, 0x00, 0x00, 0x00, 0x00, 0x10, 0x00, 0x00,
    0x30, 0x39, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00,
    0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00,
    0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00,
    0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00,
    0x00, 0x00, 0x00, 0x00, 0x00, 0x01, 0x00, 0x00,
    0x00, 0x07, 0x00, 0x00, 0x12, 0x30, 0x9c, 0xd7,
    0x07, 0x8b, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00,
    0x00, 0x00, 0x00, 0x00, 0x00, 0x01, 0x00, 0x00,
    0x00, 0x01, 0x3c, 0xb7, 0xd3, 0x84, 0x2e, 0x8c,
    0xee, 0x6a, 0x0e, 0xbd, 0x09, 0xf1, 0xfe, 0x88,
    0x4f, 0x68, 0x61, 0xe1, 0xb2, 0x9c, 0x00, 0x00,
    0x00, 0x01, 0x13, 0x69, 0x23, 0x58, 0x27, 0x36,
    0xd4, 0x44, 0xa9, 0x71, 0x69, 0x3d, 0xde, 0xd0,
    0xaa, 0x05, 0x90, 0x53, 0xb3, 0x6a, 0x85, 0xe9,
    0x8e, 0x39, 0x44, 0x7c, 0xc9, 0x2d, 0xeb, 0x9c,
    0xc4, 0xd7, 0x00, 0x00, 0x00, 0x00, 0x34, 0x5a,
    0xa9, 0x8e, 0x8a, 0x99, 0x0f, 0x41, 0x01, 0xe2,
    0x26, 0x8f, 0xab, 0x4c, 0x4e, 0x1f, 0x73, 0x1c,
    0x8d, 0xfb, 0xcf, 0xfa, 0x3a, 0x77, 0x97, 0x86,
    0x86, 0xe6, 0x39, 0x0d, 0x62, 0x4f, 0x00, 0x00,
    0x00, 0x05, 0x00, 0x00, 0x12, 0x30, 0x9c, 0xd7,
    0xdd, 0xb0, 0x00, 0x00, 0x00, 0x01, 0x00, 0x00,
    0x00, 0x00, 0x00, 0x00, 0x00, 0x00,
    // Node ID
    0xe9, 0x09, 0x4f, 0x73, 0x69, 0x80, 0x02, 0xfd, 0x52,
    0xc9, 0x08, 0x19, 0xb4, 0x57, 0xb9, 0xfb, 0xc8, 0x66,
    0xab, 0x80,
    // Amount
    0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0xd4, 0x31,
    // StartTime
    0x00, 0x00, 0x00, 0x00, 0x5f, 0x21, 0xf3, 0x1d,
    // EndTime
    0x00, 0x00, 0x00, 0x00, 0x5f, 0x49, 0x7d, 0xc6,
    // Destination
    0x3c, 0xb7, 0xd3, 0x84, 0x2e, 0x8c, 0xee, 0x6a, 0x0e,
    0xbd, 0x09, 0xf1, 0xfe, 0x88, 0x4f, 0x68, 0x61, 0xe1,
    0xb2, 0x9c,
]
```

***

### What Unsigned Add Delegator Tx Contains

An unsigned add delegator tx contains a `TypeID`, `BaseTx`, `NodeID`, `StartTime`, `EndTime`, `Weight`, `LockedOuts`, `Locktime`, `Threshold` and `Destination`.

- **`TypeID`** is the ID for this type. It is `0x0000000c`.
- **`BaseTx`**
- **`NodeID`** is 20 bytes which is the node ID of the delegatee.
- **`StartTime`** is a long which is the Unix time when the delegator starts delegating.
- **`EndTime`** is a long which is the Unix time when the delegator stops delegating (and staked AVAX is returned).
- **`Weight`** Amount the delegator stakes
- **`LockedOuts`** An array of Transferable Outputs
- **`Locktime`** is a long that contains the unix timestamp that this output can be spent after. The unix timestamp is specific to the second.
- **`Threshold`** is an int that names the number of unique signatures required to spend the output. Must be less than or equal to the length of **`Addresses`**. If **`Addresses`** is empty, must be 0.
- **`Destination`** is 20 bytes which is the address of the account the staked AVAX and validation reward (if applicable) are sent to at `EndTime`.

### Gantt Unsigned Add Delegator Tx Specification

```boo
+---------------+----------------------+-----------------------------------------+
| type_id       : int                  |                                 4 bytes |
+---------------+----------------------+-----------------------------------------+
| base_tx       : BaseTx               |                     size(base_tx) bytes |
+---------------+----------------------+-----------------------------------------+
| node_id       : [20]byte             |                                20 bytes |
+---------------+----------------------+-----------------------------------------+
| start_time    : long                 |                                 8 bytes |
+---------------+----------------------+-----------------------------------------+
| end_time      : long                 |                                 8 bytes |
+---------------+----------------------+-----------------------------------------+
| weight        : long                 |                                 8 bytes |
+---------------+----------------------+-----------------------------------------+
| locked_outs   : []Output             |                 4 + size(outputs) bytes |
+---------------+----------------------+-----------------------------------------+
| locktime      : long                 |                                 8 bytes |
+---------------+----------------------+-----------------------------------------+
| threshold     : int                  |                                 4 bytes |
+---------------+----------------------+-----------------------------------------+
| destination   : [20]byte             |                                20 bytes |
+---------------+----------------------+-----------------------------------------+
                                      | 84 + size(outputs) + size(base_tx) bytes |
                                      +------------------------------------------+
```

### Proto Unsigned Add Delegator Tx Specification

```protobuf
message AddDelegatorTx {
    uint32 type_id = 1;              // 04 bytes
    BaseTx base_tx = 2;              // size(base_tx)
    bytes node_id = 3;               // 20 bytes
    uint64 start_time = 4;           // 08 bytes
    uint64 end_time = 5;             // 08 bytes
    uint64 weight = 6;               // 08 bytes
    repeated Output locked_outs = 7; // 4 + size(outputs) bytes
    uint64 lock_time = 8;            // 08 bytes
    uint32 threshold = 9;            // 04 bytes
    bytes destination = 10;          // 20 bytes
}
```

### Unsigned Add Delegator Tx Example

Let's make an unsigned add delegator tx that uses the inputs and outputs from the previous examples:

- **`BaseTx`**: `"Example BaseTx as defined above with ID set to 10"`
- **`NodeID`**: `0xe9094f73698002fd52c90819b457b9fbc866ab80`
- **`weight`**: `0x000000000000d431`
- **`StarTime`**: `0x000000005f21f31d`
- **`EndTime`**: `0x000000005f497dc6`
- **`Destination`**: `0x3cb7d3842e8cee6a0ebd09f1fe884f6861e1b29c`

```splus
[
    BaseTx       <- 0x0000000000100000303900000000000000000000000000000000000000000000000000000000000000000000007000012309cd7078b000000000000000000000001000000013cb7d3842e8cee6a0ebd09f1fe884f6861e1b29c136923582736d444a971693dded0aa059053b36a85e98e39447cc92deb9cc4d700000000345aa98e8a990f4101e2268fab4c4e1f731c8dfbcffa3a77978686e6390d624f00000005000012309cd7ddb00000000100000000
    NodeID       <- 0xe9094f73698002fd52c90819b457b9fbc866ab80
    Amount       <- 0x000000000000d431
    StarTime     <- 0x000000005f21f31d
    EndTime      <- 0x000000005f497dc6
    Destination  <- 0x3cb7d3842e8cee6a0ebd09f1fe884f6861e1b29c
]
=
[
    // base tx:
    0x00, 0x00, 0x00, 0x00, 0x00, 0x10, 0x00, 0x00,
    0x30, 0x39, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00,
    0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00,
    0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00,
    0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00,
    0x00, 0x00, 0x00, 0x00, 0x00, 0x01, 0x00, 0x00,
    0x00, 0x07, 0x00, 0x00, 0x12, 0x30, 0x9c, 0xd7,
    0x07, 0x8b, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00,
    0x00, 0x00, 0x00, 0x00, 0x00, 0x01, 0x00, 0x00,
    0x00, 0x01, 0x3c, 0xb7, 0xd3, 0x84, 0x2e, 0x8c,
    0xee, 0x6a, 0x0e, 0xbd, 0x09, 0xf1, 0xfe, 0x88,
    0x4f, 0x68, 0x61, 0xe1, 0xb2, 0x9c, 0x00, 0x00,
    0x00, 0x01, 0x13, 0x69, 0x23, 0x58, 0x27, 0x36,
    0xd4, 0x44, 0xa9, 0x71, 0x69, 0x3d, 0xde, 0xd0,
    0xaa, 0x05, 0x90, 0x53, 0xb3, 0x6a, 0x85, 0xe9,
    0x8e, 0x39, 0x44, 0x7c, 0xc9, 0x2d, 0xeb, 0x9c,
    0xc4, 0xd7, 0x00, 0x00, 0x00, 0x00, 0x34, 0x5a,
    0xa9, 0x8e, 0x8a, 0x99, 0x0f, 0x41, 0x01, 0xe2,
    0x26, 0x8f, 0xab, 0x4c, 0x4e, 0x1f, 0x73, 0x1c,
    0x8d, 0xfb, 0xcf, 0xfa, 0x3a, 0x77, 0x97, 0x86,
    0x86, 0xe6, 0x39, 0x0d, 0x62, 0x4f, 0x00, 0x00,
    0x00, 0x05, 0x00, 0x00, 0x12, 0x30, 0x9c, 0xd7,
    0xdd, 0xb0, 0x00, 0x00, 0x00, 0x01, 0x00, 0x00,
    0x00, 0x00, 0x00, 0x00, 0x00, 0x00,
    // Node ID
    0xe9, 0x09, 0x4f, 0x73, 0x69, 0x80, 0x02, 0xfd, 0x52,
    0xc9, 0x08, 0x19, 0xb4, 0x57, 0xb9, 0xfb, 0xc8, 0x66,
    0xab, 0x80,
    // Amount
    0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0xd4, 0x31,
    // StartTime
    0x00, 0x00, 0x00, 0x00, 0x5f, 0x21, 0xf3, 0x1d,
    // EndTime
    0x00, 0x00, 0x00, 0x00, 0x5f, 0x49, 0x7d, 0xc6,
    // Destination
    0x3c, 0xb7, 0xd3, 0x84, 0x2e, 0x8c, 0xee, 0x6a, 0x0e,
    0xbd, 0x09, 0xf1, 0xfe, 0x88, 0x4f, 0x68, 0x61, 0xe1,
    0xb2, 0x9c,
]
```

***

### What Unsigned Import Tx Contains

An unsigned import tx contains a `TypeID`, `BaseTx`, `SourceChain`, and `Ins`.

- **`TypeID`** is the ID for this type. It is `0x00000011`.
- **`BaseTx`**
- **`SourceChain`** is a 32-byte source blockchain ID.
- **`Ins`** is a variable length array of Transferable Inputs.

### Gantt Unsigned Import Tx Specification

```boo
+-----------------+--------------|---------------------------------+
| type ID         : int          |                         4 bytes |
+-----------------+--------------+---------------------------------+
| base_tx         : BaseTx       |             size(base_tx) bytes |
+-----------------+--------------+---------------------------------+
| source_chain    : [32]byte     |                        32 bytes |
+-----------------+--------------+---------------------------------+
| ins             : []TransferIn |             4 + size(ins) bytes |
+-----------------+--------------+---------------------------------+
                            | 40 + size(ins) + size(base_tx) bytes |
                            +--------------------------------------+
```

### Proto Unsigned Import Tx Specification

```protobuf
message ImportTx {
    uint32 TypeID = 1;           // 4 bytes
    BaseTx base_tx = 2;          // size(base_tx)
    bytes source_chain = 2;      // 32 bytes
    repeated TransferIn ins = 3; // 4 bytes + size(ins)
}
```

### Unsigned Import Tx Example

Let’s make an unsigned import tx that uses the inputs from the previous examples:

- **`TypeID`**: `0x00000011`
- **`BaseTx`**: "Example BaseTx as defined above"
- **`SourceChain`**:
- **`Ins`**: "Example SECP256K1 Transfer Input as defined above"

```splus
[
    TypeID        <- 0x00000011
    BaseTx        <- 0x0000303900000000000000000000000000000000000000000000000000000000000000000000000139c33a499ce4c33a3b09cdd2cfa01ae70dbf2d18b2d7d168524440e55d55008800000007000012309cd5fdc0000000000000000000000001000000013cb7d3842e8cee6a0ebd09f1fe884f6861e1b29c0000000000000000
    SourceChain   <- 0x787cd3243c002e9bf5bbbaea8a42a16c1a19cc105047c66996807cbf16acee10
    Ins <- [
        f1e1d1c1b1a191817161514131211101f0e0d0c0b0a09080706050403020100000000005000102030405060708090a0b0c0d0e0f101112131415161718191a1b1c1d1e1f0000000500000000075bcd150000000100000000,
    ]
]
=
[
    // Type ID
    0x00, 0x00, 0x00, 0x11,
    // base tx:
    0x00, 0x00, 0x30, 0x39, 0x00, 0x00, 0x00, 0x00,
    0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00,
    0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00,
    0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00,
    0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x01,
    0x39, 0xc3, 0x3a, 0x49, 0x9c, 0xe4, 0xc3, 0x3a,
    0x3b, 0x09, 0xcd, 0xd2, 0xcf, 0xa0, 0x1a, 0xe7,
    0x0d, 0xbf, 0x2d, 0x18, 0xb2, 0xd7, 0xd1, 0x68,
    0x52, 0x44, 0x40, 0xe5, 0x5d, 0x55, 0x00, 0x88,
    0x00, 0x00, 0x00, 0x07, 0x00, 0x00, 0x12, 0x30,
    0x9c, 0xd5, 0xfd, 0xc0, 0x00, 0x00, 0x00, 0x00,
    0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x01,
    0x00, 0x00, 0x00, 0x01, 0x3c, 0xb7, 0xd3, 0x84,
    0x2e, 0x8c, 0xee, 0x6a, 0x0e, 0xbd, 0x09, 0xf1,
    0xfe, 0x88, 0x4f, 0x68, 0x61, 0xe1, 0xb2, 0x9c,
    0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00,
    // sourceChain
    0x78, 0x7c, 0xd3, 0x24, 0x3c, 0x00, 0x2e, 0x9b,
    0xf5, 0xbb, 0xba, 0xea, 0x8a, 0x42, 0xa1, 0x6c,
    0x1a, 0x19, 0xcc, 0x10, 0x50, 0x47, 0xc6, 0x69,
    0x96, 0x80, 0x7c, 0xbf, 0x16, 0xac, 0xee, 0x10,
    // input count:
    0x00, 0x00, 0x00, 0x01,
    // txID:
    0xf1, 0xe1, 0xd1, 0xc1, 0xb1, 0xa1, 0x91, 0x81,
    0x71, 0x61, 0x51, 0x41, 0x31, 0x21, 0x11, 0x01,
    0xf0, 0xe0, 0xd0, 0xc0, 0xb0, 0xa0, 0x90, 0x80,
    0x70, 0x60, 0x50, 0x40, 0x30, 0x20, 0x10, 0x00,
    // utxoIndex:
    0x00, 0x00, 0x00, 0x05,
    // assetID:
    0x00, 0x01, 0x02, 0x03, 0x04, 0x05, 0x06, 0x07,
    0x08, 0x09, 0x0a, 0x0b, 0x0c, 0x0d, 0x0e, 0x0f,
    0x10, 0x11, 0x12, 0x13, 0x14, 0x15, 0x16, 0x17,
    0x18, 0x19, 0x1a, 0x1b, 0x1c, 0x1d, 0x1e, 0x1f,
    // input:
    0x00, 0x00, 0x00, 0x05, 0x00, 0x00, 0x00, 0x00,
    0x07, 0x5b, 0xcd, 0x15, 0x00, 0x00, 0x00, 0x01,
    0x00, 0x00, 0x00, 0x00,
]
```
