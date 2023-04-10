def next_list(l: list, index: int):
    if index + 1 < len(l):
        return l[index + 1]
    else:
        return l[0]


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
        print("Iniciando transmición...")

    def finish_transmission(self):
        print("Terminando transmición...")

    def change_camera(self):
        if len(self.camera_list) == 1 and self.camera_on_use == 0:
            self.camera_on_use = self.camera_list[0]
            return
        elif len(self.camera_list) < 1:
            return

        ref = self.camera_on_use
        self.camera_on_use = next_list(self.camera_list, self.camera_list.index(ref))


class Main:
    def __init__(self):
        sesion = 0
        transmission = False

        while True:
            __input = input(
                """
Para crear una sesión de VideoLlamada, ingrese ( 1 )
Para cambiar o ingresar una cámara, ingrese ( 2 )
Para ver que camará tiene seleccionada y ver la lista de cámaras, ingrese ( 3 )
Para iniciar la transmición, ingrese ( 4 )
Para terminar la transmición, ingrese ( 5 )
Para cerrar el programa, ingrese ( 0 )
- """
            )

            match __input:
                case "0":
                    break
                case "1":
                    sesion = Session(0,
                                     input("Cree un nombre para la sesión "),
                                     input("Ponga su nombre como profesor "),
                                     int(input("Ponga un codigo para la clase ")),
                                     input("Ponga la fecha de la clase "),
                                     input("Ponga la hora que empezará la clase así, por ejemplo ( 00:00 ) "),
                                     input("Ahora ponga la hora que terminará la clase "),
                                     0,
                                     []
                                     )
                    print("La sesión a sido creado correctamente")
                case "2":
                    if sesion == 0:
                        print("No puede cambiar de cámara cuando no tiene un sesión creada")
                        continue

                    __input = input("Para ingrear una cámara ingrese ( 1 ) \nPara cambiar de cámara si es que tiene ingrese ( 2 ) \n")
                    aux = max(0, len(sesion.camera_list)-1)

                    if __input == "1":
                        sesion.camera_list += [Device(input("Ingrese la marca de la cámara "), input("Ingrese su modelo "), aux, input("Ingrese el nombre para la cámara "),
                                                      input("ingrese su resolución por ejemplo ( 1024x784 ) "))]
                        print("Cámara ingresada")
                    else:
                        sesion.change_camera()
                        print(f"La cámara a sido cambiada a {sesion.camera_on_use}")
                case "3":
                    if sesion == 0:
                        print("No puede ver las cámaras cuando no tiene una seción creada")
                        continue

                    if len(sesion.camera_list) > 0:
                        for i in sesion.camera_list:
                            print(i.name)
                case "4":
                    if sesion == 0:
                        print("No puede iniciar una transmición si no a creado una seción")
                        continue

                    if not transmission:
                        sesion.begin_transmission()
                        transmission = True

                case "5":
                    if sesion == 0:
                        print("No puede terminar una transmición si no a creado una seción")
                        continue

                    if transmission:
                        sesion.end_transmission()
                        transmission = False


if __name__ == "__main__":
    Main()
