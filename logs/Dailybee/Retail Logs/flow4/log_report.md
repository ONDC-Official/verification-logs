**/on_search**
- Either one of fixed (range) or split (frequency and times) timings should be provided in /bpp/providers[0]/locations[0]/time

**/on_select**
- Warning: Quoted Price in /on_select INR 710.8 does not match with the total price of items in /select INR 805.8

**/init**
- value of address.name, address.building and address.locality should be unique
- Warning: items[0].quantity.count for item 62d8068348fd04957a9a8a4f mismatches with the items quantity selected in /select

**/on_init**
- Warning: items[0].quantity.count for item 62d8068348fd04957a9a8a4f mismatches with the items quantity selected in /select
- Discrepancies between the quote object in /on_select and /on_init

**/confirm**
- Warning: items[0].quantity.count for item 62d8068348fd04957a9a8a4f mismatches with the items quantity selected in /select
- address/door mismatches in /billing in /init and /confirm
- Discrepancies between the quote object in /on_select and /confirm

**/on_confirm**
- Discrepancies between the quote object /on_select and /on_confirm

**/update**
- /message/order/items/0/tags/ttl_approval must match format "duration"

