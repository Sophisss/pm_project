import pm4py
import pm4py.objects.conversion.heuristics_net.variants.to_petri_net as hn_to_petri_converter
from pm4py.algo.discovery.heuristics import algorithm as heuristics_miner
from pm4py.visualization.heuristics_net import visualizer as hn_visualizer
from pm4py.visualization.petri_net import visualizer as pn_visualizer
from pm4py.algo.conformance.tokenreplay import algorithm as token_replay
from pm4py.algo.evaluation.replay_fitness.variants import token_replay as fitness_evaluator
from pm4py.algo.evaluation.precision import algorithm as precision_evaluator
from import_xes import import_xes

def run_heuristic_miner(log):
    # Discover and visualize the Heuristic Net
    heu_net = heuristics_miner.apply_heu(log)

    gviz = hn_visualizer.apply(heu_net)
    hn_visualizer.view(gviz)

    # Convert the Heuristic Net into a Petri Net (needed for token-based replay)
    net, initial_marking, final_marking = hn_to_petri_converter.apply(heu_net)
    gviz = pn_visualizer.apply(net, initial_marking, final_marking)
    pn_visualizer.view(gviz)

    # Perform token-based replay for conformance checking
    tbr_result = token_replay.apply(log, net, initial_marking, final_marking)
    # Calculate the fitness
    _evaluate_fitness(tbr_result)
    # Calculate the precision
    _evaluate_precision(log, net, initial_marking, final_marking)


def _evaluate_fitness(tbr_result):
    fitness = fitness_evaluator.evaluate(tbr_result)
    print("Heuristic Miner Fitness:", fitness)
    return fitness

def _evaluate_precision(log, net, initial_marking, final_marking):
    precision = precision_evaluator.apply(log, net, initial_marking, final_marking)
    print("Heuristic Miner Precision:", precision)
    return precision


if __name__ == "__main__":
    event_log = import_xes()
    run_heuristic_miner(event_log)