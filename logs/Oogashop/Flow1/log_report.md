**/on_search**
- Timestamp not in RFC 3339 (YYYY-MM-DDTHH:MN:SS.MSSZ) Format
- Either one of fixed timings (range) or split timings (both frequency and times) should be provided in /bpp/providers[0]/locations[0]/time

**/select**
- /message/order/items/0/quantity/count must be integer
- /message/order/items/1/quantity/count must be integer

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
- Quoted Price in /on_init INR 148 does not match with the quoted price in /on_select INR undefined
- Discrepancies between the quote object in /on_select and /on_init

**/confirm**
- /message/order/quote/breakup/0/@ondc~1org~1item_quantity/count must be integer
- /message/order/quote/breakup/2/@ondc~1org~1item_quantity/count must be integer
- /message/order/quote/breakup/3/price/value must match pattern "^(\d*.?\d{1,2})$"
- address/door mismatches in /billing in /init and /confirm
- Discrepancies between the quote object in /on_select and /confirm
- Quoted Price in /confirm INR 148 does not match with the quoted price in /on_select INR undefined

**/on_confirm**
- /items/0/quantity/count must be integer
- /items/1/quantity/count must be integer
- /quote/breakup/0/@ondc~1org~1item_quantity/count must be integer
- /quote/breakup/2/@ondc~1org~1item_quantity/count must be integer
- /quote/breakup/3/price/value must match pattern "^(\d*.?\d{1,2})$"
- Timestamp not in RFC 3339 (YYYY-MM-DDTHH:MN:SS.MSSZ) Format
- order.created_at timestamp mismatches in /confirm and /on_confirm
- address/door mismatches in /billing in /confirm and /on_confirm
- Discrepancies between the quote object /on_select and /on_confirm
- Quoted Price in /on_confirm 148 does not match with the quoted price in /on_select undefined

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

