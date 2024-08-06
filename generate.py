import os
from datetime import datetime, timedelta
import nepali_datetime

# 1. Create the main folder
folder_name = "convertToBS"
if not os.path.exists(folder_name):
    os.makedirs(folder_name)

# Function to convert AD to BS
def convert_ad_to_bs(ad_date):
    ad_datetime = datetime.strptime(ad_date, "%Y-%m-%d")
    ad_date_only = ad_datetime.date()  # Convert to datetime.date object
    bs_datetime = nepali_datetime.date.from_datetime_date(ad_date_only)
    return bs_datetime

# 2. Generate files for each day and convert AD to BS
start_date = datetime(1943, 4, 14)
end_date = datetime(2043, 4, 14)
current_date = start_date

while current_date <= end_date:
    ad_date_str = current_date.strftime("%Y-%m-%d")
    bs_date = convert_ad_to_bs(ad_date_str)
    bs_date_str = bs_date.strftime("%Y-%m-%d")
    
    # Create a file for each day
    file_name = f"{ad_date_str}"
    file_path = os.path.join(folder_name, file_name)
    
    with open(file_path, 'w') as file:
        # file.write(f"AD Date: {ad_date_str}\n")
        file.write(f"{bs_date_str}\n")
    
    current_date += timedelta(days=1)

print("Folder structure and files created successfully.")
