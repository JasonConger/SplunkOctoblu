Splunk Octoblu Trigger Example
==================
This app demonstrates how to trigger an Octoblu workflow from Splunk.

Setup
==
* Copy this app to $SPLUNK_HOME/etc/apps
* Restart Splunk

Generating Demo Data
==

In the bin folder of the app is a file named generate.py.  This is used to generate some dummy data for the demo application.

From a command line start the generate.py script (require Python to be installed)

Example:

    python generate.py 1Command line arguments:

* 1 = green (a.k.a. all good)
* 2 = yellow
* 3 = red
* 4 = code red