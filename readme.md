# xmastree

> Gentlemen, start your engines.    


## What's this?

xmastree is a simple scheduler that runs simple jobs in cron with close to 1-second precision.  
Jobs are defined in a JSON file and executed in child forks as the internal clock strikes their start times.


## How do I run this?

1. Populate a JSON file 
2. Schedule xmastree in cron to run every minute (assuming you have a long job queue) as ```xmastree commands.json```  


## Known Issues

* Child processes are reaped at completeion of the cycle (about a minute after they start)
