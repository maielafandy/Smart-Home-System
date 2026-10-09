# ---------------------------------
# This file is for learning
# creator: Mai Mohamed
# creation date : 8/2/2026
# ---------------------------------
# learned super to call the initialization
# learned how to use isinstance
from vaildation import get_integer_in_range, check_a_list


class Device():
    def __init__(self, name, status):
        self.name = name
        self.status = status

    def turn_on(self):
        self.status = "on"
        return self.status

    def turn_off(self):
        self.status = "off"
        return self.status

    def display_status(self):
        return self.status


class Light(Device):
    def __init__(self, name, status, brightness):
        self.brightness = brightness
        super().__init__(name, status)

    def change_brightness(self, new_brightness):
        self.brightness = new_brightness

    def display_brightness(self):
        return self.brightness


class Fan(Device):
    def __init__(self, name, status, speed):
        self.speed = speed
        super().__init__(name, status)

    def change_speed(self, new_speed):
        self.speed = new_speed

    def display_speed(self):
        return self.speed


class AirConditioner(Device):
    def __init__(self, name, status, temperature):
        self.temperature = temperature
        super().__init__(name, status)

    def change_temperature(self, new_temperature):
        self.temperature = new_temperature

    def display_temperature(self):
        return self.temperature


def display_menu():
    choice = get_integer_in_range(
        "Choose for the menu : \n1- Add Device\n2- View Devices\n3- Turn ON\n4- Turn OFF\n5- Change Device Setting\n6- Exit", 6, 1)
    return choice


def add_device(devices):

    choice = get_integer_in_range(
        "choose the type of device you want to add \n1-Light\n2-Fan\n3-Air Conditioner", 3, 1)
    if choice == 1:
        light_name = input("enter the light name ")

        choose_status = get_integer_in_range("1-on\n2-off", 2, 1)
        if choose_status == 1:
            status = "on"

        elif choose_status == 2:
            status = "off"

        brightness = get_integer_in_range(
            "enter the brightness", 100, 0)
        light = Light(light_name, status, brightness)
        devices.append(light)
        return True

    elif choice == 2:
        fan_name = input("enter the fan name ")

        choose_status = get_integer_in_range("1-on\n2-off", 2, 1)
        if choose_status == 1:
            status = "on"

        elif choose_status == 2:
            status = "off"

        speed = get_integer_in_range("enter the speed", 100, 0)
        fan = Fan(fan_name, status, speed)
        devices.append(fan)
        return True
    elif choice == 3:
        air_conditioner_name = input(
            "enter the Air Conditioner name ")

        choose_status = get_integer_in_range("1-on\n2-off", 2, 1)
        if choose_status == 1:
            status = "on"

        elif choose_status == 2:
            status = "off"

        temperature = get_integer_in_range(
            "enter the temperature", 30, 18)
        air_conditioner = AirConditioner(
            air_conditioner_name, status, temperature)
        devices.append(air_conditioner)
        return True


def view_devices(devices):
    check = check_a_list(
        "there is no devices , please add device first", devices)
    print("*"*30)
    for i, device in enumerate(devices):
        if isinstance(device, Light):
            print(
                f"{i+1}-{device.name} type:light , state :{device.display_status()} , brightness: {device.display_brightness()}")
        elif isinstance(device, Fan):
            print(
                f"{i+1}-{device.name} type:Fan , state :{device.display_status()} , speed: {device.display_speed()}")
        elif isinstance(device, AirConditioner):
            print(f"{i+1}-{device.name} type:Air conditioner , state :{device.display_status()} , temperature: {device.display_temperature()}")
    print("*"*30)
    return check


def turn_on(devices):
    print("choose the device:\n")
    check = view_devices(devices)
    if check:
        chosen_device_device = get_integer_in_range(
            "choose device", len(devices), 1)
        devices[chosen_device_device-1].turn_on()


def turn_off(devices):
    print("choose the device:\n")
    check = view_devices(devices)
    if check:
        chosen_device_device = get_integer_in_range(
            "choose device", len(devices), 1)
        devices[chosen_device_device-1].turn_off()


def change_setting(devices):
    print("choose the device:\n")
    check = view_devices(devices)

    if check:
        chosen_device_device = devices[(get_integer_in_range(
            "choose device", len(devices), 1))-1]

        if isinstance(chosen_device_device, Light):
            new_brightness = get_integer_in_range(
                "enter the new_brightness", 100, 0)
            chosen_device_device.change_brightness(new_brightness)
        elif isinstance(chosen_device_device, Fan):
            new_speed = get_integer_in_range("enter the new_speed", 100, 0)
            chosen_device_device.change_speed(new_speed)
        elif isinstance(chosen_device_device, AirConditioner):
            new_temperature = get_integer_in_range(
                "enter the new_temperature", 30, 18)
            chosen_device_device.change_temperature(new_temperature)


# main
devices = []
while True:

    choice = display_menu()
    if choice == 1:
        add_device(devices)

    elif choice == 2:
        view_devices(devices)
    elif choice == 3:
        turn_on(devices)
    elif choice == 4:
        turn_off(devices)
    elif choice == 5:
        change_setting(devices)
    elif choice == 6:
        break
