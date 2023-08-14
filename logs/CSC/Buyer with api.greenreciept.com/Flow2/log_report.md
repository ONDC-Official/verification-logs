**/on_search**
- context/timestamp difference between /on_search and /search should be smaller than 5 sec
- /bpp/providers[0]/locations[0]/gps coordinates must be specified with at least six decimal places of precision.

**/on_select**
- context/timestamp difference between /on_select and /select should be smaller than 5 sec

**/on_init**
- context/timestamp difference between /on_init and /init should be smaller than 5 sec

**/confirm**
- /message/order/payment must have required property '@ondc/org/settlement_details'
- created_at, updated_at mismatches in /billing in /init and /confirm

**/on_confirm**
- context/timestamp difference between /on_confirm and /confirm should be smaller than 5 sec
- created_at, updated_at mismatches in /billing in /confirm and /on_confirm
- payment object mismatches in /confirm & /on_confirm

