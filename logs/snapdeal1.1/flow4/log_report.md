**/on_search**
- /message/catalog/bpp~1providers/0/items/0/category_id category_id should be one of the valid categories as defined in [enhanced sub-category list](https://docs.google.com/spreadsheets/d/1ayRbp-WmXwwbzp7z1MgRO0NuKZM1AQk4GGZ8SE4NTnw/edit#gid=0)
- /message/catalog/bpp~1providers/0/items/1/category_id category_id should be one of the valid categories as defined in [enhanced sub-category list](https://docs.google.com/spreadsheets/d/1ayRbp-WmXwwbzp7z1MgRO0NuKZM1AQk4GGZ8SE4NTnw/edit#gid=0)
- /message/catalog/bpp~1providers/0/items/2/category_id category_id should be one of the valid categories as defined in [enhanced sub-category list](https://docs.google.com/spreadsheets/d/1ayRbp-WmXwwbzp7z1MgRO0NuKZM1AQk4GGZ8SE4NTnw/edit#gid=0)
- /message/catalog/bpp~1providers/0/items/3/category_id category_id should be one of the valid categories as defined in [enhanced sub-category list](https://docs.google.com/spreadsheets/d/1ayRbp-WmXwwbzp7z1MgRO0NuKZM1AQk4GGZ8SE4NTnw/edit#gid=0)
- /message/catalog/bpp~1providers/0/items/4/category_id category_id should be one of the valid categories as defined in [enhanced sub-category list](https://docs.google.com/spreadsheets/d/1ayRbp-WmXwwbzp7z1MgRO0NuKZM1AQk4GGZ8SE4NTnw/edit#gid=0)
- /message/catalog/bpp~1providers/0/items/5/category_id category_id should be one of the valid categories as defined in [enhanced sub-category list](https://docs.google.com/spreadsheets/d/1ayRbp-WmXwwbzp7z1MgRO0NuKZM1AQk4GGZ8SE4NTnw/edit#gid=0)
- /message/catalog/bpp~1providers/0/items/6/category_id category_id should be one of the valid categories as defined in [enhanced sub-category list](https://docs.google.com/spreadsheets/d/1ayRbp-WmXwwbzp7z1MgRO0NuKZM1AQk4GGZ8SE4NTnw/edit#gid=0)

**/select**
- /message/order/items/0 must have required property 'location_id'
- /message/order/items/1 must have required property 'location_id'

**/on_select**
- context/timestamp difference between /on_select and /select should be smaller than 5 sec
- Warning: Quoted Price in /on_select INR 1659 does not match with the total price of items in /select INR 2212

**/init**
- Warning: items[1].quantity.count for item SDL365501449_0cac8d mismatches with the items quantity selected in /select

**/on_init**
- Warning: items[1].quantity.count for item SDL365501449_0cac8d mismatches with the items quantity selected in /select
- Discrepancies between the quote object in /on_select and /on_init

**/confirm**
- Warning: items[1].quantity.count for item SDL365501449_0cac8d mismatches with the items quantity selected in /select
- address/door mismatches in /billing in /init and /confirm
- Discrepancies between the quote object in /on_select and /confirm

**/on_confirm**
- Discrepancies between the quote object /on_select and /on_confirm

**/on_update (Return_Delivered)**
- /fulfillments/1/start/location must have required property 'descriptor'

