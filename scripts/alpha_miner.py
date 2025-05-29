from import_xes import import_xes
from pm4py.algo.discovery.alpha import algorithm as alpha_miner
from pm4py.visualization.petri_net import visualizer as pn_visualizer
from pm4py.algo.conformance.tokenreplay import algorithm as token_replay


def run_alpha_miner(log):
    # Petri Net
    net, initial_marking, final_marking = alpha_miner.apply(log)
    gviz = pn_visualizer.apply(net, initial_marking, final_marking)
    pn_visualizer.view(gviz)

    #Calculate fitness
    replay_result_alpha = token_replay.apply(log, net, initial_marking, final_marking)
    fitness_alpha = replay_result_alpha[1]
    print("Fitness: ", fitness_alpha)

if __name__ == "__main__":
    event_log = import_xes()
    run_alpha_miner(event_log)