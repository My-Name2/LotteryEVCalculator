def calculate_ev():
    print("Welcome to the Lottery EV Calculator!")

    # Input odds of winning
    try:
        odds = float(input("Enter the odds of winning (e.g., 292000000 for 1 in 292 million): "))
        if odds <= 0:
            raise ValueError("Odds must be a positive number.")
    except ValueError as e:
        print("Invalid input for odds. Please enter a positive number.")
        return

    # Input payout
    try:
        payout = float(input("Enter the total payout amount (e.g., 1000000000 for $1 billion): "))
        if payout < 0:
            raise ValueError("Payout cannot be negative.")
    except ValueError as e:
        print("Invalid input for payout. Please enter a positive number.")
        return

    # Input cost of ticket
    try:
        ticket_cost = float(input("Enter the cost of a single ticket (e.g., 2 for $2): "))
        if ticket_cost <= 0:
            raise ValueError("Cost of ticket must be a positive number.")
    except ValueError as e:
        print("Invalid input for ticket cost. Please enter a positive number.")
        return

    # Additional considerations
    try:
        tax_rate = float(input("Enter the tax rate on winnings as a percentage (e.g., 30 for 30%): ")) / 100
        if tax_rate < 0 or tax_rate > 1:
            raise ValueError("Tax rate must be between 0 and 100.")
    except ValueError as e:
        print("Invalid input for tax rate. Please enter a number between 0 and 100.")
        return

    try:
        sharing_probability = float(input("Enter the probability of sharing the jackpot (e.g., 0.5 for 50%): "))
        if sharing_probability < 0 or sharing_probability > 1:
            raise ValueError("Sharing probability must be between 0 and 1.")
    except ValueError as e:
        print("Invalid input for sharing probability. Please enter a number between 0 and 1.")
        return

    # Adjust net payout and effective probability
    net_payout = payout * (1 - tax_rate)
    effective_probability = (1 / odds) * (1 - sharing_probability)

    # Calculate EV
    ev = (effective_probability * net_payout) - ticket_cost

    # Display results
    print("\nLottery EV Analysis:")
    print(f"  - Odds of Winning: 1 in {odds}")
    print(f"  - Adjusted Net Payout (after taxes): ${net_payout:,.2f}")
    print(f"  - Effective Probability of Winning (adjusted for sharing): {effective_probability:.10f}")
    print(f"  - Cost of Ticket: ${ticket_cost:.2f}")
    print(f"  - Expected Value (EV): ${ev:.2f}")

    if ev > 0:
        print("This lottery is +EV, meaning it is theoretically profitable to play.")
    else:
        print("This lottery is -EV, meaning it is not profitable to play on average.")

# Run the script
if __name__ == "__main__":
    calculate_ev()
