class ClusterCenter:
    cluster_center_x = 0
    cluster_center_y = 0
    cluster_center_z = 0
    cluster_original_x = 0
    cluster_original_y = 0
    cluster_original_z = 0
    cluster_class = 0
    list_of_points = []

    def __init__(self, x, y, z, ox, oy, oz, data_class):
        self.cluster_center_x = x
        self.cluster_center_y = y
        self.cluster_center_z = z
        self.cluster_original_x = ox
        self.cluster_original_y = oy
        self.cluster_original_z = oz
        self.list_of_points = []
        self.cluster_class = data_class

    def add_to_list(self, new_data):
        self.list_of_points.append(new_data)

    def get_list(self):
        return self.list_of_points

    def get_class(self):
        return self.cluster_class

    def get_x(self):
        return self.cluster_center_x

    def get_y(self):
        return self.cluster_center_y

    def get_z(self):
        return self.cluster_center_z

    def get_original_x(self):
        return self.cluster_original_x

    def get_original_y(self):
        return self.cluster_original_y

    def get_original_z(self):
        return self.cluster_original_z

