import numpy as np
import math
import time

# Ball Tree Implementation Without NumPy
class BallTreeNodeNonNumPy:
    def __init__(self, points, left=None, right=None):
        self.points = points
        self.left = left
        self.right = right
        self.center = None
        self.radius = 0
        if points:
            self.center = self.mean(points)
            self.radius = self.compute_radius(points, self.center)

    def mean(self, points):
        num_points = len(points)
        num_dimensions = len(points[0])
        center = [0] * num_dimensions

        for point in points:
            for i in range(num_dimensions):
                center[i] += point[i]

        return [x / num_points for x in center]

    def distance(self, point1, point2):
        return math.sqrt(sum((a - b) ** 2 for a, b in zip(point1, point2)))

    def compute_radius(self, points, center):
        return max(self.distance(p, center) for p in points)

class BallTreeNonNumPy:
    def __init__(self, points):
        start_time = time.time()
        self.root = self.build_tree(points)
        print(f"Non-NumPy Ball Tree Construction Time: {time.time() - start_time} seconds")

    def build_tree(self, points):
        if len(points) == 0:
            return None

        if len(points) == 1:
            return BallTreeNodeNonNumPy(points)

        center = BallTreeNodeNonNumPy.mean(self, points)
        distances = [BallTreeNodeNonNumPy.distance(self, p, center) for p in points]

        median_distance = sorted(distances)[len(distances) // 2]

        left_points = [p for p, d in zip(points, distances) if d <= median_distance]
        right_points = [p for p, d in zip(points, distances) if d > median_distance]

        if len(left_points) == 0 or len(right_points) == 0:
            return BallTreeNodeNonNumPy(points)

        left_child = self.build_tree(left_points)
        right_child = self.build_tree(right_points)

        return BallTreeNodeNonNumPy(points, left_child, right_child)

    def nearest_neighbor(self, point):
        return self._nearest_neighbor(self.root, point)

    def _nearest_neighbor(self, node, point, best=None, best_dist=float('inf')):
        if node is None:
            return best, best_dist

        if node.center is None:
            return best, best_dist

        dist_to_center = BallTreeNodeNonNumPy.distance(self, point, node.center)

        if dist_to_center - node.radius < best_dist:
            for p in node.points:
                dist = BallTreeNodeNonNumPy.distance(self, point, p)
                if dist < best_dist:
                    best = p
                    best_dist = dist

            best, best_dist = self._nearest_neighbor(node.left, point, best, best_dist)
            best, best_dist = self._nearest_neighbor(node.right, point, best, best_dist)

        return best, best_dist

# Ball Tree Implementation With NumPy
class BallTreeNodeNumPy:
    def __init__(self, points, left=None, right=None):
        self.points = points
        self.left = left
        self.right = right
        self.center = None
        self.radius = 0
        if points.size > 0:
            self.center = np.mean(points, axis=0)
            self.radius = self.compute_radius(points, self.center)

    def compute_radius(self, points, center):
        return np.max(np.linalg.norm(points - center, axis=1))

class BallTreeNumPy:
    def __init__(self, points):
        start_time = time.time()
        self.root = self.build_tree(np.array(points))
        print(f"NumPy Ball Tree Construction Time: {time.time() - start_time} seconds")

    def build_tree(self, points):
        if points.shape[0] == 0:
            return None

        if points.shape[0] == 1:
            return BallTreeNodeNumPy(points)

        center = np.mean(points, axis=0)
        distances = np.linalg.norm(points - center, axis=1)

        median_distance = np.median(distances)

        left_indices = distances <= median_distance
        right_indices = distances > median_distance

        left_points = points[left_indices]
        right_points = points[right_indices]

        if len(left_points) == 0 or len(right_points) == 0:
            return BallTreeNodeNumPy(points)

        left_child = self.build_tree(left_points)
        right_child = self.build_tree(right_points)

        return BallTreeNodeNumPy(points, left_child, right_child)

    def nearest_neighbor(self, point):
        return self._nearest_neighbor(self.root, np.array(point))

    def _nearest_neighbor(self, node, point, best=None, best_dist=float('inf')):
        if node is None:
            return best, best_dist

        if node.center is None:
            return best, best_dist

        dist_to_center = np.linalg.norm(point - node.center)

        if dist_to_center - node.radius < best_dist:
            for p in node.points:
                dist = np.linalg.norm(point - p)
                if dist < best_dist:
                    best = p
                    best_dist = dist

            best, best_dist = self._nearest_neighbor(node.left, point, best, best_dist)
            best, best_dist = self._nearest_neighbor(node.right, point, best, best_dist)

        return best, best_dist

# Test and Comparison
def print_tree_non_numpy(node, depth=0):
    if node is not None:
        print("  " * depth + f"Center: {node.center}, Radius: {node.radius}")
        print_tree_non_numpy(node.left, depth + 1)
        print_tree_non_numpy(node.right, depth + 1)

def print_tree_numpy(node, depth=0):
    if node is not None:
        print("  " * depth + f"Center: {node.center}, Radius: {node.radius}")
        print_tree_numpy(node.left, depth + 1)
        print_tree_numpy(node.right, depth + 1)

points = [
    [1, 2],
    [3, 4],
    [5, 6],
    [7, 8],
    [9, 10]
]

search_point = [5, 5]

print("Non-NumPy Ball Tree:")
tree_non_numpy = BallTreeNonNumPy(points)
print_tree_non_numpy(tree_non_numpy.root)

print("\nNumPy Ball Tree:")
tree_numpy = BallTreeNumPy(points)
print_tree_numpy(tree_numpy.root)

# Perform nearest neighbor search
non_numpy_nn, non_numpy_dist = tree_non_numpy.nearest_neighbor(search_point)
print(f"\nNon-NumPy nearest neighbor for {search_point}: {non_numpy_nn}, Distance: {non_numpy_dist}")

numpy_nn, numpy_dist = tree_numpy.nearest_neighbor(search_point)
print(f"NumPy nearest neighbor for {search_point}: {numpy_nn}, Distance: {numpy_dist}")