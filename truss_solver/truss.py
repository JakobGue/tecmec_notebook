class Support:

    # type: fixed, roller
    def __init__(self, pos: tuple, type: str):
        self.pos = pos
        self.type = type



class Truss:

    def __init__(self):
        self.supports = []
        self.nodes = []
        self.rods = []
        self.loads = []

    

    def add_node(self, pos: tuple):
        self.nodes.append(pos)


    def add_rod(self, node1: tuple, node2: tuple):
        self.rods.append((node1, node2))


    def add_load(self, pos: tuple, force: tuple, axis: str):
        self.loads.append((pos, force, axis))


    def add_support(self, pos: tuple, type: str):
        s = Support(pos, type)
        self.supports.append(s)


    def solve_stiffness(self, output: bool = True):
        bearing_value = self.calc_bearing_value()
        if output:
            print("2 * k  = a + s")
            print("2 * {}  = {} + {}".format(2 * len(self.nodes), bearing_value, len(self.rods)))
        return 2 * len(self.nodes) == bearing_value + len(self.rods)


    def calc_bearing_value(self):
        bearing_value = 0
        for s in self.supports:
            if s.type == 'fixed':
                bearing_value += 2
            elif s.type == 'roller':
                bearing_value += 1

        return bearing_value

    def solve_reaction_forces(self):
        if not self.solve_stiffness(output=False):
            return "Truss is not stiff enough to solve reaction forces"
        missing_forces = []
        for s in self.supports:
            if s.type == 'fixed':
                missing_forces.append((s.pos, 'x'))
                missing_forces.append((s.pos, 'y'))
            elif s.type == 'roller':
                missing_forces.append((s.pos, 'y'))
        
        for force in missing_forces:
            



