import subprocess

# Start script1.py and script2.py as separate processes
process1 = subprocess.Popen(["python", "D:/MyStuffs/Code/azure/azure_service_bus/queue/azure_service_bus_consumer_1.py"])
process2 = subprocess.Popen(["python", "D:/MyStuffs/Code/azure/azure_service_bus/queue/azure_service_bus_consumer_2.py"])

# Wait for both processes to finish
process1.wait()
process2.wait()