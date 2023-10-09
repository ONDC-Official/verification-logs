**/on_search**
- /message/catalog/bpp~1providers/0/items/0/@ondc~1org~1statutory_reqs_packaged_commodities/month_year_of_manufacture_packing_import must match pattern "^(?!\s*$).+"
- /message/catalog/bpp~1providers/0/items/1/@ondc~1org~1statutory_reqs_packaged_commodities/month_year_of_manufacture_packing_import must match pattern "^(?!\s*$).+"
- /message/catalog/bpp~1providers/0/items/2/@ondc~1org~1statutory_reqs_packaged_commodities/month_year_of_manufacture_packing_import must match pattern "^(?!\s*$).+"
- /message/catalog/bpp~1providers/0/items/3/@ondc~1org~1statutory_reqs_packaged_commodities/month_year_of_manufacture_packing_import must match pattern "^(?!\s*$).+"
- /message/catalog/bpp~1providers/0/items/4/@ondc~1org~1statutory_reqs_packaged_commodities/month_year_of_manufacture_packing_import must match pattern "^(?!\s*$).+"

**/on_select**
- Warning: Quoted Price in /on_select INR 1798 does not match with the total price of items in /select INR 3596

**/on_init**
- items[0].fulfillment_id mismatches for Item 8903017060338 in /on_select and /on_init
- Discrepancies between the quote object in /on_select and /on_init

**/confirm**
- address/door mismatches in /billing in /init and /confirm
- Discrepancies between the quote object in /on_select and /confirm

**/on_confirm**
- store name  /fulfillments[0]/start/location/descriptor/name can't change
- Discrepancies between the quote object /on_select and /on_confirm

