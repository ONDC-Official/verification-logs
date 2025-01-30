**/on_select**
- Warning: Quoted Price in /on_select INR 370 does not match with the total price of items in /select INR 420

**/init**
- Warning: items[1].quantity.count for item OOGASHOP-ONDC-47098 mismatches with the items quantity selected in /select

**/on_init**
- Warning: items[0].quantity.count for item OOGASHOP-ONDC-47098 mismatches with the items quantity selected in /select
- gps coordinates in fulfillments[0].end.location mismatch in /select & /on_init

**/confirm**
- Warning: items[1].quantity.count for item OOGASHOP-ONDC-47098 mismatches with the items quantity selected in /select
- address/door mismatches in /billing in /init and /confirm
- fulfillments[0].end.location gps is not matching with gps in /select

**/on_confirm**
- address/door mismatches in /billing in /confirm and /on_confirm
- fulfillments[0].end.location gps is not matching with gps in /select

**/on_status (Pending)**
- address/door mismatches in /billing in /confirm and /on_status_pending

**/on_status (Order-picked-up)**
- address/door mismatches in /billing in /confirm and /on_status_picked

**/on_status (Order-Delivered)**
- address/door mismatches in /billing in /confirm and /on_status_delivered

