import psutil
import datetime 

def get_system_metrics():
    metrics = {
        'cpu_usage': psutil.cpu_percent(interval=1),
        'memory_usage': psutil.virtual_memory().percent,
        'disk_usage': psutil.disk_usage('/').percent,
        'network_stats': psutil.net_io_counters(),
        'timestamp': datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    }

    return metrics