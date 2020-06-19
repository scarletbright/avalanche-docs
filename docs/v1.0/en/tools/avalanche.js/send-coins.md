# Tutorial &mdash; Sending An Asset

This example sends an asset in the AVM to a single recipient. The first step in this process is to create an instance of Avalanche connected to our AVA Platform endpoint of choice.

```js
let myNetworkID = 12345; //default is 3, we want to override that for our local network
let myBlockchainID = "GJABrZ9A6UQFpwjPU8MDxDd8vuyRoDVeDAXc694wJ5t3zEkhU"; // The AVM blockchainID on this network
let ava = new avalanche.Avalanche("localhost", 9650, "http", myNetworkID, myBlockchainID);
let avm = ava.AVM(); //returns a reference to the AVM API used by Avalanche.js
```

We're also assuming that the keystore contains a list of addresses used in this transaction.

## Getting the UTXO Set

The AVM stores all available balances in a datastore called Unspent Transaction Outputs (UTXOs). A UTXO Set is the unique list of outputs produced by transactions, addresses that can spend those outputs, and other variables such as lockout times (a timestamp after which the output can be spent) and thresholds (how many signers are required to spend the output). 

For the case of this example, we're going to create a simple transaction that spends an amount of available coins and sends it to a single address without any restrictions. The management of the UTXOs will mostly be abstracted away. 

However, we do need to get the UTXO Set for the addresses we're managing. 

```js
let myAddresses = avm.keyChain().getAddresses(); //returns an array of addresses the keychain manages
let addressStrings = avm.keyChain().getAddressStrings(); //returns an array of addresses the keychain manages as strings
let utxos = await avm.getUTXOs(myAddresses);
```

## Spending the UTXOs

The `buildBaseTx()` helper function sends a single asset type. We have a particular assetID whose coins we want to send to a recipient address. This is an imaginary asset for this example which we believe to have 400 coins. Let's verify that we have the funds available for the transaction.

```js
let assetid = "23wKfz3viWLmjWo2UZ7xWegjvnZFenGAVkouwQCeB9ubPXodG6"; //avaSerialized string
let mybalance = utxos.getBalance(myAddresses, assetid); //returns 400 as a BN
```
We have 400 coins! We're going to now send 100 of those coins to our friend's address.

```js
let sendAmount = new BN(100); //amounts are in BN format
let friendsAddress = "X-B6D4v1VtPYLbiUvYXtW4Px8oE9imC2vGW"; //AVA serialized address format

//The below returns a UnsignedTx
//Parameters sent are (in order of appearance):
//   * The UTXO Set
//   * The amount being sent as a BN
//   * An array of addresses to send the funds
//   * An array of addresses sending the funds
//   * An array of addresses any leftover funds are sent
//   * The AssetID of the funds being sent
let unsignedTx = await avm.buildBaseTx(utxos, sendAmount, [friendsAddress], addressStrings, addressStrings, assetid);
let signedTx = avm.signTx(unsignedTx);
let txid = await avm.issueTx(signedTx);
```

And the transaction is sent!

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

## Check the results

The transaction finally came back as "Accepted", now let's update the UTXOSet and verify that the transaction balance is as we expected. 

*Note: In a real network the balance isn't guaranteed to match this scenario. Transaction fees or additional spends may vary the balance. For the purpose of this example, we assume neither of those cases.*

```js
let updatedUTXOs = await avm.getUTXOs();
let newBalance = updatedUTXOs.getBalance(myAddresses, assetid);
if(newBalance.toNumber() != mybalance.sub(sendAmount).toNumber()){
    throw Error("heyyy these should equal!");
}
```
