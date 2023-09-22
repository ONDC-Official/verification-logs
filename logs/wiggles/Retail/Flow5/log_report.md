**/on_select** (Expected as one of the items is not available Out of stock) 
- Warning: Quoted Price in /on_select INR 607 does not match with the total price of items in /select INR 761

**/on_init** (Validator bug. comparing with item of qty 0 in on_select against absence of the item in on_init)
- Discrepancies between the quote object in /on_select and /on_init

**/confirm**
- address/door mismatches in /billing in /init and /confirm (BAP Issue) 
- Discrepancies between the quote object in /on_select and /confirm (Validator bug. comparing with item of qty 0 in on_select against absence of the item in on_init)

**/on_confirm**
- Discrepancies between the quote object /on_select and /on_confirm (Validator bug. comparing with item of qty 0 in on_select against absence of the item in on_init)
- payment object mismatches in /confirm & /on_confirm (RSP Elements present)

