import pm4py
from pm4py import get_start_activities, get_end_activities

def import_xes():
    log = pm4py.read_xes("../dataset/Road_Traffic_Fine_Management_Process.xes")
    num_events = len(log)
    start_activities = get_start_activities(log)
    end_activities = get_end_activities(log)
    print(
        "Number of events: {}\nNumber of start activities: {}\nStart activities: {}\nNumber of end activities: {}\nEnd activities: {}".format(
            num_events, len(start_activities), start_activities,
            len(end_activities), end_activities))
    return log

if __name__ == "__main__":
    import_xes()