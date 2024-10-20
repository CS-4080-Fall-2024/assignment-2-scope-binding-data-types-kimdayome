class RubiksCube:
    def __init__(self):
        # initialize the cube with six sides, each face has 3x3 tiles.
        self.face = self.initialize_cube()

    # initialize the cube with numbers and colors
    def initialize_cube(self):
        # representing the cube faces with 'indexced color' tiles
        cube = {
            'Top': [[(1, "W"), (2, "W"), (3, "W")], 
                    [(4, "W"), (5, "W"), (6, "W")], 
                    [(7, "W"), (8, "W"), (9, "W")]],  #top (White)
            
            'Bottom': [[(1, "Y"), (2, "Y"), (3, "Y")], 
                       [(4, "Y"), (5, "Y"), (6, "Y")], 
                       [(7, "Y"), (8, "Y"), (9, "Y")]],  #bottom (Yellow)
            
            'Front': [[(1, "R"), (2, "R"), (3, "R")], 
                      [(4, "R"), (5, "R"), (6, "R")], 
                      [(7, "R"), (8, "R"), (9, "R")]],  #front (Red)
            
            'Back': [[(1, "O"), (2, "O"), (3, "O")], 
                     [(4, "O"), (5, "O"), (6, "O")], 
                     [(7, "O"), (8, "O"), (9, "O")]],  #back (Orange)
            
            'Left': [[(1, "G"), (2, "G"), (3, "G")], 
                     [(4, "G"), (5, "G"), (6, "G")], 
                     [(7, "G"), (8, "G"), (9, "G")]],  #left (Green)
            
            'Right': [[(1, "B"), (2, "B"), (3, "B")], 
                      [(4, "B"), (5, "B"), (6, "B")], 
                      [(7, "B"), (8, "B"), (9, "B")]]   #right (Blue)
        }
        return cube

    # rotate face 90 degrees clockwise
    def rotate_face_clockwise(self, face_name):
        face = self.face[face_name]
        # Rotate Corner 
        temp = face[0][0]
        face[0][0] = face[2][0]   # shift bottom-left to top-left
        face[2][0] = face[2][2]   # shift bottom-right to bottom-left
        face[2][2] = face[0][2]   # shift top-right to bottom-right
        face[0][2] = temp         # shift top-left to top-right

        # Rotate Edge 
        temp = face[0][1]
        face[0][1] = face[1][0]   # shift left-center to top-center
        face[1][0] = face[2][1]   # shift bottom-center to left-center
        face[2][1] = face[1][2]   # shift right-center to bottom-center
        face[1][2] = temp         # shift top-center to right-center

    # rotate face 90 degrees counterclockwise
    def rotate_face_counter_clockwise(self, face_name):
        face = self.face[face_name]
        # Rotate Corner 
        temp = face[0][0]
        face[0][0] = face[0][2]   # shift top-right to top-left
        face[0][2] = face[2][2]   # shift bottom-right to top-right
        face[2][2] = face[2][0]   # shift bottom-left to bottom-right
        face[2][0] = temp         # shift top-left to bottom-left

        # Rotate Edge 
        temp = face[0][1]
        face[0][1] = face[1][2]   # shift right-center to top-center
        face[1][2] = face[2][1]   # shift bottom-center to right-center
        face[2][1] = face[1][0]   # shift left-center to bottom-center
        face[1][0] = temp         # shift top-center to left-center

    # Rotate the top layer clockwise
    def rotate_top_layer_clockwise(self):
        self.rotate_face_clockwise("Top")
        # save the top row of Front face and then move the rows of adjacent faces
        temp = self.face["Front"][0]
        self.face["Front"][0] = self.face["Right"][0]
        self.face["Right"][0] = self.face["Back"][0]
        self.face["Back"][0] = self.face["Left"][0]
        self.face["Left"][0] = temp

    # Rrtate the bottom layer area clockwise
    def rotate_bottom_layer_clockwise(self):
        self.rotate_face_clockwise("Bottom")
        # save the bottom row of Front face and rotate the rows of adjacent faces
        temp = self.face["Front"][2]
        self.face["Front"][2] = self.face["Left"][2]
        self.face["Left"][2] = self.face["Back"][2]
        self.face["Back"][2] = self.face["Right"][2]
        self.face["Right"][2] = temp

    # rotate the left column clockwise
    def rotate_left_column_clockwise(self):
        self.rotate_face_clockwise("Left")
        # save the left column of the Top face
        temp_col = [self.face["Top"][i][0] for i in range(3)]
        # rotate left columns of adjacent faces
        for i in range(3):
            self.face["Top"][i][0] = self.face["Back"][2 - i][2]
            self.face["Back"][2 - i][2] = self.face["Bottom"][i][0]
            self.face["Bottom"][i][0] = self.face["Front"][i][0]
            self.face["Front"][i][0] = temp_col[i]

    # rotate the right column clockwise
    def rotate_right_column_clockwise(self):
        self.rotate_face_clockwise("Right")
        # save the right column of the Top face
        temp_col = [self.face["Top"][i][2] for i in range(3)]
        # rotate right columns of adjacent faces
        for i in range(3):
            self.face["Top"][i][2] = self.face["Front"][i][2]
            self.face["Front"][i][2] = self.face["Bottom"][i][2]
            self.face["Bottom"][i][2] = self.face["Back"][2 - i][0]
            self.face["Back"][2 - i][0] = temp_col[i]

    # print the full state of the cube with all faces
    def print_full_cube(self):
        faces = ["Top", "Bottom", "Front", "Back", "Left", "Right"]
        for face_name in faces:
            print(f"--- {face_name} Face 😀 ---")
            self.print_face(face_name)

    # print a single face of the cube
    def print_face(self, face_name):
        content = ""
        for row in self.face[face_name]:
            content += f"| {row[0]} | {row[1]} | {row[2]} |\n"
        print(content)

# test the updated cube!
cube = RubiksCube()

# print the initial state of the cube
print("Initial Cube:")
cube.print_full_cube()

# rotate top layer clockwise and print
cube.rotate_top_layer_clockwise()
print("\nAfter rotating top layer clockwise:")
cube.print_full_cube()

# rotate bottom layer clockwise and print
cube.rotate_bottom_layer_clockwise()
print("\nAfter rotating bottom layer clockwise:")
cube.print_full_cube()

# rotate left column clockwise and print
cube.rotate_left_column_clockwise()
print("\nAfter rotating left column clockwise:")
cube.print_full_cube()

# rotate right column clockwise and print
cube.rotate_right_column_clockwise()
print("\nAfter rotating right column clockwise:")
cube.print_full_cube()

# solution approach reference used : https://medium.com/@ekollie324/how-to-build-a-rubiks-cube-in-python-c3bd19cbcd73