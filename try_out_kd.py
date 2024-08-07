import numpy as np

class KDTreeNode:
    def __init__(self, point, left=None, right=None, axis=0):
        self.point = point
        self.left = left
        self.right = right
        self.axis = axis

class KDTreeNonNumPy:
    def __init__(self, points):
        self.root = self.build_tree(points)

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

        point_dist = self.distance(point, node.point)
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

        if (point[axis] - node.point[axis])**2 < next_best_dist:
            next_best, next_best_dist = self._nearest_neighbor(other_branch, point, depth + 1, next_best, next_best_dist)

        return next_best, next_best_dist

    def distance(self, point1, point2):
        return np.sqrt(sum((a - b) ** 2 for a, b in zip(point1, point2)))


class KDTreeNumPy:
    def __init__(self, points):
        points = np.array(points)  # Convert points to a NumPy array
        self.root = self.build_tree(points)

    def build_tree(self, points, depth=0):
        if len(points) == 0:
            return None

        k = points.shape[1]
        axis = depth % k

        points = points[points[:, axis].argsort()]  # Sort points by the specified axis
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

        if (point[axis] - node.point[axis])**2 < next_best_dist:
            next_best, next_best_dist = self._nearest_neighbor(other_branch, point, depth + 1, next_best, next_best_dist)

        return next_best, next_best_dist


def print_tree(node, depth=0):
    if node is not None:
        print("  " * depth + f"Axis: {node.axis}, Point: {node.point}")
        print_tree(node.left, depth + 1)
        print_tree(node.right, depth + 1)


# Test and comparison
points = [
    [1, 2],
    [3, 4],
    [5, 6],
    [7, 8],
    [9, 10]
]

print("Non-NumPy KD Tree:")
tree_non_numpy = KDTreeNonNumPy(points)
print_tree(tree_non_numpy.root)

print("\nNumPy KD Tree:")
tree_numpy = KDTreeNumPy(points)
print_tree(tree_numpy.root)

# Perform nearest neighbor search
point_to_search = [5, 5]

non_numpy_nn, non_numpy_dist = tree_non_numpy.nearest_neighbor(point_to_search)
print(f"\nNon-NumPy nearest neighbor for {point_to_search}: {non_numpy_nn}, Distance: {non_numpy_dist}")

numpy_nn, numpy_dist = tree_numpy.nearest_neighbor(point_to_search)
print(f"NumPy nearest neighbor for {point_to_search}: {numpy_nn}, Distance: {numpy_dist}")