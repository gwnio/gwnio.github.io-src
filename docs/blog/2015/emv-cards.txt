Title: EMV Cards
Date: 2015-09-08 11:10:23 -0400
Tags: emv cards

The following are some notes I took while doing research on EMV cards.

<!-- PELICAN_END_SUMMARY -->

## EMV - Europay, MasterCard and Visa (aka chip card, smart card, etc)

* cards equipped with computer chips and the technology used to authenticate chip-card transactions making retail shopping more secure
* magnetic strips will remain unchanged, whoever accesses that data gains sensitive card information
* every time a EMV card is used, the card chip creates a unique transaction ID to every purchase, that unique ID cannot be used again
    * If a hacker stole the chip information from one specific point of sale, typical card duplication would never work "because the stolen transaction number created in that instance wouldn't be usable again and the card would just get denied," Witts says.
* Chip cards don't eliminate the problem of fraud. In particular, these cards still have numbers, expiry dates, and three-digit codes on their backs. Someone could copy this information and use it to make purchases online. A chip-and-signature card could be used at a point-of-sale terminal along with a forged signature. The magnetic strip can still be used in the old way at many terminals around the world.
    * But, although chip cards won't eliminate all fraud, they will make fraud more difficult. This will also help prevent future breaches of payment systems - like the one that happened at Target - from being so damaging.

## No longer just card swiping
* card dipping
    * inserted into a terminal slot; card legitimacy verified and unique transaction data created
* contactless transactions; near field communication (NFC)
    * tap against a terminal scanner
* financial institutions are issuing contact cards (for card dipping)

## Enter a PIN?
* a PIN connects the payment terminal to the payment processor for real-time transaction verification and approval
    * many payment processors are not equipped with the technology to handle EMV chip-and-PIN credit transactions
    * many issuers will just be issuing chip-and-signature cards

## Fraud liability
* currently, if an in-store transaction is conducted using a counterfeit or compromised card, consumer losses from that transaction fall back on the payment processor
* after October 1, 2015 the liability will shift to whichever party is least EMV-compliant in a fraudulent transaction
* merchant responsible
    * If a consumer presents a chip card at a merchant that does not have EMV-enabled equipment, the liability for credit card fraud will shift to the merchant
* card issuer responsible
    * If a traditional magstripe card is presented at an EMV-enabled terminal, the card issuer will be responsible for any financial liability resulting from fraudulent transactions
* while compliance is not mandatory, card issuers are bringing people on board with EMV by encouraging compliance to avoid liability costs

## Chip-card retailer support
* The first round of EMV cards -- many of which are already in consumers' hands -- will be equipped with both chip and magnetic-stripe functions so consumer spending is not disrupted and merchants can adjust.

## EMV payment options in online world
* MasterCard - Chip Authenticated Program (CAP)
* Visa - Dynamic Passcode Authentication (DPA)
* Many e-commerce stores throughout Europe have already begun using these two EMV security features with their own online customers. And they could soon become mandatory for e-stores in the Americas.

## Card-not-present (CNP) merchants
* CNP merchants will see a rise in fraudulent transactions as thieves migrate towards least secure channels
    * "In the United Kingdom, online fraud -- known in the industry as 'card not present,' or CNP, fraud -- rose 79 percent in the first three years after the country switched to chip cards, and it more than doubled in Australia and Canada, according to Aite Group."
* Senior Payment Analyst at Javelin Strategy & Research. "CNP fraud cannot be underestimated in growth or expense."
* Javelin predicts CNP fraud in the U.S. to be nearly four times greater than fraud at the POS by 2018, simply because of the explosive growth expected in the number of e-commerce transactions
    * While the U.S. migration to EMV is expected to curb card present fraud, experts are predicting that it may lead to an increase in card not present fraud- when the UK migrated to EMV in 2004 and 2005, online CNP fraud increased from  $184 million in 2005 when EMV was fully implemented to $283 million in 2007.
* So how can you protect your customers and your business? Using AVS (Address Verification) and CVV (Card Validation Values or security code) are definitely steps in the right direction.  [Other fraud management tools](https://www.bluepay.com/payment-processing/pci-compliance/fraud-management-tools/){:target="_blank"}:
    * On-hold functionality
    * Velocity filter
    * Threshold
    * AVS
    * CVV
    * Card Issuing Country
    * Geo IP Tracking
    * Negative Database