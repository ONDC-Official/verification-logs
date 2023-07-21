Logs submission for Seller NP By Oogashop

Hi,

We are from Paralleldots Pvt. Ltd. and submitting the logs for our seller np application Oogashop. The buyer app used for the generation of logs is ONDC Preprod Buyer Reference App and have generated logs for all the flows as per the `Test Case Scenarios v1.1` document. We have ran the log validation utility and found few suggestions. Either we are misunderstanding them or they are not valid. We are attaching them below with our comments in parenthesis just after the suggestion. Please go through them and suggest us if we are missing something.

**/on_search**

- Either one of fixed timings (range) or split timings (both frequency and times) should be provided in /bpp/providers[0]/locations[0]/time (In the earlier review, we were suggested to remove range key from schedule for  this case but still we are getting this suggestion.)
- Either one of fixed timings (range) or split timings (both frequency and times) should be provided in /bpp/providers[1]/locations[0]/time (In the earlier review, we were suggested to remove range key from schedule for  this case but still we are getting this suggestion.)

**/select**

- /message/order/items/0/quantity/count must be integer
- /message/order/items/1/quantity/count must be integer

**/on_select**

- /quote/breakup/0/@ondc~1org~1item_quantity/count must be integer (We tried to convert it to integer but then we were getting it must be string.)
- /quote/breakup/1/@ondc~1org~1item_quantity/count must be integer (We tried to convert it to integer but then we were getting it must be string.)
- Item's unit and total price mismatch for id: OOGASHOP-ONDC-47134 (We were trying to understand but did not find which key is associated to total price.)
- quote.price.value 225 does not match with the price breakup 75.00 (We have let's say quote of flow1, where it is simple calculation that 65x3+10x3=225)
- Warning: Quoted Price in /on_select INR 75 does not match with the total price of items in /select INR 225

**/init**

- /message/order/items/0/quantity/count must be integer (We tried to convert it to integer but then we were getting it must be string.)
- /message/order/items/1/quantity/count must be integer

**/on_init**

- /items/0/quantity/count must be integer (We tried to convert it to integer but then we were getting it must be string.)
- /items/1/quantity/count must be integer
- /quote/breakup/0/@ondc~1org~1item_quantity/count must be integer
- /quote/breakup/1/@ondc~1org~1item_quantity/count must be integer
- gps coordinates in fulfillments[0].end.location mismatch in /select & /on_init (They are the same, last time we were told not worry about it.)
- Quoted Price 225 does not match with Net Breakup Price 75 in /on_init (Simple calculation but we did not get it how to calculation is being done or we are misinterpreting some key.)

**/confirm**

- /message/order/quote/breakup/0/@ondc~1org~1item_quantity/count must be integer (We tried to convert it to integer but then we were getting it must be string.)
- /message/order/quote/breakup/1/@ondc~1org~1item_quantity/count must be integer
- address/door mismatches in /billing in /init and /confirm
- fulfillments[0].end.location gps is not matching with gps in /select

**/on_confirm**

- /items/0/quantity/count must be integer (We tried to convert it to integer but then we were getting it must be string.)
- /items/1/quantity/count must be integer
- /quote/breakup/0/@ondc~1org~1item_quantity/count must be integer
- /quote/breakup/1/@ondc~1org~1item_quantity/count must be integer
- address/door mismatches in /billing in /confirm and /on_confirm
- fulfillments[0].end.location gps is not matching with gps in /select

**/on_update (Liquidated)**

- must have required property 'payment' (Payment not coming from buyer app, that's why we aren't sending.)
- /items/0/quantity/count must be integer (We tried to convert it to integer but then we were getting it must be string.)
- /items/1/quantity/count must be integer
- /items/2/quantity/count must be integer
- /quote/breakup/0/@ondc~1org~1item_quantity/count must be integer
- /quote/breakup/1/@ondc~1org~1item_quantity/count must be integer
- item quantity should be updated in quote/breakup for item: OOGASHOP-ONDC-47131 when state is Liquidated
- quantity of returned item: OOGASHOP-ONDC-47131 mismatches in /update and /on_update (that is right, we are sending the right items as per recommended by doc 1.1.0)
- Item's unit and total price mismatch for id: OOGASHOP-ONDC-47134
- quote.price.value 160 does not match with the price breakup 75

Please go through all the logs of different flow and suggest us if some improvement is required as well as clarify the above confusions if they need some piece of attention from our side.

Thank you very much!!!!
