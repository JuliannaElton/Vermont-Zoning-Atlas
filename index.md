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
  fetch('data/vt-zoning-expanded-ACRPC.geojson')
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
  fetch('data/vt-zoning-expanded-BCRC.geojson')
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
  fetch('data/vt-zoning-expanded-CCRPC.geojson')
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
  fetch('data/vt-zoning-expanded-CVRPC.geojson')
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
  fetch('data/vt-zoning-expanded-LCPC.geojson')
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
  fetch('data/vt-zoning-expanded-MARC.geojson')
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
  fetch('data/vt-zoning-expanded-NVDA.geojson')
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
  fetch('data/vt-zoning-expanded-NWRPC.geojson')
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
  fetch('data/vt-zoning-expanded-NWRPC.geojson')
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
  fetch('data/vt-zoning-expanded-RRPC.geojson')
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

  fetch('data/vt-zoning-expanded-TRORC.geojson')
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

      fetch('data/vt-zoning-expanded-WRC.geojson')
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




The Vermont Zoning Atlas is a database and web tool that brings together zoning laws from 1,755 districts across the state of Vermont. Its goal is to help answer fundamental questions facing cities and towns: for the land that we have, what can be built?

Zoning laws regulate the types of housing that can be built. But for ordinary people, they can be complex, overwhelming, and hard to find. The Vermont Zoning Atlas takes inspiration from the National Zoning Atlas project to "digitize, demystify, and democratize information" that is often hidden under many layers of hard to parse paperwork.

As a rural state, Vermont's zoning laws can be especially difficult to find and understand. Many towns use their own methods of record keeping and governance. But we believe that universal access to this information is critical for smart community growth.

Without this tool, one would have to read thousands of pages of dense legal code to answer simple questions - this is why we believe our tool will democratize zoning policy and make it possible for advocates and researchers to identify barriers to things like affordable housing development, climate resiliency, and community desegregation more quickly.