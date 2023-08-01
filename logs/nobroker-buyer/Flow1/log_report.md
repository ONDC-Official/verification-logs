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

**/on_update (Liquidated)**
-  must have required property 'created_at'
-  must have required property 'updated_at'
- Invalid quote/breakup item: 32AE547A9C88B65D08D8A5FC8BAE79B0_43459841294595_default can't have multiple objects
- order/updated_at timestamp can't be future dated (should match context/timestamp)
- order/created_at timestamp can't change (should remain same as in /confirm)

