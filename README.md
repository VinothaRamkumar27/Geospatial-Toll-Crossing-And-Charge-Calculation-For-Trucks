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
'''
📁 File Inputs
copyyyy.csv — VTS (vehicle tracking system) data with columns like latitude, longitude, vehicle_number, trip_id, etc.

report_truck_bus_output_output.csv — Toll plaza data with columns like Latitude, Longitude, Toll Plaza Name, and Single Journey toll cost.

---

📁 File Inputs
copyyyy.csv — VTS (vehicle tracking system) data with columns like latitude, longitude, vehicle_number, trip_id, etc.

report_truck_bus_output_output.csv — Toll plaza data with columns like Latitude, Longitude, Toll Plaza Name, and Single Journey toll cost.

🧠 Key Features
Accurate distance-based toll plaza crossing detection using geopy.distance.great_circle

Real-time toll cost calculation per vehicle

Interactive Folium map showing:

Red markers for toll plazas

Green markers for tolls that have been crossed

Blue path representing the vehicle route

Output CSV summary including:

Trip ID

Vehicle number

Company name

Number of tolls crossed

Toll cost breakdown

Total toll cost

---

📤 Outputs
trip_summary1.csv — A CSV summary with toll cost and crossing details.

toll_plaza_map.html — An interactive map visualization.

---

📌 Example Output
yaml
Copy
Edit
Vehicle TN01AB1234 has crossed Toll Plaza XYZ Toll
Total Trip Cost: ₹320.0

---

🛠 How to Use
Update the file paths in the script to match your local system:

copyyyy.csv

report_truck_bus_output_output.csv

Run the script in a Python environment.

View:

Console outputs for toll crossings.

trip_summary1.csv for cost summary.

toll_plaza_map.html in your browser for route and toll visualization.

---

## Sample Outputs

![Alt Text](https://github.com/VinothaRamkumar27/Geospatial-Toll-Crossing-And-Charge-Calculation-For-Trucks/blob/0f88a01781ff39f0e72afed2c8066f5c6978a797/Geospatial%20Toll%20Crossing%20And%20Charge%20Calculation%20For%20Trucks/Sample%20Outputs/Sample%20Trip.png)

![Alt Text](https://github.com/VinothaRamkumar27/Geospatial-Toll-Crossing-And-Charge-Calculation-For-Trucks/blob/0f88a01781ff39f0e72afed2c8066f5c6978a797/Geospatial%20Toll%20Crossing%20And%20Charge%20Calculation%20For%20Trucks/Sample%20Outputs/Visualization%20of%20Toll%20plaza%20locations%20in%20Tamilnadu.png)

---
