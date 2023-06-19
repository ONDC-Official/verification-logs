**/on_search**
- category in serviceability construct should be one of the category ids bpp/providers[0]/items/category_id

**/init**
- /message/order/billing/address must have required property 'building'
- /message/order/fulfillments/0/end/location/address/building must NOT have fewer than 3 characters
- City code mismatch in /search and /init
- address.building should be more than 3 chars

**/on_init**
- /billing/address must have required property 'building'
- City code mismatch in search & on_init
- context/timestamp difference between /on_init and /init should be smaller than 5 sec

**/confirm**
- /message/order/billing/address must have required property 'building'
- City code mismatch in /search and /confirm
- Discrepancies between the quote object in /on_select and /confirm

**/on_confirm**
- /billing/address must have required property 'building'
- City code mismatch in /search and /on_confirm

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

