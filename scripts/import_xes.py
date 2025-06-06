from pm4py.objects.log.importer.xes import importer as xes_importer
from pm4py import get_start_activities, get_end_activities

def import_xes():
    log = xes_importer.apply("../dataset/Road_Traffic_Fine_Management_Process.xes")
    num_traces = len(log)
    num_events = sum(len(trace) for trace in log)
    start_activities = get_start_activities(log)
    end_activities = get_end_activities(log)
    activities = set(event["concept:name"] for trace in log for event in trace)
    num_activities = len(activities)
    print(
        "Number of traces: {}\nNumber of events: {}\nNumber of start activities: {}\nStart activities: {}\nNumber of end activities: {}\nEnd activities: {}\n"
        "Number of unique activities: {}".format(
            num_traces, num_events, len(start_activities), start_activities,
            len(end_activities), end_activities, num_activities))
    return log

if __name__ == "__main__":
    import_xes()