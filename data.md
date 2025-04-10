---
title: Data
layout: default
---
# Data

Data has been broken into smaller files for ease in editing. In "[data/RPC](https://github.com/VERSO-UVM/Vermont-Zoning-Atlas/tree/main/data/RPCs)" all the zoning files are split out into the Regional Planning Commissions (RPC). This geojson can be explored in the abbreviated viewer on the homepage of this site or downloaded for further analysis.

|Management Region | Website | Abbrev. |
|--------|------------|------|
|Addison County | 	[www.acrpc.org/](http://www.acrpc.org/) | ACRPC |
|Bennington County | 	[www.bcrcvt.org/](http://www.bcrcvt.org/) | BCRC |
|Chittenden County | [www.ccrpcvt.org](www.ccrpcvt.org) | CCRPC |
|Central Vermont | 	[www.centralvtplanning.org](www.centralvtplanning.org) | CVRPC |
|Lamoille County | 	[www.lcpcvt.org](www.lcpcvt.org) | LCPC |
|Mount Ascutney  |  	[https://marcvt.org/](https://marcvt.org/) | MARC |
|Northwest | 	[www.nrpcvt.com](www.nrpcvt.com) | NWRPC |
|Northeastern | [www.nvda.net](www.nvda.net) | NVDA |
|Rutland | 	[www.rutlandrpc.org](www.rutlandrpc.org) | RPC |
|Two Rivers-Ottauquechee | [www.trorc.org](www.trorc.org) | TRORC |
|Windham | [www.windhamregional.org](www.windhamregional.org) | WRC |

There is also a state-wide single file, "[data/State of Vermont](https://github.com/VERSO-UVM/Vermont-Zoning-Atlas/tree/main/data/State_of_Vermont)", this is not the preferred way to update the files but rather for analysis.

If you are interested in viewing the legal PDFs downloaded as part of this process, explore "[data/Town_Bylaw_Text](https://github.com/VERSO-UVM/Vermont-Zoning-Atlas/tree/main/data/Town_Bylaw_Text)" and the downloaded maps from town websites here: "[data/Town_Zoning_Maps](https://github.com/VERSO-UVM/Vermont-Zoning-Atlas/tree/main/data/Town_Zoning_Maps)"

## Collection Timeline and Data Error Warning
This effort is a collection of teams which includes volunteers, interns, and students. This was done over a year period from 2023-2024 and during this time updates to the zoning codes have already made some of this data inaccurate. It is likely that this data will only be updated once a year at most so this data can be out of date. It is also possible that the regulation from the State of Vermont may not be reflected in town zoning just due to the time it takes to update and comply with legislation and the very limited capacity many of these towns have to complete that work. 

## Fields
There is a large number of fields, the naming and in some cases the implementation will differ from the National Zoning Atlas. We will also only be maintaining a subset of these dataset over time and markers will be added to the list below when that has been determined.

| Field Names | Description | Data Type | Potential Maintained Fields |
|--------|------------|------|-----|
|County| County the jurisdiction lies in|Text| Yes |
|RPC| Regional Planning Commission Abbreviation the jurisdiction lies in|Text| Yes |
|Jurisdiction| Jurisdiction (ex. Salisbury)|Text| Yes |
|Jurisdiction District Name| Jurisdiction + Full District Name (ex. Salisbury Low Density Residential)|Text| Yes |
|District Name| Full District Name (ex. Low Density Residential)|Text| Yes |
|Abbreviated District Name| Abbreviated District Name (ex. LDR)|Text| Yes |
|District Mapped| Is the District Mapped (yes/no) |Text|
|Overlay District| Is the District an Overlay District (yes/no) |Text| Yes |
|Extinct District| Is the District Extinct (yes/no)|Text|
|District Type| One of 4 options (Primarily Residential, Mixed with Residential, Nonresidential, Overlay, Overlay Not Affecting Use)|Text|
|Affordable Housing District| Affordable Housing District (yes/no)|Text|
|Elderly Housing District| Elderly Housing District (yes/no)|Text|
|1F Allowance| Single Family Home Allowance (Permitted, Public Hearing, Prohibited, and Overlay)|Text| Yes |
|2F Allowance| Two Family Home Allowance (Permitted, Public Hearing, Prohibited, and Overlay)|Text| Yes |
|3F Allowance| Three Family Home Allowance (Permitted, Public Hearing, Prohibited, and Overlay)|Text| Yes |
|4F Allowance| Four Family Home Allowance (Permitted, Public Hearing, Prohibited, and Overlay)|Text| Yes |
|5F Allowance| Five Family Home Allowance (Permitted, Public Hearing, Prohibited, and Overlay)|Text|
|ADU Allowance| Accessory Dwelling Unit Allowance (Permitted, Public Hearing, Prohibited, and Overlay)|Text| Yes |
|Affordable Housing Allowance| Affordable Housing Allowance (Permitted, Public Hearing, Prohibited, and Overlay)|Text| Yes |
|PRD Allowance| Planned Residential Development Allowance (Permitted, Public Hearing, Prohibited, and Overlay)|Text| Yes |
|Base Density| District density before modifiers are applied in units per acre|Number (2 decimal places)|
|Notes| Notes about the bylaws that would otherwise not be included in the dataset|Text|
|XF Affordable Housing Only| X is any number between 1-5; District only allows affordable housing (yes/no)|Text|
|XF Elderly Housing Only| X is any number between 1-5; District only allows elderly housing (yes/no)|Text|
|XF Min Lot| X is any number between 1-5; Min Lot size in acres|Number (2 decimal places)| Yes |
|XF Max Density| X is any number between 1-5; Max density of units in units per acre|Number (2 decimal places)| Yes |
|XF Front Setback| X is any number between 1-5; Min Front Setback in feet|Number (2 decimal places)|
|XF Side Setback| X is any number between 1-5; Min Side Setback in feet|Number (2 decimal places)|
|XF Rear Setback| X is any number between 1-5; Min Rear Setback in feet|Number (2 decimal places)|
|XF Frontage| X is any number between 1-5; Min Frontage in feet|Number (2 decimal places)|
|XF Max Lot Building Coverage| X is any number between 1-5; Max percent of plot that can be covered by buildings|Number (2 decimal places)|
|XF Max Lot Impervious Coverage| X is any number between 1-5; Max percent of plot that can be covered by impervious surfaces|Number (2 decimal places)|
|XF Min Parking Spaces 1BR| X is any number between 1-5; Min Parking Spaces required per 1 bedroom unit (Note: "1F Min Parking Spaces" field does not include "1BR")|Number (2 decimal places)|
|XF Min Parking Spaces mult BR| X is any number between 1-5; Min Parking Spaces required per 2 or more bedroom unit|Number (2 decimal places)|
|XF Max Stories| X is any number between 1-5; Max building height in stories|Number (2 decimal places)|
|XF Max Height| X is any number between 1-5; Max building height in feet|Number (2 decimal places)|
|XF Floor to Area Ratio| X is any number between 1-5; Min building floor area relative to the lot size|Number (2 decimal places)|
|XF Min Unit Size| X is any number between 1-5; Min unit size in square feet|Number (2 decimal places)|
|XF Connection to Sewage/Water Required| X is any number between 1-5; Connection to Public Sewage/Water required (yes/no)|Text| Yes |
|XF Proximity to Public Transit Required| X is any number between 1-5; Proximity to Public Transit required (yes/no)|Text|
|XF Max Bedrooms| X is any number between 1-5; Max bedrooms per X family unit|Number (2 decimal places)|
|XF Max Units per Building| X is any number between 1-5; Max X family units per building|Number (2 decimal places)|
|Affordable Housing Definition| Jurisdiction's definition, sometimes varies/refers to other sources|Text|
|Affordable Housing Elderly Only| Is affordable housing limited to elderly housing? (yes/no)|Text|
|Affordable Housing Min Lot Size| Min lot size for affordable housing units in acres|Number (2 decimal places)|
|Affordable Housing Max Density| Max density of affordable housing units in units per acre|Number (2 decimal places)|
|Affordable Housing Min Parking Spaces per 1BR| Min Parking Spaces required per 1 bedroom affordable housing unit|Number (2 decimal places)|
|Affordable Housing Min Perking Spaces per mult BR| Min Parking Spaces required per 2 or more bedroom affordable housing unit|Number (2 decimal places)|
|Affordable Housing Min Unit Size| Affordable Housing min U=unit size in square feet|Number (2 decimal places)|
|Affordable Housing Max Bedrooms| Affordable housing max bedrooms per unit|Number (2 decimal places)|
|Affordable Housing Max Units per Building| Max number of affordable housing units per building|Number (2 decimal places)|
|ADU Employee or Family Occupancy Required| Employee or family occupancy required (yes/no)|Text|
|ADU Renter Occupancy Prohibited| Renter occupancy prohibited in accessory dwelling units (yes/no)|Text|
|ADU Owner Occupancy Required| Owner occupancy required (yes/no)|Text|
|ADU Elderly Housing Only| Accessory dwelling units are restricted to elderly housing only (yes/no)|Text|
|ADU Min Lot Size| Accessory dwelling unit min lot size in acres|Number (2 decimal places)|
|ADU Min Parking Spaces| Min Parking Spaces required per accessory dwelling unit|Number (2 decimal places)|
|ADU Restricted to Primary Structure| Accessory dwelling units restricted to additions on primary structures (yes/no)|Text|
|ADU Max Size as Percent of Primary Structure| Accessory dwelling unit max size as percent of the primary structure|Number (2 decimal places)|
|ADU Max Size in sq ft| Accessory dwelling unit max size in square feet|Number (2 decimal places)|
|ADU Max Bedrooms| Max bedrooms per accessory dwelling unit|Number (2 decimal places)|
|PRD Mobile or Manufactured Home Park| Does the district allow Mobile or Manufactured Home Parks? (yes/no)|Text| Yes |
|PRD Min Lot Size| Planned Residential District min lot size in acres|Number (2 decimal places)|
|PRD Max Density| Planned Residential District max density in units per acre|Number (2 decimal places)|
|PRD Max Units| Max units per Planned Residential District|Number (2 decimal places)|
|PUD Required with Subdivision| Planned Unit Development required with parcel sub-division (yes/no)|Text|
|PUD Threshold Number| Planned Unit Development threshold Number|Number (0 decimal places)|
|PUD Allowance| Are Planned Unit Developments in bylaws? (yes/no)|Text|
|PUD Requires Land Conservation| Planned Unit Developments require land conservation (yes/no)|Text|
|CONDITIONAL + Other Field name| alternative value for field (ex. CONDITIONAL 1F Min Lot = 2 if Water And Sewer; 3 W/Out Water And Sewer)|Text (generally multiple lines to explain)|
|Bylaw Date| Date of Bylaw that data is based off (for versioning purposes)| YYYY-MM-DD (Ex. 2024-05-31)|
|Version| Zoning Atlas version (also for versioning purposes)|Number (0 decimal places)
|Acres| Size of district in acres| Number (many decimal places, calculated via Shape_Area field)|

