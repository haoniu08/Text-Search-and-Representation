import numpy as np
import time

class KDTreeNode:
    def __init__(self, point, left=None, right=None, axis=0):
        self.point = point
        self.left = left
        self.right = right
        self.axis = axis

class KDTree:
    def __init__(self, points):
        start_time = time.time()
        self.root = self.build_tree(points)
        end_time = time.time()
        print(f"Tree construction time: {end_time - start_time:.6f} seconds")

    def build_tree(self, points, depth=0):
        if not points:
            return None

        k = len(points[0])
        axis = depth % k

        points.sort(key=lambda x: x[axis])
        median = len(points) // 2

        return KDTreeNode(
            point=points[median],
            left=self.build_tree(points[:median], depth + 1),
            right=self.build_tree(points[median + 1:], depth + 1),
            axis=axis
        )

    def nearest_neighbor(self, point):
        return self._nearest_neighbor(self.root, point)

    def _nearest_neighbor(self, node, point, depth=0, best=None, best_dist=float('inf')):
        if node is None:
            return best, best_dist

        k = len(point)
        axis = depth % k

        next_best = best
        next_best_dist = best_dist

        point_dist = np.linalg.norm(np.array(point) - np.array(node.point))
        if point_dist < next_best_dist:
            next_best = node.point
            next_best_dist = point_dist

        if point[axis] < node.point[axis]:
            next_branch = node.left
            other_branch = node.right
        else:
            next_branch = node.right
            other_branch = node.left

        next_best, next_best_dist = self._nearest_neighbor(next_branch, point, depth + 1, next_best, next_best_dist)

        # if abs(point[axis] - node.point[axis]) < next_best_dist:
        # try square of distance 
        if (point[axis] - node.point[axis])**2 < next_best_dist:
            next_best, next_best_dist = self._nearest_neighbor(other_branch, point, depth + 1, next_best, next_best_dist)

        return next_best, next_best_dist