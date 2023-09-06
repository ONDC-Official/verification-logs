**/on_select**
- /quote/breakup/5/price/value must match pattern "^(\d*.?\d{1,2})$"
- Warning: Quoted Price in /on_select INR 840 does not match with the total price of items in /select INR 1240

**/init**
- Warning: items[1].quantity.count for item item_007 mismatches with the items quantity selected in /select

**/on_init**
- /quote/breakup/5/price/value must match pattern "^(\d*.?\d{1,2})$"
- Warning: items[1].quantity.count for item item_007 mismatches with the items quantity selected in /select

**/confirm**
- /message/order/quote/breakup/5/price/value must match pattern "^(\d*.?\d{1,2})$"
- Warning: items[1].quantity.count for item item_007 mismatches with the items quantity selected in /select

**/on_confirm**
- /quote/breakup/5/price/value must match pattern "^(\d*.?\d{1,2})$"

**/on_status (Pending)**
- /quote/breakup/5/price/value must match pattern "^(\d*.?\d{1,2})$"

**/on_status (Order-picked-up)**
- /quote/breakup/5/price/value must match pattern "^(\d*.?\d{1,2})$"

**/on_status (Order-Delivered)**
- /quote/breakup/5/price/value must match pattern "^(\d*.?\d{1,2})$"

**/on_update (Initiated)**
- /quote/breakup/5/price/value must match pattern "^(\d*.?\d{1,2})$"

**/on_update (Return_Approved)**
- /quote/breakup/5/price/value must match pattern "^(\d*.?\d{1,2})$"

**/on_update (Return_Picked)**
- /quote/breakup/5/price/value must match pattern "^(\d*.?\d{1,2})$"

**/on_update (Return_Delivered)**
- /quote/breakup/5/price/value must match pattern "^(\d*.?\d{1,2})$"

