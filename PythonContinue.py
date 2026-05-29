import random
import time

def sensor_data_stream(sensor_type,max_value=100):
    while True:
        data=round(random.uniform(0,max_value),2)
        timestamp=time.strftime("%Y-%m-%d %H:%M:%S",time.localtime())
        yield f"{timestamp} - {sensor_type}: {data}"
        time.sleep(1)

humidity_sensor=sensor_data_stream("nem sensörü",50)  

for _ in range(15):
    print(next(humidity_sensor))


#örnek f = dosyayı kastediyor = folder (Bence)

def temiz_satirlar(dosya_yolu):
    with open(dosya_yolu,"r",encoding="utf-8") as f:
        for line in f:
            s = line.strip()
            if s and not s.startswith("#"):
                yield s

for satir in temiz_satirlar("log.txt"):
    print(satir)                        
