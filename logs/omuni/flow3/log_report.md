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

**/on_status (Order-picked-up)**
- /billing/address must have required property 'building'
- /fulfillments/0/end/time delivery time should not be present until order is delivered
- /fulfillments/1/end/time delivery time should not be present until order is delivered

**/on_status (Order-Delivered)**
- /billing/address must have required property 'building'
- delivery timestamp (/end/time/timestamp) can't be less than or equal to the pickup timestamp (start/time/timestamp)

