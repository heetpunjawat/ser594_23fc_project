import os
import csv

def process_table_1(input_path, output_path):
    # Read the input CSV file
    with open(input_path, 'r', newline='') as input_file:
        reader = csv.reader(input_file)
        data = list(reader)

    # Extract relevant data and modify the header
    headers = ["First Harmful Event Type", "Total Crashes", "Fatal Crashes", "Injury Crashes", "PDO Crashes"]
    filtered_data = []
    total_values = [0, 0, 0, 0] 

    for row in data[2:11]:
        filtered_row = [cell.strip() for cell in row if cell.strip()]
        if filtered_row:
            filtered_data.append(filtered_row)
            numerical_values = [int(cell.replace(',', '')) for cell in filtered_row[1:]]  
            total_values = [total + value for total, value in zip(total_values, numerical_values)]  

    total_row = ["Total"] + total_values

    # Write modified data to a new CSV file inside the data_processed folder
    with open(output_path, 'w', newline='') as output_file:
        writer = csv.writer(output_file)
        writer.writerow(headers)
        writer.writerows(filtered_data)
        writer.writerow(total_row)  


def process_table_2(input_path, output_path):
    # Read the input CSV file
    with open(input_path, 'r', newline='') as input_file:
        reader = csv.reader(input_file)
        data = list(reader)

    # Extract relevant data and modify the header
    headers = ["Type of Lighting Conditions", "Total Crashes", "Fatal Crashes", "Injury Crashes", "PDO Crashes"]
    filtered_data = []
    total_values = [0, 0, 0, 0]

    for row in data[2:8]:
        filtered_row = [cell.strip() for cell in row if cell.strip()]
        if filtered_row:
            filtered_data.append(filtered_row)
            numerical_values = [int(cell.replace(',', '')) for cell in filtered_row[1:]] 
            total_values = [total + value for total, value in zip(total_values, numerical_values)]  

    total_row = ["Total"] + total_values

    # Write modified data to a new CSV file inside the data_processed folder
    with open(output_path, 'w', newline='') as output_file:
        writer = csv.writer(output_file)
        writer.writerow(headers)
        writer.writerows(filtered_data)
        writer.writerow(total_row) 


def process_table_3(input_path, output_path):
    # Read the input CSV file
    with open(input_path, 'r', newline='') as input_file:
        reader = csv.reader(input_file)
        data = list(reader)

    # Extract relevant data and modify the header
    headers = ["Type of Road Surface Condition", "Total Crashes", "Fatal Crashes", "Injury Crashes", "PDO Crashes"]
    filtered_data = []
    total_values = [0, 0, 0, 0]

    for row in data[2:8]:
        filtered_row = [cell.strip() for cell in row if cell.strip()]
        if filtered_row:
            filtered_data.append(filtered_row)
            numerical_values = [int(cell.replace(',', '')) for cell in filtered_row[1:]] 
            total_values = [total + value for total, value in zip(total_values, numerical_values)]  

    total_row = ["Total"] + total_values

    # Write modified data to a new CSV file inside the data_processed folder
    with open(output_path, 'w', newline='') as output_file:
        writer = csv.writer(output_file)
        writer.writerow(headers)
        writer.writerows(filtered_data)
        writer.writerow(total_row)  


def process_table_4(input_path, output_path):
    # Read the input CSV file
    with open(input_path, 'r', newline='') as input_file:
        reader = csv.reader(input_file)
        data = list(reader)

    # Extract relevant data and modify the header
    headers = ["Category of Crash", "Total", "Urban Location", "% of Total", "Rural Location", "% of Total"]
    filtered_data = []
    total_values = [0, 0, 0, 0]

    for row in data[1:]:
        filtered_row = [cell.strip() for cell in row if cell.strip()]
        if filtered_row:
            filtered_data.append(filtered_row)
            numerical_values = [float(cell.replace(',', '').replace('%', '')) for cell in filtered_row[1:]] 
            total_values = [total + value for total, value in zip(total_values, numerical_values)] 

    # Write modified data to a new CSV file inside the data_processed folder
    with open(output_path, 'w', newline='') as output_file:
        writer = csv.writer(output_file)
        writer.writerow(headers)
        writer.writerows(filtered_data)


def process_table_5(input_path, output_path):
# Read the input CSV file
    with open(input_path, 'r', newline='') as input_file:
        reader = csv.reader(input_file)
        data = list(reader)

    # Extract relevant data and modify the header
    headers = ["Operator Age Group", "Total Crashes", "% of Total Crashes", "In Fatal Crashes", "% of Fatal Crashes", "In Injury Crashes", "% of Injury Crashes", "In PDO Crashes", "% of PDO Crashes"]
    filtered_data = []
    total_values = [0, 0, 0, 0]

    for row in data[2:]:
        filtered_row = [cell.strip() for cell in row if cell.strip()]
        if filtered_row:
            filtered_data.append(filtered_row)
            numerical_values = [float(cell.replace(',', '').replace('%', '')) for cell in filtered_row[1:]] 
            total_values = [total + value for total, value in zip(total_values, numerical_values)]  

    # Write modified data to a new CSV file inside the data_processing folder
    with open(output_path, 'w', newline='') as output_file:
        writer = csv.writer(output_file)
        writer.writerow(headers)
        writer.writerows(filtered_data)


