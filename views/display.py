#display.py


import matplotlib.pyplot as plt
from pandas.plotting import table
import pandas as pd

def display_portfolio_table(securities):
    """
    Displays the portfolio table both graphically and in the console with appropriate margins.
    """
    # Prepare the data for both console and graphical table
    data = {
        "ID": [sec[0] for sec in securities],          # Include ID
        "Name": [sec[2] for sec in securities],
        "Ticker": [sec[3] for sec in securities],
        "Price ($)": [sec[4] for sec in securities],
        "Share (%)": [sec[5] for sec in securities],
        "Risk": [sec[7] for sec in securities],
    }

    # Display the table in the console
    print("\nPortfolio Table:")
    print(f"{'ID':<5} {'Name':<15} {'Ticker':<10} {'Price ($)':<10} {'Share (%)':<10} {'Risk':<5}")
    print("-" * 70)
    for sec in securities:
        print(f"{sec[0]:<5} {sec[2]:<15} {sec[3]:<10} {sec[4]:<10.2f} {sec[5]:<10.2f} {sec[7]:<5.2f}")

    # Convert the data to a Pandas DataFrame for the graphical table
    df = pd.DataFrame(data)

    # Create a figure and axis for graphical display
    fig, ax = plt.subplots(figsize=(12, 6))
    ax.axis('tight')  # Ensure the table fits within the axis
    ax.axis('off')    # Turn off the axis

    # Add the table to the plot
    tab = table(ax, df, loc='center', cellLoc='center', colWidths=[0.15] * len(df.columns))
    tab.auto_set_font_size(False)
    tab.set_fontsize(12)
    tab.scale(1.8, 1.8)  # Scale the table for better readability

    # Adjust layout for spacing, adding left and right margins
    fig.subplots_adjust(left=0.2, right=0.8, top=0.85, bottom=0.15)

    # Add professional styling
    for key, cell in tab.get_celld().items():
        cell.set_linewidth(2.0)  # Thicker border
        cell.set_edgecolor('darkblue')  # Border color
        if key[0] == 0:  # Header row
            cell.set_facecolor('#4682B4')  # Steel blue background for header
            cell.set_text_props(fontweight='bold', color='white')  # Bold white text
        else:
            cell.set_facecolor('#F5F5F5')  # Light grey background for data rows

    # Display the title with styling
    plt.title("Portfolio Table", fontsize=24, weight='bold', color='darkblue', pad=20)
    plt.show()





import matplotlib.pyplot as plt
import numpy as np
import matplotlib.cm as cm

def display_portfolio_graph(securities):
    # Extract labels and risk values
    labels = [sec[2] for sec in securities]  # Names of securities
    sizes = [sec[7] for sec in securities]  # Risk levels

    # Use a colormap to generate consistent colors
    colormap = cm.get_cmap('viridis', len(labels))  # 'viridis' is one of the color maps
    colors = [colormap(i) for i in range(len(labels))]

    # Create a larger figure
    plt.figure(figsize=(10, 6))

    # Create bar positions
    x_positions = np.arange(len(labels))

    # Plot bars with the fixed colors
    bars = plt.bar(x_positions, sizes, color=colors)

    # Add labels on top of bars
    for bar in bars:
        height = bar.get_height()
        plt.text(bar.get_x() + bar.get_width() / 2.0, height, f'{height:.1f}',
                 ha='center', va='bottom', fontsize=12, color='black', fontweight='bold')

    # Add grid to both axes
    plt.grid(axis='both', linestyle='--', alpha=0.7)

    # Customize axes and title
    plt.xticks(x_positions, labels, fontsize=12)
    plt.xlabel('Securities', fontsize=14)
    plt.ylabel('Risk Level', fontsize=14)
    plt.title('Portfolio Composition by Risk', fontsize=16)

    # Optimize layout and display the graph
    plt.tight_layout()
    plt.show()






def calculate_average_risk(securities):
    """
    Calculates and displays the average risk of the portfolio.

    Args:
        securities (list): A list of securities in the portfolio.

    Returns:
        float: The average portfolio risk.
    """
    if not securities:
        print("No securities in the portfolio.")
        return 0
    total_risk = sum(sec[7] for sec in securities)  # Sum the risk values of all securities
    avg_risk = total_risk / len(securities)  # Calculate the average
    return avg_risk


