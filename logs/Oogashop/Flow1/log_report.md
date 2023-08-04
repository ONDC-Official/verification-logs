**/on_init**
- gps coordinates in fulfillments[0].end.location mismatch in /select & /on_init

**/confirm**
- address/door mismatches in /billing in /init and /confirm
- fulfillments[0].end.location gps is not matching with gps in /select

**/on_confirm**
- address/door mismatches in /billing in /confirm and /on_confirm
- fulfillments[0].end.location gps is not matching with gps in /select

**/on_status (Pending)**
- address/door mismatches in /billing in /confirm and /on_status_pending

**/on_status (Order-picked-up)**
- address/door mismatches in /billing in /confirm and /on_status_picked

**/on_status (Order-Delivered)**
- address/door mismatches in /billing in /confirm and /on_status_delivered

