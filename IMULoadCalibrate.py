import board
import busio
import adafruit_bno055

i2c = busio.I2C(board.SCL, board.SDA)
sensor1 = adafruit_bno055.BNO055_I2C(i2c)
sensor1.mode = adafruit_bno055.CONFIG_MODE

sensor2 = adafruit_bno055.BNO055_I2C(i2c)
sensor2.mode = adafruit_bno055.CONFIG_MODE

fn1 = open("IMU_in_case.txt","r")
fn2 = open("IMU_out_of_case.txt","r")

sensor1calib = fn1.readlines()
sensor2calib = fn2.readlines()

fn1.close()
fn2.close()

for x in range(0,len(sensor1calib)):
	sensor1calib[x] = sensor1calib[x].replace("\n","")
	sensor2calib[x] = sensor2calib[x].replace("\n","")

sensor1.offsets_accelerometer = eval(sensor1calib[0])
sensor1.offsets_magnetometer = eval(sensor1calib[1])
sensor1.offsets_gyroscope = eval(sensor1calib[2])
sensor1.radius_accelerometer = eval(sensor1calib[3])
sensor1.radius_magnetometer = eval(sensor1calib[4])

sensor2.offsets_accelerometer = eval(sensor2calib[0])
sensor2.offsets_magnetometer = eval(sensor2calib[1])
sensor2.offsets_gyroscope = eval(sensor2calib[2])
sensor2.radius_accelerometer = eval(sensor2calib[3])
sensor2.radius_magnetometer = eval(sensor2calib[4])

sensor1.mode = adafruit_bno055.NDOF_MODE
sensor2.mode = adafruit_bno055.NDOF_MODE

