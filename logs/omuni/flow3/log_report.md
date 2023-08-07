**/on_search**
- /message/catalog/bpp~1providers/0/items/0/@ondc~1org~1statutory_reqs_packaged_commodities/month_year_of_manufacture_packing_import must match pattern "^(?!\s*$).+"
- /message/catalog/bpp~1providers/0/items/1/@ondc~1org~1statutory_reqs_packaged_commodities/month_year_of_manufacture_packing_import must match pattern "^(?!\s*$).+"
- /message/catalog/bpp~1providers/0/items/2/@ondc~1org~1statutory_reqs_packaged_commodities/month_year_of_manufacture_packing_import must match pattern "^(?!\s*$).+"
- /message/catalog/bpp~1providers/0/items/3/@ondc~1org~1statutory_reqs_packaged_commodities/month_year_of_manufacture_packing_import must match pattern "^(?!\s*$).+"
- /message/catalog/bpp~1providers/0/items/4/@ondc~1org~1statutory_reqs_packaged_commodities/month_year_of_manufacture_packing_import must match pattern "^(?!\s*$).+"

**/init**
- /message/order/billing/address must have required property 'building'

**/on_init**
- /billing/address must have required property 'building'

**/confirm**
- /message/order/billing/address must have required property 'building'

**/on_confirm**
- /billing/address must have required property 'building'
- store name  /fulfillments[1]/start/location/descriptor/name can't change

**/on_status (Pending)**
- /billing/address must have required property 'building'
- Message Id cannot be same for different sets of APIs

**/on_status (Order-picked-up)**
- /billing/address must have required property 'building'
- Message Id cannot be same for different sets of APIs

**/on_status (Order-Delivered)**
- /billing/address must have required property 'building'
- Message Id cannot be same for different sets of APIs

