import time
import logging
from functools import wraps

# Configure global logging format
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s | %(levelname)s | %(message)s",
    datefmt="%Y-%m-%d %H:%M:%S"
)

def log_node(node_name: str):
    """
    Decorator to log LangGraph node execution time and status.
    """
    def decorator(func):
        @wraps(func)
        def wrapper(state, *args, **kwargs):
            start = time.time()
            logging.info(f"🚀 [{node_name}] Started")
            try:
                result = func(state, *args, **kwargs)
                elapsed = time.time() - start
                logging.info(f"✅ [{node_name}] Completed in {elapsed:.2f}s")
                return result
            except Exception as e:
                elapsed = time.time() - start
                logging.error(f"❌ [{node_name}] Failed after {elapsed:.2f}s | Error: {e}")
                raise
        return wrapper
    return decorator