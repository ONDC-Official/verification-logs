**/on_search**
- /message/catalog/bpp~1providers/0/items/0/@ondc~1org~1statutory_reqs_packaged_commodities/month_year_of_manufacture_packing_import must match pattern "^(?!\s*$).+"
- /message/catalog/bpp~1providers/0/items/1/@ondc~1org~1statutory_reqs_packaged_commodities/month_year_of_manufacture_packing_import must match pattern "^(?!\s*$).+"
- /message/catalog/bpp~1providers/0/items/2/@ondc~1org~1statutory_reqs_packaged_commodities/month_year_of_manufacture_packing_import must match pattern "^(?!\s*$).+"
- /message/catalog/bpp~1providers/0/items/3/@ondc~1org~1statutory_reqs_packaged_commodities/month_year_of_manufacture_packing_import must match pattern "^(?!\s*$).+"
- /message/catalog/bpp~1providers/0/items/4/@ondc~1org~1statutory_reqs_packaged_commodities/month_year_of_manufacture_packing_import must match pattern "^(?!\s*$).+"

**/confirm**
- address/door mismatches in /billing in /init and /confirm

**/on_confirm**
- store name  /fulfillments[1]/start/location/descriptor/name can't change

**/on_status (Pending)**
- Message Id cannot be same for different sets of APIs

**/on_status (Order-picked-up)**
- Message Id cannot be same for different sets of APIs

**/on_status (Order-Delivered)**
- Message Id cannot be same for different sets of APIs

**/on_update (Return_Approved)**
- returned item: 8903017060376 should not be removed from quote when return state is Return_Approved
- quote price should not change for return state Return_Approved

