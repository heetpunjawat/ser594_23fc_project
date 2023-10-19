import os
import pandas as pd 
import re
import seaborn as sns
import matplotlib.pyplot as plt


def remove_commas_and_quotes(value):
    # Remove non-numeric characters using regular expression
    return re.sub(r'[^\d]', '', str(value))


def compute(input_csv_path, summary_txt_path, correlations_txt_path, visuals_path):
    # Read the CSV file excluding the last "Total" row and last two "Persons Killed" and "Persons Injured" columns
    data = pd.read_csv(input_csv_path, skipfooter=1, usecols=lambda column: column not in ['Persons Killed', 'Persons Injured'], engine='python')

    # Remove quotes and commas, and convert to integers
    numeric_columns = ['Total Crashes', 'Fatal Crashes', 'Injury Crashes', 'PDO Crashes']
    for column in numeric_columns:
        data[column] = data[column].apply(remove_commas_and_quotes).astype(int)

    # Quantitative Features
    quantitative_features = ['Total Crashes', 'Fatal Crashes', 'Injury Crashes', 'PDO Crashes']

    # Calculate Min, Max, and Median for Quantitative Features
    quantitative_summary = data[quantitative_features].apply(lambda x: {'Min': x.min(), 'Max': x.max(), 'Median': x.median()}).transpose()

    # Qualitative Features
    qualitative_feature = 'County'

    # Calculate Number of Categories, Most Frequent, and Least Frequent Category for Qualitative Feature
    number_of_categories = data[qualitative_feature].nunique()
    max_total_crashes = data['Total Crashes'].max()
    most_frequent_categories = data[data['Total Crashes'] == max_total_crashes][qualitative_feature].tolist()
    min_total_crashes = data['Total Crashes'].min()
    least_frequent_categories = data[data['Total Crashes'] == min_total_crashes][qualitative_feature].tolist()

    # Flatten the nested dictionaries in quantitative_summary
    quantitative_summary_flat = pd.DataFrame(quantitative_summary.to_dict()).transpose()    
    # Prepare Summary Table
    summary_table = pd.DataFrame({
        '(Considering all Counties)': quantitative_summary_flat.index,
        'Min': quantitative_summary_flat['Min'].values,
        'Max': quantitative_summary_flat['Max'].values,
        'Median': quantitative_summary_flat['Median'].values
    })

    # Write summary table to summary.txt
    with open(summary_txt_path, 'w') as file:
        file.write(summary_table.to_string(index=False) + '\n\n')
        file.write(f'Number of Counties(Categories): {number_of_categories}\n')
        file.write(f'Most Frequent Counties(Categories): {", ".join(most_frequent_categories)}\n')
        file.write(f'Least Frequent Counties(Categories): {", ".join(least_frequent_categories)}\n')

    # Compute pairwise correlations between quantitative features
    correlations = data[quantitative_features].corr()

    # Writing correlations matrix to correlations.txt 
    with open(correlations_txt_path, 'w') as file:
        # Write header row
        header = "\t".join([""] + correlations.columns.tolist())
        file.write(header + "\n")
        
        # Write lower triangular part of the matrix
        for i, (index, row) in enumerate(correlations.iterrows()):
            formatted_row = "\t".join([index] + [f'{row[col]:.3f}'.ljust(12) for col in correlations.columns[:i+1]])
            file.write(formatted_row + "\n")

    # Define the quantitative features and pairs for scatter plots
    quantitative_features = ['Total Crashes', 'Fatal Crashes', 'Injury Crashes', 'PDO Crashes']
    scatter_plot_pairs = [
        ('Total Crashes', 'Fatal Crashes'),
        ('Total Crashes', 'Injury Crashes'),
        ('Total Crashes', 'PDO Crashes'),
        ('Fatal Crashes', 'Injury Crashes'),
        ('Fatal Crashes', 'PDO Crashes'),
        ('Injury Crashes', 'PDO Crashes')
    ]

    # Color-coding each county differently for scatter plots
    colors = sns.color_palette('hsv', len(data['County'].unique()))
    # Creating scatter plots for each pair
    for i, (x_feature, y_feature) in enumerate(scatter_plot_pairs):
        plt.figure(figsize=(10, 6))
        for j, county in enumerate(data['County'].unique()):
            county_data = data[data['County'] == county]
            plt.scatter(county_data[x_feature], county_data[y_feature], color=colors[j], label=county)

        plt.xlabel(x_feature)
        plt.ylabel(y_feature)
        plt.title(f'{x_feature} vs {y_feature} for each county')
        plt.legend(loc='upper right', bbox_to_anchor=(1.25, 1), title='Counties')
        plt.tight_layout()

        # Save scatter plots as PNG files
        plot_filename = f'visuals/{x_feature}_vs_{y_feature}_scatter.png'
        plt.savefig(plot_filename)
        plt.close()

    # Histogram for Counties vs their number of "Total Crashes"
    plt.figure(figsize=(10, 6))
    ax = sns.barplot(data=data, x='County', y='Total Crashes', estimator=sum, palette='hsv', dodge=False)
    plt.xticks(rotation=45, ha='right')
    plt.xlabel('County')
    plt.ylabel('Total Crashes')
    plt.title('Histogram for County VS Total Crashes')
    plt.tight_layout()

    # Add annotations for total crashes on top of each bar
    for p in ax.patches:
        height = p.get_height()
        ax.annotate(f'{height}', (p.get_x() + p.get_width() / 2., height),
                    ha='center', va='center', fontsize=8, color='black', xytext=(0, 5),
                    textcoords='offset points')

    # Save histogram plot as PNG file
    histogram_filename = os.path.join(visuals_path, 'Counties_vs_Total Crashes_histogram.png')
    plt.savefig(histogram_filename)
    plt.close()



if __name__ == '__main__':
    input_csv_path = os.path.join(os.getcwd(), 'data_processed/table13_processed.csv')
    summary_txt_path = os.path.join(os.getcwd(), 'data_processed/summary.txt')
    correlations_txt_path = os.path.join(os.getcwd(), 'data_processed/correlations.txt')

    # Create a new directory "visuals" to store the png files if it doesnot exist 
    os.makedirs(os.path.join(os.getcwd(), 'visuals'), exist_ok=True)
    visuals_path = os.path.join(os.getcwd(), 'visuals')

    compute(input_csv_path, summary_txt_path, correlations_txt_path, visuals_path)
    