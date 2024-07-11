def generate_report(dataframe):
    report = "Top 5 Campaigns for Today\n\n"
    for index, row in dataframe.iterrows():
        report += f"{index + 1}. {row['campaign_name']}: {row['performance_metric']}\n"
    return report
