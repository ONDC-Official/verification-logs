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

**/confirm**
- /message/order/billing/address must have required property 'building'
- City code mismatch in /search and /confirm

**/on_confirm**
- /billing/address must have required property 'building'
- City code mismatch in /search and /on_confirm

**/on_status (Order-picked-up)**
- /billing/address must have required property 'building'
- /fulfillments/0/end must have required property 'time'
- City code mismatch in search and /on_status_picked

**/on_status (Order-Delivered)**
- /billing/address must have required property 'building'
- City code mismatch in search and /on_status_delivered

**/update**
- City code mismatch in /search and /update

**/on_update (Initiated)**
- City code mismatch in /search and /on_update_Return_Initiated

**/on_update (Return_Approved)**
- City code mismatch in /search and /on_update_Return_Approved

