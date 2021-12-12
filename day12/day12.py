def can_visit_again(visited):
    double_visit = 0
    for f in filter(lambda v: v.islower(), visited):
        if visited.count(f) > 1:
            double_visit += 1

    # set to 1 for part1
    if double_visit > 2:
        return False
    return True


class Node:
    links = []
    name = ''

    def __init__(self, name):
        self.name = name
        self.links = []

    def add(self, link):
        if self.links.count(link) > 0:
            return
        self.links.append(link)

    def traverse(self, visited: [], routes: []):
        if self.name == 'start' and len(visited) != 0:
            return None

        if self.name == 'end':
            routes.append(['end'] + visited)
            return 'end'

        if not can_visit_again(visited + [self.name]):
            return None

        res = []
        for link in self.links:
            t = link.traverse([self.name] + visited, routes)
            if t:
                res.append(t)

        if len(res) <= 0:
            return None

        res.insert(0, self)
        return res

    def __str__(self):
        return self.name

    def __repr__(self):
        return self.name


def count_paths(a):
    if isinstance(a, Node) or isinstance(a, str):
        return 1

    c = 0
    for x in a:
        c += count_paths(x)
    return c


def day12():
    with open('day12.txt') as data:
        lines = list(data.read().splitlines())
        nodes = {}
        for line in lines:
            src, dst = line.split('-')
            s_node = nodes.get(src)
            d_node = nodes.get(dst)
            if not s_node:
                s_node = Node(src)
                nodes[src] = s_node
            if not d_node:
                d_node = Node(dst)
                nodes[dst] = d_node
            s_node.add(d_node)
            d_node.add(s_node)

        routes = []
        nodes['start'].traverse([], routes)
        print(len(routes))


if __name__ == '__main__':
    day12()
