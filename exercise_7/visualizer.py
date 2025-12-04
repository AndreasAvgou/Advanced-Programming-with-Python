# File: visualizer.py
import matplotlib.pyplot as plt

def plot_top_items(counter_obj, title, color='blue', top_n=10):
    """
    Generic function to plot a bar chart from a Counter object.
    """
    if not counter_obj:
        print(f"[Warning] No data to plot for {title}.")
        return

    # Get the top N items
    most_common = counter_obj.most_common(top_n)
    items, counts = zip(*most_common)
    
    plt.figure(figsize=(10, 6))
    plt.bar(items, counts, color=color)
    plt.title(f'Top {top_n} {title}')
    plt.xlabel('Item')
    plt.ylabel('Frequency')
    plt.xticks(rotation=45)
    plt.grid(axis='y', linestyle='--', alpha=0.7)
    plt.tight_layout()
    plt.show()
    print(f"[Info] Plot generated: {title}")