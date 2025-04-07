---
title: Data
layout: default
---
# Data

Data uploaded to the National Zoning Atlas can be found in the "ZoningAtlas" folder as follows:
- data/zoning_atlas_geojson - The Vermont Zoning Map geojson data, this is where changes or updates to geojson should be added
- data/zoning_bylaws - Zoning Bylaw text from towns in PDF or Word for reference
- data/zoning_maps - Maps of jurisdictions in PDF, PNG or JPG format for reference

## Join the Effort
This effort is a collection of teams which includes volunteers, interns, and students getting course credit. Please reach out in Discussions to see if you can join the effort! Take a look at at the [Contribute](contribute.md) page to understand how to submit changes once you have made yourself familiar with this data

---
|Field Names| Description|Data Type|
|--------|------------|------|
|County| County the jurisdiction lies in|Text|
|RPC| Regional Planning Comission Abbreviation the jurisdiction lies in|Text|
|Jurisdiction| Jurisdiction (ex. Salisbury)|Text|
|Jurisdiction District Name| Jurisdiction + Full District Name (ex. Salisbury Low Denisty Residential)|Text|
|District Name| Full District Name (ex. Low Density Residential)|Text|
|Abbreviated District Name| Abbreviated District Name (ex. LDR)|Text|
|District Mapped| Is the District Mapped (yes/no) |Text|
|Overlay District| Is the District an Overlay District (yes/no) |Text|
|Extinct District| Is the District Extinct (yes/no)|Text|
|District Type| One of 4 options (Primarily Residential, Mixed with Residential, Nonresidential, Overlay, Overlay Not Affecting Use)|Text|
|Affordable Housing District| Affordable Housing District (yes/no)|Text|
|Elderly Housing District| Elderly Housing District (yes/no)|Text|
|1F Allowance| Single Family Home Allowance (Permitted, Public Hearing, Prohibited, and Overlay)|Text|
|2F Allowance| Two Family Home Allowance (Permitted, Public Hearing, Prohibited, and Overlay)|Text|
|3F Allowance| Three Family Home Allowance (Permitted, Public Hearing, Prohibited, and Overlay)|Text|
|4F Allowance| Four Family Home Allowance (Permitted, Public Hearing, Prohibited, and Overlay)|Text|
|5F Allowance| Five Family Home Allowance (Permitted, Public Hearing, Prohibited, and Overlay)|Text|
|ADU Allowance| Accessory Dwelling Unit Allowance (Permitted, Public Hearing, Prohibited, and Overlay)|Text|
|Affordable Housing Allowance| Affordable Housing Allowance (Permitted, Public Hearing, Prohibited, and Overlay)|Text|
|PRD Allowance| Planned Residential Development Allowance (Permitted, Public Hearing, Prohibited, and Overlay)|Text|
|Base Density| District density before modifiers are applied in units per acre|Number (2 decimal places)|
|Notes| Notes about the bylaws that would otherwise not be included in the dataset|Text|
|XF Affordable Housing Only| X is any number between 1-5; District only allows affordable housing (yes/no)|Text|
|XF Eldely Housing Only| X is any number between 1-5; District only allows elderly housing (yes/no)|Text|
|XF Min Lot| X is any number between 1-5; Min Lot size in acres|Number (2 decimal places)|
|XF Max Density| X is any number between 1-5; Max density of units in units per acre|Number (2 decimal places)|
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
|XF Min Unit Size| X is any number between 1-5; Min unit size in squre feet|Number (2 decimal places)|
|XF Connection to Sewage/Water Required| X is any number between 1-5; Connection to Public Sewage/Water required (yes/no)|Text|
|XF Proximity to Public Transit Required| X is any number between 1-5; Proximity to Public Transit required (yes/no)|Text|
|XF Max Bedrooms| X is any number between 1-5; Max bedrooms per X family unit|Number (2 decimal places)|
|XF Max Units per Building| X is any number between 1-5; Max X family units per building|Number (2 decimal places)|
|Affordable Housing Definition| Jurisdiction's definition, sometimes varies/refers to other sources|Text|
|Affordable Housing Elderly Only| Is affordable housing limited to elderly housing? (yes/no)|Text|
|Affordable Housing Min Lot Size| Min lot size for affordable housing units in acres|Number (2 decimal places)|
|Affordable Housing Max Density| Max density of affordable houisng units in units per acre|Number (2 decimal places)|
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
|ADU Min Parking Spaces| Min Parking Spaces required per accesory dwelling unit|Number (2 decimal places)|
|ADU Restricted to Primary Structure| Accessory dwelling units restricted to additions on primary structures (yes/no)|Text|
|ADU Max Size as Percent of Primary Structure| Accessory dwelling unit max size as percent of the primary structure|Number (2 decimal places)|
|ADU Max Size in sq ft| Accessory dwelling unit max size in square feet|Number (2 decimal places)|
|ADU Max Bedrooms| Max bedrooms per accessory dwelling unit|Number (2 decimal places)|
|PRD Mobile or Manufactured Home Park| Does the district allow Mobile or Manufactured Home Parks? (yes/no)|Text|
|PRD Min Lot Size| Planned Residential District min lot size in acres|Number (2 decimal places)|
|PRD Max Density| Planned Residential District max density in units per acre|Number (2 decimal places)|
|PRD Max Units| Max units per Planned Residential District|Number (2 decimal places)|
|PUD Required with Subdivision| Planned Unit Development required with parcel subidivision (yes/no)|Text|
|PUD Threshold Number| Planned Unit Development threshold Number|Number (0 decimal places)|
|PUD Allowance| Are Planned Unit Developments in bylaws? (yes/no)|Text|
|PUD Requires Land Conservation| Planned Unit Developments require land conservation (yes/no)|Text|
|CONDITIONAL + Other Field name| alternative value for field (ex. CONDITIONAL 1F Min Lot = 2 if Water And Sewer; 3 W/Out Water And Sewer)|Text (generally multiple lines to explain)|
|Bylaw Date| Date of Bylaw that data is based off (for versioning purposes)|Date Year-MM-DD (Ex. 2024-05-31)|
|Version| Zoning Atlas version (also for versioning purposes)|Number (0 decimal places)
|Acres| Size of district in acres| Number (many decimal places, calculated via Shape_Area field)|
---
