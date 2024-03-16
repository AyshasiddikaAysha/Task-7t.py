import datetime

def create_timestamp_file():
    # Get the current timestamp
    current_time = datetime.datetime.now()
    
    # Format the timestamp as a string
    timestamp_str = current_time.strftime("%Y-%m-%d %H:%M:%S")
    
    # Create a file with the timestamp as the filename
    file_name = f"{timestamp_str}.txt"
    
    # Write the timestamp to the file
    with open(file_name, 'w') as file:
        file.write(timestamp_str)
    
    print(f"File '{file_name}' created with the timestamp: {timestamp_str}")

# Call the function to create the timestamp file
create_timestamp_file()

QUS -02.py
def read_text_file(file_name):
    try:
        with open(file_name, 'r') as file:
            content = file.read()
            print(f"Content of '{file_name}':\n{content}")
    except FileNotFoundError:
        print(f"File '{file_name}' not found.")
    except Exception as e:
        print(f"An error occurred while reading '{file_name}': {str(e)}")

file_name = "2023-10-11 13:45:00.txt" 
read_text_file(file_name)
