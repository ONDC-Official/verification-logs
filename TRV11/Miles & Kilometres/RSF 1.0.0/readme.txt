Hello QA Team, All other logs that have been approved so far have been against pramaan mock seller app (bppId: pramaan.ondc.org/beta/preprod/mock/seller) . 
RSF logs are against bppId: ondc-preprod.sequelstring.com/seller/dmrc - The reason is - pramaan mock seller app lets you do all work flow EXCEPT RSF.  

ondc-preprod.sequelstring.com/seller/dmrc - allows you to do RSF, however DOES NOT allow you to execute "cancel" - 
So that's the reason you will the RSF logs NOT having the same ondcTransactionId. 

Hope this clarification helps.
