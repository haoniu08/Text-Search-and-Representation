import math
import time

class BallTreeNode:
    def __init__(self, points, left=None, right=None):
        self.points = points
        self.left = left
        self.right = right

class BallTree:
    def __init__(self, points):
        start_time = time.time()
        self.root = self.build_tree(points)
        end_time = time.time()
        print(f"Tree construction time: {end_time - start_time:.6f} seconds")

    def build_tree(self, points):
        if len(points) == 0:
            return None

        if len(points) == 1:
            return BallTreeNode(points)

        center = self.mean(points)
        distances = [self.distance(p, center) for p in points]

        if len(distances) == 1:
            median_distance = distances[0]
        else:
            median_distance = sorted(distances)[len(distances) // 2]

        left_points = [p for p, d in zip(points, distances) if d <= median_distance]
        right_points = [p for p, d in zip(points, distances) if d > median_distance]

        if len(left_points) == 0 or len(right_points) == 0:
            return BallTreeNode(points)

        left_child = self.build_tree(left_points)
        right_child = self.build_tree(right_points)

        return BallTreeNode(points, left_child, right_child)

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

    def nearest_neighbor(self, point):
        return self._nearest_neighbor(self.root, point)

    def _nearest_neighbor(self, node, point, best=None, best_dist=float('inf')):
        if node is None:
            return best, best_dist

        if node.left is None and node.right is None:
            for p in node.points:
                dist = self.distance(point, p)
                if dist < best_dist:
                    best = p
                    best_dist = dist
            return best, best_dist

        dist_to_center = self.distance(point, self.mean(node.points))
        radius = self.compute_radius(node.points, self.mean(node.points))

        if dist_to_center - radius < best_dist:
            for p in node.points:
                dist = self.distance(point, p)
                if dist < best_dist:
                    best = p
                    best_dist = dist

            best, best_dist = self._nearest_neighbor(node.left, point, best, best_dist)
            best, best_dist = self._nearest_neighbor(node.right, point, best, best_dist)

        return best, best_dist

    def compute_radius(self, points, center):
        return max(self.distance(p, center) for p in points)
