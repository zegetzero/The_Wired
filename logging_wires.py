import logging  

def log_wired (file_name): # actual logger for presses  again just keeping to my theme 
        logging.basicConfig(filename=file_name, level=logging.INFO, format='%(asctime)s - [EVENT]:  %(message)s', datefmt='%Y-%m-%d %H:%M:%S', force=True)
        logging.info("Wire log started.")
    
    # im so tired chat 