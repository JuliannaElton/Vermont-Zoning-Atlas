---
title: Index
layout: default
---
<head>
  <link rel="stylesheet" href="https://unpkg.com/leaflet/dist/leaflet.css" />
  <script src="https://unpkg.com/leaflet/dist/leaflet.js"></script>
  <script src="https://unpkg.com/flatgeobuf@3.26.2/dist/flatgeobuf-geojson.min.js"></script>
</head>


# Vermont Zoning Atlas

**This is a community built dataset, use at your own risk and check with your local town offices!**

The [Vermont Zoning Atlas](https://www.zoningatlas.org/vermont) is a web-based geospatial interface that visualizes zoning code distributions across all of Vermont. 
<div id="map" style="width: 100%; height: 800px;"></></div>

<script>
  // Initialize the map
  var map = L.map('map').setView([43.951, -72.756], 7);

  // Add a tile layer to the map
  L.tileLayer('https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png', {
    attribution: '&copy; <a href="https://www.openstreetmap.org/copyright">OpenStreetMap</a> contributors'
  }).addTo(map);

  // List of fields to display in the popup
  var fieldsToDisplay = ["Jurisdiction County","Jurisdiction District Name", "District Type", "District Name","Overlay District","1F Allowance","2F Allowance","3F Allowance","3F Connection to Sewage/Water Required","3F Elderly Housing Only","4F Allowance","4F Connection to Sewage/Water Required","4F Elderly Housing Only", "Affordable Housing District","ADU Owner Occupancy Required","1F Connection to Sewage/Water Required","1F Elderly Housing Only","2F Connection to Sewage/Water Required","2F Elderly Housing Only"]; 

  // Function to bind popups to each feature
  function onEachFeature(feature, layer) {
    if (feature.properties) {
      var popupContent = "<p><strong>Attributes:</strong></p>";
      fieldsToDisplay.forEach(field => {
        if (feature.properties[field] !== undefined) {
          popupContent += "<p>" + field + ": " + feature.properties[field] + "</p>";
        }
      });
      layer.bindPopup(popupContent);
    }
  }


  // Fetch the GeoJSON data and add it to the map
  fetch('data/RPC/ACRPC/ACRPC_Zoning.geojson')
    .then(response => {
      if (!response.ok) {
        throw new Error('Network response was not ok ' + response.statusText);
      }
      return response.json();
    })
    .then(data => {
      L.geoJSON(data, {
        onEachFeature: onEachFeature
      }).addTo(map);
    })
    .catch(error => console.error('Error loading GeoJSON data:', error));

    // Fetch the GeoJSON data and add it to the map
  fetch('data/RPC/BCRC/BCRC_Zoning.geojson')
    .then(response => {
      if (!response.ok) {
        throw new Error('Network response was not ok ' + response.statusText);
      }
      return response.json();
    })
    .then(data => {
      L.geoJSON(data, {
        onEachFeature: onEachFeature
      }).addTo(map);
    })
    .catch(error => console.error('Error loading GeoJSON data:', error));

    // Fetch the GeoJSON data and add it to the map
  fetch('data/RPC/CCRPC/CCRPC_Zoning.geojson')
    .then(response => {
      if (!response.ok) {
        throw new Error('Network response was not ok ' + response.statusText);
      }
      return response.json();
    })
    .then(data => {
      L.geoJSON(data, {
        onEachFeature: onEachFeature
      }).addTo(map);
    })
    .catch(error => console.error('Error loading GeoJSON data:', error));

      // Fetch the GeoJSON data and add it to the map
  fetch('data/RPC/CVRPC/CVRPC_Zoning.geojson')
    .then(response => {
      if (!response.ok) {
        throw new Error('Network response was not ok ' + response.statusText);
      }
      return response.json();
    })
    .then(data => {
      L.geoJSON(data, {
        onEachFeature: onEachFeature
      }).addTo(map);
    })
    .catch(error => console.error('Error loading GeoJSON data:', error));


      // Fetch the GeoJSON data and add it to the map
  fetch('data/RPC/LCPC/LCPC_Zoning.geojson')
    .then(response => {
      if (!response.ok) {
        throw new Error('Network response was not ok ' + response.statusText);
      }
      return response.json();
    })
    .then(data => {
      L.geoJSON(data, {
        onEachFeature: onEachFeature
      }).addTo(map);
    })
    .catch(error => console.error('Error loading GeoJSON data:', error));


      // Fetch the GeoJSON data and add it to the map
  fetch('data/RPC/MARC/MARC_Zoning.geojson')
    .then(response => {
      if (!response.ok) {
        throw new Error('Network response was not ok ' + response.statusText);
      }
      return response.json();
    })
    .then(data => {
      L.geoJSON(data, {
        onEachFeature: onEachFeature
      }).addTo(map);
    })
    .catch(error => console.error('Error loading GeoJSON data:', error));

          // Fetch the GeoJSON data and add it to the map
  fetch('data/RPC/NVDA/NVDA_Zoning.geojson')
    .then(response => {
      if (!response.ok) {
        throw new Error('Network response was not ok ' + response.statusText);
      }
      return response.json();
    })
    .then(data => {
      L.geoJSON(data, {
        onEachFeature: onEachFeature
      }).addTo(map);
    })
    .catch(error => console.error('Error loading GeoJSON data:', error));

          // Fetch the GeoJSON data and add it to the map
  fetch('data/RPC/NWRPC/NWRPC_Zoning.geojson')
    .then(response => {
      if (!response.ok) {
        throw new Error('Network response was not ok ' + response.statusText);
      }
      return response.json();
    })
    .then(data => {
      L.geoJSON(data, {
        onEachFeature: onEachFeature
      }).addTo(map);
    })
    .catch(error => console.error('Error loading GeoJSON data:', error));
    
          // Fetch the GeoJSON data and add it to the map
  fetch('data/RPC/RRPC/RRPC_Zoning.geojson')
    .then(response => {
      if (!response.ok) {
        throw new Error('Network response was not ok ' + response.statusText);
      }
      return response.json();
    })
    .then(data => {
      L.geoJSON(data, {
        onEachFeature: onEachFeature
      }).addTo(map);
    })
    .catch(error => console.error('Error loading GeoJSON data:', error));
          // Fetch the GeoJSON data and add it to the map

  fetch('data/RPC/TRORC/TRORC_Zoning.geojson')
    .then(response => {
      if (!response.ok) {
        throw new Error('Network response was not ok ' + response.statusText);
      }
      return response.json();
    })
    .then(data => {
      L.geoJSON(data, {
        onEachFeature: onEachFeature
      }).addTo(map);
    })
    .catch(error => console.error('Error loading GeoJSON data:', error));

      fetch('data/RPC/WRC/WRC_Zoning.geojson')
    .then(response => {
      if (!response.ok) {
        throw new Error('Network response was not ok ' + response.statusText);
      }
      return response.json();
    })
    .then(data => {
      L.geoJSON(data, {
        onEachFeature: onEachFeature
      }).addTo(map);
    })
    .catch(error => console.error('Error loading GeoJSON data:', error));
</script>
Zoning rules can present barriers to effective city planning, impairing our ability to achieve important policy objectives like community desegregation, climate change resiliency, transportation access, homelessness relief, and affordable housing development. The Vermont Zoning Atlas seeks to democratize researchers', policymakers', advocates', and everyday citizens' understanding of zoning regulations and enable apples-to-apples cross-jurisdiction comparisons through a methodology developed by the [National Zoning Atlas](https://www.zoningatlas.org/).

The Vermont Zoning Atlas is a database and web tool that brings together zoning laws from 1,755 districts across the state of Vermont. Without this tool, one would have to read thousands of pages of dense legal code to answer simple questions. Its goal is to help answer fundamental questions facing cities and towns: for the land that we have, what can be built?

If you use this data in publications, please Cite it with this DOI: [https://doi.org/10.5281/zenodo.11508694](https://doi.org/10.5281/zenodo.11508694)

## Quicklinks

* [Learn More About the Project](https://verso-uvm.github.io/Vermont-Zoning-Atlas/about.html)
* [Explore the Structure of the Data](https://verso-uvm.github.io/Vermont-Zoning-Atlas/data.html)
* [See How to Contribute](https://verso-uvm.github.io/Vermont-Zoning-Atlas/contribute.html)
* [Resource and Analysis](https://verso-uvm.github.io/Vermont-Zoning-Atlas/resources.html)
* [MIT License](https://github.com/VERSO-UVM/Vermont-Zoning-Atlas/blob/main/LICENSE)
