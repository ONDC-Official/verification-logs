**/confirm** (Bug in bap)
- address/door mismatches in /billing in /init and /confirm

**/on_confirm**
- payment object mismatches in /confirm & /on_confirm (RSP elements)

**/on_update (Return_Approved)**  (Bug in validator code. Incorrectly validating reverse qc fulfillment as if it is regular fulfillments- start and end are interchanged) 
- /fulfillments/0/start/location must have required property 'descriptor'
- /fulfillments/0/end/location/address must have required property 'building'

**/on_update (Return_Delivered)**(Bug in validator code. Incorrectly validating reverse qc fulfillment as if it is regular fulfillments- start and end are interchanged) 
- /fulfillments/0/start/location must have required property 'descriptor'
- /fulfillments/0/end/location/address must have required property 'building'




