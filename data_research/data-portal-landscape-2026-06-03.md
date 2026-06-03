# 🗺️ Australian Data Portal Landscape Analysis

**Date:** 2026-06-03  
**Focus:** NSW & VIC Data Sources  
**Scope:** 18 major Australian data portals

## 🎯 Critical Sources for NSW/VIC Products

### CRITICAL (Must integrate)
1. **NSW Open Data** — data.nsw.gov.au — Government data +  APIs
2. **DataVic** — data.vic.gov.au — Victoria government data + APIs
3. **data.gov.au** — National portal with NSW/VIC breakdowns

### HIGH (Should integrate)
- **ABS** — Census, economic, population data (state level)
- **BOM** — Real-time weather, climate data (NSW/VIC coverage)
- **CSIRO** — Environmental, climate, agricultural data
- **GeoscienceAU** — Geological, hazard, geospatial data
- **AODN** — Real-time coastal/marine data (NSW/VIC coast)
- **ALA** — Biodiversity, species occurrence data

## 📊 CKAN Portal Status (Government Data)

| Portal | Status | Datasets | Sample Categories | Sample Formats |
|--------|--------|----------|-------------------|----------------|

## 🏢 Specialized Data Agencies

### ABS
Australian Bureau of Statistics - Census, economic indicators

- **API:** REST API available
- **NSW/VIC Focus:** State-level breakdowns available for most datasets
- **Product Utility:** ⭐⭐⭐⭐⭐ - High-quality, regularly updated official statistics

### BOM
Bureau of Meteorology - Weather, climate data

- **API:** Public data available
- **NSW/VIC Focus:** Complete coverage - NSW/VIC weather stations + forecasts
- **Product Utility:** ⭐⭐⭐⭐⭐ - Real-time, API-accessible, live updates

### CSIRO
Scientific data from Australia's research agency

- **API:** varies by dataset
- **NSW/VIC Focus:** Regional climate data available
- **Product Utility:** ⭐⭐⭐⭐ - High-quality research, may require licensing

### GeoscienceAU
Geological surveys, natural hazards, geospatial

- **API:** Web services available
- **NSW/VIC Focus:** Comprehensive nationwide coverage
- **Product Utility:** ⭐⭐⭐⭐ - Good for location-based services

### AIHW
Health and welfare statistics

- **API:** Data downloads available
- **NSW/VIC Focus:** State-level health data available
- **Product Utility:** ⭐⭐⭐ - Good for healthcare products, may be aggregated

### ALA
Atlas of Living Australia - Biodiversity observations

- **API:** REST API available
- **NSW/VIC Focus:** Complete occurrence data for both states
- **Product Utility:** ⭐⭐⭐⭐ - Great for location-based nature/ecology products

### AODN
Australian Ocean Data Network - Coastal/marine

- **API:** Thematic Mapping Service available
- **NSW/VIC Focus:** Coastal NSW/VIC data including Victoria coast
- **Product Utility:** ⭐⭐⭐⭐⭐ - Real-time marine data, perfect for apps

### NationalMap
Interactive geospatial platform with government datasets

- **API:** Web-based/GIS API
- **NSW/VIC Focus:** Complete geospatial coverage
- **Product Utility:** ⭐⭐⭐⭐ - Visual data discovery, good for map products

### RDA
Research Data Australia - National research data aggregator

- **API:** OAI-PMH, REST API
- **NSW/VIC Focus:** Contains NSW/VIC research from universities
- **Product Utility:** ⭐⭐⭐ - Useful for research collaboration, hit-or-miss

## 💡 Product Categories & Best Sources

### Real-time/API-driven
**Sources:** BOM, AODN, ABS, ALA, data.gov.au

### Geospatial
**Sources:** GeoscienceAU, NationalMap, AODN, CSIRO, ALA

### Health/Welfare
**Sources:** AIHW, ABS

### Environmental
**Sources:** CSIRO, AODN, ALA, BOM, TERN, GeoscienceAU

### Economic/Social
**Sources:** ABS, data.gov.au

### Scientific
**Sources:** CSIRO, RDA, ALA, TERN

## 🚀 Next Steps for Discovery

1. **Deep dive into NSW/VIC CKAN APIs** — Extract top datasets by category
2. **Test real-time data access** — BOM, AODN, ALA APIs
3. **Map data schemas** — Understanding structure for each critical source
4. **Identify data gaps** — What's missing that users would want?
5. **Prototype data pipeline** — Build ETL for top 5 sources
