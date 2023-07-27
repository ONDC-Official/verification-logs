**/on_search**
- /message/catalog/bpp~1providers/0/locations/0/address must have required property 'street'
- /message/catalog/bpp~1providers/0/locations/0/time/schedule/frequency must match format "duration"
- /message/catalog/bpp~1providers/1/locations/0/address must have required property 'street'
- /message/catalog/bpp~1providers/1/locations/0/time/schedule/frequency must match format "duration"
- /message/catalog/bpp~1providers/2/locations/0/address must have required property 'street'
- /message/catalog/bpp~1providers/2/locations/0/time/schedule/frequency must match format "duration"
- /message/catalog/bpp~1providers/3/locations/0/address must have required property 'street'
- /message/catalog/bpp~1providers/3/locations/0/time/schedule/frequency must match format "duration"
- /message/catalog/bpp~1providers/4/locations/0/address must have required property 'street'
- /message/catalog/bpp~1providers/4/locations/0/time/schedule/frequency must match format "duration"
- Either one of fixed (range) or split (frequency and times) timings should be provided in /bpp/providers[0]/locations[0]/time
- @ondc/org/contact_details_consumer_care should be in the format "name,email,contactno" in /bpp/providers[0]/items
- Either one of fixed (range) or split (frequency and times) timings should be provided in /bpp/providers[1]/locations[0]/time
- @ondc/org/contact_details_consumer_care should be in the format "name,email,contactno" in /bpp/providers[1]/items
- Either one of fixed (range) or split (frequency and times) timings should be provided in /bpp/providers[2]/locations[0]/time
- @ondc/org/contact_details_consumer_care should be in the format "name,email,contactno" in /bpp/providers[2]/items
- Either one of fixed (range) or split (frequency and times) timings should be provided in /bpp/providers[3]/locations[0]/time
- @ondc/org/contact_details_consumer_care should be in the format "name,email,contactno" in /bpp/providers[3]/items
- Either one of fixed (range) or split (frequency and times) timings should be provided in /bpp/providers[4]/locations[0]/time
- @ondc/org/contact_details_consumer_care should be in the format "name,email,contactno" in /bpp/providers[4]/items

**/on_select**
- context/timestamp difference between /on_select and /select should be smaller than 5 sec
- /fulfillments[0]/@ondc/org/TAT (O2D) in /on_select can't be equal to @ondc/org/time_ship (O2S) in /on_search
- Count of item with id: 43ec1346-4b23-4630-8720-fd6d75fff469 does not match in select & on_select (suitable domain error should be provided)
- tax line item should not be present if price=0
- Warning: Quoted Price in /on_select INR 90 does not match with the total price of items in /select INR 115

**/init**
- /message/order/billing/address must have required property 'building'
- /message/order/fulfillments/0/end/location/address/building must NOT have fewer than 3 characters
- address.building should be more than 3 chars
- Warning: items[1].quantity.count for item 43ec1346-4b23-4630-8720-fd6d75fff469 mismatches with the items quantity selected in /select

**/on_init**
- /billing/address must have required property 'building'
- Warning: items[1].quantity.count for item 43ec1346-4b23-4630-8720-fd6d75fff469 mismatches with the items quantity selected in /select
- Buyer app finder fee can't change in /on_init
- Discrepancies between the quote object in /on_select and /on_init

**/confirm**
- /message/order/billing/address must have required property 'building'
- Warning: items[1].quantity.count for item 43ec1346-4b23-4630-8720-fd6d75fff469 mismatches with the items quantity selected in /select
- order.created_at timestamp should match context.timestamp
- Discrepancies between the quote object in /on_select and /confirm

**/on_confirm**
- /billing/address must have required property 'building'
- /fulfillments/0/start/location must have required property 'id'
- context/timestamp difference between /on_confirm and /confirm should be smaller than 5 sec
- order.updated_at timestamp should be updated as per the context.timestamp (since default fulfillment state is added)
- Discrepancies between the quote object /on_select and /on_confirm

