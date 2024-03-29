def calculate_and_display_average_price(data):
    all_period = len(data)
    average_period = data['Close'].sum() / all_period
    return average_period