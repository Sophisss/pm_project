from pm4py.algo.conformance.tokenreplay import algorithm as token_replay
from pm4py.algo.evaluation.replay_fitness.variants import token_replay as fitness_evaluator
from pm4py.algo.evaluation.precision import algorithm as precision_evaluator

def perform_token_based_replay(log, net, initial_marking, final_marking):
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

