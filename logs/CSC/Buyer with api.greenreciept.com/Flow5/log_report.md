**/on_search**
- context/timestamp difference between /on_search and /search should be smaller than 5 sec
- /bpp/providers[0]/locations[0]/gps coordinates must be specified with at least six decimal places of precision.

**/on_select**
- context/timestamp difference between /on_select and /select should be smaller than 5 sec
- Warning: Quoted Price in /on_select INR 51000 does not match with the total price of items in /select INR 55500

**/init**
- Warning: items[1].quantity.count for item 4633_360599 mismatches with the items quantity selected in /select

**/on_init**
- context/timestamp difference between /on_init and /init should be smaller than 5 sec
- Warning: items[1].quantity.count for item 4633_360599 mismatches with the items quantity selected in /select

**/confirm**
- /message/order/payment must have required property '@ondc/org/settlement_details'
- Warning: items[1].quantity.count for item 4633_360599 mismatches with the items quantity selected in /select

**/on_confirm**
- context/timestamp difference between /on_confirm and /confirm should be smaller than 5 sec
- payment object mismatches in /confirm & /on_confirm

