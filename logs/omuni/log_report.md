**/on_init**
- provider_location.id mismatches in /on_search and /on_init

**/confirm**
- provider.locations[0].id mismatches in /on_search and /confirm
- address/door mismatches in /billing in /init and /confirm

**/on_confirm**
- provider.locations[0].id mismatches in /on_search and /on_confirm
- store name  /fulfillments[1]/start/location/descriptor/name can't change

**/on_status (Pending)**
- provider.locations[0].id mismatches in /on_search and /on_status_pending

**/on_status (Order-picked-up)**
- /fulfillments/0/end/time delivery time should not be present until order is delivered
- /fulfillments/1/end/time delivery time should not be present until order is delivered
- provider.locations[0].id mismatches in /on_search and /on_status_picked

**/on_status (Order-Delivered)**
- provider.locations[0].id mismatches in /on_search and /on_status_delivered
- delivery timestamp (/end/time/timestamp) can't be less than or equal to the pickup timestamp (start/time/timestamp)

