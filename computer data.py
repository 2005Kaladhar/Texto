import time
import psutil as pu

for i in range(20):
    time.sleep(1)
    for j,k in pu.virtual_memory()._asdict().items():
        if j == 'percent':
            print(f"{j}:{k}%")
        else:
            print( ("{}:{:.2f}GB").format(j,int(k)/1000000000))
    print("\nDisk usage for C:Drive ")
    for item, value in pu.disk_usage("C:")._asdict().items():
        if item == 'percent':
            print(f"Disk {item} : {value}%")
        else:
            print( ("Disk {} : {:.2f}GB").format(item,int(value)/1000000000) )

    print("---------------------------------------")

