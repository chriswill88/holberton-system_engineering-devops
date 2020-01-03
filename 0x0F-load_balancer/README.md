This is the README for the load balancer project

Notes (What I learned from this project)
load balancers job is to distribute the work load to multiple systems,
or a group of systems to reduce the amount of load on a particular system.
load balancers incerase the reliablility, efficiency, and availability of
your app or website.

load balancers...
... reduce work loads
... increase performance because of a faster response
... take away the single point of a system
... allow for scaliability - meaning we can increase or decrease the number of
servers without bringing the down the application
... allows for work to be done concurrenctly on multiple servers
... increase the reliabilty of your app

Software Load Balancers
implement a combination of one or more scheduling algorithms

Algorithms Include

weighted Schedualing Algorithm
this algorithm assigns work to a server according to the weight assigned to
the server.

Round Robin Schdualing
sends work to each server one after the other.

Least connction First Schedualing
the requests are sent to the first server currently handiling the least 
number of connections

