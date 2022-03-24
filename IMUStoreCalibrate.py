import board
import busio
import adafruit_bno055

i2c = busio.I2C(board.SCL, board.SDA)

sensor1 = adafruit_bno055.BNO055_I2C(i2c)
sensor2 = adafruit_bno055.BNO055_I2C(i2c,0x29)

while not sensor1.calibrated:
	print("Calib1 (S,G,A,M): {}".format(sensor1.calibration_status))

fn = open("IMU_in_case.txt","w")
fn.write("{}\n".format(sensor1.offsets_accelerometer))
fn.write("{}\n".format(sensor1.offsets_magnetometer))
fn.write("{}\n".format(sensor1.offsets_gyroscope))
fn.write("{}\n".format(sensor1.radius_accelerometer))
fn.write("{}\n".format(sensor1.radius_magnetometer))
fn.close()

while not sensor2.calibrated:
	print("Calib2 (S,G,A,M): {}".format(sensor2.calibration_status))

fn = open("IMU_out_of_case.txt","w")
fn.write("{}\n".format(sensor2.offsets_accelerometer))
fn.write("{}\n".format(sensor2.offsets_magnetometer))
fn.write("{}\n".format(sensor2.offsets_gyroscope))
fn.write("{}\n".format(sensor2.radius_accelerometer))
fn.write("{}\n".format(sensor2.radius_magnetometer))
fn.close()

