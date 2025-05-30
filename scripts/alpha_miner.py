from import_xes import import_xes
from pm4py.algo.discovery.alpha import algorithm as alpha_miner
from pm4py.visualization.petri_net import visualizer as pn_visualizer
from pm4py.algo.conformance.tokenreplay import algorithm as token_replay
from pm4py.algo.evaluation.replay_fitness.variants import token_replay as fitness_evaluator
from pm4py.algo.evaluation.precision import algorithm as precision_evaluator
from pm4py.algo.conformance.alignments.petri_net import algorithm as alignments

def run_alpha_miner(log):
    # Discover and visualize the Petri Net
    net, initial_marking, final_marking = alpha_miner.apply(log)
    gviz = pn_visualizer.apply(net, initial_marking, final_marking)
    pn_visualizer.view(gviz)

    # Conformance checking
    _perform_token_based_replay(log, net, initial_marking, final_marking)
    # _perform_alignment(log, net, initial_marking, final_marking)

def _perform_token_based_replay(log, net, initial_marking, final_marking):
    # Perform token-based replay
    tbr_result = token_replay.apply(log, net, initial_marking, final_marking)
    # Calculate the fitness
    token_replay_fitness = _evaluate_fitness(tbr_result)
    print("Token-Based Replay Fitness:", token_replay_fitness)
    # Calculate the precision
    token_replay_precision = _evaluate_precision(log, net, initial_marking, final_marking)
    print("Token-Based Replay Precision:", token_replay_precision)

def _evaluate_fitness(tbr_result):
    fitness = fitness_evaluator.evaluate(tbr_result)
    return fitness

def _evaluate_precision(log, net, initial_marking, final_marking):
    precision = precision_evaluator.apply(log, net, initial_marking, final_marking)
    return precision

def _perform_alignment(log, net, initial_marking, final_marking):
    alignment = alignments.apply(log, net, initial_marking, final_marking)
    print("alignment:", alignment)
    alignment_fitness = _evaluate_fitness(alignment)
    print("Alignment Fitness:", alignment_fitness)
    precision_alignment = _evaluate_precision(log, net, initial_marking, final_marking)
    print("Precision Alignment Fitness:", precision_alignment)


if __name__ == "__main__":
    event_log = import_xes()
    run_alpha_miner(event_log)