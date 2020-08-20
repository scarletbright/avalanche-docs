# Avalanche.js - The Avalanche Platform JavaScript Library

## Overview

Avalanche.js is a JavaScript Library for interfacing with the Avalanche Platform. It is built using TypeScript and intended to support both browser and Node.js. The Avalanche.js library allows one to issue commands to the Avalanche node APIs. 

The APIs currently supported by default are:

  * Admin API
  * AVM API (X-Chain)
  * Health API
  * Info API
  * Keystore API
  * Metrics API
  * PlatformVM API

We built Avalanche.js with ease of use in mind. With this library, any Javascript developer is able to interact with a node on the Avalanche Platform who has enabled their API endpoints for the developer's consumption. We keep the library up-to-date with the latest changes in the [Avalanche Platform Specification](https://docs.avax.network). 

  Using Avalanche.js, developers can:

  * Locally manage private keys
  * Retrieve balances on addresses
  * Get UTXOs for addresses
  * Build and sign transactions
  * Issue signed transactions to the X-Chain
  * Create a Subnetwork
  * Administer a local node
  * Retrieve Avalanche network information from a node

## Requirements

Avalanche.js requires Node.js LTS version 12.13.1 or higher to compile. 

Avalanche.js depends on the following two Node.js modules internally, and we suggest that your project uses them as well:

 * Buffer: Enables Node.js's Buffer library in the browser.
    * https://github.com/feross/buffer
    * `npm install --save buffer`
 * BN.js: A bignumber library for Node.js and browser.
    * https://github.com/indutny/bn.js/
    * `npm install --save bn.js`

Both of the above modules are extremely useful when interacting with Avalanche as they are the input and output types of many base classes in the library. 

## Installation 

Avalanche is available for install via `npm`:

`npm install --save avalanche`

You can also pull the repo down directly and build it from scratch:

`npm run build`

This will generate a pure javascript library and place it in a folder named "dist" in the project root. The "avalanche.js" file can then be dropped into any project as a pure javascript implementation of Avalanche.

The Avalanche.js library can be imported into your existing Node.js project as follows:

```js
const avalanche = require("avalanche");
```
Or into your TypeScript project like this:

```js
import { Avalanche } from "avalanche"
```

## Importing essentials

```js
import {
    Avalanche,
    BinTools,
    Buffer,
    BN
  } from "avalanche"

let bintools = BinTools.getInstance();
```

The above lines import the libraries used in the tutorials. The libraries include:
  
  * avalanche: Our javascript module.
  * bn.js: A bignumber module use by Avalanche.js.
  * buffer: A Buffer library.
  * BinTools: A singleton built into Avalanche.js that is used for dealing with binary data.
