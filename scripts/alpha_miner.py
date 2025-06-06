from import_xes import import_xes
from pm4py.algo.discovery.alpha import algorithm as alpha_miner
from pm4py.visualization.petri_net import visualizer as pn_visualizer
from token_based_replay import perform_token_based_replay

def run_alpha_miner(log):
    # Discover and visualize the Petri Net
    net, initial_marking, final_marking = alpha_miner.apply(log)
    gviz = pn_visualizer.apply(net, initial_marking, final_marking)
    pn_visualizer.view(gviz)

    # Conformance checking
    perform_token_based_replay(log, net, initial_marking, final_marking)

if __name__ == "__main__":
    event_log = import_xes()
    run_alpha_miner(event_log)