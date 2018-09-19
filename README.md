# URLLookUpService
URL lookup service

We have an HTTP proxy that is scanning traffic looking for malware URL's. Before allowing HTTP connections to be made, this proxy asks a service that maintains several databases of malware URL's if the resource being requested is known to contain malware.

Write a small web service, preferably in Python, that responds to GET requests where the caller passes in a URL and the service responds with some information about that URL. The GET requests would look like this:

 GET /urlinfo/1/{hostname_and_port}/{original_path_and_query_string}

 

The caller wants to know if it is safe to access that URL or not. You get to choose the response format and structure. These lookups are blocking users from accessing the URL until the caller receives a response from your service.

Give some thought to the following:

1.The size of the URL list could grow infinitely, how might you scale this beyond the memory capacity of the system? Bonus if you implement this.

2.The number of requests may exceed the capacity of this system, how might you solve that? Bonus if you implement this.

3.What are some strategies you might use to update the service with new URLs? Updates may be as much as 5 thousand URLs a day with updates arriving every minute