def process_table_6(input_path, output_path):
# Read the input CSV file
    with open(input_path, 'r', newline='') as input_file:
        reader = csv.reader(input_file)
        data = list(reader)

    # Extract relevant data and modify the header
    headers = ["Operator Condition", "Total Crashes", "% of Total Crashes", "In Fatal Crashes", "% of Fatal Crashes", "In Injury Crashes", "% of Injury Crashes", "In PDO Crashes", "% of PDO Crashes"]
    filtered_data = []
    total_values = [0, 0, 0, 0]

    for row in data[2:]:
        filtered_row = [cell.strip() for cell in row if cell.strip()]
        if filtered_row:
            filtered_data.append(filtered_row)
            numerical_values = [float(cell.replace(',', '').replace('%', '')) for cell in filtered_row[1:]] 
            total_values = [total + value for total, value in zip(total_values, numerical_values)]  

    # Write modified data to a new CSV file inside the data_processing folder
    with open(output_path, 'w', newline='') as output_file:
        writer = csv.writer(output_file)
        writer.writerow(headers)
        writer.writerows(filtered_data)


def process_table_7(input_path, output_path):
    # Read the input CSV file
    with open(input_path, 'r', newline='') as input_file:
        reader = csv.reader(input_file)
        data = list(reader)

    # Extract relevant data and modify the header
    headers = ["Operator's Severity of Injury", "Helmet Used", "% of Total", "Helmet Not Used", "% of Total", "Unknown", "% of Total", "Total", "% of Total"]
    filtered_data = []
    total_values = [0, 0, 0, 0]

    for row in data[1:]:
        filtered_row = [cell.strip() for cell in row if cell.strip()]
        if filtered_row:
            filtered_data.append(filtered_row)
            numerical_values = [float(cell.replace(',', '').replace('%', '')) for cell in filtered_row[1:]] 
            total_values = [total + value for total, value in zip(total_values, numerical_values)] 

    # Write modified data to a new CSV file inside the data_processed folder
    with open(output_path, 'w', newline='') as output_file:
        writer = csv.writer(output_file)
        writer.writerow(headers)
        writer.writerows(filtered_data)


def process_table_8(input_path, output_path):
    # Read the input CSV file
    with open(input_path, 'r', newline='') as input_file:
        reader = csv.reader(input_file)
        data = list(reader)

    # Extract relevant data and modify the header
    headers = ["Passenger's Severity of Injury", "Helmet Used", "% of Total", "Helmet Not Used", "% of Total", "Unknown", "% of Total", "Total", "% of Total"]
    filtered_data = []
    total_values = [0, 0, 0, 0]

    for row in data[1:]:
        filtered_row = [cell.strip() for cell in row if cell.strip()]
        if filtered_row:
            filtered_data.append(filtered_row)
            numerical_values = [float(cell.replace(',', '').replace('%', '')) for cell in filtered_row[1:]] 
            total_values = [total + value for total, value in zip(total_values, numerical_values)] 

    # Write modified data to a new CSV file inside the data_processed folder
    with open(output_path, 'w', newline='') as output_file:
        writer = csv.writer(output_file)
        writer.writerow(headers)
        writer.writerows(filtered_data)


def process_table_9(input_path, output_path):
# Read the input CSV file
    with open(input_path, 'r', newline='') as input_file:
        reader = csv.reader(input_file)
        data = list(reader)

    # Extract relevant data and modify the header
    headers = ["Gender", "Helmet Used", "% of Helmet Used", "Helmet Not Used", "% of Helmet Not Used", "Unknown", "% of Unknown", "Total", "% of Total"]
    filtered_data = []
    total_values = [0, 0, 0, 0]

    for row in data[2:]:
        filtered_row = [cell.strip() for cell in row if cell.strip()]
        if filtered_row:
            filtered_data.append(filtered_row)
            numerical_values = [float(cell.replace(',', '').replace('%', '')) for cell in filtered_row[1:]] 
            total_values = [total + value for total, value in zip(total_values, numerical_values)]  

    # Write modified data to a new CSV file inside the data_processing folder
    with open(output_path, 'w', newline='') as output_file:
        writer = csv.writer(output_file)
        writer.writerow(headers)
        writer.writerows(filtered_data)


