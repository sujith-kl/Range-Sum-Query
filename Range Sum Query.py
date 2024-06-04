class SegmentTree:
    def __init__(self, data):
        self.n = len(data)
        self.tree = [0] * (2 * self.n)
        self.build_tree(data)

    def build_tree(self, data):
        # Initialize leaves
        for i in range(self.n):
            self.tree[self.n + i] = data[i]
        # Build the tree by calculating parents
        for i in range(self.n - 1, 0, -1):
            self.tree[i] = self.tree[i * 2] + self.tree[i * 2 + 1]

    def update(self, pos, value):
        # Update the value at position pos
        pos += self.n
        self.tree[pos] = value
        # Update the rest of the tree
        while pos > 1:
            pos //= 2
            self.tree[pos] = self.tree[2 * pos] + self.tree[2 * pos + 1]

    def query(self, left, right):
        # Range query from left to right
        left += self.n
        right += self.n
        sum = 0
        while left < right:
            if left % 2:
                sum += self.tree[left]
                left += 1
            if right % 2:
                right -= 1
                sum += self.tree[right]
            left //= 2
            right //= 2
        return sum
# Sample data representing the scores of students
student_scores = [15, 20, 30, 40, 25, 35, 50, 45]

# Initialize the Segment Tree with student scores
segment_tree = SegmentTree(student_scores)

# Query the sum of scores from index 1 to 4 (20 + 30 + 40 + 25)
print("Sum of scores from index 1 to 4:", segment_tree.query(1, 5))

# Update the score of the student at index 3 to 55
segment_tree.update(3, 55)

# Query the sum of scores from index 1 to 4 again after the update
print("Sum of scores from index 1 to 4 after update:", segment_tree.query(1, 5))

# Query the sum of scores for the entire range
print("Sum of scores for the entire range:", segment_tree.query(0, len(student_scores)))
