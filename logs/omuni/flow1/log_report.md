**/confirm**
- address/door mismatches in /billing in /init and /confirm

**/on_confirm**
- store name  /fulfillments[1]/start/location/descriptor/name can't change

**/on_status (Order-picked-up)**
- /fulfillments/0/end/time delivery time should not be present until order is delivered
- /fulfillments/1/end/time delivery time should not be present until order is delivered

**/on_status (Order-Delivered)**
- delivery timestamp (/end/time/timestamp) can't be less than or equal to the pickup timestamp (start/time/timestamp)

