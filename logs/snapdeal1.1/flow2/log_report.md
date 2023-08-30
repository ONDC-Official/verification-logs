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
- context/timestamp difference between /on_search and /search should be smaller than 5 sec

**/select**
- /message/order/items/0 must have required property 'location_id'
- /message/order/items/1 must have required property 'location_id'

**/init**
- /message/order/fulfillments/0/end/location/address/building must NOT have fewer than 3 characters
- address.building should be more than 3 chars

**/on_init**
- Discrepancies between the quote object in /on_select and /on_init

**/confirm**
- address/door mismatches in /billing in /init and /confirm
- Discrepancies between the quote object in /on_select and /confirm

**/on_confirm**
- address/door mismatches in /billing in /confirm and /on_confirm
- Discrepancies between the quote object /on_select and /on_confirm

**/on_cancel**
- cancellation_reason_id should be a valid cancellation id (unsolicited seller app initiated)

