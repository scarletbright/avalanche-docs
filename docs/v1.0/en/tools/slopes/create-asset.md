# Tutorial &mdash; Creating An Asset

This example creates an asset in the AVM and publishes it to the AVA Platform. The first step in this process is to create an instance of Slopes connected to our AVA Platform endpoint of choice.

```js
let myNetworkID = 12345; //default is 3, we want to override that for our local network
let myBlockchainID = "4R5p2RXDGLqaifZE4hHWH9owe34pfoBULn1DrQTWivjg8o4aH"; // The AVM blockchainID on this network
let ava = new slopes.Slopes("localhost", 9650, "http", myNetworkID, myBlockchainID);
let avm = ava.AVM(); //returns a reference to the AVM API used by Slopes
```

## Describe the new asset

The first steps in creating a new asset using Slopes is to determine the qualities of the asset. We will give the asset a name, a ticker symbol, as well as a denomination. 

```js
// The fee to pay for the asset, we assume this network is fee-less
let fee = new BN(0);

// Name our new coin and give it a symbol
let name = "Rickcoin is the most intelligent coin";
let symbol = "RICK";

// Where is the decimal point indicate what 1 asset is and where fractional assets begin
// Ex: 1 AVA is denomination 9, so the smallest unit of AVA is nanoAVA (nAVA) at 10^-9 AVA
let denomination = 9;
```

## Creating the initial state
We want to mint an asset with 400 coins to all of our managed keys, 500 to the second address we know of, and 600 to the second and third address. This sets up the state that will result from the Create Asset transaction. 

*Note: This example assumes we have the keys already managed in our AVM Keychain.*

```js
let addresses = avm.keyChain().getAddresses();

// Create outputs for the asset's initial state
let secpbase1 = new slopes.SecpOutBase(new BN(400), addresses);
let secpbase2 = new slopes.SecpOutBase(new BN(500), [addresses[1]]);
let secpbase3 = new slopes.SecpOutBase(new BN(600), [addresses[1], addresses[2]]);

// Populate the initialState array
// The AVM needs to know what type of output is produced. 
// The constant slopes.AVMConstants.SECPFXID is the correct output.
// It specifies that we are using a secp256k1 signature scheme for this output.
let initialState = new slopes.InitialStates();
initialState.addOutput(secpbase1, slopes.AVMConstants.SECPFXID);
initialState.addOutput(secpbase2, slopes.AVMConstants.SECPFXID);
initialState.addOutput(secpbase3, slopes.AVMConstants.SECPFXID);
```

## Creating the signed transaction

Now that we know what we want an asset to look like, we create an output to send to the network. There is an AVM helper function `makeCreateAssetTx()` which does just that. 

```js
// Fetch the UTXOSet for our addresses
let utxos = await avm.getUTXOs(addresses);

// Make an unsigned Create Asset transaction from the data compiled earlier
let unsigned = await avm.makeCreateAssetTx(utxos, fee, addresses, initialState, name, symbol, denomination);

let signed = avm.keyChain().signTx(unsigned); //returns a Tx class
```

## Issue the signed transaction

Now that we have a signed transaction ready to send to the network, let's issue it! 

Using the Slopes AVM API, we going to call the issueTx function. This function can take either the Tx class returned in the previous step, a base-58 string AVA serialized representation of the transaction, or a raw Buffer class with the data for the transaction. Examples of each are below:

```js
// using the Tx class
let txid = await avm.issueTx(signed); //returns an AVA serialized string for the TxID
```

```js
// using the base-58 representation
let txid = await avm.issueTx(signed.toString()); //returns an AVA serialized string for the TxID
```

```js
// using the transaction Buffer
let txid = await avm.issueTx(signed.toBuffer()); //returns an AVA serialized string for the TxID
```

We assume ONE of those methods are used to issue the transaction.

## Get the status of the transaction

Now that we sent the transaction to the network, it takes a few seconds to determine if the transaction has gone through. We can get an updated status on the transaction using the TxID through the AVM API.

```js
// returns one of: "Accepted", "Processing", "Unknown", and "Rejected"
let status = await avm.getTxStatus(txid); 
```

The statuses can be one of "Accepted", "Processing", "Unknown", and "Rejected":

  * "Accepted" indicates that the transaction has been accepted as valid by the network and executed
  * "Processing" indicates that the transaction is being voted on.
  * "Unknown" indicates that node knows nothing about the transaction, indicating the node doesn't have it
  * "Rejected" indicates the node knows about the transaction, but it conflicted with an accepted transaction

## Identifying the newly created asset

The AVM uses the TxID of the transaction which created the asset as the unique identifier for the asset. This unique identifier is henceforth known as the "AssetID" of the asset. When assets are traded around the AVM, they always reference the AssetID that they represent.