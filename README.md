# Process Mining Project

## About

This project demonstrates the application of basic Process Mining techniques and algorithms using the [PM4PY](https://pm4py.fit.fraunhofer.de) library. It focuses on discovering process models from event logs, comparing algorithms like **Alpha Miner** and **Heuristic Miner**, and evaluating the quality of the discovered models using metrics such as **fitness** and **precision**.

The analysis is based on a real-world dataset:  
📁 [Road Traffic Fine Management Process](https://data.4tu.nl/articles/dataset/Road_Traffic_Fine_Management_Process/12683249) published by the 4TU Centre for Research Data.

## Structure

The repository has the following folder structure:

- _scripts_ : contains the Python scripts defined to run the Process Discovery and Conformance Checking algorithms.
- _results_ : contains the output models obtained from the Process Discovery algorithms and the fitness and precision scores for each algorithm.
- _documentation_ : contains the project's documentation.
- _dataset_ : `road_traffic_log.xes.zip` unzip the file before running the analysis scripts.

## Requirements
- Python 3.8+
- PM4Py

You can install the required packages using:

```bash
    pip install -r requirements.txt
```

## Output
The resulting process models and evaluation metrics are stored in the `results/` folder. Specifically, you can find:

- **Petri nets** discovered by each algorithm;
- **Fitness** and **precision** scores.

## References
- **PM4Py Documentation**  
  A Python framework for process mining, providing discovery, and conformance algorithms.  
  [https://pm4py.fit.fraunhofer.de/](https://pm4py.fit.fraunhofer.de/)

- **XES Standard**  
  The international standard format for storing and exchanging event logs in process mining.  
  [https://www.xes-standard.org/](https://www.xes-standard.org/)

- **Road Traffic Fine Dataset**  
  The dataset used for analysis, available in the 4TU Data Archive. Contains real-world traffic fine data.  
  [https://data.4tu.nl/](https://data.4tu.nl/)
