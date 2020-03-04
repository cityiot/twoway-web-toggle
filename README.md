# twoway-web-toggle
Simple Web front &amp; backend for two-way synchronization of IoT device via FIWARE Orion Context Broker

(more documentation TODO)

## Notes
In this implementation, there are two separate entities in Orion: one for getting an attribute value, and another for setting it. This was necessary because Orion triggered a change notification for all attributes, when any of the attributes in an entity changed. This resulted in an infinite loop of change notifications when the 3rd party system, that was used to connect to an actual building automation system, was used to both set and read a test attribute from Orion.

Newer version of Orion has an option, for subscriptions, to fix this issue: https://github.com/telefonicaid/fiware-orion/pull/3490 , "Notify only attributes that change". However we did not update the server version while the pilots were running so could not utilize this.