def process_table_10(input_path, output_path):
# Read the input CSV file
    with open(input_path, 'r', newline='') as input_file:
        reader = csv.reader(input_file)
        data = list(reader)

    # Extract relevant data and modify the header
    headers = ["Age of Victim", "Total Persons Killed", "Total Males Killed", "Total Females Killed", "Total Persons Injured", "Total Males Injured", "Total Females Injured", "Uknown Gender Injured"]
    filtered_data = []
    total_values = [0, 0, 0, 0]

    for row in data[2:]:
        filtered_row = [cell.strip() for cell in row if cell.strip()]
        if filtered_row:
            filtered_data.append(filtered_row)
            numerical_values = [float(cell.replace(',', '').replace('%', '')) for cell in filtered_row[1:]] 
            total_values = [total + value for total, value in zip(total_values, numerical_values)]  

    # Write modified data to a new CSV file inside the data_processing folder
    with open(output_path, 'w', newline='') as output_file:
        writer = csv.writer(output_file)
        writer.writerow(headers)
        writer.writerows(filtered_data)


def process_table_11(input_path, output_path):
# Read the input CSV file
    with open(input_path, 'r', newline='') as input_file:
        reader = csv.reader(input_file)
        data = list(reader)

    # Extract relevant data and modify the header
    headers = ["Type of Violation", "Total Crashes", "% of Total Crashes", "In Fatal Crashes", "% of Fatal Crashes", "In Injury Crashes", "% of Injury Crashes", "In PDO Crashes", "% of PDO Crashes"]
    filtered_data = []
    total_values = [0, 0, 0, 0]

    for row in data[2:]:
        filtered_row = [cell.strip() for cell in row if cell.strip()]
        if filtered_row:
            filtered_data.append(filtered_row)
            numerical_values = [float(cell.replace(',', '').replace('%', '')) for cell in filtered_row[1:]] 
            total_values = [total + value for total, value in zip(total_values, numerical_values)]  

    # Write modified data to a new CSV file inside the data_processing folder
    with open(output_path, 'w', newline='') as output_file:
        writer = csv.writer(output_file)
        writer.writerow(headers)
        writer.writerows(filtered_data)


def process_table_12(input_path, output_path):
# Read the input CSV file
    with open(input_path, 'r', newline='') as input_file:
        reader = csv.reader(input_file)
        data = list(reader)

    # Extract relevant data and modify the header
    headers = ["Time", "All Crashes", "Fatal Crashes", "Monday-All Crashes", "Monday-Fatal Crashes", "Tuesday-All Crashes", "Tuesday-Fatal Crashes", "Wednesday-All Crashes", "Wednesday-Fatal Crashes", "Thursday-All Crashes", "Thursday-Fatal Crashes", "Friday-All Crashes", "Friday-Fatal Crashes", "Saturday-All Crashes", "Saturday-Fatal Crashes", "Sunday-All Crashes", "Sunday-Fatal Crashes", "Weekdays-All Crashes", "Weekdays-Fatal Crashes", "Weekends-All Crashes", "Weekends-Fatal Crashes"]
    filtered_data = []
    total_values = [0, 0, 0, 0]

    for row in data[2:]:
        filtered_row = [cell.strip() for cell in row if cell.strip()]
        if filtered_row:
            filtered_data.append(filtered_row)
            numerical_values = [float(cell.replace(',', '').replace('%', '')) for cell in filtered_row[1:]] 
            total_values = [total + value for total, value in zip(total_values, numerical_values)]  

    # Write modified data to a new CSV file inside the data_processing folder
    with open(output_path, 'w', newline='') as output_file:
        writer = csv.writer(output_file)
        writer.writerow(headers)
        writer.writerows(filtered_data)


def process_table_13(input_path, output_path):
# Read the input CSV file
    with open(input_path, 'r', newline='') as input_file:
        reader = csv.reader(input_file)
        data = list(reader)

    # Extract relevant data and modify the header
    headers = ["County", "Total Crashes", "Fatal Crashes", "Injury Crashes", "PDO Crashes", "Persons Killed", "Persons Injured"]
    filtered_data = []
    total_values = [0, 0, 0, 0]

    for row in data[2:]:
        filtered_row = [cell.strip() for cell in row if cell.strip()]
        if filtered_row:
            filtered_data.append(filtered_row)
            numerical_values = [float(cell.replace(',', '').replace('%', '')) for cell in filtered_row[1:]] 
            total_values = [total + value for total, value in zip(total_values, numerical_values)]  

    # Write modified data to a new CSV file inside the data_processing folder
    with open(output_path, 'w', newline='') as output_file:
        writer = csv.writer(output_file)
        writer.writerow(headers)
        writer.writerows(filtered_data)


