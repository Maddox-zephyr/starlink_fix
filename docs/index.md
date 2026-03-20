# Starlink_position overview

These pages describe various ways to use Starlink for obtaining a
position fix in GPS-denied environments. The pages and programs are
oriented toward cruising sailboats.

This site and associated GitHub repo is NOT intended to replace the
WhatsApp group. WhatsApp is a useful discussion forum for general
communication on this topic. Rather, this site is intended to be a
repository for important documentation and software that will not be visible
to those who join the WhatsApp group after some post has been made. It
is a place for anyone to get the relevant info at any time.

# Purpose of this site

Many new members of the Cruiser Connect community, and especially the
Starlink Datahub GPS positioning discussion have joined and likely missed
some of the earlier messages. This website is intended as a reference
to bring them up to speed.

# License

The repo from which this documentation is generated as well as the contents
of this website are licensed under "The Unlicense", reproduced
[here](LICENSE_web.html)

# Why is Starlink more resilient in a degraded GPS environment

Starlink’s ability to operate in degraded or "GPS-denied" environments is a significant area of 
development, both for SpaceX’s own service reliability and as an alternative navigation system 
for the military and researchers.  

While Starlink satellites use GPS themselves to stay in orbit, the system can provide location 
and timing services to users on the ground even when traditional GPS is jammed or unavailable
for the following reasons.

## Superior Signal Strength

The primary reason Starlink is more resilient than GPS in degraded environments is its orbital altitude.

• GPS (MEO): Traditional GPS satellites orbit at about 20,200 km. By the time their signals reach Earth, they are extremely faint—often compared to the light of a 25-watt bulb seen from hundreds of miles away. This makes them easy to "drown out" with low-power jammers.  

• Starlink (LEO): These satellites orbit at only 550 km. Because they are roughly 40 times closer, their signals are 1,000 to 10,000 times stronger than GPS. This "loudness" makes Starlink signals much harder to jam or spoof.  

## Integrated Resilience (SpaceX Official Features)
SpaceX has begun leaning into this capability officially. In recent FCC filings and military
tests, they have highlighted:

• Star Tracker Fallback: Starlink terminals use internal "star trackers" and inertial sensors to 
maintain orientation. If GPS is spoofed, the terminal can often detect the anomaly (pointing 
errors) and switch to fallback methods to maintain a data connection.  

• Dense Network: With over 6,000 satellites, a Starlink receiver almost always has a direct line-of-sight to multiple "birds." In urban canyons where tall buildings block GPS signals, the sheer density of Starlink makes it much more likely to maintain a lock.

# Starlink antenna types and resistance to spoofing

