# Platform Transaction Serialization

This file is meant to be the single source of truth for how we serialize transactions in Avalanche's Platform Virtual Machine, aka the `Platform Chain` or `P-Chain`. This document uses the [primitive serialization](./serialization-primitives.md) format for packing and [secp256k1](./cryptographic-primitives.md#cryptography-in-the-avalanche-virtual-machine) for cryptographic user identification.

***

### Platform `BaseTx` Specification

### Unsigned Base Tx Identifier

The transaction identifier for a base tx is `0x0000000a`.

### What Unsigned Base Tx Contains

An unsigned base tx contains a `CodecVersion`, `ID`, `NetworkID`, `BlockchainID`, `Outputs`, `Inputs`, and `Memo`.

- **`CodecVersion`** is a short that defines which codec version. Default is `0x0000`.
- **`ID`** is an int that defines which transaction type this is. Default is `0x0000000a`.
- **`NetworkID`** is an int that defines which network this transaction is meant to be issued to. This value is meant to support transaction routing and is not designed for replay attack prevention.
- **`BlockchainID`** is a 32-byte array that defines which blockchain this transaction was issued to. This is used for replay attack prevention for transactions that could potentially be valid across network or blockchain. In practice this is always the empty ID.
- **`Outputs`** is an array of transferable output objects. Outputs must be sorted lexicographically by their serialized representation. The total quantity of the assets created in these outputs must be less than or equal to the total quantity of each asset consumed in the inputs minus the transaction fee.
- **`Inputs`** is an array of transferable input objects. Inputs must be sorted and unique. Inputs are sorted first lexicographically by their **`TxID`** and then by the **`UTXOIndex`** from low to high. If there are inputs that have the same **`TxID`** and **`UTXOIndex`**, then the transaction is invalid as this would result in a double spend.
- **`Memo`** Memo field contains arbitrary bytes, up to 256 bytes.

### Gantt Unsigned Base Tx Specification

```boo
+---------------+----------------------+-----------------------------------------+
| codec_version : short                |                                 2 bytes |
+---------------+----------------------+-----------------------------------------+
| id            : int                  |                                 4 bytes |
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
                          | 54 + size(outputs) + size(inputs) + size(memo) bytes |
                          +------------------------------------------------------+
```

### Proto Unsigned Base Tx Specification

```protobuf
message BaseTx {
    uint16 codec_version = 1;    // 02 bytes
    uint32 id = 2;               // 04 bytes
    uint32 network_id = 3;       // 04 bytes
    bytes blockchain_id = 4;     // 32 bytes
    repeated Output outputs = 5; // 04 bytes + size(outs)
    repeated Input inputs = 6;   // 04 bytes + size(ins)
    bytes memo = 7;              // 04 bytes + size(memo)
}
```

### Unsigned Base Tx Example

Let's make an unsigned base tx that uses the inputs and outputs from the previous examples:

- `CodecVersion`: `0`
- `ID`: `10`
- `NetworkID`: `12345`
- `BlockchainID`: `0x000000000000000000000000000000000000000000000000000000000000000`
- `Outputs`: `00000007000012309cd7078b000000000000000000000001000000013cb7d3842e8cee6a0ebd09f1fe884f6861e1b29c`
- `Inputs`: `136923582736d444a971693dded0aa059053b36a85e98e39447cc92deb9cc4d700000000345aa98e8a990f4101e2268fab4c4e1f731c8dfbcffa3a77978686e6390d624f00000005000012309cd7ddb00000000100000000`

```splus
[
    CodecVersion <- 0 = 0x0000
    ID           <- 10 = 0x0000000a
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
    // codec_version:
    0x00, 0x00,
    // id:
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
