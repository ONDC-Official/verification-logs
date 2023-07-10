**/on_search**
- Timestamp not in RFC 3339 (YYYY-MM-DDTHH:MN:SS.MSSZ) Format
- context/timestamp difference between /on_search and /search should be smaller than 5 sec
- Either one of fixed timings (range) or split timings (both frequency and times) should be provided in /bpp/providers[0]/locations[0]/time

**/select**
- /message/order/items/0/quantity/count must be integer
- /message/order/items/1/quantity/count must be integer

**/on_select**
- Timestamp not in RFC 3339 (YYYY-MM-DDTHH:MN:SS.MSSZ) Format
- /quote/breakup/0/@ondc~1org~1item_quantity/count must be integer
- /quote/breakup/2/@ondc~1org~1item_quantity/count must be integer
- /quote/breakup/3/price/value must match pattern "^(\d*.?\d{1,2})$"
- /fulfillments[0]/@ondc/org/TAT (O2D) in /on_select can't be smaller than @ondc/org/time_ship (O2S) in /on_search
- invalid  id: OOGASHOP-ONDC-11 in delivery line item (should be a valid fulfillment_id)
- invalid  id: OOGASHOP-ONDC-12 in delivery line item (should be a valid fulfillment_id)

**/init**
- /message/order/items/0/quantity/count must be integer
- /message/order/items/1/quantity/count must be integer

**/on_init**
- /items/0/quantity/count must be integer
- /items/1/quantity/count must be integer
- /quote/breakup/0/@ondc~1org~1item_quantity/count must be integer
- /quote/breakup/2/@ondc~1org~1item_quantity/count must be integer
- /quote/breakup/3/price/value must match pattern "^(\d*.?\d{1,2})$"
- Timestamp not in RFC 3339 (YYYY-MM-DDTHH:MN:SS.MSSZ) Format
- gps coordinates in fulfillments[0].end.location mismatch in /select & /on_init
- Discrepancies between the quote object in /on_select and /on_init

**/confirm**
- /message/order/quote/breakup/0/@ondc~1org~1item_quantity/count must be integer
- /message/order/quote/breakup/2/@ondc~1org~1item_quantity/count must be integer
- /message/order/quote/breakup/3/price/value must match pattern "^(\d*.?\d{1,2})$"
- address/door mismatches in /billing in /init and /confirm
- fulfillments[0].end.location gps is not matching with gps in /select
- Discrepancies between the quote object in /on_select and /confirm

**/on_confirm**
- /items/0/quantity/count must be integer
- /items/1/quantity/count must be integer
- /quote/breakup/0/@ondc~1org~1item_quantity/count must be integer
- /quote/breakup/2/@ondc~1org~1item_quantity/count must be integer
- /quote/breakup/3/price/value must match pattern "^(\d*.?\d{1,2})$"
- Timestamp not in RFC 3339 (YYYY-MM-DDTHH:MN:SS.MSSZ) Format
- order.created_at timestamp mismatches in /confirm and /on_confirm
- address/door mismatches in /billing in /confirm and /on_confirm
- fulfillments[0].end.location gps is not matching with gps in /select
- Discrepancies between the quote object /on_select and /on_confirm

**/on_status (Order-picked-up)**
- /items/0/quantity/count must be integer
- /items/1/quantity/count must be integer
- /quote/breakup/0/@ondc~1org~1item_quantity/count must be integer
- /quote/breakup/2/@ondc~1org~1item_quantity/count must be integer
- /quote/breakup/3/price/value must match pattern "^(\d*.?\d{1,2})$"
- Timestamp not in RFC 3339 (YYYY-MM-DDTHH:MN:SS.MSSZ) Format
- Message Id cannot be same for different sets of APIs
- address/door mismatches in /billing in /confirm and /on_status_picked
- order/created_at timestamp can't change (should remain same as in /confirm)
- order created_at timestamp must always be earlier than the updated_at timestamp
- fulfillments/state should be Order-picked-up for /on_status_picked

**/on_status (Order-Delivered)**
- /items/0/quantity/count must be integer
- /items/1/quantity/count must be integer
- /quote/breakup/0/@ondc~1org~1item_quantity/count must be integer
- /quote/breakup/2/@ondc~1org~1item_quantity/count must be integer
- /quote/breakup/3/price/value must match pattern "^(\d*.?\d{1,2})$"
- Timestamp not in RFC 3339 (YYYY-MM-DDTHH:MN:SS.MSSZ) Format
- Message Id cannot be same for different sets of APIs
- address/door mismatches in /billing in /confirm and /on_status_delivered
- order/created_at timestamp can't change (should remain same as in /confirm)
- order created_at timestamp must always be earlier than the updated_at timestamp
- order/updated_at timestamp can't be less than the delivery time

