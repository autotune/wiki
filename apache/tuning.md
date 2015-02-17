After reading about ab and MaxClients, I could never really find a clear-cut explanation as to what a "client" actually means. Does it mean a single hit from a single visitor, does it mean multiple hits from multiple visitors, what exactly does it mean when apachebuddy says your server can support x number of clients? When will that limit be reached? Can a single page result in said limit being reached and if so, which one? Finally, why isn't the MaxClients limit being reached when testing a basic page in ab or httperf? I'll attempt to answer these questions and clear up any confusion in this article. 

Think of MaxClients like a lane on a freeway; each request is a new lane, where one request occupies one line for a the length of time it takes for a page to load. As soon as that page loads and the request goes through, the lane is free for a new request. If that lane is unavailable, the next one is used. What this all means is that Apache will reach its max connections limit if each lane is simultaneously being for a given number of seconds, this being the time it takes to load a page.

If it takes 5 seconds to load a page, for example, and you have 50 clients requesting that page before the end of those 5 seconds are up with a MaxClients limit of 50, then you'll reach your MaxClients limit. As a result, you would need 500 MaxClients to support 50 visitors if each visitor clicked a page that took 5 seconds to load within a period of those 5 seconds. If, however, you reduced your page load time to say, 3 seconds, 50 visitors would only require 150 MaxClients and 1 second could support 50 visitors clicking a page on your site at the same time during a period of high traffic. What you have to consider though is visitors are not necessarily going to be clicking the same page with the same load times or consistently unless you have a high traffic event or consistently have high traffic volume. You'll want to anticipate which pages will be accessed the most amount of times, and take the page that takes the longest to load into your calculations for MaxClients for a high traffic event.

We can test this theory out using httperf (not a huge fan of ab as dmesg reports "possible SYN flooding on port 80" when using it) and a simple php script as follows:
 
<?php
    # echo out current time
    echo date('h:i:s');
    echo "</br>";
    sleep(3);
    echo date('h:i:s');
?>
 
With this page, you can see it will basically hold open a connection for 3 seconds by forcing a wait time of 3 seconds for that page. The following values for httpd.conf will be used as well:
 
<IfModule mpm_prefork_module>
    StartServers          2
    MinSpareServers       2 # todo: figure out the conditions for which this breaks
    MaxSpareServers       8 # todo: figure out the conditions for which this breaks
    ServerLimit           8 # set to MaxClients dir per http://httpd.apache.org/docs/2.0/mod/mpm_common.html#serverlimit
    MaxClients            8
    MaxRequestsPerChild  2000 # todo: figure out the conditions for which this breaks
</IfModule>
 
The "max values" have been set to one higher than MaxClients for exact testing. You can run the following command to help bring up the MaxClients message:
httperf --server herpderp.com --rate 3 --num-conn 8 --uri /clients.php
If you set "--num-conn" one lower, you'll see that MaxClients will NOT be reached; this will hit the URL at a rate of 3 hits per second, the amount of time the script is set to remain open. 