def process_table_14(input_path, output_path):
# Read the input CSV file
    with open(input_path, 'r', newline='') as input_file:
        reader = csv.reader(input_file)
        data = list(reader)

    # Extract relevant data and modify the header
    headers = ["Manner of Collision", "Total Crashes", "% of Total Crashes", "Fatal Crashes", "% of Fatal Crashes", "Injury Crashes", "% of Injury Crashes", "In PDO Crashes", "% of PDO Crashes"]
    filtered_data = []
    total_values = [0, 0, 0, 0]

    for row in data[2:]:
        filtered_row = [cell.strip() for cell in row if cell.strip()]
        if filtered_row:
            filtered_data.append(filtered_row)
            numerical_values = [float(cell.replace(',', '').replace('%', '')) for cell in filtered_row[1:]] 
            total_values = [total + value for total, value in zip(total_values, numerical_values)]  

    # Write modified data to a new CSV file inside the data_processing folder
    with open(output_path, 'w', newline='') as output_file:
        writer = csv.writer(output_file)
        writer.writerow(headers)
        writer.writerows(filtered_data)


if __name__ == '__main__':

    # Create a new directory "data_processed" to store the processed csv files if it doesnot exist 
    os.makedirs(os.path.join(os.getcwd(), 'data_processed'), exist_ok=True)

    input_csv1_path = os.path.join(os.getcwd(), 'data_original/table1.csv')
    output_csv1_path = os.path.join(os.getcwd(), 'data_processed/table1_processed.csv')
    process_table_1(input_csv1_path, output_csv1_path)

    input_csv2_path = os.path.join(os.getcwd(), 'data_original/table2.csv')
    output_csv2_path = os.path.join(os.getcwd(), 'data_processed/table2_processed.csv')
    process_table_2(input_csv2_path, output_csv2_path)

    input_csv3_path = os.path.join(os.getcwd(), 'data_original/table3.csv')
    output_csv3_path = os.path.join(os.getcwd(), 'data_processed/table3_processed.csv')
    process_table_3(input_csv3_path, output_csv3_path)

    input_csv4_path = os.path.join(os.getcwd(), 'data_original/table4.csv')
    output_csv4_path = os.path.join(os.getcwd(), 'data_processed/table4_processed.csv')
    process_table_4(input_csv4_path, output_csv4_path)

    input_csv5_path = os.path.join(os.getcwd(), 'data_original/table5.csv')
    output_csv5_path = os.path.join(os.getcwd(), 'data_processed/table5_processed.csv')
    process_table_5(input_csv5_path, output_csv5_path)    

    input_csv6_path = os.path.join(os.getcwd(), 'data_original/table6.csv')
    output_csv6_path = os.path.join(os.getcwd(), 'data_processed/table6_processed.csv')
    process_table_6(input_csv6_path, output_csv6_path)

    input_csv7_path = os.path.join(os.getcwd(), 'data_original/table7operator.csv')
    output_csv7_path = os.path.join(os.getcwd(), 'data_processed/table7operator_processed.csv')
    process_table_7(input_csv7_path, output_csv7_path)

    input_csv8_path = os.path.join(os.getcwd(), 'data_original/table8passenger.csv')
    output_csv8_path = os.path.join(os.getcwd(), 'data_processed/table8passenger_processed.csv')
    process_table_8(input_csv8_path, output_csv8_path)

    input_csv9_path = os.path.join(os.getcwd(), 'data_original/table9.csv')
    output_csv9_path = os.path.join(os.getcwd(), 'data_processed/table9_processed.csv')
    process_table_9(input_csv9_path, output_csv9_path)

    input_csv10_path = os.path.join(os.getcwd(), 'data_original/table10operators&passengers.csv')
    output_csv10_path = os.path.join(os.getcwd(), 'data_processed/table10operators&passengers_processed.csv')
    process_table_10(input_csv10_path, output_csv10_path)

    input_csv11_path = os.path.join(os.getcwd(), 'data_original/table11.csv')
    output_csv11_path = os.path.join(os.getcwd(), 'data_processed/table11_processed.csv')
    process_table_11(input_csv11_path, output_csv11_path)

    input_csv12_path = os.path.join(os.getcwd(), 'data_original/table12.csv')
    output_csv12_path = os.path.join(os.getcwd(), 'data_processed/table12_processed.csv')
    process_table_12(input_csv12_path, output_csv12_path)

    input_csv13_path = os.path.join(os.getcwd(), 'data_original/table13.csv')
    output_csv13_path = os.path.join(os.getcwd(), 'data_processed/table13_processed.csv')
    process_table_13(input_csv13_path, output_csv13_path)

    input_csv14_path = os.path.join(os.getcwd(), 'data_original/table14.csv')
    output_csv14_path = os.path.join(os.getcwd(), 'data_processed/table14_processed.csv')
    process_table_14(input_csv14_path, output_csv14_path)

