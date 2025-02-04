from threading import Timer

# Timer function to update every second (for example, countdown timer or other background task)
def start_timer(callback, interval=1):
    """
    Starts a recurring timer that calls the provided callback every 'interval' seconds.
    The callback function should be thread-safe (e.g., it can use 'window.after()' for GUI updates).
    """
    def countdown():
        callback()  # Call the callback function
        start_timer(callback, interval)  # Recursively call start_timer to keep the timer going
    
    t = Timer(interval, countdown)
    t.start()  # Start the timer
