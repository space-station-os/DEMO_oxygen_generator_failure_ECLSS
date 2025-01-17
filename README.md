# DEMO_oxygen_generator_failure_ECLSS
Demo for SSOS/ECLSS system 

## SCENARIO
To test a scenario where the O2 generator fails and only the backup supplies are working. Scenario in which the main oxygen generator on both the Russian-module (Elektron) and the US module (Oxygen Generator Assembly (OGA)), cannot be repaired in a short period of time and a new crew is about to orbit the ISS, also there is an air leak entering for a small hole from Russian module located in a vestibule that separates a progress docking port form the rest of the service module. 
This repository will determinate How long the oxygen backup will be remained in the international space station. Hole size and hole direction can be selected by the user as well as the number of crew members.

![Image reference from: https://www.adastraspace.com/p/iss-air-leaks-2030](https://github.com/space-station-os/DEMO_oxygen_generator_failure_ECLSS/blob/main/Figures/hole_location.png?raw=true)

The backups system to consider are: 
1.Vozdukh (which means "air" in Russian): backup carbon dioxide removal system with oxygen supply capability.
2.Rodnik (SFOGs): non-rechargeable oxygen generators for emergency situations.
(tanks)
Both Backup systems are part of the Russian Module Zvezda. The (CDRA removal located in the American side will not be used as backup system in this material as we are assuming that OGS doesn’t work.)

![Table reference “from Life Support Baseline Values and Assumptions Document
https://ntrs.nasa.gov/api/citations/20210024855/downloads/BVAD_2.15.22-final.pdf”](https://raw.githubusercontent.com/space-station-os/DEMO_oxygen_generator_failure_ECLSS/refs/heads/main/Figures/Table_oxygen_consumption.png)
