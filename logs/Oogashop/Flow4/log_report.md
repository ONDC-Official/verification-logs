**/on_select**
- /quote/breakup/2/price/value must match pattern "^(\d*.?\d{1,2})$"
- Warning: Quoted Price in /on_select INR 94 does not match with the total price of items in /select INR 196

**/init**
- Warning: items[0].quantity.count for item OOGASHOP-ONDC-4 mismatches with the items quantity selected in /select

**/on_init**
- /quote/breakup/2/price/value must match pattern "^(\d*.?\d{1,2})$"
- Warning: items[1].quantity.count for item OOGASHOP-ONDC-4 mismatches with the items quantity selected in /select
- gps coordinates in fulfillments[0].end.location mismatch in /select & /on_init

**/confirm**
- /message/order/quote/breakup/2/price/value must match pattern "^(\d*.?\d{1,2})$"
- Warning: items[0].quantity.count for item OOGASHOP-ONDC-4 mismatches with the items quantity selected in /select
- address/door mismatches in /billing in /init and /confirm
- fulfillments[0].end.location gps is not matching with gps in /select

**/on_confirm**
- /quote/breakup/2/price/value must match pattern "^(\d*.?\d{1,2})$"
- address/door mismatches in /billing in /confirm and /on_confirm
- fulfillments[0].end.location gps is not matching with gps in /select

