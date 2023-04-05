def next_list(l: list, obj: object):
    j = l.index(obj)
    for i in l:
        if obj != i:
            return i
        else:
            if j < len(l):
                j += 1
            elif j == len(l):
                j = 0
                i = l[0]


class Camera:
    def __init__(self, id, name, resolution):
        self.id = id
        self.name = name
        self.resolution = resolution

    def transmit(self):
        pass


class Device(Camera):
    def __init__(self, brand, model, id, name, resolution):
        super().__init__(id, name, resolution)
        self.brand = brand
        self.model = model

    def transmit(self):
        return f"El nombre de la camara es {self.name}"


class Session:
    def __init__(self, id, name_session, name_teacher, classroom,
                 date, date_begin, date_finish, camera_on_use, camera_list: list):
        self.camera_list = camera_list
        self.camera_on_use = camera_on_use
        self.date_finish = date_finish
        self.date_begin = date_begin
        self.date = date
        self.classroom = classroom
        self.name_teacher = name_teacher
        self.name_session = name_session
        self.id = id

    def begin_transmission(self):
        pass

    def finish_transmission(self):
        pass

    def change_camera(self):
        if type(self.camera_list) == list:
            if len(self.camera_list) > 1:
                self.camera_on_use = next_list(self.camera_list, self.camera_on_use)
                print(self.camera_on_use.name)


if __name__ == "__main__":
    a = Device("ada", "ada001", 0, "nicon", 2000)
    b = Device("ada", "ada001", 0, "ffaf", 2000)
    c = Device("ada", "ada001", 0, "lele", 2000)
    d = Session(0, 0, 0, 0, 0, 0, 0, a, [a, b, c])
    d.change_camera()
    d.change_camera()
    d.change_camera()
    print(a.transmit())
