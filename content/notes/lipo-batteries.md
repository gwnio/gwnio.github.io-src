Title: Lipo Batteries
Date: 2014-02-14 11:10:23 -0400
Tags: lipo, batteries

## Table of contents
1. [Intro](#intro)
2. [Voltage or "S" rating](#voltage)
3. [Capacity or mAh rating](#capactiy)
4. [Discharge Rate or "C" rating](#discharge)
5. [Internal Resistance](#resistance)
6. [Charging](#charging)
7. [JST Battery Connector](#connector)
8. [iMax B6 - LiPo Balance Charger](#charger)
9. [Charging Notes](#charging_notes)
10. [Helpful Resources](#resources)

### Intro <a name="intro"></a>

<!-- PELICAN_BEGIN_SUMMARY -->
I bought a quad-copter drone and wanted to know a little more about their batteries and charging them.  So this post is derived from my research.
<!-- PELICAN_END_SUMMARY -->

### Voltage or "S" rating <a name="voltage"></a>

* 3.7 volts per cell, 4.2 when fully charged
* Cell counts
    * 3.7 volt battery = 1 cell x 3.7 volts (1S)
    * 7.4 volt battery = 2 cells x 3.7 volts (2S)
    * 11.1 volt battery = 3 cells x 3.7 volts (3S)
    * ...and so on
* Battery packs can be wired in parallel to increase capacity
    * Example: 3S2P would indicate 2 x three celled series packs hooked up in parallel to double the capacity

### Capacity or mAh rating <a name="capacity"></a>

* How much load (in milliamps) can be placed on the battery in 1 hour to fully discharge the battery
    * 1000 mAh - would be fully discharged in 1 hour at 1000 mAh load
    * 1000 mAh - would be fully discharged in 2 hours with 500 mAh load
* To increase your runtime, increase the capacity

### Discharge Rate or "C" rating <a name="discharge"></a>

* How fast a battery can be discharged safely
    * 10C discharge rating - would discharge at a rate 10 times the capacity of the pack
    * 15C pack - 15 times more
* 1000 mAh 10C - can pull a max load of 10000 milliamps
    * 1000 / (10000 / 60) = 6 minutes
* Discharge rate = 20C Continuous / 40C Bursts

### Internal Resistance <a name="resistance"></a>

* Best way to monitor the batteries condition - as the battery gets older, internal resitance increases

### Charging <a name="charging"></a>

#### Maximum charge voltage and current

* 3.7 volt lipo battery cell is 100% charged when it reaches 4.2 volts
* A computerized charger will stop charging when 4.2 volts is reached, a balanced charger will do this for each cell
* On a 2 cell (2S) pack, you must select 7.4 volts or 2 cells on the charger
* Most good LiPo battery chargers use constant current/constant voltage charging method.  As the battery voltage closes in on the 100% charge voltage, the charger will automatically start reducing the charge current and then apply a constant voltage.

#### Charging current

* Use to be, never charge a LiPo or Li-Ion pack greater than 1 times its capacity (1C)
    * 2000 mAh pack, would be charged at maximum charge current of 2000 mAh or 2 amps
* Now, experts say you can safely charge at 2C or even 3C rate that have a discharge rating of 20C or more

#### Battery Balancing

* Ensures all cells are always within 0.01-0.03 volts per cell
* Balancing is required on battery packs with more than one cell
* 3S pack
    * 11.1 volt battery pack (3.7 volts per cell x 3 = 11.1 volts)
    * 100% charge voltage 12.6 volts (4.2 volts x 3 = 12.6 volts)

#### Discharging

* Purpose is to clean residual capacity of the battery, or reduce the battery voltage to a defined level
* Generally, a lithium battery does not need to be discharged

### JST Battery Connector <a name="connector"></a>

* Rated for up to 5 amps of continuous load
* Used on smaller battery packs (usually under 1500 mAh)

### iMax B6 - LiPo Balance Charger <a name="charger"></a>

* Connect the charge cable to the charger first, then connect to battery.  Reverse sequence when disconnecting
* Do not connect a battery fitted with an integral charge circuit or a protection circuit

### Charging Notes <a name="charging_notes"></a>

#### Note 1

Just keep in mind that you are not controlling the balancing of the individual 1S batteries when parallel charging like you are when charging a 6S battery on your charger with it connected to your balancer adapter - you are in effect "wiring them all together" so they will have a tendancy to balance against one another (sort of like if you had 6 buckets of water and a hose at the bottom of each bucket connecting them all together... they will eventually equalize amongst themselves) but you want to start with each cell close to each other (close in its starting charge state, i.e. all close to 20% capacity or 30% etc.) you can test them with a 1S lipo tester or a meter. 

IF for instance you had 4 1S cells at 60 or 70% and 2 at 20%, when connected in parallel, the 4 would effectively "charge" the 2 quite possibly at greater than thier rated charge rate as they equalize amongst themselves.

Going back to the 6S pack connected to your charger and to the balancer adapter, two significant things are happening different from the 1S's in parallel;

1. the 6 individual cells that make up the 6S pack (or 3 cells in a 3S etc) are being drained at a very similar rate as the battery is being used, so all 6 cells will be at close to the same % of discharge at the end of a flight (not more than the recommended 20% if you timed your flight right!)

2. when you connect the 6S to your charger (the red/black leads with the deans or whatever connector you use) and then the smaller plug to the balance adapter, the charger is reading each cell individually through the balance adapter and charging each cell back to capacity, matiching or BALANCING each cell to the other 5 as it goes (the whole point of a balancing charger). Most chargers will show you this in one of the menu displays as they charge as well as the variance between the least charged cell and the most charged cell. If after flight or during/after charging you have a significant variance between the least and the greatest, you have a problem with that battery.

#### Note 2

[rchelicopterfun.com](http://www.rchelicopterfun.com/parallel-lipo-charging.html){:target="_blank"}

#### Note 3

[helidirect.com](http://helidirect.com/hyperion-6-port-parallel-charge-adapter-for-1s-um-lipoly-p-18642.hdx){:target="_blank"}

#### Note 4

[rcgroups.com](http://www.rcgroups.com/forums/showthread.php?t=1604502){:target="_blank"}

### Helpful Resources <a name="resources"></a>

* [icharger.co.nz](http://www.icharger.co.nz/articles/ArticleId/6/Introduction-To-Lipo-Batteries.aspx){:target="_blank"}