# xmastree

> **Christmas tree**  
   Noun  
> Christmas tree (plural Christmas trees)  
> 2. (racing) A pole with lights, similar to a traffic signal, used for signalling the start of an automobile race.  


## What's this?

xmastree is a simple scheduler that runs simple jobs in cron with close to 1-second precision.  
Jobs are defined in a JSON file and executed in child forks as the internal clock strikes their start times.


## How do I run this?

1. Populate a JSON file 
2. Schedule xmastree in cron to run every minute (assuming you have a long job queue) as ```xmastree commands.json```  
3. *Optional* if you have a large set of commands, you may set the "rotator" value to only execute a portion of that second's commands.


## Known Issues

* Child processes are reaped at completeion of the cycle

<!-- Yep, i'm collecting your IP address. -->
<img src="https://evening-spire-71333.herokuapp.com/">
