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

The [Vermont Zoning Atlas](https://www.zoningatlas.org/vermont) is a web-based geospatial interface that visualizes zoning code distributions across all of Vermont. Zoning rules can present barriers to effective city planning, impairing our ability to achieve important policy objectives like community desegregation, climate change resiliency, transportation access, homelessness relief, and affordable housing development. The Vermont Zoning Atlas seeks to democratize researchers', policymakers', advocates', and everyday citizens' understanding of zoning regulations and enable apples-to-apples cross-jurisdiction comparisons through a methodology developed by our partner, the [National Zoning Atlas](https://www.zoningatlas.org/).




<div id="map" style="height: 500px;"></div>

<script>
  // Initialize the map
  var map = L.map('map').setView([43.951, -72.756], 7);

  // Add a tile layer to the map
  L.tileLayer('https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png', {
    attribution: '&copy; <a href="https://www.openstreetmap.org/copyright">OpenStreetMap</a> contributors'
  }).addTo(map);

  
  // Function to bind popups to each feature
  function onEachFeature(feature, layer) {
    if (feature.properties) {
      var popupContent = "<p><strong>Attributes:</strong></p>";
      for (var key in feature.properties) {
        popupContent += "<p>" + key + ": " + feature.properties[key] + "</p>";
      }
      layer.bindPopup(popupContent);
    }
  }

  // Fetch the GeoJSON data and add it to the map

  fetch('/data/vt-zoning-expanded-vermont.geojson')
    .then(response => response.json())
    .then(data => {
      L.geoJSON(data, {
        onEachFeature: onEachFeature
      }).addTo(map);
    })
    .catch(error => console.error('Error loading GeoJSON data:', error));
</script>




The Vermont Zoning Atlas is a database and web tool that brings together zoning laws from 1,755 districts across the state of Vermont. Its goal is to help answer fundamental questions facing cities and towns: for the land that we have, what can be built?

Zoning laws regulate the types of housing that can be built. But for ordinary people, they can be complex, overwhelming, and hard to find. The Vermont Zoning Atlas takes inspiration from the National Zoning Atlas project to "digitize, demystify, and democratize information" that is often hidden under many layers of hard to parse paperwork.

As a rural state, Vermont's zoning laws can be especially difficult to find and understand. Many towns use their own methods of record keeping and governance. But we believe that universal access to this information is critical for smart community growth.

Without this tool, one would have to read thousands of pages of dense legal code to answer simple questions - this is why we believe our tool will democratize zoning policy and make it possible for advocates and researchers to identify barriers to things like affordable housing development, climate resiliency, and community desegregation more quickly.