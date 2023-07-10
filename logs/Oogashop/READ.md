Logs submission for Seller NP By Oogashop

Hi,

We are from Paralleldots Pvt. Ltd. and submitting the logs for our seller np application Oogashop. The buyer app used for the generation of logs is ONDC Preprod Buyer Reference App and have generated logs for all the flows as per the `Test Case Scenarios v1.1` document. We have ran the log validation utility and found few suggestions. Either we are misunderstanding them or they are not valid. We are attaching them below with our comments in parenthesis just after the suggestion. Please go through them and suggest us if we are missing something.

We want to draw attention on one more point that is we will not be sending `returnable = true` for now for any product but we have implemented them for log verification only and have submitted those logs too. Logs in `/on_update` contain either the `Return_Initiated` or `Return_Rejected` as specified in test case scenarios document.

**/on_search**

- Timestamp not in RFC 3339 (YYYY-MM-DDTHH:MN:SS.MSSZ) Format (Already in RFC3339 Format)
- Either one of fixed timings (range) or split timings (both frequency and times) should be provided in /bpp/providers[0]/locations[0]/time (Have sent it too)

**/select**

    (These seem buyer app issues)

- /message/order/items/0/quantity/count must be integer
- /message/order/items/1/quantity/count must be integer

**/on_select**

- Timestamp not in RFC 3339 (YYYY-MM-DDTHH:MN:SS.MSSZ) Format (Already in the format)
- /quote/breakup/0/@ondc~1org~1item_quantity/count must be integer (We were earlier suggested to use String when submitted for log verification)
- /quote/breakup/2/@ondc~1org~1item_quantity/count must be integer (We were earlier suggested to use String when submitted for log verification)
- /quote/breakup/3/price/value must match pattern "^(\d*.?\d{1,2})$" (This is something new but can't understand why in dollers.)
- context/timestamp difference between /on_select and /select should be smaller than 5 sec (For the first call of /select, we are not supposed to call /on_select with in 5 seconds but for subsequent calls which we have followed.)
- /fulfillments[0]/@ondc/org/TAT (O2D) in /on_select can't be smaller than @ondc/org/time_ship (O2S) in /on_search (Earlier we were sending it to equal and it was suggesting that they can not be equal. We are unable to understand this behavior.)
- invalid  id: OOGASHOP-ONDC-11 in delivery line item (should be a valid fulfillment_id)
  (Can't understand why fulfillment_id as it says item_id specifically in key.)
- invalid  id: OOGASHOP-ONDC-12 in delivery line item (should be a valid fulfillment_id)(Can't understand why fulfillment_id as it says item_id specifically in key.)

**/init**

    (These seem buyer app issues)

- /message/order/items/0/quantity/count must be integer
- /message/order/items/1/quantity/count must be integer

**/on_init**

- /items/0/quantity/count must be integer (We were earlier suggested to use String when submitted for log verification)
- /items/1/quantity/count must be integer (We were earlier suggested to use String when submitted for log verification)
- /quote/breakup/0/@ondc~1org~1item_quantity/count must be integer (We were earlier suggested to use String when submitted for log verification)
- /quote/breakup/2/@ondc~1org~1item_quantity/count must be integer (We were earlier suggested to use String when submitted for log verification)
- /quote/breakup/3/price/value must match pattern "^(\d*.?\d{1,2})$"
  (Do not know why in dollers.)
- Timestamp not in RFC 3339 (YYYY-MM-DDTHH:MN:SS.MSSZ) Format (Already in the desired format)
- gps coordinates in fulfillments[0].end.location mismatch in /select & /on_init (They are literally same)
- Discrepancies between the quote object in /on_select and /on_init (We are unable to find any descripancy)

**/confirm**

    (These seem buyer app issues)

- /message/order/quote/breakup/0/@ondc~1org~1item_quantity/count must be integer
- /message/order/quote/breakup/2/@ondc~1org~1item_quantity/count must be integer
- /message/order/quote/breakup/3/price/value must match pattern "^(\d*.?\d{1,2})$"
- address/door mismatches in /billing in /init and /confirm
- fulfillments[0].end.location gps is not matching with gps in /select
- Discrepancies between the quote object in /on_select and /confirm

**/on_confirm**

- /items/0/quantity/count must be integer (We were earlier suggested to use String when submitted for log verification)
- /items/1/quantity/count must be integer (We were earlier suggested to use String when submitted for log verification)
- /quote/breakup/0/@ondc~1org~1item_quantity/count must be integer (We were earlier suggested to use String when submitted for log verification)
- /quote/breakup/2/@ondc~1org~1item_quantity/count must be integer (We were earlier suggested to use String when submitted for log verification)
- /quote/breakup/3/price/value must match pattern "^(\d*.?\d{1,2})$"
  (Unable to understand why using dollers as it was earlier working very nicely.)
- Timestamp not in RFC 3339 (YYYY-MM-DDTHH:MN:SS.MSSZ) Format (Already in the desired format)
- order.created_at timestamp mismatches in /confirm and /on_confirm (Buyer app is not sending correct created_at in /confirm as it supposes its context.timestamp to be created at.)
- address/door mismatches in /billing in /confirm and /on_confirm (Buyer app is missing to send door in billing object in /confirm.)
- fulfillments[0].end.location gps is not matching with gps in /select (They are already the same.)
- Discrepancies between the quote object /on_select and /on_confirm (we are unable to find any descripency)

**/on_status (Order-Delivered)**

- /items/0/quantity/count must be integer (We were earlier suggested to use String when submitted for log verification)
- /items/1/quantity/count must be integer (We were earlier suggested to use String when submitted for log verification)
- /quote/breakup/0/@ondc~1org~1item_quantity/count must be integer (We were earlier suggested to use String when submitted for log verification)
- /quote/breakup/2/@ondc~1org~1item_quantity/count must be integer (We were earlier suggested to use String when submitted for log verification)
- /quote/breakup/3/price/value must match pattern "^(\d*.?\d{1,2})$"
  (It was earlier working nicely this is the first time it suggesting dollers but I am unable to understand why.)
- Timestamp not in RFC 3339 (YYYY-MM-DDTHH:MN:SS.MSSZ) Format (Already in the desired format.)
- Message Id cannot be same for different sets of APIs (As we are in the same set of APIs and using the very same message id as was used in confirm and on_confirm)
- address/door mismatches in /billing in /confirm and /on_status_delivered (`billing.door` is not being sent by buyer app in `/confirm`)
- order/created_at timestamp can't change (should remain same as in /confirm) (Buyer app not sending correct `created_at` timestamp in `/confirm`)
- order created_at timestamp must always be earlier than the updated_at timestamp (`created_at` is either earlier or same as `updated_at`

Please go through all the logs of different flow and suggest us if some improvement is required as well as clarify the above confusions if they need some piece of attention from our side.

Thank you very much!!!!
