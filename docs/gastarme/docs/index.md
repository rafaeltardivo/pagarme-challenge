# Welcome to Gastar.me

A service built to make your life easier by improving your payment experience.

## How it works

**Gastar.me** will manage all of your credit cards and choose the best considering the billing date and credit limit.


## Card Management Criteria

#### Billing date
Let's say you have a wallet with these two cards:

|   |  Number |  Limit |  Billing Day |
|---|---|---|---|
|  *Card One* | 4291749290818600  | 900.00  |  9 |
|  *Card Two*  | 4291749290818622  | 800.00  | 8  |

The **first priority** is the later billing date, so the card chosen is the one who bills later, which is the **Card One**.

#### Limit
Let's say you have a wallet with these two cards:

|   |  Number |  Limit |  Billing Day |
|---|---|---|---|
|  *Card One* | 4291749290818600  | 900.00  |  8 |
|  *Card Two*  | 4291749290818622  | 800.00  | 8  |

The **second priority** is the lower limit. Since they are billed on the same day, **Card Two** will be chosen for having the lower credit limit.

#### Using more than one card

If your purchase exceeds the chosen card limit, the next one will be used considering the same criteria.

