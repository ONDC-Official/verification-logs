**/on_search**
- Either one of fixed timings (range) or split timings (both frequency and times) should be provided in /bpp/providers[0]/locations[0]/time
- Either one of fixed timings (range) or split timings (both frequency and times) should be provided in /bpp/providers[1]/locations[0]/time

**/select**
- /message/order/items/0/quantity/count must be integer
- /message/order/items/1/quantity/count must be integer

**/on_select**
- /quote/breakup/0/@ondc~1org~1item_quantity/count must be integer
- /quote/breakup/2/@ondc~1org~1item_quantity/count must be integer
- context/timestamp difference between /on_select and /select should be smaller than 5 sec
- Count of item with id: OOGASHOP-ONDC-47131 does not match in select & on_select (suitable domain error should be provided)
- Item's unit and total price mismatch for id: OOGASHOP-ONDC-47134
- item with id: OOGASHOP-ONDC-47131 in quote.breakup[2] does not exist in items[]
- quote.price.value 105 does not match with the price breakup 35.00
- Warning: Quoted Price in /on_select INR 35 does not match with the total price of items in /select INR 150

**/init**
- /message/order/items/0/quantity/count must be integer
- /message/order/items/1 must have required property 'fulfillment_id'
- /message/order/items/1/quantity/count must be integer
- Item Id OOGASHOP-ONDC-47131 does not exist in /on_select
- Warning: items[1].quantity.count for item OOGASHOP-ONDC-47131 mismatches with the items quantity selected in /select

**/on_init**
- /items/0/quantity/count must be integer
- /quote/breakup/0/@ondc~1org~1item_quantity/count must be integer
- gps coordinates in fulfillments[0].end.location mismatch in /select & /on_init
- Quoted Price 105 does not match with Net Breakup Price 35 in /on_init
- Discrepancies between the quote object in /on_select and /on_init

**/confirm**
- /message/order/items/1 must have required property 'fulfillment_id'
- /message/order/quote/breakup/0/@ondc~1org~1item_quantity/count must be integer
- Item Id OOGASHOP-ONDC-47131 does not exist in /on_select
- Warning: items[1].quantity.count for item OOGASHOP-ONDC-47131 mismatches with the items quantity selected in /select
- address/door mismatches in /billing in /init and /confirm
- fulfillments[0].end.location gps is not matching with gps in /select
- Discrepancies between the quote object in /on_select and /confirm

**/on_confirm**
- /items/0/quantity/count must be integer
- /quote/breakup/0/@ondc~1org~1item_quantity/count must be integer
- /quote/breakup/2/@ondc~1org~1item_quantity/count must be integer
- address/door mismatches in /billing in /confirm and /on_confirm
- fulfillments[0].end.location gps is not matching with gps in /select

