# import mpld3
# import matplotlib.pyplot as plt
# from backdated import get_backdated_values

# def plot(graph_type, variables, expression_array, assets, backdate_period=30, figsize=(9, 4)):
#     df = get_backdated_values(
#         expression_array = expression_array,
#         assets = assets,
#         backdate_period = backdate_period)
    
#     fig = plt.figure(figsize = figsize)
#     if(graph_type == "line"):
#         for v in variables:
#             plt.plot(df.index, df[v])
#             plt.title("line graph")
#             plt.xlabel("period")
#             plt.legend()

#     html_str = mpld3.fig_to_html(fig)
#     # Html_file= open("graph.html","w")
#     # Html_file.write(html_str)
#     # Html_file.close()
#     return html_str