# Slopes - The AVA Platform JavaScript Library

## Overview

Slopes is a JavaScript Library for interfacing with the AVA Platform. It is built using TypeScript and intended to support both browser and Node.js. The Slopes library allows one to issue commands to the AVA node APIs. 

The APIs currently supported by default are:

  * The AVA Virtual Machine (AVM) API
  * The Keystore API
  * The Admin API
  * The Platform API

We built Slopes with ease of use in mind. With this library, any Javascript developer is able to interact with a node on the AVA Platform who has enabled their API endpoints for the developer's consumption. We keep the library up-to-date with the latest changes in the [AVA Platform Specification](https://docs.ava.network). 

  Using Slopes, developers can:

  * Locally manage private keys
  * Retrieve balances on addresses
  * Get UTXOs for addresses
  * Build and sign transactions
  * Issue signed transactions to the AVM
  * Create a Subnetwork
  * Administer a local node
  * Retrieve AVA network information from a node

## Requirements

Slopes requires Node.js LTS version 12.13.1 or higher to compile. 

Slopes depends on the following two Node.js modules internally, and we suggest that your project uses them as well:

 * Buffer: Enables Node.js's Buffer library in the browser.
    * https://github.com/feross/buffer
    * `npm install --save buffer`
 * BN.js: A bignumber library for Node.js and browser.
    * https://github.com/indutny/bn.js/
    * `npm install --save bn.js`

Both of the above modules are extremely useful when interacting with Slopes as they are the input and output types of many base classes in the library. 

## Installation 

Slopes is available for install via `npm`:

`npm install --save slopes`

You can also pull the repo down directly and build it from scratch:

`npm run build`

This will generate a pure javascript library and place it in a folder named "dist" in the project root. The "slopes.js" file can then be dropped into any project as a pure javascript implementation of Slopes.

The Slopes library can be imported into your existing Node.js project as follows:

```js
const slopes = require("slopes");
```
Or into your TypeScript project like this:

```js
import * as slopes from "slopes"
```

## Importing essentials

```js
import * as slopes from "slopes";
import BN from 'bn.js';
import { Buffer } from 'buffer/'; // the slash forces this library over native Node.js Buffer

let bintools = slopes.BinTools.getInstance();
```

The above lines import the libraries used in the tutorials. The libraries include:
  
  * slopes: Our javascript module.
  * bn.js: A bignumber module use by Slopes.
  * buffer: A Buffer library.
  * BinTools: A singleton built into Slopes that is used for dealing with binary data.