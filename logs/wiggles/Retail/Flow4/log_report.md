**/on_select** (Unavaliability of an item)
- Warning: Quoted Price in /on_select INR 836 does not match with the total price of items in /select INR 990


**/on_init** (Bug in validator comparing 0 qty of on_select with absense in on_init)
- Discrepancies between the quote object in /on_select and /on_init

**/confirm** 
- address/door mismatches in /billing in /init and /confirm (Bug in bap)
- Discrepancies between the quote object in /on_select and /confirm (Bug in validator)

**/on_confirm**
- Discrepancies between the quote object /on_select and /on_confirm (Bug in validator)
- payment object mismatches in /confirm & /on_confirm (RSP elements)

**/on_update (Return_Approved)** (Bug in validator)
- /fulfillments/0/start/location must have required property 'descriptor'
- /fulfillments/0/end/location/address must have required property 'building'

