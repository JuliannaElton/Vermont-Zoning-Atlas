# Updating a Jurisdiction

<h4> Updating a Jurisdiction will require using ArcGIS Pro or another GIS software. This guide will go over how to use ArcGIS Pro.</h4>

## Step 1: Downloading the Data

The first step to updating your jurisdiction is downloading the data from this repository. If you are unfamiliar with GitHub lingo, fear not!  

From the main Vermont Zoning Atlas page, if you open the "Data" folder, you'll find a folder called "RPC". You'll want to open this folder, and download the RPC your jurisdiction is in (you're looking for a .geojson file). If you aren't sure which RPC your jurisdiction belongs to, you can always do a quick google search or check https://github.com/VERSO-UVM/Vermont-Livability-Map/blob/main/Visualization%20Guide%20by%20Layer.pdf (You'll have to scroll a bit/use command F, as this document is primarily for data visualizations)

## Step 2: Opening the data in ArcGIS Pro

Now that you have the RPC .geojson file downloaded, you're going to want to open up ArcGIS Pro.

First, make a new project, and then open up the geoprocessing window
![1](https://github.com/user-attachments/assets/d7e3dacd-8d89-4aec-9763-b2bdcf983b9c)

Then, type in "geojson" into the search bar. We want the "JSON to Features" tool
![2](https://github.com/user-attachments/assets/b563738f-4bd5-4ccc-8894-ab5e03cfdd84)

From here, you'll fill out the tool with the .geojson file you downloaded, and give the feature class a reasonable name like "VT_Zoning"  

The resulting feature class will be in the coordinate system "WGS 1984". This is not great if you are planning on changing any geometries, so we're going to project our feature class. Skip this step if you are **only changing the attribute table**  

To project the state-wide zoning feature class, go back to geoprocessing and find the "project" tool.  

![3](https://github.com/user-attachments/assets/d4765985-7448-413b-bd69-4cfa20973ab6)

From there, be sure to select "NAD 1983 StatePlane Vermont FIPS 4400 (Meters)". The easiest way to access this coordinate system is to type "32145" into the search bar.

![4](https://github.com/user-attachments/assets/5a1ea6e8-3bc9-48be-ad68-b744c05bdcf0)

Be sure to give your output feature class a name to distiguish it from the old feature class. A good convention is to add "_32145" to the end of the name, so you know the coordinate system.  

Great! So now we have a nice looking state-wide zoning dataset, but the scale just a bit too large for us to make edits and upload back to GitHub.

## Step 3: Exporting your Jurisdiction into a new Feature Class

The first thing we want to do is make sure we are exporting the right geometries. We can ensure this by going to select by attributes, and setting an expression where the jurisdiction is equal to the jurisdiction we want to edit
![5](https://github.com/user-attachments/assets/cb6185b5-e704-4e24-8c2f-603e6d4ad938)

![6](https://github.com/user-attachments/assets/5705759a-4547-4d9d-a82d-e4c7276136e5)

After that we want to export our selected features as a new feature class. We can do this in a few ways, but the easiest way is to right click on our state-wide zoning layer and hover over the "data" section, and then click export features. This will take you to a new menu where you can give the new feature class a name (a good idea is to name it the jurisdiction name).  

A note before you run the tool:  
Make sure your selection went through, you should have a number at the bottom right. In the example below, I had 24 items selected which corresponds to the 24 districts in the jurisdiction of Hardford.

![7](https://github.com/user-attachments/assets/890c6f78-760b-4762-b7a0-4fed679d7b32)

## Step 4: Editing Jurisdiction Data

Ideally, at this point we should have a feature class with your just the jurisdiction we want to edit, and nothing else.  

This feature class should also have the Vermont StatePlane coordinate system, and if you haven't yet be sure to change your map's coordinate system to also be "NAD 1983 StatePlane Vermont FIPS 4400 (Meters)"  

You can right click on the map in your contents pane (same process as exporting the feature class), and click "properties" 

![8](https://github.com/user-attachments/assets/8a5b0e07-b60e-427c-a7ff-cc701d1b446a)

You can then click "coordinate systems", and under that click on the "NAD 1983 StatePlane Vermont FIPS 4400 (Meters)" option, under "Layers"

![9](https://github.com/user-attachments/assets/dcb32bc5-ac5b-4c25-879e-cfb81d6029f3)

#### But why does this matter?

That's a great question!  

If you are editing geometries, and especially if you are digitizing a pdf/jpg/png map, you want to make sure you aren't stretching Vermont into a weird shape. The default "WGS 1984" coordinate system does just that.  

Here's what Vermont looks like in the WGS 1984 projection: (very wide, and short)

![10](https://github.com/user-attachments/assets/1018f89b-4abb-438e-8bae-111228b49d96)

Here's what Vermont looks like in the StatePlane projection: (normal)

![11](https://github.com/user-attachments/assets/9a1db45d-76a0-42a1-8a7c-eccda533df93)

#### Editing the Attribute Table

If you are not changing the shape/location of any districts within your jurisdiction, you can open up the attribute table and change the values based on the zoning bylaws.  

To do this, we'll start by opening the attribute table by right clicking the jurisdiction feature class.

![12](https://github.com/user-attachments/assets/f097852d-8ab2-4062-b57a-bfa3c2d7e9e1)

Now in this example, I want to edit the "1F Allowance" field. I can do this by double clicking the cell I want to change, and typing in what I want to replace it with. Be sure to check out the documentation in this repository on the data types and structures. This is important for data to be standardized statewide! For example, if one jurisdiction had "allowed" instead of "permitted", it would make running statistical analysis much harder, and these values will have to be replaced manually.  

So, if you're not certain about something, check out the documentation (https://github.com/VERSO-UVM/Vermont-Zoning-Atlas/blob/main/data.md), or send an email!

![13](https://github.com/user-attachments/assets/c4def805-5cc1-4d01-b923-06c050b4c577)

#### Editing Geometries

Explaining how ArcGIS Pro handles modify and create features is not something I will be outlining here, but I do want to make a few important notes.  

1: All jurisdictions are bound to **US CENSUS TIGER Boundaries**. If you have updated geometries, these need to be clipped/stretched to fit within the TIGER boundary. Using these boundaries allows for easier state-wide viewing, and smoothes over boundary confusion. Download TIGER boundary files [INSERT LINK HERE] (you will want to do the same process of exporting your jurisdiction in a new feature class to avoid confusion).  
2: We do not want districts overlapping (aside from overlay districts). Overlaps make it difficult to run accurate statistics (especially area based statistics), and can be very hard to notice. Topologies are the best way to avoid running into these, but you can always reach out or upload your update files with a message if you are unsure how to avoid overlaps.  

Best pathways to editing geometries:  
Ideally, we don't want to upload new files to the reopository, because we would then lose the existing structure (namely the attribute table). So what can we do to keep the table in tact, but change the geometries?

1) Starting from a .shp file (or any other GIS file) with the new geometries
- Ensure that both the new GIS file, and the jurisdiction feature class (with the table we want) share a field in common with a unique value for each row (you might have to make a new field on the new GIS file, but this shouldn't be too hard as most jurisdictions have less than 40 unique districts).
- You'll then want to use the "Join Field" geoprocessing tool to join all the field from the table we want to the feature class with the new geometry (the new GIS file). The "join field" is the field that both tables have (this is what ArcGIS uses to figure out what rows get joined where)
- Then delete any fields that weren't in the attribute table that you downloaded from GitHub, we don't want extra fields! 

2) Starting from a .jpg (or any other image file) map
- Make sure your image file can be brought into ArcGIS Pro (.png and .jpg are safe bets) and then do so.
- You're then going to want to do a georeference which can be a bit confusing, so stay with me!
- I have linked below a video I made for the Maine Zoning Atlas (some of the information might be catered towards the National Zoning Atlas website, so you can ignore those parts).
- You'll want to start at the 35:30 timestamp in the video for how to georeference
- [https://www.youtube.com/watch?time_continue=2132&v=fDVrvpTZVPw&embeds_widget_referrer=https%3A%2F%2Fstorymaps.arcgis.com%2Fstories%2Fc8c4f421004f46fc862d296f3b277022&embeds_referring_euri=https%3A%2F%2Fcdn.embedly.com%2F&embeds_referring_origin=https%3A%2F%2Fcdn.embedly.com&source_ve_path=MTM5MTE3LDE2NDk5LDIzODUx ](https://www.youtube.com/watch?v=fDVrvpTZVPw&t=2132s)


## Uploading Data

Now that we have our updated jurisdiction data we need to do a few final steps before we can upload it to GitHub.

First, we need to put our data into the same format that we downloaded it as, a .geojson file

Type "geojson" into the geoprocessing search bar, and this time we want "features to json"
![14](https://github.com/user-attachments/assets/861a5937-ab74-4bd9-a19d-6cd52008bc41)


Once we're in the tool menu, we want to have the input feature be the file we've been working on, and we need to check off "Output to GeoJSON", "Project to WGS_1984", and "Use field aliases"
![15](https://github.com/user-attachments/assets/1a2cfa92-bb6b-4080-b639-337f5823d772)

Great! We're now done with the hard part!

From here everything will be on GitHub (the browser), so you can save and close your ArcGIS Pro project.

If you do not already have a GitHub account, make sure you create one or sign in before continuing (having an account is also helpful for us to see where changes are coming from).
  
We're going to create a "fork" from the repository and submit a "pull request" to have our data merged with everything else in the repository.

How does this work?
  
Essentially, we're just making a copy of the repository, adding in our one new file, and then asking the manager of the repository to merge the fork into the repository (this is how most open source projects work).

#### Step 1: Create a Fork

Go to the Vermont Zoning Atlas GitHub page, and click "Fork" at the top of the page

![16](https://github.com/user-attachments/assets/a2424f94-914e-4fae-be42-0bc9d518a7e7)

You can keep the defaults, and click, "Create fork"

![17](https://github.com/user-attachments/assets/5a816b06-c711-4494-8221-d0f60262afd7)

Now, we're in the copied (forked) version of the repository. You can open up the "Data" folder, and click "Add file" and "Upload files"

![18](https://github.com/user-attachments/assets/55dd2d61-a9f1-4aac-9d52-ddeef34ee4fa)

Here, you'll upload the updated jurisdiction .geojson file you created into the repo. [ADD MORE INFO IF THIS UPDATES TO BE A SPECIFIC FOLDER]

![19](https://github.com/user-attachments/assets/df76d707-b84c-4423-875b-620eb1f4c266)


Now we're going to go back to the original repository (the UVM VERSO one https://github.com/VERSO-UVM/Vermont-Zoning-Atlas), and we want to click "pull requests" at the top

![20](https://github.com/user-attachments/assets/8a3bd1b1-1fcb-4675-b269-e821419cc0ba)

From here we want to click "New pull request"

![21](https://github.com/user-attachments/assets/ad7ea001-9f7b-4d6d-85fc-03490e1b606f)

And then, "Compare across forks"

![22](https://github.com/user-attachments/assets/85e2211b-ab49-4072-aceb-ad8bf365adab)

This part is the most involved to stay with me, we're almost there!

1) Make sure the left repository is the "VERSO-UVM" repository, and the one on the right is your forked repository (it will start with your user name)
2) At the bottom, you should see some additions (green highlight) and ideally no deletions (red highlight). If this is not the case, first make sure you uploaded your .geojson file to your repository. Then, reach out to us if you have further problems. Worst case, your data can be added in from our end!
3) Click "Create pull request" and then you''re done!

![23](https://github.com/user-attachments/assets/2c210051-2ed4-43b8-bb59-67af0893b47f)


