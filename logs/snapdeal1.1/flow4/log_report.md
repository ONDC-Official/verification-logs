**/on_search**
- /message/catalog/bpp~1providers/0/items/0/category_id category_id should be one of the valid categories as defined in [enhanced sub-category list](https://docs.google.com/spreadsheets/d/1ayRbp-WmXwwbzp7z1MgRO0NuKZM1AQk4GGZ8SE4NTnw/edit#gid=0)
- /message/catalog/bpp~1providers/0/items/1/category_id category_id should be one of the valid categories as defined in [enhanced sub-category list](https://docs.google.com/spreadsheets/d/1ayRbp-WmXwwbzp7z1MgRO0NuKZM1AQk4GGZ8SE4NTnw/edit#gid=0)
- /message/catalog/bpp~1providers/0/items/2/category_id category_id should be one of the valid categories as defined in [enhanced sub-category list](https://docs.google.com/spreadsheets/d/1ayRbp-WmXwwbzp7z1MgRO0NuKZM1AQk4GGZ8SE4NTnw/edit#gid=0)
- /message/catalog/bpp~1providers/0/items/3/category_id category_id should be one of the valid categories as defined in [enhanced sub-category list](https://docs.google.com/spreadsheets/d/1ayRbp-WmXwwbzp7z1MgRO0NuKZM1AQk4GGZ8SE4NTnw/edit#gid=0)
- /message/catalog/bpp~1providers/0/items/4/category_id category_id should be one of the valid categories as defined in [enhanced sub-category list](https://docs.google.com/spreadsheets/d/1ayRbp-WmXwwbzp7z1MgRO0NuKZM1AQk4GGZ8SE4NTnw/edit#gid=0)
- /message/catalog/bpp~1providers/0/items/5/category_id category_id should be one of the valid categories as defined in [enhanced sub-category list](https://docs.google.com/spreadsheets/d/1ayRbp-WmXwwbzp7z1MgRO0NuKZM1AQk4GGZ8SE4NTnw/edit#gid=0)
- /message/catalog/bpp~1providers/0/items/6/category_id category_id should be one of the valid categories as defined in [enhanced sub-category list](https://docs.google.com/spreadsheets/d/1ayRbp-WmXwwbzp7z1MgRO0NuKZM1AQk4GGZ8SE4NTnw/edit#gid=0)
- /message/catalog/bpp~1providers/0/items/7/category_id category_id should be one of the valid categories as defined in [enhanced sub-category list](https://docs.google.com/spreadsheets/d/1ayRbp-WmXwwbzp7z1MgRO0NuKZM1AQk4GGZ8SE4NTnw/edit#gid=0)
- /message/catalog/bpp~1providers/0/items/8/category_id category_id should be one of the valid categories as defined in [enhanced sub-category list](https://docs.google.com/spreadsheets/d/1ayRbp-WmXwwbzp7z1MgRO0NuKZM1AQk4GGZ8SE4NTnw/edit#gid=0)
- /message/catalog/bpp~1providers/0/items/9/category_id category_id should be one of the valid categories as defined in [enhanced sub-category list](https://docs.google.com/spreadsheets/d/1ayRbp-WmXwwbzp7z1MgRO0NuKZM1AQk4GGZ8SE4NTnw/edit#gid=0)
- context/timestamp difference between /on_search and /search should be smaller than 5 sec

**/select**
- /message/order/items/0 must have required property 'location_id'
- /message/order/items/1 must have required property 'location_id'

**/on_select**
- context/timestamp difference between /on_select and /select should be smaller than 5 sec
- Warning: Quoted Price in /on_select INR 1659 does not match with the total price of items in /select INR 2212

**/init**
- Warning: items[1].quantity.count for item SDL097402002_0cac8d mismatches with the items quantity selected in /select

**/on_init**
- Warning: items[1].quantity.count for item SDL097402002_0cac8d mismatches with the items quantity selected in /select
- Discrepancies between the quote object in /on_select and /on_init

**/confirm**
- Warning: items[1].quantity.count for item SDL097402002_0cac8d mismatches with the items quantity selected in /select
- address/door mismatches in /billing in /init and /confirm
- Discrepancies between the quote object in /on_select and /confirm

**/on_confirm**
- address/door mismatches in /billing in /confirm and /on_confirm
- Discrepancies between the quote object /on_select and /on_confirm

**/on_status (Order-Delivered)**
- address/country, address/door mismatches in /billing in /confirm and /on_status_delivered

**/on_update (Initiated)**
- Item's unit and total price mismatch for id: SDL133546301_0cac8d

**/on_update (Return_Delivered)**
- Item's unit and total price mismatch for id: SDL133546301_0cac8d

