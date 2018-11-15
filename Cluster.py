class ClusterCenter:
    cluster_center_x = 0
    cluster_center_y = 0
    cluster_center_z = 0
    list_of_points = []

    def __init__(self, x, y, z):
        self.cluster_center_x = x
        self.cluster_center_y = y
        self.cluster_center_z = z
        self.list_of_points = []

    def add_to_list(self, new_data):
        self.list_of_points.append(new_data)

    def get_list(self):
        return self.list_of_points

    def get_x(self):
        return self.cluster_center_x

    def get_y(self):
        return self.cluster_center_y

    def get_z(self):
        return self.cluster_center_z

