from import_xes import import_xes
from pm4py.algo.discovery.heuristics import algorithm as heuristics_miner
from pm4py.visualization.heuristics_net import visualizer as hn_visualizer
from pm4py.visualization.petri_net import visualizer as pn_visualizer
from token_based_replay import perform_token_based_replay

def run_heuristic_miner(log):
    # Discover and visualize the Heuristic Net
    heu_net = heuristics_miner.apply_heu(log)
    gviz = hn_visualizer.apply(heu_net)
    hn_visualizer.view(gviz)

    # Convert the Heuristic Net into a Petri Net
    net, initial_marking, final_marking = heuristics_miner.apply(event_log)
    gviz = pn_visualizer.apply(net, initial_marking, final_marking)
    pn_visualizer.view(gviz)

    # Conformance checking
    perform_token_based_replay(log, net, initial_marking, final_marking)

if __name__ == "__main__":
    event_log = import_xes()
    run_heuristic_miner(event_log)