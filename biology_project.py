class graph_node:
    brute_force_list = []
    copy_list = []

    def __init__(this, label, id):
        this.id = id
        this.label = label
        this.adjacency_list = []
        this.visited = False

    def reset(this):
        this.visited = False

    def print_adjacency_list(this):
        s = str(this.id) + ":" + this.label + " -> "
        if (len(this.adjacency_list) != 0):
            for i in this.adjacency_list:
                if (i != this.adjacency_list[len(this.adjacency_list) - 1]):
                    s = s + str(i.id) + ":" + i.label + ", "
                else:
                    s = s + str(i.id) + ":" + i.label
        else:
            s = s + "nill"
        print(s)

    def visit_checker(this):
        check = True
        if (len(this.adjacency_list) != 0):
            for i in this.adjacency_list:
                if (i.visited == False):
                    check = False
                    break
        return check

    def dfs_single_string(this, size):
        this.visited = True
        graph_node.brute_force_list[0].append(this.label)
        if (this.visit_checker() == False):
            for i in this.adjacency_list:
                if (i.visited == False):
                    check = i.dfs_single_string(size)
                    if (check == True):
                        return True
        if (len(graph_node.brute_force_list[0]) == size):
            return True
        graph_node.brute_force_list[0].pop()
        this.visited = False

    def dfs(this, size):
        this.visited = True
        graph_node.copy_list.append(this.label)
        if (this.visit_checker() == False):
            for i in this.adjacency_list:
                if (i.visited == False):
                    i.dfs(size)
        if (len(graph_node.copy_list) == size):
            graph_node.brute_force_list.append(graph_node.copy_list.copy())
        graph_node.copy_list.pop()
        this.visited = False

class graph:
    def __init__(this, kmer):
        this.graph_nodes_list = []
        this.kmer = kmer
        this.method = False

    def add_node(this, node_label):
        if (len(node_label) == this.kmer):
            this.graph_nodes_list.append(graph_node(node_label, len(this.graph_nodes_list)))
        else:
            print()
            print("Kmer size doesn't match the label of the node entered")
            print()

    def add_nodes_with_string(this, gene):
        if (gene.isalpha()):
            this.graph_nodes_list.clear()
            for i in range(len(gene) - kmer + 1):
                this.add_node(gene[i:(i + kmer)])
        else:
            print()
            print("Gene is made of characters other than alphabets")
            print()


    def add_edges_by_similarity(this):
        for i in range(len(this.graph_nodes_list)):
            for j in range(len(this.graph_nodes_list)):
                if (i != j):
                    if (this.graph_nodes_list[i].label[(-this.kmer + 1):] == this.graph_nodes_list[j].label[:(this.kmer - 1)]):
                        this.add_edge(i, j)

    def add_edge(this, from_node, to_node):
        this.graph_nodes_list[from_node].adjacency_list.append(this.graph_nodes_list[to_node])

    def single_string_reconstructor(this):
        this.method = True
        this.reset()
        graph_node.brute_force_list.clear()
        graph_node.brute_force_list.append([])
        for i in this.graph_nodes_list:
            check = i.dfs_single_string(len(this.graph_nodes_list))
            if (check == True):
                break
        print()
        print("Path Analysis completed")
        print()

    def multiple_strings_reconstructor(this):
        this.method = False
        this.reset()
        graph_node.brute_force_list.clear()
        graph_node.copy_list.clear()
        for i in this.graph_nodes_list:
            i.dfs(len(this.graph_nodes_list))
        print()
        print("Path Analysis completed")

        real_list = []
        for i in graph_node.brute_force_list:
            if i not in real_list:
                real_list = real_list + [i]

        graph_node.brute_force_list = real_list.copy()
        print("Removed unwanted or duplicate paths")
        print()

    def string_printer(this):
        if (len(graph_node.brute_force_list) != 0):
            print()
            if (this.method == False):
                print("All possible Hamiltonian Paths in the graph are: ")
            else:
                print("The Hamiltonian Path found in the graph is: ")
            for i in graph_node.brute_force_list:
                s = ""
                r = ""
                for j in range(len(i)):
                    if ((j + 1) != len(i)):
                        s = s + i[j] + " -> "
                        if (j == 0):
                            r = r + i[j]
                        else:
                            r = r + i[j][-1:]
                    else:
                        s = s + i[j] + " = "
                        r = r + i[j][-1:]
                print(s + r)
            print()
        else:
            print()
            print("There is no Hamiltonian Path for this Graph")
            print()

    def print_all_nodes_adjacency_lists(this):
        if (len(this.graph_nodes_list) != 0):
            print()
            print("Adjacency List of the Graph: ")
            print()
            for i in this.graph_nodes_list:
                i.print_adjacency_list()
            print()
        else:
            print()
            print("There are no nodes added in the graph")
            print()

    def reset(this):
        for i in this.graph_nodes_list:
            i.reset()
        print()
        print("Resetted all the nodes in the graph")

if __name__ == "__main__":
    gene = input("Enter a String: ").upper()
    kmer = int(input("Enter the Kmer size: "))

    if (gene.isalpha()):
         graph_1 = graph(kmer)

         graph_1.add_nodes_with_string(gene)
         graph_1.add_edges_by_similarity()
         graph_1.print_all_nodes_adjacency_lists()
         graph_1.single_string_reconstructor()
         graph_1.string_printer()
         graph_1.multiple_strings_reconstructor()
         graph_1.string_printer()
    else:
        print("The gene entered consists of characters other than alphabets")
