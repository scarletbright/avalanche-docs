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

- `TypeID`: `0`
- `NetworkID`: `12345`
- `BlockchainID`: `0x000000000000000000000000000000000000000000000000000000000000000`
- `Outputs`: `00000007000012309cd7078b000000000000000000000001000000013cb7d3842e8cee6a0ebd09f1fe884f6861e1b29c`
- `Inputs`: `136923582736d444a971693dded0aa059053b36a85e98e39447cc92deb9cc4d700000000345aa98e8a990f4101e2268fab4c4e1f731c8dfbcffa3a77978686e6390d624f00000005000012309cd7ddb00000000100000000`

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

### What Unsigned Add Delegator Tx Contains

An unsigned add delegator tx contains a `TypeID`, `BaseTx`, `NodeID`, `StartTime`, `EndTime`, and `Destination`.

- **`TypeID`** is the ID for this type. It is `0x0000000c`.
- **`BaseTx`**
- **`NodeID`** is 20 bytes which is the node ID of the delegatee.
- **`StartTime`** is a long which is the Unix time when the delegator starts delegating.
- **`EndTime`** is a long which is the Unix time when the delegator stops delegating (and staked AVAX is returned).
- **`Weight`**
- **`LockedOuts`**
- **`Locktime`**
- **`Threshold`**
- **`Destination`** is 20 bytes which is the address of the account the staked AVAX and validation reward (if applicable) are sent to at `EndTime`.

### Gantt Unsigned Base Tx Specification

```boo
+---------------+----------------------+-----------------------------------------+
| type_id       : int                  |                                 4 bytes |
+---------------+----------------------+-----------------------------------------+
| base_tx       : BaseTx               |                     size(base_tx) bytes |
+---------------+----------------------+-----------------------------------------+
| node_id       : [20]byte             |                                20 bytes |
+---------------+----------------------+-----------------------------------------+
| weight        : long                 |                                 8 bytes |
+---------------+----------------------+-----------------------------------------+
| start_time    : long                 |                                 8 bytes |
+---------------+----------------------+-----------------------------------------+
| end_time      : long                 |                                 8 bytes |
+---------------+----------------------+-----------------------------------------+
| destination   : [20]byte             |                                20 bytes |
+---------------+----------------------+-----------------------------------------+
                                                      | 64 + size(base_tx) bytes |
                                                      +--------------------------+
```

### Proto Unsigned Base Tx Specification

```protobuf
message BaseTx {
    BaseTx base_tx = 1;          // size(base_tx)
    bytes node_id = 2;           // 20 bytes
    uint64 weight = 3;           // 08 bytes
    uint64 start_time = 4;       // 08 bytes
    uint64 end_time = 5;         // 08 bytes
    bytes destination = 6;       // 20 bytes
}
```

### Unsigned Base Tx Example

Let's make an unsigned base tx that uses the inputs and outputs from the previous examples:

- `BaseTx`: `"Example BaseTx as defined above with ID set to 10"`
- `NodeID`: `0xe9094f73698002fd52c90819b457b9fbc866ab80`
- `weight`: `0x000000000000d431`
- `StarTime`: `0x000000005f21f31d`
- `EndTime`: `0x000000005f497dc6`
- `Destination`: `0x3cb7d3842e8cee6a0ebd09f1fe884f6861e1b29c`

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
