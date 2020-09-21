# Staking

This document explains staking on the Avalanche network.
See the [quickstart guide](quickstart.md) for a step-by-step guide to staking.

## Validators

The security of the Avalanche Network is secured by a group of computers called **validators**.
Validators create new blocks/vertices and process transactions.
As part of Avalanche consensus, validators repeatedly sample each other.

The probability that a given validator is sampled is proportional to its **stake**.
A stake is a bond, in AVAX tokens, put forward by a node in order to become a validator.

When you add a node to the validator set you specify:

* Your node's ID
* When you want to start and stop validating
* How many AVAX you are staking
* The address to send any rewards to
* Your delegation fee rate (see below)

## Validator rewards

Validators receive a reward, in AVAX, to incentivize them to secure the network.
A validator only receives a reward if they are sufficiently correct and responsive while it was validating. 
The size of the reward depends on how long they validate, how much they stake, and how many AVAX tokens exist.

## Timeline of fund movement for validators

When you issue the transaction to add a validator, the staked tokens and transaction fee are deducted from the addresses you control.
When you are done validating, the staked funds are returned to the addresses they came from.
If you earned a reward, it is sent to the address you specified when you added yourself as a validator.

## Delegators

You can stake your own tokens in order to increase the sampling weight of another validator.
This is called delegation.

When you delegate stake to a validator you specify:

* The ID of the node you're delegating to
* When you want to start/stop delegating stake (must be while the validator is validating)
* How many AVAX you are staking
* The address to send any rewards to

## Delegator rewards

If the validator that you delegate stake to is sufficiently correct and responsive while you delegate stake to them, you receive a reward when you are done delegating to them.
Delegators are rewarded according to the same function as validators.
However, the validator that you delegate to keeps a portion of your reward.
The percentage of your reward that they keep is specified by the validator's delegation fee rate,
If it's set to 10%, then they keep 10% of any rewards from stake delegated to them.

## Timeline of fund movement for delegators

When you issue the transaction to delegate stake, the staked tokens and transaction fee are deducted from the addresses you control.
When you are done delegating stake, the staked funds are returned to the addresses they came from.
If you earned a reward, it is sent to the address you specified when you delegated stake.

## Staking parameters

* The minimum amount that a validator must stake is 2,000 AVAX
* The minimum amount that a delegator must stake is 25 AVAX
* The minimum amount of time one can stake funds for validation is 2 weeks
* The maximum amount of time one can stake funds for validation is 1 year
* The minimum amount of time one can stake funds for delegation is 2 weeks
* The maximum amount of time one can stake funds for delegation is 1 year
* The maximum weight of a validator (their own stake + stake delegated to them) is the minimum of 3e6 AVAX and 5 times the amount the validator staked
* The minimum percentage of the time a validator must be correct and online in order to receive a reward is 60%.