import sys


class Node:
    state = None
    score = 0
    level = 0
    alpha = -sys.maxsize
    beta = sys.maxsize
    children = []

    def add_child(self, child):
        self.children.append(child)
        child.level = self.level + 1
        if child.level % 2 == 0:
            child.score = sys.maxsize
        else:
            child.score = -sys.maxsize


class MinimaxTree:
    root = None

    def run_alg(self, node=root):
        if len(node.children) == 0:
            return node.score
        for child in node.children:
            score_of_child = self.run_alg(child)
            if node.level % 2 == 0:  # max
                if node.score < score_of_child:
                    node.score = score_of_child
                    if node.alpha < node.score:
                        node.alpha = node.score
            else:  # min
                if node.score > score_of_child:
                    node.score = score_of_child
                    if node.beta > node.score:
                        node.beta = node.score
            if node.beta <= node.alpha:
                return node.score


