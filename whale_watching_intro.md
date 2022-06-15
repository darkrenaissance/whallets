---
title: Intro to whale wallet watching
author: serinko
header-includes: |
    \usepackage{amsmath}
Abstract: How-to notes on the practice of finding, following and analysing alpha wallets. The teaching is mainly inspired by OnchainWizzard and other professionals in the field.
---
# Introduction

**Several important tools:**

* [Etherscan](https://etherscan.io) (and the similar free scanners for AVAX, FTM, Arbitrum, etc)
* [Debank](https://debank.com/)
  * Alternativelly: [0xcheck](https://twitter.com/0xCheck) - Telegram "version" of debank account (list of own wallets, notifications etc)
* [Nansen](https://www.nansen.ai/) (a 7 day trial is $9)
* Dexscreener or dextools
* [~wiki/wallets](https://github.com/darkrenaissance/wiki/blob/master/wallets/) - our own repo to develop tools for monitoring wallets

Alpha does not mean to follow these wallets blindly. The "smart money" wallets, we aim to find, have better inside information or are better traders. It is important to analyse where is their conviction coming from to define the time horizon of the investment/trade.
For example a long term investor wallet may have a conviction, which if we did not understand and the project falls 30%, we may sell the bottom before the actual explosion.
Generally bigger gains are in smaller cap projects, where such information can help us to build stronger analyses.

Remember that crypto is a very volatile 24/7 market. No one actually knows what the price will be like in the future. This is only a tool to gain additional information and inform your own conviction.

# Ways to Find the Wallets

Except looking at top holders, there are 3 main ways to find the wallets to monitor:

1. Nansen [smart money](https://www.nansen.ai/nansen-101/introducing-smart-money) or [token god](https://www.nansen.ai/nansen-101/introducing-token-god-mode) modules
2. Finding large, early investors to a very successful project
3. Using wallets that you can find from others (reports etc)

## Nansen
Either screen for "smart money" moves on DEXs or find wallets to watch based on "notable wallets" on a token of choice.
Impotant to check the token was actually bought and not sent by a scammer who want people to get their token and rug pull.

In Nansen we can check addresses if they belong to CEX as that usually shows as a dead end on chain tracking.

*Example #1*

Using the module "smart money", we can watch an inbound capital flows from DEXs on ETH. Trying to find tokens, rather then wallets.
Weekend has a low volume and scammers may be more prominent.

![Smart Money example 1](https://substackcdn.com/image/fetch/f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fbucketeer-e05bbc84-baa3-437e-9518-adb32be77984.s3.amazonaws.com%2Fpublic%2Fimages%2F434c971d-7431-4f7a-9c2a-cb39d8866057_1302x746.png)

From the example above, only meaningful info is ALI (probably frontrunning crypto.com), the 0x.. wallets are rugpull scammers.

*Example #2*

Nansen has a smart money dashboard of changes in token holdings. Filter 7 day $ amount changes in tokens.
These are the smart money - worth to dig into a deeper research. [Here](https://github.com/darkrenaissance/wiki/blob/master/defi/l2_tokenomics.md) is a guide to evaluate a protocol. In short:

1. what the project does or is trying to solve
2. are there any near term catalysts on why the price should go up
3. how high is the relative valuation vs similar projects, and how much upside could there be
4. what are the risks

![smart money example](https://substackcdn.com/image/fetch/f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fbucketeer-e05bbc84-baa3-437e-9518-adb32be77984.s3.amazonaws.com%2Fpublic%2Fimages%2Fa143937f-d305-43f0-ac69-3adc46d7751d_1296x745.png)

This report is to learn to find wallets, not evaluate protocol. In the picture above, an interesting protocl could be MPL ( undercollateralized loans primarily for institutions). We can check MPL on Nansen in Notable wallets.
Over the time we shall aim to build a large list of wallets. The fact that the wallets are on chain helps not only to see the movement, but to evaluate and rank how did their investment go.

![30 days token move](https://substackcdn.com/image/fetch/f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fbucketeer-e05bbc84-baa3-437e-9518-adb32be77984.s3.amazonaws.com%2Fpublic%2Fimages%2Fd82083f4-973a-4d98-9c8c-50374a0f3541_1324x741.png)

ParaFi fund wallet is our main focus:

* click and copy the address
* save it to your list
* check it out on [debank](https://debank.com/profile/0x4655b7ad0b5f5bacb9cf960bbffceb3f0e51f363)

## Debank

* Connects to web3 wallet
* Possible to make profile
* Follow the list of your wallets
* clear overview of used chains
* history is simple to read
* Note: The "recieved" are scams so ignore them.  If you don't see a contract  interaction from the actual wallet holder, it means they did not buy it and it needs to be ignored. 

**Portfolio sizing in %**

We can use debank to atch the wallets and use our own conviction to generate strong analyses.
The example of PraFi and $MPL - We can make a track record assessment here as well, along with portfolio sizing perspectives.   They bought $800k of MPL, which is now worth ~$1.1mm, which is obviously a decent trade given they bought on 3/21.   So we know that this does seem to be "smart" money, with likely better information that ourselves.

Do **NOT** look at the $ invested, but the portion of portfolio in %! The investment to $MPL was just 6% so maybe it was not so high conviction or seen as having a large upside vs the risk exposure. On the other hand the $BTRFLY is nearly half of the portfolio.

**Smart Money Wallets**

Check more wallets and:

* compare them
* rank their historical investment data
* check the portfolio sizing
* activity - more active = more data
* check the size of the entire portfolio - is it a whale worth to monitor?
* see connections to new interesting wallets
* follow the money flow in big transactions

## Early Winners Method

* A time consuming method, but can be more benefitial. 
* Less accessible wallets ~ more alpha inside
* Ways to do it:
  * Filter a token through a dexscener or some dextool by $ buy size early in the project
  * Etherscan (etc) and find large buys early on.
  * It may be a good spot or inside information
  * Try to again crosscheck the history of their success
  * If active and successfull, keep a close eye on the wallet moves next time and use it with your conviction
  
Example:
Check a project which is succesfull and download the explorer history around the launch time period.
Scan through it and look for large buys or multiple calls (automatize). These wallets can give you information whether they still hold onto the project (check their debank portfolio). 
If not, you may think to sell as well. Or vise versa.

## Another Possibilities

* Discord and othe chat rooms

# Conclusion

Do not forget that these tools can be powerful if not used isolated from other knowledge. Epecially important is to understand what stage of cycle we are in.
Watching these wallets can give you token ideas, farming ideas, and give you signals of when you are early (maybe only 1 whale is in, more whales are accumulating) or late (its being shilled on CT, but whales/insiders are dumping).
Over the time it is possible to watch a tandem wallet movements, front running big CEX listing etc.