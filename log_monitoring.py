import logging
import psutil
import datetime 

logging.basicConfig(filename='logs/monitoring.log',
                    level=logging.INFO, format='%(asctime)s - %(message)s')

def get_system_metrics():
    try:
        metrics = {
            'cpu_usage': psutil.cpu_percent(interval=1),
            'memory_usage': psutil.virtual_memory().percent,
            'disk_usage': psutil.disk_usage('/').percent,
            'network_stats': psutil.net_io_counters(),
            'timestamp': datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        }
        logging.info("Successfully retrieved system metrics")
        return metrics
    except Exception as e:
        logging.error(f"Error retrieving system metrics: {e}")
        return None