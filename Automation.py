import os
directory = "C:/Users/91938/OneDrive/Desktop/Task Automation" # Replace with your folder directory
new_name = "document"
files = os.listdir(directory)
for i,file in enumerate(files):
    file_extension = os.path.splitext(file)[1]
    new_file_name = f'{new_name}_{i+1}{file_extension}'
    old_file_path = os.path.join(directory,file)
    new_file_path = os.path.join(directory,new_file_name)
    os.rename(old_file_path,new_file_path)
    print(f"Renamed '{file}' to '{new_file_name}'")
print("All files have been renamed successfully!")
