 Troubleshooting Methods
Skip to end of metadata

    Created and last modified by Brian Adams on Feb 03, 2015

Go to start of metadata

The book "Systems Performance: Enterprise and the Cloud" by Brendan Gregg has thus far given an impression of being incredibly relevant. The goal here will be to document and reinterpret some of what it goes over and apply it to our own environment here at The Rack. As of now it is just me documenting this for my own benefit and personal use but if it proves to continue to be applicable anyone reading this is welcome to apply it and contribute as well.  This is in no way an official document and should not be interpreted as one, just another system of organization. 

 
LINKED PAGES

Performance Metrics (Tools Method/Linux)
TERMS

Response time: the time for an operation to complete
Throughput: the rate of work performed. Operations per second
Latency: measure of time an application spends waiting to be serviced.
KEYWORDS & PHRASES

observational analysis => obs
hypothetical analysis => hyp
capacity planning => cap
experimental analysis => exp
METHODS
Streetlight anti-method 

observational ("Google it") => easiest, and/or first place to look (see: http://en.wikipedia.org/wiki/Streetlight_effect)
Random change anti-method 

hypothetical => make a change at random without truly understanding what you're changing =>
Blame-someone-else anti-method 

hypothetical => find component not responsible (e.g. network switch or Windows Server as a Linux Admin) => hypothesize issue is with that => redirect to that team => if not, repeat. In order to make this a valid escalation or transfer, acquire data proving it is valid.
Ad hoc checklist method

observational and hypothetical => checklist to troubleshoot common issues. This has been mostly automated via ADC.
Problem statement

info gathering => what is the actual problem? => has this issue already been occurring? => recent changes => latency or uptime? => other people or apps => what is the environment (packages, versions, config) => is it supported?
Scientific method

observational => What is the issue? => Slow web page. => DoS, code errors, database issues, etc. => If we block this DoS attack, it will return to normal => block IP or IPs hitting server => Test load time with gtmetrics or pingdom => update ticket.
Diagnosis cycle

analysis life cycle => Same as above but uses tools without asking questions or making predictions => gather as much data as possible, i.e. test as much data gathered as possible automatically via rs-sysmon or recap.
Tools method

observational => list available performance tools (rs-sysmon/recap, sar, free -m, top, iostat, df -Th, tcpdump, netstat, ps aux) => list useful metrics => list possible interpretation for each metric.
