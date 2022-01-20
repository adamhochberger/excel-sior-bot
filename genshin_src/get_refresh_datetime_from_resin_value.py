from datetime import datetime, timedelta

MAX_RESIN_VALUE = 160
MINUTES_PER_RESIN = 8

def get_refresh_datetime_from_resin_value(current_resin_value: int) -> str:
    resin_remaining = MAX_RESIN_VALUE - current_resin_value
    minutes_remaining = MINUTES_PER_RESIN * resin_remaining

    current_time = datetime.now()

    time_with_full_resin = current_time + timedelta(minutes=minutes_remaining)
    formatted_final_time = time_with_full_resin.strftime("%Y-%m-%d %l:%M %p")
    formatted_return_string = f"Your Original Resin ({current_resin_value}/{MAX_RESIN_VALUE}) will be fully refreshed at {formatted_final_time}"

    return formatted_return_string
