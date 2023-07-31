**/on_search**
- /message/catalog/bpp~1providers/0/items/0/descriptor/images must NOT have more than 3 items
- /message/catalog/bpp~1providers/0/items/1/descriptor/images must NOT have more than 3 items
- /message/catalog/bpp~1providers/0/items/2/descriptor/images must NOT have more than 3 items
- /message/catalog/bpp~1providers/0/items/3/descriptor/images must NOT have more than 3 items
- context/timestamp difference between /on_search and /search should be smaller than 5 sec

**/on_select**
- Warning: Quoted Price in /on_select INR 4745 does not match with the total price of items in /select INR 4740

**/on_confirm**
- order.updated_at timestamp should be updated as per the context.timestamp (since default fulfillment state is added)

**/on_status (Order-picked-up)**
- /fulfillments/0/end must have required property 'time'

**/on_update (Initiated)**
- /quote must have required property 'ttl'
- message_id of all unsolicited /on_update calls should be same for a particular /update request

**/on_update (Liquidated)**
-  must have required property 'created_at'
-  must have required property 'updated_at'
- message_id of all unsolicited /on_update calls should be same for a particular /update request
- order/updated_at timestamp can't be future dated (should match context/timestamp)
- order/created_at timestamp can't change (should remain same as in /confirm)

