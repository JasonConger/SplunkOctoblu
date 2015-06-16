import time
import logging
import sys
import random

if len(sys.argv) < 2:
    print("Usage: icartt.py <int>")
    sys.exit(1)

state = sys.argv[1]

logging.basicConfig(filename='icartt.log', format='%(asctime)s %(message)s', level=logging.DEBUG)

while True:
    # Create values with variance
    if state == "1":
        icartt_val = 20 + random.uniform(-2,2)
        server_cpu_val = 10 + random.uniform(-5,5)
        server_mem_val = 10 + random.uniform(-5,5)
        server_disk_val = 10 + random.uniform(-5,5)
        hyp_cpu_val = 10 + random.uniform(-5,5)
        hyp_mem_val = 44 + random.uniform(-5,5)
        hyp_disk_val = 10 + random.uniform(-5,5)
        storage_write_lat_val = 2 + random.uniform(-0.05,0.05)
        storage_read_lat_val = 2 + random.uniform(-0.05,0.05)
        logging.info("STR INFO - 192.168.180.%s [established connection] partner:online %s" % (random.uniform(2,4), random.uniform(0,10)))
        
        
    elif state == "2":
        icartt_val = 40 + random.uniform(-2,2)
        server_cpu_val = 50 + random.uniform(-5,5)
        server_mem_val = 50 + random.uniform(-5,5)
        server_disk_val = 30 + random.uniform(-5,5)
        hyp_cpu_val = 10 + random.uniform(-5,5)
        hyp_mem_val = 55 + random.uniform(-5,5)
        hyp_disk_val = 40 + random.uniform(-5,5)
        storage_write_lat_val = 6 + random.uniform(-1,1)
        storage_read_lat_val = 2 + random.uniform(-1,1)
    
    elif state == "3":
        icartt_val = 63 + random.uniform(-2,2)
        server_cpu_val = 75 + random.uniform(-5,5)
        server_mem_val = 85 + random.uniform(-5,5)
        server_disk_val = 60 + random.uniform(-5,5)
        hyp_cpu_val = 20 + random.uniform(-5,5)
        hyp_mem_val = 75 + random.uniform(-5,5)
        hyp_disk_val = 60 + random.uniform(-5,5)
        storage_write_lat_val = 12 + random.uniform(-5,5)
        storage_read_lat_val = 4 + random.uniform(-1,1)
        logging.info("STR WARNING - 192.168.180.%s [controller] status:%s" % (random.uniform(2,4), random.uniform(0,1)))
        
    elif state == "4":
        icartt_val = 200 + random.uniform(-50,50)
        server_cpu_val = 80 + random.uniform(-5,5)
        server_mem_val = 85 + random.uniform(-5,5)
        server_disk_val = 90 + random.uniform(-5,5)
        hyp_cpu_val = 30 + random.uniform(-5,5)
        hyp_mem_val = 80 + random.uniform(-5,5)
        hyp_disk_val = 90 + random.uniform(-5,5)
        storage_write_lat_val = 40 + random.uniform(-5,5)
        storage_read_lat_val = 8 + random.uniform(-2,2)
        logging.info("STR ERROR - 192.168.180.%s [controller] partner:offline status:0" % (random.uniform(2,4)))
        

    
    
    logging.info("ICARTT=%s, username=MarkT, server_cpu=%s, server_mem=%s, server_disk=%s, hyp_cpu=%s, hyp_mem=%s, hyp_disk=%s, storage_write_lat=%s, storage_read_lat=%s" % (icartt_val, server_cpu_val, server_mem_val, server_disk_val, hyp_cpu_val, hyp_mem_val, hyp_disk_val, storage_write_lat_val, storage_read_lat_val))
    
    time.sleep(1)