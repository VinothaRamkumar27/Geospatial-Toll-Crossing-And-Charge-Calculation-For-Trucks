# Geospatial-Toll-Crossing-And-Charge-Calculation-For-Trucks
# 🚛 Toll Plaza Crossing Detection and Cost Estimation

This project uses Python to analyze vehicle GPS data and detect toll plaza crossings using geospatial comparison. It visualizes toll locations and vehicle paths using Folium and calculates the total trip cost based on toll rates.

## 📂 Project Overview

The script performs the following tasks:

1. **Loads vehicle tracking data (`copyyyy.csv`)** and **toll plaza report data (`report_truck_bus_output_output.csv`)**.
2. **Calculates distances** between vehicle GPS coordinates and toll plaza coordinates using the `geopy` library.
3. **Identifies toll crossings** when a vehicle is within a 1 km radius of a toll location.
4. **Logs and sums up toll costs** for each trip.
5. **Plots toll plazas and vehicle paths** on a Folium map.
6. **Exports a trip summary CSV** with trip ID, vehicle number, total tolls crossed, and total cost.
7. **Saves the interactive map** as `toll_plaza_map.html`.

## 📌 Dependencies

Make sure to install the following Python libraries:

```bash
pip install pandas folium geopy
```
## 📁 Input Files

- `copyyyy.csv`  
  Contains VTS (Vehicle Tracking System) data with fields like:
  - `latitude`
  - `longitude`
  - `vehicle_number`
  - `trip_id`
  - `name` (optional)

- `report_truck_bus_output_output.csv`  
  Contains toll plaza data with:
  - `Latitude`
  - `Longitude`
  - `Toll Plaza Name`
  - `Single Journey` (toll cost)

---

## 🧠 Key Features

- Accurate toll plaza crossing detection using **geopy's great-circle distance**
- Dynamic toll cost calculation
- **Interactive Folium map**:
  - Red markers for all toll plazas
  - Green markers for tolls that were crossed
  - Blue circles for vehicle path points
- Outputs summary with:
  - Trip ID
  - Vehicle Number
  - Company Name
  - Number of Toll Plazas Crossed
  - Individual Toll Costs
  - Total Toll Cost

---

## 📤 Output Files

- `trip_summary1.csv` – CSV file summarizing the toll data for the trip
- `toll_plaza_map.html` – Interactive map showing route and toll locations

---

## 📌 Example Output (Console)
Vehicle TN01AB1234 has crossed Toll Plaza XYZ Toll
Total Trip Cost: ₹320.0

---

## 🛠 How to Use

1. Update the file paths in the script to your local system:

   ```python
   vts_df = pd.read_csv(r'C:\path\to\copyyyy.csv')
   report_df = pd.read_csv(r'C:\path\to\report_truck_bus_output_output.csv')

2. Run the script in a Python environment.

3. Review the outputs:

Console will show tolls crossed.

Check trip_summary1.csv for cost summary.

Open toll_plaza_map.html in a browser for visualization.

📍 Notes
You can modify the crossing detection threshold (default is 1.0 km) in this condition:

if distance < 1.0
to adjust the sensitivity of toll detection.

---

## Sample Outputs:


![Alt Text](https://github.com/VinothaRamkumar27/Geospatial-Toll-Crossing-And-Charge-Calculation-For-Trucks/blob/0f88a01781ff39f0e72afed2c8066f5c6978a797/Geospatial%20Toll%20Crossing%20And%20Charge%20Calculation%20For%20Trucks/Sample%20Outputs/Sample%20Trip.png)

![Alt Text](https://github.com/VinothaRamkumar27/Geospatial-Toll-Crossing-And-Charge-Calculation-For-Trucks/blob/0f88a01781ff39f0e72afed2c8066f5c6978a797/Geospatial%20Toll%20Crossing%20And%20Charge%20Calculation%20For%20Trucks/Sample%20Outputs/Visualization%20of%20Toll%20plaza%20locations%20in%20Tamilnadu.png)

---






