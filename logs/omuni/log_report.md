**/on_init**
- Timestamp not in RFC 3339 (YYYY-MM-DDTHH:MN:SS.MSSZ) Format
- provider_location.id mismatches in /on_search and /on_init
- Discrepancies between the quote object in /on_select and /on_init

**/confirm**
- provider.locations[0].id mismatches in /on_search and /confirm
- address/door mismatches in /billing in /init and /confirm
- Discrepancies between the quote object in /on_select and /confirm

**/on_confirm**
- provider.locations[0].id mismatches in /on_search and /on_confirm
- store name  /fulfillments[1]/start/location/descriptor/name can't change
- Discrepancies between the quote object /on_select and /on_confirm

**/on_status (Pending)**
-  Invoice url must be present as part of documents objects (only in Order-picked-up state and thereafter)
- /fulfillments/0/start must have required property 'time'
- /fulfillments/0/end must have required property 'time'
- /fulfillments/1/start must have required property 'time'
- /fulfillments/1/end must have required property 'time'
- provider.locations[0].id mismatches in /on_search and /on_status_pending
-  order.updated_at timestamp should match context timestamp for /on_status_pending api

**/on_status (Order-picked-up)**
- /fulfillments/0/start must have required property 'time'
- /fulfillments/0/end must have required property 'time'
- /fulfillments/1/start must have required property 'time'
- /fulfillments/1/end must have required property 'time'
- provider.locations[0].id mismatches in /on_search and /on_status_picked

**/on_status (Order-Delivered)**
- /fulfillments/0/start must have required property 'time'
- /fulfillments/0/end must have required property 'time'
- /fulfillments/1/start must have required property 'time'
- /fulfillments/1/end must have required property 'time'
- provider.locations[0].id mismatches in /on_search and /on_status_delivered

**/on_update (Initiated)**
-  must have required property 'payment'
- /items/0 must have required property 'fulfillment_id'
- /items/0/tags/status tags should only be used for part returned/cancelled items
- /fulfillments/0 must have required property 'id'
- /fulfillments/0/state/descriptor/code must be equal to one of the allowed values (Pending,Packed,Order-picked-up,Out-for-delivery,Order-delivered,RTO-Initiated,RTO-Delivered,RTO-Disposed,Cancelled)
- /fulfillments/0/start/time must have required property 'range'
- /quote must have required property 'ttl'
- /quote/breakup/0 must have required property 'title'
- quote price should not change for return state Return_Initiated
- item for which return was initiated is not present in /items
- Reverse QC fulfillment should not be created for return state Return_Initiated
- order/created_at timestamp can't change (should remain same as in /confirm)
- order created_at timestamp must always be earlier than the updated_at timestamp