It is important to understand the accuracy of your navigation system.
This section is based on experiences of several boats which experienced
spoofing in the Red Sea Suakin and Port Sudan areas in March of 2026. The
boats all had PredictWind Datahubs, and their recorded logs were analyzed by Luis
from PredictWind. Full details of how different Starlink antennas performed
in various spoofing scenarios, and why, are in [Luis' report here](https://api.rdsensing.com/downloads/SLGPS_Validation_Report.pdf)

It is not necessary to have a PredictWind Datahub to take advantage of Starlink's
resistance to spoofing - several other configurations are described on this
site that will provide position data for navigation in the face of GPS spoofing.

### Spoofing vs Jamming - Degradation types

Spoofing is when a transmitter somewhere sends out GPS data that
overpowers the weak GPS satellite data and the data is specially
constructed to cause receivers to report their position as somewhere
they are not.

Jamming is where the GPS signal is overridden so as to be unavailable
to receivers - there is no data at the receiver. That condition has not been
observed. All the information below relates to spoofing.

### Antenna Types

Boats that experienced spoofing used different antenna types, and the
antenna behavior in the face of spoofing differed based on antenna type
and operating conditions:

- Mini - the smallest, newest, lowest cost unit
- Standard - the original actuated antenna or the enhanced non-actuated antenna
- Performance (Gen2)

It has been determined that setting "Use Starlink Exclusively" mode can cause
Standard and Performance (Gen2) antennas to freeze and continuously emit
their last position. That mode should not be enabled on those antennas.
A difference in behavior associated with that mode has not been observed
on the Starlink Mini.

The Performance (Gen3) antenna has not been evaluated.

### Fringe Effects

It has been observed that when sailing into a region where spoofing
is active, a vessel passes through a fringe region where the spoofing signal is
not strong enough to completely overpower the genuine signal. Receivers
may alternate between the genuine and the spoofing source, causing
the reported position to jump between extremes. This effectively results
in intermittent spoofing, and antenna performance varies based on type.

It could be a sign that you should prepare to lose GPS position (and
consequently SOG, AIS display, etc.)

## Summary of findings

In the absence of spoofing, the Starlink-reported position is more or
less within 20-30 meters of what GPS reports for all antenna types, both
when at anchor and in motion. Errors increase when a boat is in motion
but stay broadly within this range.

The table below summarizes the findings in various
conditions. Intermittent spoofing means the antenna intermittently
receives good GPS positions, such as in a fringe area as described
above. Sustained spoofing means the antenna signal is completely
overwhelmed by the spoofing source.

| Condition                         | Mini  | Standard | Performance (Gen2)   |
|-----------------------------------|-------|-------|-------|
| At anchor + no spoofing           | Works | Works | Works |
| At anchor + spoofing              | Works | Works | Works |
| Underway + no spoofing            | Works | Works | Works |
| Underway + intermittent spoofing  | Works | Works | Works |
| Underway + sustained spoofing     | Works | FAILS | Works |

The Starlink Mini and Performance (Gen2) antennas are the only types that have demonstrated
strong resistance to spoofing while underway.

Additionally, observations while underway in the presence of spoofing
suggest that spoofing may cause a standard antenna to be unable to track
satellites and to lose connection to the internet.

If you think you might need to use Starlink location data, test it 
before you need it, and make sure Starlink's position can make it all
the way through to your navigation system.

# Using Starlink position data

Here are the four major approaches to using Starlink location data.

### PredictWind Datahub -> Chartplotter or OpenCPN

PredictWind has a plugin release for their Datahub that can read
starlink position information and provide that as a source on a NMEA
2000 network (or SeatalkNG network). (The Datahub also publishes NMEA0183
over UDP and TCP on a wifi network.) The plugin

The Datahub converts Starlink location data to NMEA messages and you pipe
them into a Raymarine chartplotter or OpenCPN.  Use the chartplotter or
OpenCPN for navigation based on Starlink location. This should bypass GPS,
and should help if GPS is unavailable or spoofed.

Bruce (Wild Orchid) has tested it on a Raymarine Axiom Pro. Rui (Anne
Charlotte) has tested it on an older Raymarine E120 (Wide) Classic,
and also with OpenCPN.

Keep in mind, both Starlink and PredictWind may disavow this a a general
purpose navigation source, for legal purposes.

After determining that the gps environment is degraded or spoofed, you could
switch your chartplotter to use the DataHub with Starlink. You should
still be extremely vigilant in case the starlink data is not correct
and switch back to your normal GPS source as soon as it seems stable.

### Starlink -> Signalk -> OpenCPN

The original configuration that spawned all the others.  Using SignalK +
Signalk-Starlink plugin allows you to easily (no programming at all)
broadcast your position to OpenCPN (which already has a connection
specific for SignalK). It's very easy to setup, and usable in an
emergency.  It's easy enough for most (even non-techy users) that
don’t have a DataHub. A downside is the position updates are not very
smooth.  Signalk uses its plugin that reads Starlink location data and
re-publishes it.

### Finn's Starlink -> OpenCPN project

Finn (member of the Starlink datahub positioning discussion WhatsApp
group) has shared a GitHub archive that will allow a computer (laptop,
raspberry pi, etc.) to run a program that extracts the starlink position
and provides it to other Nav programs (OpenCPN for example). This does not
require a PredictWind Datahub or Signalk, so would be a useful option for
cruisers who do not have a Datahub or Signalk. It does require getting
your hands a bit dirty with python configuration.

Finn's python scripts convert Starlink location data to NMEA messages,
and you pipe them into OpenCPN.  You then use OpenCPN for navigation
based on Starlink location. This should bypass GPS, and should help if
GPS is unavailable or spoofed.

### GPS loss-alerting

The GPS_loss_alerting folder in this software contains a program that
pulls starlink and NMEA positions from signalk and compares them and
sends an alert when the two gps sources disagree by more than 0.1
nautical miles. This alert could indicate you should switch from your
standard chartplotter gps source to an alternate way of getting location
data into your chartplotter or OpenCPN (e.g. by selecting Starlink as
a location data source).

It will also detect when Starlink or GPS location becomes unavailable
(data timeout). It will send an email alert. This should help warn a
cruiser that they need to switch to alternate navigation solution.

#### System Requirements

This program requires that there be a computer running signalk that
has access to your NMEA network.  It is built to be a linux service,
but can be run from the command-line or an IDE on any computer - it is
intended to work on both Windows and Linux.

# Starlink setup

All these capabilities that use Starlink position data rely 
on the Starlink antennrereada making its position
data available on the local network. Depending on the capability, other
configuration or software installation may be needed.

Follow the instructions at [this page](starlink_setup.html) to configure your
Starlink antenna to make its data available on the local network.

# Starlink->PredictWind Datahub->Chartplotter or OpenCPN setup

Follow the instructions at [this page](pw_datahub_setup.html) to configure your
Starlink location data to be forwarded via PredictWind's Datahub to your
chartplotter or OpenCPN

# Starlink->Signalk->OpenCPN setup

Follow the instructions at [this page](signalk_opencpn_setup.html)
to configure Signalk and OpenCPN to use Starlink data.

# Starlink->Finn's python scripts -> OpenCPN setup

Follow the instructions at [this page](opencpn_setup.html) to configure the
python scripts to forward Starlink location data to OpenCPN

# GPS Loss-Alerting setup

Follow the instructions at [this page](gps_loss_alerting_setup.html) to configure
your Starlink location to be compared to GPS, and the comparison results printed
and sent to email and/or Telegram if they don't match.

# The GitHub repo

The capabilities described above are supported by various software and documentation
which is stored on Github at [Maddox-zephyr/starlink_position](https://github.com/Maddox-zephyr/starlink_position).

# Repo Maintainers

See the [repo maintainer instructions](repo_maintainer_instructions.html) for
more information about the structure of the repo and how to make changes to it.

# Repo tabs

The repo also has tabs for various purposes:

- A wiki tab. The wiki is open and can be read and updated by anyone with a GitHub
account, and is intended for documenting user-findings that are not in the
documentation.
- An issues tab, used for reporting bugs
- A discussion tab, used for asking questions, making suggestions, etc

Generally, you can browse the repo, look at the issues list etc without
logging into GitHub. If you wish to create discussions or issues, modify the wiki,
or other activities that modify the repo contents you must be logged into GitHub.
Create an account if you don't have one at https://github.com and log in, and
you'll be more powerful, and be able to contribute to the happiness of your
fellow cruisers.

# Future sections

1. FAQ
