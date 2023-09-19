**/on_search**
- /message/catalog/bpp~1providers/0/items/0/descriptor/images must NOT have more than 3 items
- /message/catalog/bpp~1providers/0/items/1/descriptor/images must NOT have more than 3 items

**/on_select**
- Warning: Quoted Price in /on_select INR 408 does not match with the total price of items in /select INR 507

**/init**
- value of address.name, address.building and address.locality should be unique
- Warning: items[0].quantity.count for item 64f5c5e4e74e8b40056721df mismatches with the items quantity selected in /select

**/on_init**
- Timestamp for init api cannot be greater than or equal to on_init api
- Warning: items[0].quantity.count for item 64f5c5e4e74e8b40056721df mismatches with the items quantity selected in /select

**/confirm**
- Warning: items[0].quantity.count for item 64f5c5e4e74e8b40056721df mismatches with the items quantity selected in /select
- address/door mismatches in /billing in /init and /confirm

**/update**
- /message/order/items/0/tags/ttl_approval must match format "duration"

**/on_update (Return_Picked)**
- available count can't be greater than maximum count for item id: 64f5c5e4e74e8b40056721da

**/on_update (Return_Delivered)**
- available count can't be greater than maximum count for item id: 64f5c5e4e74e8b40056721da

**/update (Refund)**
- /message/order/items/0/tags/ttl_approval must match format "duration"

