class EnemyPath:
    def __init__(self, path_points):
        self.path_points = path_points

    def get_next_point(self, current_index):
        if current_index < len(self.path_points) - 1:
            return self.path_points[current_index + 1]
        return None

class PathManager:
    def __init__(self):
        self.paths = {}

    def add_path(self, path_name, path_points):
        self.paths[path_name] = EnemyPath(path_points)

    def get_path(self, path_name):
        return self.paths.get(path_name)

# Predefined paths for enemies
def initialize_paths():
    path_manager = PathManager()
    path_manager.add_path("path1", [(0, 0), (1, 1), (2, 1), (3, 0)])
    path_manager.add_path("path2", [(0, 0), (0, 2), (2, 2), (2, 0)])
    path_manager.add_path("path3", [(0, 0), (1, 0), (1, 2), (0, 2)])
    return path_manager

# Example usage
if __name__ == "__main__":
    paths = initialize_paths()
    next_point = paths.get_path("path1").get_next_point(0)
    print(next_point)  # Output: (1, 1)