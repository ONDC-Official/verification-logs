**/on_search**
- context/timestamp difference between /on_search and /search should be smaller than 5 sec
- /bpp/providers[0]/locations[0]/gps coordinates must be specified with at least six decimal places of precision.

**/confirm**
- /message/order/payment must have required property '@ondc/org/settlement_details'

**/on_confirm**
- context/timestamp difference between /on_confirm and /confirm should be smaller than 5 sec
- payment object mismatches in /confirm & /on_confirm

**/on_update (Rejected)**
- Invalid quantity of items present in /order/items (returned & non-returned) for item: 4633_360598

