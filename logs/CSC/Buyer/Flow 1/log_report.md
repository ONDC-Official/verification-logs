**/search**
- /message/intent/payment/@ondc~1org~1buyer_app_finder_fee_type must be equal to constant (percent)

**/on_search**
- context/timestamp difference between /on_search and /search should be smaller than 5 sec

**/on_select**
- context/timestamp difference between /on_select and /select should be smaller than 5 sec
- packing line item should not be present if price=0

**/init**
- Timestamp for  /on_select api cannot be greater than or equal to /init api

**/on_init**
- context/timestamp difference between /on_init and /init should be smaller than 5 sec

**/confirm**
- /message/order/payment must have required property '@ondc/org/settlement_details'
- Timestamp for /on_init api cannot be greater than or equal to /confirm api
- created_at, updated_at, address/district_code mismatches in /billing in /init and /confirm

**/on_confirm**
- /payment must have required property '@ondc/org/settlement_details'
- context/timestamp difference between /on_confirm and /confirm should be smaller than 5 sec

**/on_status (Pending)**
- /payment must have required property '@ondc/org/settlement_details'

**/on_status (Order-picked-up)**
- /payment must have required property '@ondc/org/settlement_details'

**/on_update (Liquidated)**
- /payment must have required property '@ondc/org/settlement_details'

