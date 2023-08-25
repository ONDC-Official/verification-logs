**/init**
- value of address.name, address.building and address.locality should be unique

**/confirm**
- address/door mismatches in /billing in /init and /confirm

**/update**
- /message/order/items/0/tags/ttl_approval must match format "duration"

**/update (Refund)**
- /message/order/items/0/tags/ttl_approval must match format "duration"
- Inaccurate calculation of refund amount (pls check the quote price in refund triggering state)

