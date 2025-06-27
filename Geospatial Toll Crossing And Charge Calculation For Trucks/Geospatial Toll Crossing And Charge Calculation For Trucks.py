import pandas as pd
import folium
from geopy.distance import great_circle

# Load datasets
vts_df = pd.read_csv(r'C:\Users\Vinotha R\Downloads\copyyyy.csv')  # Update with your file path
report_df = pd.read_csv(r'C:\Users\Vinotha R\Downloads\report_truck_bus_output_output.csv')  # Update with your file path

# Function to calculate distance between two points
def calculate_distance(coord1, coord2):
    return great_circle(coord1, coord2).kilometers

# Create a base Folium map centered around the first location in vts_df
start_location = (vts_df.iloc[0]['latitude'], vts_df.iloc[0]['longitude'])
m = folium.Map(location=start_location, zoom_start=10)

# Add toll plaza locations to the map
for idx, report_row in report_df.iterrows():
    toll_coordinates = (report_row['Latitude'], report_row['Longitude'])
    toll_plaza_name = report_row['Toll Plaza Name']
    folium.Marker(toll_coordinates, popup=toll_plaza_name, icon=folium.Icon(color='red')).add_to(m)

# Initialize total trip cost and a set to keep track of crossed toll plazas
total_trip_cost = 0
crossed_plazas = set()
crossed_plaza_costs = {}

# Track the route and detect toll plaza crossings
for index, vts_row in vts_df.iterrows():
    try:
        vts_coordinates = (vts_row['latitude'], vts_row['longitude'])
        vehicle_id = vts_row['vehicle_number']
        company_name = vts_row.get('name', 'Unknown')  # Use 'Unknown' if 'name' is missing
        trip_id = vts_row['trip_id']  # Assuming trip_id is a column in vts_df
        
        # Add the truck's location to the map
        folium.CircleMarker(location=vts_coordinates, radius=3, color='blue').add_to(m)

        # Check if the truck has crossed any toll plaza
        for idx, report_row in report_df.iterrows():
            toll_coordinates = (report_row['Latitude'], report_row['Longitude'])
            toll_plaza_name = report_row['Toll Plaza Name']
            toll_cost = report_row['Single Journey']  # Adjust column name if different

            distance = calculate_distance(vts_coordinates, toll_coordinates)
            
            # Assuming a crossing is detected if distance is less than 1 km
            if distance < 1.0 and toll_plaza_name not in crossed_plazas:  # Adjust this threshold based on your actual data and requirements
                print(f"Vehicle {vehicle_id} has crossed Toll Plaza {toll_plaza_name}")
                folium.Marker(toll_coordinates, popup=f"{toll_plaza_name} (Crossed)", icon=folium.Icon(color='green')).add_to(m)
                
                # Add the toll cost to the total trip cost
                total_trip_cost += toll_cost
                
                # Add the toll plaza to the set of crossed plazas
                crossed_plazas.add(toll_plaza_name)
                crossed_plaza_costs[toll_plaza_name] = toll_cost
    
    except KeyError as e:
        print(f"KeyError: {e} occurred. Check if column names are correct or if the data is missing.")
    except Exception as e:
        print(f"Exception occurred: {e}")

# Create a DataFrame to store the results
trip_data = {
    'Trip ID': [trip_id],
    'Vehicle Number': [vehicle_id],
    'Company Name': [company_name],
    'No. of Tolls Crossed': [len(crossed_plazas)],
    'Cost of Each Toll Plaza': [crossed_plaza_costs],
    'Total Cost': [total_trip_cost]
}

trip_df = pd.DataFrame(trip_data)

# Specify the full path where you want to save the CSV file
csv_file_path = r'C:\Users\Vinotha R\Downloads\trip_summary1.csv'  # Update with your desired path and filename

# Save the DataFrame to a CSV file
trip_df.to_csv(csv_file_path, index=False)

# Print the total trip cost
print(f"Total Trip Cost: {total_trip_cost}")

# Save the map to an HTML file
m.save('toll_plaza_map.html')



