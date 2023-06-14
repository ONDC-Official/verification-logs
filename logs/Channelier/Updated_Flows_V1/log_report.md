**/on_search**
- Either one of fixed (range) or split (frequency and times) timings should be provided in /bpp/providers[0]/locations[0]/time
- category in serviceability construct should be one of the category ids bpp/providers[0]/items/category_id

**/on_select**
- /fulfillments[0]/@ondc/org/TAT (O2D) in /on_select can't be smaller than @ondc/org/time_ship (O2S) in /on_search

**/init**
- /message/order/billing/address must have required property 'building'
- /message/order/fulfillments/0/end/location/address/building must NOT have fewer than 3 characters
- City code mismatch in /search and /init
- address.building should be more than 3 chars

**/on_init**
-  must have required property 'provider_location'
- /billing/address must have required property 'building'
- City code mismatch in search & on_init
- context/timestamp difference between /on_init and /init should be smaller than 5 sec
- provider_location object is missing in /on_init
- Discrepancies between the quote object in /on_select and /on_init

**/confirm**
- /message/order/billing/address must have required property 'building'
- City code mismatch in /search and /confirm
- Discrepancies between the quote object in /on_select and /confirm

**/on_confirm**
- /billing/address must have required property 'building'
- City code mismatch in /search and /on_confirm
- store gps location /fulfillments[0]/start/location/gps can't change
- store name  /fulfillments[0]/start/location/descriptor/name can't change
- Discrepancies between the quote object /on_select and /on_confirm

**/on_status (Order-picked-up)**
- /billing/address must have required property 'building'
- City code mismatch in search and /on_status_picked
- Message Id cannot be same for different sets of APIs

**/on_status (Order-Delivered)**
- /billing/address must have required property 'building'
- City code mismatch in search and /on_status_delivered
- Message Id cannot be same for different sets of APIs

**/update**
- City code mismatch in /search and /update

**/on_update (Initiated)**
- City code mismatch in /search and /on_update_Return_Initiated
- delivery timestamp (/end/time/timestamp) can't change for fulfillment id L-F-1686623003097

**/on_update (Return_Approved)**
- City code mismatch in /search and /on_update_Return_Approved
- new fulfillment id should be created for item: CU0I1 when return state is Return_Approved
- delivery timestamp (/end/time/timestamp) can't change for fulfillment id L-F-1686623003097

