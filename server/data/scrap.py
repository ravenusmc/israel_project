    # # I need to break this down by selected group - Israeli's and Palestinians 
    # def deaths_of_people_took_part_in_event(self, year):
    #     df_filtered = self.data[self.data['date_of_death'].dt.year <= year]
    #     df_filtered_citizenship = df_filtered[df_filtered['citizenship'] == 'Palestinian']
    #     columns = ['Participated', 'Count']
    #     took_part_list = ['Yes', 'No']
    #     for item in took_part_list:
    #         rows = []
    #         rows.append(item)
    #         df_filtered_took_part = df_filtered_citizenship[df_filtered_citizenship['took_part_in_the_hostilities'] == item]
    #         count = len(df_filtered_took_part)
    #         rows.append(count)
    #         columns.append(rows)
    #     return columns 