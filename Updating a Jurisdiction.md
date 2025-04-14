# Updating a Jurisdiction

<h4> Updating a Jurisdiction will require using ArcGIS Pro or another GIS software. This guide will go over how to use ArcGIS Pro.</h4>

## Step 1: Downloading the Data

The first step to updating your jurisdiction is downloading the statewide data from this repository. If you are unfamiliar with GitHub lingo, fear not!  
If you open the "Data" folder in a new tab, you'll find a ".geojson" file that has all the zoning data for the state of Vermont. You'll want to download this (it might take a bit, because it is a large file)

## Step 2: Opening the data in ArcGIS Pro

Now that you have the statewide .geojson file downloaded, you're going to want to open up ArcGIS Pro.

First, make a new project, and then open up the geoprocessing window
![1](https://github.com/user-attachments/assets/d7e3dacd-8d89-4aec-9763-b2bdcf983b9c)

Then, type in "geojson" into the search bar. We want the "JSON to Features" tool
![2](https://github.com/user-attachments/assets/b563738f-4bd5-4ccc-8894-ab5e03cfdd84)

From here, you'll fill out the tool with the .geojson file you downloaded, and give the feature class a reasonable name like "VT Zoning"  

The resulting feature class will be in the coordinate system "WGS 1984". This is not great if you are planning on changing any geometries, so we're going to project our feature class. Skip this step if you are **only changing the attribute talbe**  

To project the state-wide zoning feature class, go back to geoprocessing and find the "project" tool.  

![3](https://github.com/user-attachments/assets/d4765985-7448-413b-bd69-4cfa20973ab6)

From there, be sure to select "NAD 1983 StatePlane Vermont FIPS 4400 (Meters)". The easiest way to access this coordinate system is to type "32145" into the search bar.

![4](https://github.com/user-attachments/assets/5a1ea6e8-3bc9-48be-ad68-b744c05bdcf0)

Be sure to give your output feature class a name to distiguish it from the old feature class. A good convention is to add "_32145" to the end of the name, so you know the coordinate system.  

Great! So now we have a nice looking state-wide zoning dataset, but the scale just a bit too large for us to make edits and upload back to GitHub.

## Step 3: Exporting your Jurisdiction into a new Feature Class

The first thing we want to do is make sure we are exporting the right geometries. We can ensure this by going to select by attributes, and setting an exxpression where the jurisdiction is equal to the jurisdiction we want to edit
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




