## Temperature Checker

## Installation
### Arduino
In oderder to install the arduino program you must have installed the [DHT library](https://www.arduino.cc/reference/en/libraries/dht-sensor-library/).
Also, you must set the `prod` variable to `true` in the code. Example:
```
float temp;
bool prod = true;
```
Otherwise it will execute a random temperatures generator.
Besides that, there's no other only requirements to make this work.

### Server
The server makes use of the following Python dependencies:
```
- yaml
- flask
- flask_sqlalchemy
- flask_marshmallow
- marshmallow
- sqlalchemy
- serial
- pymysql
```

Also you would probably have to change the `config.yml` file in the `arduino:serialport` key to set your connection port.
Once you have done that you just can run the `server.py` file and everything should work fine.