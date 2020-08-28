# Platform Transaction Serialization

This file is meant to be the single source of truth for how we serialize transactions in Avalanche's Platform Virtual Machine, aka the `Platform Chain` or `P-Chain`. This document uses the [primitive serialization](./serialization-primitives.md) format for packing and [secp256k1](./cryptographic-primitives.md#cryptography-in-the-avalanche-virtual-machine) for cryptographic user identification.

***

## Codec ID

Some data is prepended with a codec ID (unt16) that denotes how the data should be deserialized.
Right now, the only valid codec ID is 0 (`0x00 0x00`).

***

## Unsigned Transactions

Unsigned transactions contain the full content of a transaction with only the signatures missing. Unsigned transactions have one possible type: `AddValidatorTx`. They embed `BaseTx`, which contains common fields and operations.

### What Base Tx Contains

A base tx contains a `TypeID`, `NetworkID`, `BlockchainID`, `Outputs`, `Inputs`, and `Memo`.

- **`TypeID`** is an id for this type. It is `0x0000000a`.
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

## Platform `AddDefaultSubnetDelegatorTx` Specification

### Unsigned Add Default Subnet Delegator Tx Identifier

The transaction identifier for a add default subnet delegator tx is `0x00000010`.

### What Unsigned Add Default Subnet Delegator Tx Contains

An unsigned base tx contains a `BaseTx`, `NodeID`, `StartTime`, `EndTime`, and `Destination`.

- **`ID`** is defined in `BaseTx`. For a default subnet delegator tx the ID is `0x00000010`.
- **`NodeID`** is 20 bytes which is the node ID of the delegatee.
- **`StartTime`** is a long which is the Unix time when the delegator starts delegating.
- **`EndTime`** is a long which is the Unix time when the delegator stops delegating (and staked AVAX is returned).
- **`Destination`** is 20 bytes which is the address of the account the staked AVAX and validation reward (if applicable) are sent to at `EndTime`.

### Gantt Unsigned Base Tx Specification

```boo
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