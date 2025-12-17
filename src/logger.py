import logging
import os
from datetime import datetime

LOG_FILE = f"{datetime.now().strftime('%Y-%m-%d_%H-%M-%S')}.log"
logs_path = os.path.join(os.getcwd(), "logs", LOG_FILE)
os.makedirs(logs_path, exist_ok=True)

LOG_FILE= os.path.join(logs_path, LOG_FILE)

logging.basicConfig(
    filename = LOG_FILE,
    format='[%(asctime)s] %(lineno)d %(name)s - %(levelname)s - %(message)s',
    level = logging.INFO

)    

# if __name__ == "__main__":
#     logging.info("Logging has been configured.")

# import logging
# import os
# from datetime import datetime

# # Step 1: unique log file name
# LOG_FILE_NAME = f"{datetime.now().strftime('%Y-%m-%d_%H-%M-%S')}.log"

# # Step 2: logs folder path
# logs_folder = os.path.join(os.getcwd(), "logs")
# os.makedirs(logs_folder, exist_ok=True)  # create folder if not exists

# # Step 3: full log file path
# LOG_FILE_PATH = os.path.join(logs_folder, LOG_FILE_NAME)

# # Step 4: configure logging
# logging.basicConfig(
#     filename=LOG_FILE_PATH,
#     format='[%(asctime)s] %(lineno)d %(name)s - %(levelname)s - %(message)s',
#     level=logging.INFO
# )

# # Step 5: test logging
# logging.info("Logger initialized successfully")
# print(f"Log file created at: {LOG_FILE_PATH}")
