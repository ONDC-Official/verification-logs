**/on_search**
- Either one of fixed timings (range) or split timings (both frequency and times) should be provided in /bpp/providers[0]/locations[0]/time
- Either one of fixed timings (range) or split timings (both frequency and times) should be provided in /bpp/providers[1]/locations[0]/time

**/select**
- /message/order/items/0/quantity/count must be integer
- /message/order/items/1/quantity/count must be integer

**/on_select**
- /quote/breakup/0/@ondc~1org~1item_quantity/count must be integer
- /quote/breakup/1/@ondc~1org~1item_quantity/count must be integer
- Item's unit and total price mismatch for id: OOGASHOP-ONDC-47134
- quote.price.value 225 does not match with the price breakup 75.00
- Warning: Quoted Price in /on_select INR 75 does not match with the total price of items in /select INR 225

**/init**
- /message/order/items/0/quantity/count must be integer
- /message/order/items/1/quantity/count must be integer

**/on_init**
- /items/0/quantity/count must be integer
- /items/1/quantity/count must be integer
- /quote/breakup/0/@ondc~1org~1item_quantity/count must be integer
- /quote/breakup/1/@ondc~1org~1item_quantity/count must be integer
- gps coordinates in fulfillments[0].end.location mismatch in /select & /on_init
- Quoted Price 225 does not match with Net Breakup Price 75 in /on_init

**/confirm**
- /message/order/quote/breakup/0/@ondc~1org~1item_quantity/count must be integer
- /message/order/quote/breakup/1/@ondc~1org~1item_quantity/count must be integer
- address/door mismatches in /billing in /init and /confirm
- fulfillments[0].end.location gps is not matching with gps in /select

**/on_confirm**
- /items/0/quantity/count must be integer
- /items/1/quantity/count must be integer
- /quote/breakup/0/@ondc~1org~1item_quantity/count must be integer
- /quote/breakup/1/@ondc~1org~1item_quantity/count must be integer
- address/door mismatches in /billing in /confirm and /on_confirm
- fulfillments[0].end.location gps is not matching with gps in /select

**/on_update (Liquidated)**
-  must have required property 'payment'
- /items/0/quantity/count must be integer
- /items/1/quantity/count must be integer
- /items/2/quantity/count must be integer
- /quote/breakup/0/@ondc~1org~1item_quantity/count must be integer
- /quote/breakup/1/@ondc~1org~1item_quantity/count must be integer
- message_id of all unsolicited /on_update calls should be same for a particular /update request
- item quantity should be updated in quote/breakup for item: OOGASHOP-ONDC-47131 when state is Liquidated
- quantity of returned item: OOGASHOP-ONDC-47131 mismatches in /update and /on_update
- Item's unit and total price mismatch for id: OOGASHOP-ONDC-47134
- quote.price.value 160 does not match with the price breakup 75

