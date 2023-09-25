**/on_select**
- /quote/breakup/4/price/value must match pattern "^(\d*.?\d{1,2})$"
- Warning: Quoted Price in /on_select INR 440 does not match with the total price of items in /select INR 1240

**/on_init**
- /quote/breakup/4/price/value must match pattern "^(\d*.?\d{1,2})$"
- Discrepancies between the quote object in /on_select and /on_init

**/confirm**
- /message/order/quote/breakup/4/price/value must match pattern "^(\d*.?\d{1,2})$"
- Discrepancies between the quote object in /on_select and /confirm

**/on_confirm**
- /quote/breakup/4/price/value must match pattern "^(\d*.?\d{1,2})$"
- Discrepancies between the quote object /on_select and /on_confirm

**/on_status (Pending)**
- /quote/breakup/3/price/value must match pattern "^(\d*.?\d{1,2})$"

