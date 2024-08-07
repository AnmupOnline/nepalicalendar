import os
from datetime import datetime, timedelta
import nepali_datetime

# 1. Create the main folder
folder_name_1 = "convertToBS"
if not os.path.exists(folder_name_1):
    os.makedirs(folder_name_1)

# 1. Create the main folder
folder_name_2 = "convertToAD"
if not os.path.exists(folder_name_2):
    os.makedirs(folder_name_2)

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
    file_path_1 = os.path.join(folder_name_1, ad_date_str)
    file_path_2 = os.path.join(folder_name_2, bs_date_str)
    
    with open(file_path_1, 'w') as file:
        file.write(f"{bs_date_str}")

    with open(file_path_2, 'w') as file:
        file.write(f"{ad_date_str}")
    
    current_date += timedelta(days=1)

print("Folder structure and files created successfully.")
